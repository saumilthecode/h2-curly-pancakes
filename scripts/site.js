// Sidebar behaviour for the notes site: the phone menu, keeping the current page
// in view, and search over assets/search.json (built by render-obsidian.js).
(() => {
  const sidebar = document.getElementById("site-sidebar");
  if (!sidebar) return;

  const toggle = sidebar.querySelector(".menu-toggle");
  const body = document.getElementById("sidebar-body");
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  const nav = sidebar.querySelector(".site-nav");
  const phone = window.matchMedia("(max-width: 820px)");

  // Scroll a container so that el sits about a third of the way down it.
  function reveal(container, el) {
    if (!container || !el) return;
    const offset = el.getBoundingClientRect().top - container.getBoundingClientRect().top;
    container.scrollTop += offset - container.clientHeight / 3;
  }

  function setMenu(open) {
    sidebar.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "Close" : "Menu";
    if (open) reveal(body, nav.querySelector(".nav-link.active"));
  }

  toggle.addEventListener("click", () => setMenu(!sidebar.classList.contains("open")));

  // On a wide screen the sidebar scrolls on its own, so bring this page into view.
  if (!phone.matches) reveal(sidebar, nav.querySelector(".nav-link.active"));

  // A link to a heading on this same page doesn't reload, so close the phone menu.
  body.addEventListener("click", (event) => {
    if (phone.matches && event.target.closest("a")) setMenu(false);
  });

  // ---- search ----

  let docs = null;
  let failed = false;
  let loading = null;

  function load() {
    if (!loading) {
      loading = fetch("assets/search.json")
        .then((response) => {
          if (!response.ok) throw new Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          docs = data.map((d) => ({ ...d, tl: d.t.toLowerCase(), sl: d.s.toLowerCase(), xl: d.x.toLowerCase() }));
          failed = false;
        })
        .catch(() => {
          failed = true;
          loading = null;
        });
    }
    return loading;
  }

  function termsOf(query) {
    // Longest first, so "sqlite" is highlighted whole rather than as "sql" + "ite".
    return query.toLowerCase().split(/\s+/).filter(Boolean).sort((a, b) => b.length - a.length);
  }

  function count(haystack, needle) {
    let n = 0;
    let i = haystack.indexOf(needle);
    while (i !== -1 && n < 5) {
      n += 1;
      i = haystack.indexOf(needle, i + needle.length);
    }
    return n;
  }

  // Every term must appear somewhere in the section. Matches in a section's own
  // heading count most, then the page title, then the text.
  function find(terms) {
    const hits = [];
    for (const d of docs) {
      let score = 0;
      let ok = true;
      for (const term of terms) {
        const inSection = d.sl.includes(term);
        const inPage = d.tl.includes(term);
        const inText = count(d.xl, term);
        if (!inSection && !inPage && !inText) {
          ok = false;
          break;
        }
        score += (inSection ? 10 : 0) + (inPage ? 4 : 0) + inText;
      }
      if (ok) hits.push({ d, score });
    }
    hits.sort((a, b) => b.score - a.score);
    const perPage = new Map();
    return hits
      .filter(({ d }) => {
        const seen = perPage.get(d.t) || 0;
        perPage.set(d.t, seen + 1);
        return seen < 3;
      })
      .slice(0, 25);
  }

  function snippet(text, terms) {
    const lower = text.toLowerCase();
    let at = -1;
    for (const term of terms) {
      const i = lower.indexOf(term);
      if (i !== -1 && (at === -1 || i < at)) at = i;
    }
    if (at === -1) return text.length > 140 ? text.slice(0, 140) + "…" : text;
    let start = Math.max(0, at - 45);
    if (start > 0) {
      const space = text.indexOf(" ", start);
      if (space !== -1 && space < at) start = space + 1;
    }
    const end = Math.min(text.length, at + 110);
    return (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
  }

  function escapeRegExp(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // Build the text as DOM nodes, so nothing from the notes is parsed as HTML.
  function highlight(el, text, terms) {
    const pattern = new RegExp("(" + terms.map(escapeRegExp).join("|") + ")", "gi");
    for (const part of text.split(pattern)) {
      if (!part) continue;
      if (terms.includes(part.toLowerCase())) {
        const mark = document.createElement("mark");
        mark.textContent = part;
        el.append(mark);
      } else {
        el.append(part);
      }
    }
  }

  function message(text) {
    const p = document.createElement("p");
    p.className = "search-empty";
    p.textContent = text;
    results.replaceChildren(p);
  }

  function show(query) {
    const q = query.trim();
    if (q.length < 2) {
      results.hidden = true;
      results.replaceChildren();
      nav.hidden = false;
      return;
    }
    nav.hidden = true;
    results.hidden = false;

    if (!docs) {
      message(failed ? "Search couldn't load. Check your connection." : "Loading…");
      if (!failed) load().then(() => {
        if (input.value.trim() === q) show(q);
      });
      return;
    }

    const terms = termsOf(q);
    const hits = find(terms);
    if (!hits.length) {
      message("No matches");
      return;
    }

    results.replaceChildren();
    for (const { d } of hits) {
      const a = document.createElement("a");
      a.className = "search-hit";
      a.href = d.h;
      const title = document.createElement("span");
      title.className = "hit-title";
      highlight(title, d.s ? d.t + " › " + d.s : d.t, terms);
      const text = document.createElement("span");
      text.className = "hit-text";
      highlight(text, snippet(d.x, terms), terms);
      a.append(title, text);
      results.append(a);
    }
  }

  let timer = null;
  input.addEventListener("focus", () => load(), { once: true });
  input.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(() => show(input.value), 60);
  });

  input.addEventListener("keydown", (event) => {
    const first = results.querySelector(".search-hit");
    if (event.key === "Enter" && first) {
      event.preventDefault();
      first.click();
    } else if (event.key === "ArrowDown" && first) {
      event.preventDefault();
      first.focus();
    } else if (event.key === "Escape") {
      input.value = "";
      show("");
      input.blur();
    }
  });

  results.addEventListener("keydown", (event) => {
    const hits = Array.from(results.querySelectorAll(".search-hit"));
    const i = hits.indexOf(document.activeElement);
    if (i === -1) return;
    if (event.key === "ArrowDown" && i < hits.length - 1) {
      event.preventDefault();
      hits[i + 1].focus();
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      (i > 0 ? hits[i - 1] : input).focus();
    } else if (event.key === "Escape") {
      input.focus();
    }
  });

  // "/" jumps to search from anywhere on the page.
  document.addEventListener("keydown", (event) => {
    if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
    if (event.target.closest && event.target.closest("input, textarea, select, [contenteditable]")) return;
    event.preventDefault();
    if (phone.matches) setMenu(true);
    input.focus();
  });
})();
