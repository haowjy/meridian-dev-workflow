// Audit the rendered page for information problems: text the screen may not
// need, system internals shown to the user, controls with no name.
// Run in the page: agent-browser eval --stdin < page-audit.js
// Prints JSON. Every finding is a question for judgment, not a failure.
(() => {
  const MAX = 25;
  const visible = (el) => {
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      if (n.getAttribute("aria-hidden") === "true" || n.hidden) return false;
      const s = getComputedStyle(n);
      if (s.display === "none" || s.visibility === "hidden" || +s.opacity === 0) return false;
    }
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const where = (el) => {
    const parts = [];
    for (let n = el; n && n.nodeType === 1 && parts.length < 4; n = n.parentElement) {
      let p = n.tagName.toLowerCase();
      if (n.id) { parts.unshift(`${p}#${n.id}`); break; }
      const cls = [...n.classList].slice(0, 2).join(".");
      if (cls) p += "." + cls;
      parts.unshift(p);
    }
    return parts.join(" > ");
  };
  const clip = (s) => (s.length > 140 ? s.slice(0, 137) + "..." : s);
  const inCode = (el) => !!el.closest("code, pre, kbd, samp");
  const CONTROLS = "button, a[href], [role=button], [role=link], [role=tab], [role=menuitem], label, summary, option";

  // Visible text blocks: the nearest block-level owner of each text node.
  const blocks = new Map();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const t = walker.currentNode;
    if (!t.textContent.trim()) continue;
    let el = t.parentElement;
    if (!el || ["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE"].includes(el.tagName)) continue;
    while (el.parentElement && getComputedStyle(el).display.startsWith("inline")) el = el.parentElement;
    if (!blocks.has(el) && visible(el)) blocks.set(el, el.innerText.replace(/\s+/g, " ").trim());
  }
  // Keep only innermost blocks so a container doesn't repeat its children.
  const texts = [...blocks].filter(([el]) => ![...blocks.keys()].some((o) => o !== el && el.contains(o)));

  const sentences = [];
  const narration = [];
  const internals = [];
  // Text about the interface instead of the content: instructions to operate
  // it, or descriptions of what a control or panel does.
  const NARRATION = [
    /^(select|choose|pick|click|tap|drag|hover|press|toggle|use|open|expand)\w*\b/i,
    /\b(this (page|screen|view|panel|section|dashboard|table|tab|card) (shows|lets|displays|contains|lists|is)|here you can|you can (see|use|find|switch|click))\b/i,
    /\b(click|tap|hover|drag)(s|ed|ing)?\b/i,
    /\b(button|toggle|tab|sidebar|rail|panel|dropdown|menu|action) (opens|shows|lets|switches|takes you)\b/i,
    /\b(one click away|stays visible|appears here|shown here|opens here)\b/i,
  ];
  const PATTERNS = [
    ["uuid", /\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/i],
    ["hash", /\b[0-9a-f]{12,}\b/i],
    ["iso-timestamp", /\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/],
    ["snake_case", /\b([a-z]+(_[a-z0-9]+)+|[A-Z][A-Z0-9]+(_[A-Z0-9]+)+)\b/],
    ["dotted.field", /\b[a-z]+[A-Za-z]*\.[a-z]+[A-Za-z]*(\.[a-z]+)*\b(?!\.\w)/],
    ["camelCase", /\b[a-z]+[A-Z][a-z]+[A-Za-z]*\b/],
  ];
  for (const [el, text] of texts) {
    if (!text) continue;
    const words = text.split(" ").length;
    const isSentence = words >= 8 || /[.!?]$/.test(text) && words >= 4;
    if (isSentence && !inCode(el)) sentences.push({ text: clip(text), where: where(el), words });
    if (NARRATION.some((re) => re.test(text)) && !inCode(el) && !el.closest(CONTROLS)) narration.push({ text: clip(text), where: where(el) });
    if (inCode(el)) continue;
    for (const [kind, re] of PATTERNS) {
      const m = text.match(re);
      if (m && !/^(e\.g|i\.e|etc)$/i.test(m[0]) && !/\.(com|org|io|dev|html|md|js|ts|py)$/i.test(m[0])) {
        internals.push({ kind, match: m[0], text: clip(text), where: where(el) });
        break;
      }
    }
  }

  // Controls with no accessible name.
  const unnamed = [];
  for (const el of document.querySelectorAll("button, a[href], [role=button], [role=link], [role=tab], [role=menuitem], input[type=button], input[type=submit]")) {
    if (!visible(el)) continue;
    const name = (el.getAttribute("aria-label") || el.getAttribute("title") || el.innerText || el.value || "").trim();
    const labelledby = el.getAttribute("aria-labelledby");
    const imgAlt = [...el.querySelectorAll("img[alt]")].some((i) => i.alt.trim());
    if (!name && !labelledby && !imgAlt) unnamed.push({ where: where(el), html: clip(el.outerHTML) });
  }

  // Text that restates its section heading.
  const restated = [];
  for (const h of document.querySelectorAll("h1, h2, h3, h4, h5, h6")) {
    if (!visible(h)) continue;
    const ht = h.innerText.trim().toLowerCase();
    if (ht.length < 4) continue;
    const next = h.nextElementSibling;
    if (next && visible(next)) {
      const nt = next.innerText.trim().toLowerCase();
      if (nt && (nt === ht || nt.startsWith(ht + " ") || nt.startsWith(ht + ":"))) {
        restated.push({ heading: h.innerText.trim(), next: clip(next.innerText.trim()), where: where(next) });
      }
    }
  }

  const out = {
    url: location.href,
    counts: {
      sentences: sentences.length,
      interface_narration: narration.length,
      internal_strings: internals.length,
      unnamed_controls: unnamed.length,
      restated_headings: restated.length,
    },
    sentences: sentences.slice(0, MAX),
    interface_narration: narration.slice(0, MAX),
    internal_strings: internals.slice(0, MAX),
    unnamed_controls: unnamed.slice(0, MAX),
    restated_headings: restated.slice(0, MAX),
  };
  return out;
})();
