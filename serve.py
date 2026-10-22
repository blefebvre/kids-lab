"""Preview server for Kids Lab.

Run:   python serve.py
Then open http://localhost:8000

It works like `python -m http.server`, with two extras:
- it tells the browser not to keep old copies of files, and
- the page reloads by itself whenever you save a file.

The reload code is only added while previewing on your computer.
The files in the repo (and the real website) don't change.
"""
import http.server
import os
import urllib.parse

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

# This little script gets added to every web page we send. Once a second it
# asks the server "has anything changed?" and reloads the page if it has.
RELOAD_SCRIPT = b"""
<script>
  // Added by serve.py for previewing: reload when a file changes.
  (function () {
    let last = null;
    setInterval(async function () {
      try {
        const response = await fetch('/__changed', { cache: 'no-store' });
        const stamp = await response.text();
        if (last !== null && stamp !== last) location.reload();
        last = stamp;
      } catch (e) {
        // The server is stopped or restarting. We'll try again in a second.
      }
    }, 1000);
  })();
</script>
"""


def latest_change():
    """Return the time of the most recently saved file in the project."""
    newest = 0
    for folder, subfolders, files in os.walk(ROOT):
        subfolders[:] = [name for name in subfolders if not name.startswith('.')]
        for name in files:
            try:
                newest = max(newest, os.path.getmtime(os.path.join(folder, name)))
            except OSError:
                pass  # The file was deleted while we were looking.
    return newest


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        # "Don't save a copy. Always ask me for the newest version."
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        url_path = urllib.parse.urlsplit(self.path).path

        if url_path == '/__changed':
            self.send_text(str(latest_change()).encode(), 'text/plain')
            return

        file_path = self.translate_path(self.path)
        if os.path.isdir(file_path) and url_path.endswith('/'):
            file_path = os.path.join(file_path, 'index.html')

        if file_path.endswith('.html') and os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                page = f.read()
            if b'</body>' in page:
                page = page.replace(b'</body>', RELOAD_SCRIPT + b'</body>', 1)
            else:
                page += RELOAD_SCRIPT
            self.send_text(page, 'text/html; charset=utf-8')
            return

        super().do_GET()

    def send_text(self, body, content_type):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # Keep the terminal quiet (it checks for changes every second).


if __name__ == '__main__':
    server = http.server.ThreadingHTTPServer(('localhost', PORT), PreviewHandler)
    print(f'Kids Lab preview: http://localhost:{PORT}  (press Ctrl+C to stop)')
    server.serve_forever()
