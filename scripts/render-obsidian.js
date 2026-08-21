const fs = require("fs");
const path = require("path");
const MarkdownIt = require("markdown-it");
const anchor = require("markdown-it-anchor");

const root = process.cwd();
const notesDir = path.join(root, "notes");
const outDir = path.join(root, "_site");

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: false,
})
  .use(anchor, {
    permalink: anchor.permalink.headerLink(),
    slugify: slugify,
  });

const calloutIcons = {
  note: "✎",
  info: "i",
  todo: "✓",
  tip: "!",
  hint: "!",
  important: "!",
  success: "✓",
  check: "✓",
  done: "✓",
  question: "?",
  help: "?",
  warning: "!",
  caution: "!",
  attention: "!",
  failure: "×",
  fail: "×",
  missing: "×",
  danger: "!",
  error: "!",
  bug: "!",
  example: "≡",
  quote: "”",
  summary: "≡",
  abstract: "≡",
  tldr: "≡",
};

function slugify(value) {
  return String(value)
    .trim()
    .toLowerCase()
    .replace(/<[^>]+>/g, "")
    .replace(/[^\w\s-]/g, "")
    .replace(/\s+/g, "-");
}

function ensureCleanDir(dir) {
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
}

function titleFromFile(file) {
  return path.basename(file, ".md");
}

function readIndexEntries(knownNotes) {
  const indexPath = path.join(notesDir, "index.md");
  if (!fs.existsSync(indexPath)) return [];

  const source = fs.readFileSync(indexPath, "utf8");
  const entries = [];
  const wikiLink = /\[\[((?:[^|\]\\]|\\.)+)(?:\|([^\]]+))?\]\]/g;
  let match;

  while ((match = wikiLink.exec(source)) !== null) {
    const target = match[1].replace(/\\\|/g, "|").replace(/\\$/, "").trim();
    const file = knownNotes.get(target.toLowerCase());
    if (!file || file === "index.md") continue;

    entries.push({
      file,
      title: (match[2] || target).trim(),
    });
  }

  return entries;
}

function outputNameForMarkdown(file) {
  const base = path.basename(file, ".md");
  return `${base}.html`;
}

function encodeHref(file) {
  return encodeURI(file).replace(/#/g, "%23");
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function splitMarkdownSegments(source) {
  const parts = [];
  const fence = /(^|\n)(```|~~~)[\s\S]*?(\n\2[^\n]*)(?=\n|$)/g;
  let last = 0;
  let match;

  while ((match = fence.exec(source)) !== null) {
    const start = match.index + match[1].length;
    if (start > last) {
      parts.push({ code: false, text: source.slice(last, start) });
    }
    parts.push({ code: true, text: source.slice(start, fence.lastIndex) });
    last = fence.lastIndex;
  }

  if (last < source.length) {
    parts.push({ code: false, text: source.slice(last) });
  }

  return parts;
}

// Inside a markdown table a wikilink alias pipe must be escaped as \| so the
// cell isn't split. Normalise that back before resolving the target.
function splitWikiTarget(rawTarget) {
  return rawTarget
    .replace(/\\\|/g, "|")
    .split("|")
    .map((s) => s.trim());
}

function resolveNoteTarget(target, knownNotes) {
  const [notePart, anchorPart] = target.split("#");
  const label = notePart.trim();
  const match = knownNotes.get(label.toLowerCase());

  if (!match) {
    return {
      href: "#",
      missing: true,
      label: label || target,
    };
  }

  let href = outputNameForMarkdown(match);
  if (anchorPart) {
    href += `#${slugify(anchorPart)}`;
  }

  return {
    href,
    missing: false,
    label: label || titleFromFile(match),
  };
}

function transformObsidianSyntax(source, knownNotes) {
  return splitMarkdownSegments(source)
    .map((part) => {
      if (part.code) return part.text;

      return part.text
        .replace(/!\[\[([^\]]+)\]\]/g, (_all, rawTarget) => {
          const [target, altText] = splitWikiTarget(rawTarget);
          const ext = path.extname(target).toLowerCase();

          if ([".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"].includes(ext)) {
            return `<img class="obsidian-embed-image" src="${encodeHref(target)}" alt="${escapeHtml(altText || target)}">`;
          }

          const resolved = resolveNoteTarget(target, knownNotes);
          return `[${altText || resolved.label}](${resolved.href})`;
        })
        .replace(/\[\[([^\]]+)\]\]/g, (_all, rawTarget) => {
          const [targetPart, aliasPart] = splitWikiTarget(rawTarget);
          const resolved = resolveNoteTarget(targetPart, knownNotes);
          const label = aliasPart || resolved.label;
          const cls = resolved.missing ? ' class="internal-link missing"' : ' class="internal-link"';
          return `<a${cls} href="${encodeHref(resolved.href)}">${escapeHtml(label)}</a>`;
        });
    })
    .join("");
}

function transformCallouts(html) {
  return html.replace(/<blockquote>\n([\s\S]*?)<\/blockquote>/g, (all, inner) => {
    const callout = inner.match(/^<p>\[!(\w+)\]([-+]?)([^\n<]*)\n?([\s\S]*?)<\/p>\n?([\s\S]*)$/);
    if (!callout) return all;

    const type = callout[1].toLowerCase();
    const fold = callout[2];
    const title = callout[3].trim() || type;
    const firstBody = callout[4].trim();
    const rest = callout[5].trim();
    const icon = calloutIcons[type] || "!";
    const body = [firstBody, rest].filter(Boolean).join("\n");
    const titleMarkup = `<span class="callout-icon">${icon}</span><span>${escapeHtml(title)}</span>`;
    const content = body ? `<div class="callout-content">${body}</div>` : "";

    // Obsidian fold markers: "-" starts collapsed, "+" starts expanded.
    if (fold) {
      return `<details class="callout callout-${type} callout-foldable"${fold === "+" ? " open" : ""}>
<summary class="callout-title">${titleMarkup}</summary>
${content}
</details>`;
    }

    return `<aside class="callout callout-${type}">
<div class="callout-title">${titleMarkup}</div>
${content}
</aside>`;
  });
}

function renderMarkdown(file, source, knownNotes, displayTitles, navEntries) {
  const transformed = transformObsidianSyntax(source, knownNotes);
  const body = transformCallouts(md.render(transformed));
  const pageTitle = file === "index.md" ? "H2 Computing Notes" : displayTitles.get(file) || titleFromFile(file);

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(pageTitle)}</title>
  <link rel="stylesheet" href="assets/site.css">
</head>
<body>
  <div class="site-shell">
    <aside class="site-sidebar">
      <a class="site-title" href="index.html">H2 Computing Notes</a>
      ${renderNav(knownNotes, file, displayTitles, navEntries)}
    </aside>
    <main class="markdown-preview-view">
      ${file !== "index.md" ? `<h1>${escapeHtml(pageTitle)}</h1>` : ""}
      ${body}
    </main>
  </div>
</body>
</html>`;
}

function renderNav(knownNotes, currentFile, displayTitles, navEntries) {
  const indexFiles = new Set(navEntries.map((entry) => entry.file));
  const ordered = [
    ...navEntries.map((entry) => entry.file),
    ...Array.from(knownNotes.values())
      .filter((file) => !indexFiles.has(file)),
  ]
    .filter((file) => file !== "index.md" && file !== "* index.md" && !file.startsWith("."))
    .filter((file, index, files) => files.indexOf(file) === index);

  const links = ordered
    .map((file) => {
      const title = displayTitles.get(file) || titleFromFile(file);
      const active = file === currentFile ? " active" : "";
      return `<a class="nav-link${active}" href="${encodeHref(outputNameForMarkdown(file))}">${escapeHtml(title)}</a>`;
    })
    .join("\n");

  return `<nav>${links}</nav>`;
}

function copyAssets() {
  const assetsDir = path.join(outDir, "assets");
  fs.mkdirSync(assetsDir, { recursive: true });
  fs.writeFileSync(path.join(assetsDir, "site.css"), siteCss());

  for (const entry of fs.readdirSync(notesDir, { withFileTypes: true })) {
    const source = path.join(notesDir, entry.name);
    const destination = path.join(outDir, entry.name);

    if (entry.isDirectory() && entry.name === "pictures") {
      copyDir(source, destination);
      continue;
    }

    if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();
      if ([".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"].includes(ext)) {
        fs.copyFileSync(source, destination);
      }
    }
  }
}

function copyDir(source, destination) {
  fs.mkdirSync(destination, { recursive: true });

  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    const sourcePath = path.join(source, entry.name);
    const destinationPath = path.join(destination, entry.name);

    if (entry.isDirectory()) {
      copyDir(sourcePath, destinationPath);
    } else if (entry.isFile()) {
      fs.copyFileSync(sourcePath, destinationPath);
    }
  }
}

function siteCss() {
  return `:root {
  --background-primary: #f8f7f4;
  --background-secondary: #eeebe4;
  --background-modifier-border: #d8d3ca;
  --text-normal: #211f1c;
  --text-muted: #6f6960;
  --text-accent: #4b6fb5;
  --interactive-accent: #5c7cba;
  --code-background: #eeece7;
  --font-text: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--background-primary);
  color: var(--text-normal);
  font-family: var(--font-text);
  line-height: 1.6;
}

.site-shell {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  min-height: 100vh;
}

.site-sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
  padding: 24px 18px;
  background: var(--background-secondary);
  border-right: 1px solid var(--background-modifier-border);
}

.site-title {
  display: block;
  margin-bottom: 18px;
  color: var(--text-normal);
  font-weight: 700;
  text-decoration: none;
}

.nav-link {
  display: block;
  padding: 7px 10px;
  border-radius: 6px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
}

.nav-link:hover,
.nav-link.active {
  background: rgba(92, 124, 186, 0.13);
  color: var(--text-normal);
}

.markdown-preview-view {
  max-width: 980px;
  width: 100%;
  padding: 48px 56px 80px;
}

h1, h2, h3 {
  line-height: 1.25;
  margin-top: 1.8em;
  margin-bottom: 0.6em;
}

h1 { margin-top: 0; font-size: 2rem; }
h2 { border-bottom: 1px solid var(--background-modifier-border); padding-bottom: 0.25rem; }

.header-anchor {
  color: inherit;
  text-decoration: none;
}

.header-anchor:hover {
  text-decoration: underline;
}

a { color: var(--text-accent); }
a.internal-link { text-decoration: none; font-weight: 500; }
a.internal-link:hover { text-decoration: underline; }
a.missing { color: #a15c45; }

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
  display: block;
  overflow-x: auto;
}

th, td {
  border: 1px solid var(--background-modifier-border);
  padding: 0.45rem 0.6rem;
  text-align: left;
}

th { background: var(--background-secondary); }

code {
  font-family: var(--font-mono);
  background: var(--code-background);
  border-radius: 4px;
  padding: 0.12rem 0.3rem;
}

pre {
  overflow-x: auto;
  background: var(--code-background);
  border: 1px solid var(--background-modifier-border);
  border-radius: 8px;
  padding: 1rem;
}

pre code {
  padding: 0;
  background: transparent;
}

.callout {
  margin: 1rem 0;
  padding: 0.85rem 1rem;
  border-left: 4px solid var(--interactive-accent);
  border-radius: 8px;
  background: rgba(92, 124, 186, 0.12);
}

.callout-title {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--text-normal);
  font-weight: 700;
}

.callout-icon {
  display: inline-flex;
  width: 1.25rem;
  height: 1.25rem;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: var(--interactive-accent);
  color: white;
  font-size: 0.8rem;
}

.callout-content > :first-child { margin-top: 0.5rem; }
.callout-content > :last-child { margin-bottom: 0; }

.callout-foldable > summary {
  cursor: pointer;
  list-style: none;
}

.callout-foldable > summary::-webkit-details-marker { display: none; }

.callout-foldable > summary::after {
  content: "\\203A";
  margin-left: auto;
  color: var(--text-muted);
  transition: transform 0.15s ease;
}

.callout-foldable[open] > summary::after { transform: rotate(90deg); }

.callout-important, .callout-warning, .callout-caution { border-color: #c28a31; background: rgba(194, 138, 49, 0.14); }
.callout-error, .callout-danger, .callout-failure { border-color: #b85d5d; background: rgba(184, 93, 93, 0.14); }
.callout-summary, .callout-info, .callout-note { border-color: #5c7cba; }

.obsidian-embed-image {
  display: block;
  max-width: 100%;
  margin: 1rem 0;
  border-radius: 8px;
}

@media (max-width: 820px) {
  .site-shell { grid-template-columns: 1fr; }
  .site-sidebar {
    position: static;
    height: auto;
    border-right: 0;
    border-bottom: 1px solid var(--background-modifier-border);
  }
  .markdown-preview-view { padding: 32px 20px 64px; }
}`;
}

function main() {
  ensureCleanDir(outDir);

  const noteFiles = fs
    .readdirSync(notesDir)
    .filter((file) => file.endsWith(".md") && !file.startsWith("_"));

  const knownNotes = new Map();
  for (const file of noteFiles) {
    knownNotes.set(titleFromFile(file).toLowerCase(), file);
  }

  const navEntries = readIndexEntries(knownNotes);
  const displayTitles = new Map(navEntries.map((entry) => [entry.file, entry.title]));

  copyAssets();

  for (const file of noteFiles) {
    const source = fs.readFileSync(path.join(notesDir, file), "utf8");
    const html = renderMarkdown(file, source, knownNotes, displayTitles, navEntries);
    fs.writeFileSync(path.join(outDir, outputNameForMarkdown(file)), html);
  }

  fs.writeFileSync(path.join(outDir, ".nojekyll"), "");
  console.log(`Rendered ${noteFiles.length} notes to ${path.relative(root, outDir)}`);
}

main();
