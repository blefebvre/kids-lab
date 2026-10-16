# Kids Lab

Games and web apps built by kids (with help from Claude), live at
**https://play.brucelefebvre.com**.

## Start something new

```bash
cd ~/Work/kids-lab
claude
```

Then say what you want to make, like *"make a game where a cat catches falling fish."*

## See it in your browser

```bash
python -m http.server 8000
```

Open http://localhost:8000.

## Layout

- `<name>/<project>/index.html`: each kid's projects
- `examples/`: starter projects to copy and remix
- `projects.json`: the list shown on the home page
