#!/usr/bin/env python3
"""Check a grey-box wireframe page against the kit.

Usage: python3 validate.py PAGE.html

Exits 1 and lists each problem when the page leaves the kit: a class the kit doesn't
define, a style beyond sizing and placement, a tag that brings colour, images or code,
a screen without a caption, or a wireframe.css that differs from the kit's copy.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

KIT_CSS = Path(__file__).resolve().parent.parent / "assets" / "wireframe.css"

ALLOWED_TAGS = {
    "html", "head", "meta", "title", "link", "body", "main", "header", "section", "nav",
    "h1", "h2", "h3", "p", "ul", "ol", "li", "figure", "figcaption", "b", "strong", "em",
    "a", "code", "div", "span", "i", "br",
    "table", "thead", "tbody", "tr", "th", "td",
}
VOID_TAGS = {"meta", "link", "br"}
STYLE_PROPS = {
    "width", "height", "min-width", "min-height", "max-width", "max-height",
    "flex", "flex-basis", "gap", "top", "left", "right", "bottom",
}
ALLOWED_ATTRS = {
    "class", "style", "id", "lang", "charset", "name", "content", "rel", "href",
    "colspan", "rowspan", "data-depth", "title", "aria-label",
}
# Pictographs and dingbats read as icons, which a wireframe leaves out. The Arrows block
# (U+2190-U+21FF) is outside these ranges and stays usable.
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]")


def kit_classes(css: str) -> set[str]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return set(re.findall(r"\.([A-Za-z][\w-]*)", css))


class Page(HTMLParser):
    def __init__(self, classes: set[str]):
        super().__init__(convert_charrefs=True)
        self.classes = classes
        self.errors: list[str] = []
        self.stack: list[dict] = []
        self.screens = 0
        self.stylesheets: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(f"line {self.getpos()[0]}: {msg}")

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED_TAGS:
            self.err(f"<{tag}> is not part of the kit")
        a = dict(attrs)
        for name in a:
            if name not in ALLOWED_ATTRS:
                self.err(f"attribute {name}= on <{tag}> is not allowed")
        if tag == "link":
            if a.get("rel") != "stylesheet" or a.get("href") != "wireframe.css":
                self.err('the only <link> allowed is rel="stylesheet" href="wireframe.css"')
            else:
                self.stylesheets.append(a["href"])
        if "href" in a and tag not in ("a", "link"):
            self.err(f"href on <{tag}>")
        for cls in (a.get("class") or "").split():
            if cls not in self.classes:
                self.err(f'class "{cls}" is not in the kit')
        if a.get("style"):
            self.check_style(a["style"])
        node = {"tag": tag, "cls": set((a.get("class") or "").split()), "caption": False}
        if "wf-screen" in node["cls"]:
            self.screens += 1
            fig = next((n for n in reversed(self.stack) if n["tag"] == "figure"), None)
            if fig is None:
                self.err("a .wf-screen must sit inside a <figure> with a <figcaption>")
            elif not fig["caption"]:
                self.err("the <figcaption> must come before the .wf-screen in its <figure>")
        if tag == "figcaption":
            fig = next((n for n in reversed(self.stack) if n["tag"] == "figure"), None)
            if fig is not None:
                fig["caption"] = True
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS and self.stack:
            self.stack.pop()

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if EMOJI.search(data):
            self.err(f"pictograph in text {data.strip()[:40]!r}: write the word instead")

    def check_style(self, style: str) -> None:
        for decl in filter(None, (d.strip() for d in style.split(";"))):
            prop, _, value = decl.partition(":")
            prop, value = prop.strip().lower(), value.strip().lower()
            if prop not in STYLE_PROPS:
                self.err(f'inline "{prop}" is not allowed; only sizing and placement go inline')
            elif re.search(r"url\(|var\(|#|rgb|hsl|gradient", value):
                self.err(f'inline "{decl}" carries more than a size')


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    page = Path(argv[1])
    kit = KIT_CSS.read_text()
    parser = Page(kit_classes(kit))
    parser.feed(page.read_text())
    parser.close()
    errors = parser.errors
    if not parser.stylesheets:
        errors.append('the page must link wireframe.css: <link rel="stylesheet" href="wireframe.css">')
    beside = page.parent / "wireframe.css"
    if not beside.exists():
        errors.append(f"{beside} is missing: copy it from {KIT_CSS}")
    elif beside.read_text() != kit:
        errors.append(f"{beside} differs from the kit: copy it again from {KIT_CSS}")
    if parser.screens == 0:
        errors.append("no .wf-screen on the page")
    if errors:
        print(f"{page}: {len(errors)} problem(s)")
        for e in errors:
            print(f"  {e}")
        return 1
    print(f"{page}: ok, {parser.screens} screen(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
