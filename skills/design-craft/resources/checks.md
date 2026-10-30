# Checking a Rendered Page

Run both checks on the rendered page before you show it or ship it, and
again after a fix that changes what renders. Each finding is a question: fix
it, or keep it and say why.

## Information

With the page open in `/agent-browser`, run this skill's
`scripts/page-audit.js`:

```bash
agent-browser eval --stdin < <design-craft skill dir>/scripts/page-audit.js
```

It returns counts and up to 25 examples, each with its location:

- **sentences:** visible text of a sentence or more. Keep one when it tells
  the reader what the screen can't show (a format, a consequence, how to
  recover, a finding); cut or shorten the rest.
- **interface_narration:** text that tells the reader how to operate the
  screen ("Select an AI to…", "opens here"). Fix the layout or the control's
  name and delete the text.
- **internal_strings:** IDs, hashes, timestamps, `snake_case` names, dotted
  fields, tool calls, raw markdown. Remove each one the reader doesn't act on, or replace
  it with the reader's word for it.
- **unnamed_controls:** buttons and links with no accessible name. Add one.
- **restated_headings:** text right under a heading that repeats it.

## Visual Tells

Run impeccable's detector on the page's URL or HTML file (Node 22 or newer;
URLs render in the installed Chrome or Edge):

```bash
npx -y impeccable@4 detect --json <url-or-file>
```

Exit code 2 means findings. It reports a failure once per element, so group
findings by rule and snippet: forty low-contrast findings are often three
colour pairs. It flags the generated look (gradients, glows, overused fonts,
cream surfaces, side stripes) and rendering faults (low contrast, tiny text,
overflow, clipped text, broken images).

When a finding is a choice the project made on purpose and wrote down (its
`DESIGN.md` names the font or the surface), record it so later runs stay
quiet, citing where it was decided:

```bash
npx -y impeccable@4 ignores add-value overused-font Inter --reason "DESIGN.md: one font, Inter"
```

This writes the committed `.impeccable/config.json`. Faults (contrast, text
size, overflow) are never choices. Taste rules such as
`kicker-above-heading` and `numbered-section-labels` are weighed against the
brief like any other default.

Two findings come from the setup rather than the page: on a dev server,
framework devtools panels count as page content and trip
`content-hidden-at-rest` and `shape-assembled-illustration`, so scan a
production build where you can; and `cramped-padding` fires on panes that
hold an image, a video, or a 3D view edge to edge by design.

To scan a page behind a login, sign in with `/agent-browser`, then attach to
that browser: `agent-browser get cdp-url` gives the port, and
`npx -y impeccable@4 detect --json --cdp <port> --target <url substring>`
scans the open page.
