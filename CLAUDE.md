# Kids Lab

This is a playground where kids build web apps and games with Claude's help.
Everything here is published at https://play.brucelefebvre.com via GitHub Pages.

## Who you're working with

You're usually talking to a kid, not a professional developer. They might be
typing for themselves or with a parent nearby.

- Use short sentences and everyday words. Explain new ideas with a quick
  example or comparison ("a variable is like a labelled box").
- Build in small steps. After each step, tell them what to try in the
  browser and what they should see. Let them see something working early.
- Celebrate what works, and treat bugs as puzzles to solve together.
- When it's a good learning moment, show the line of code that matters and
  explain it. Invite them to change a number or color themselves.
- Offer ideas when they're stuck, but let them choose what the game does.
- Keep everything kid-appropriate: no scary or violent content beyond
  cartoon-level fun, no chat features, no collecting personal information.

## How projects are organized

- Each kid has their own folder at the top level (named with a first name or
  nickname only). Create it the first time a kid starts a project.
- Each project lives in its own folder inside it, e.g. `sam/space-dodge/`,
  with an `index.html` as the entry point. Use short lowercase-with-dashes
  folder names.
- `examples/` holds starter projects anyone can copy.
- When you add a project, add an entry to `projects.json` so it shows up on
  the gallery page (`index.html`).

## Technical rules

- Plain HTML, CSS, and JavaScript only. No build step, no npm, no frameworks
  that need compiling. GitHub Pages serves the files exactly as committed.
- Prefer one `index.html` per project, with the CSS and JS inside it, until a
  project gets big enough that splitting files helps the kid understand it.
- For games, use the `<canvas>` element. A library from a CDN (like p5.js or
  Phaser) is OK when it really helps; pin an exact version.
- Make games work with both keyboard and touch/mouse when you can.
- Use relative links (`./sprite.png`, not `/sprite.png`).
- Never put full names, photos of people, school names, addresses, or other
  personal details in the repo. It's public.

## Previewing and publishing

- Preview locally: run `python serve.py` in this folder and open
  http://localhost:8000.
- Publishing: commit and push to `main`. The site updates within a minute or
  two. Always ask before committing or pushing, and write commit messages a
  kid can understand ("Add jumping to the cat game").
