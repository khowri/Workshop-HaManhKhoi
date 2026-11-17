"""Bundle a Hugo build into a bilingual HTML file for offline reading."""
import argparse
import base64
import json
import mimetypes
import re
from html import unescape, escape
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("build", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
root = args.build.resolve()
base = "http://localhost:1313/"
pages = {}
for file in sorted(root.rglob("index.html")):
    route = file.parent.relative_to(root).as_posix()
    if route == "en" or route.startswith("en/"):
        lang, slug = "en", route[3:]
    else:
        lang, slug = "vi", route if route != "." else ""
    if slug.startswith(("tags", "categories")) or slug == "vi":
        continue
    page = file.read_text(encoding="utf-8")
    if 'id="body-inner"' not in page:
        continue
    body = page.split('id="body-inner"', 1)[1]
    heading = re.search(r"<h1\b[^>]*>(.*?)</h1>", body, re.S)
    if not heading:
        raise ValueError(f"Missing heading in {file}")
    actual = body[heading.start():]
    end = re.search(r'<footer\b[^>]*footline|<div id="navigation"', actual)
    if not end:
        raise ValueError(f"Missing end of content in {file}")
    content = actual[:end.start()]
    if slug == "":
        content = re.split(r"</ol>", content, maxsplit=1)[0] + "</ol>"
    title = unescape(re.sub(r"<[^>]+>", "", heading[1])).strip()
    pages.setdefault(slug, {})[lang] = {"title": title, "body": content.strip()}

assets = {}
missing = set()
attr = re.compile(r'\b(href|src)=(["\'])(.*?)\2', re.I)
for slug, pair in pages.items():
    for lang, page in pair.items():
        current = base + ("en/" if lang == "en" else "") + (slug + "/" if slug else "")
        def rewrite(match):
            field, _, raw = match.groups()
            original = unescape(raw)
            if original.startswith(("#", "data:", "mailto:")):
                return match[0]
            url = urlsplit(urljoin(current, original))
            if url.netloc != "localhost:1313":
                return match[0]
            route = unquote(url.path).strip("/")
            target = route.removesuffix("/index.html")
            if target == "index.html":
                target = ""
            target_lang = "en" if target == "en" or target.startswith("en/") else "vi"
            if target_lang == "en":
                target = target[3:]
            if target in pages:
                fragment = f"{target_lang}/{target}"
                if url.fragment:
                    fragment += "::" + url.fragment
                return f'href="#{escape(fragment, quote=True)}"'
            file = (root / route).resolve()
            if file.is_relative_to(root) and file.is_file():
                if route not in assets:
                    mime = mimetypes.guess_type(file)[0] or "application/octet-stream"
                    assets[route] = f"data:{mime};base64," + base64.b64encode(file.read_bytes()).decode("ascii")
                return f'data-offline-{field}="{escape(route, quote=True)}"'
            missing.add((slug, original))
            return match[0]
        page["body"] = attr.sub(rewrite, page["body"])

if missing:
    raise ValueError(f"Unresolved internal links or resources: {sorted(missing)[:20]}")
if len(pages) < 70 or any(set(p) != {"vi", "en"} for p in pages.values()):
    raise ValueError("Incomplete bilingual Hugo build")

markup = """<!doctype html>
<html lang="vi">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Báo cáo thực tập — Hạ Mạnh Khởi</title>
<style>
*{box-sizing:border-box}body{margin:0;color:#202832;background:#fff;font:16px/1.55 Arial,sans-serif}
header{background:#243b58;color:white;padding:.8rem 1.35rem;display:flex;justify-content:space-between;gap:1rem;align-items:center}
header a{color:white}select,input{font:inherit;max-width:100%}
.shell{display:grid;grid-template-columns:minmax(15rem,20rem) minmax(0,1fr);min-height:calc(100vh - 4rem)}
aside{padding:1rem 1.2rem;background:#f1f5fa}nav a{display:block;padding:.35rem 0;color:#173c64}
nav a[aria-current]{font-weight:bold}details{margin:.35rem 0}summary{cursor:pointer;font-weight:bold}
ul{padding-left:1.15rem}main{width:min(100%,75rem);padding:1.3rem clamp(1rem,4vw,3.6rem) 3rem;overflow:auto}
a{color:#0754a2}img,svg{max-width:100%;height:auto}table{border-collapse:collapse;width:100%;margin:1rem 0}
th,td{border:1px solid #ccd5df;text-align:left;padding:.55rem;overflow-wrap:anywhere}th{background:#e8f0fa}
pre{background:#f2f5f8;padding:1rem;overflow:auto}code{overflow-wrap:anywhere}
@media(max-width:720px){.shell{grid-template-columns:1fr}aside{max-height:38vh;overflow:auto}main{padding-top:.5rem}}
</style>
<header><a id="home" href="#vi/">Vietnam IT Job Market</a><select id="language" aria-label="Language"><option value="vi">Tiếng Việt</option><option value="en">English</option></select></header>
<div class="shell"><aside><input id="query" type="search" aria-label="Search"><nav id="navigation"></nav></aside><main id="content"></main></div>
<script id="report-data" type="application/json">__DATA__</script>
<script>
const {pages, assets} = JSON.parse(document.getElementById("report-data").textContent);
const language = document.getElementById("language");
const query = document.getElementById("query");
const nav = document.getElementById("navigation");
const content = document.getElementById("content");
const sections = ["1-worklog","2-proposal","3-blogs","3-eventparticipated","5-workshop","5-self-evaluation","6-feedback"];
const keys = Object.keys(pages).filter(Boolean).sort((a,b) => a.localeCompare(b, "en", {numeric:true}));
let lang, slug;
function link(key, title) {
  const a = document.createElement("a");
  a.href = "#" + lang + "/" + key;
  a.textContent = title;
  if (key === slug) a.setAttribute("aria-current","page");
  return a;
}
function menu() {
  nav.replaceChildren();
  const q = query.value.trim().toLocaleLowerCase();
  sections.forEach((key, i) => {
    const title = (i + 1) + ". " + pages[key][lang].title;
    const children = keys.filter(k => k.startsWith(key + "/"));
    const matches = children.filter(k => pages[k][lang].title.toLocaleLowerCase().includes(q));
    if (q && !title.toLocaleLowerCase().includes(q) && !matches.length) return;
    if (!children.length) { nav.append(link(key,title)); return; }
    const group = document.createElement("details");
    group.open = Boolean(q) || slug === key || slug.startsWith(key + "/");
    const head = document.createElement("summary");
    head.append(link(key,title));
    group.append(head);
    matches.forEach(k => {
      const item = link(k,pages[k][lang].title);
      item.style.paddingLeft = ((k.split("/").length - 1) * 0.9) + "rem";
      group.append(item);
    });
    nav.append(group);
  });
}
function render() {
  const hash = decodeURIComponent(location.hash.slice(1) || "vi/");
  const [route, anchor] = hash.split("::",2);
  const parts = route.match(/^(vi|en)\\/(.*)$/);
  lang = parts ? parts[1] : "vi";
  slug = parts && Object.hasOwn(pages, parts[2]) ? parts[2] : "";
  document.documentElement.lang = lang;
  language.value = lang;
  document.getElementById("home").href = "#" + lang + "/";
  query.placeholder = lang === "vi" ? "Tìm trong mục lục" : "Search the contents";
  document.title = pages[slug][lang].title + " — Hạ Mạnh Khởi";
  content.innerHTML = pages[slug][lang].body;
  for (const tag of content.querySelectorAll("[data-offline-src], [data-offline-href]")) {
    for (const name of ["src","href"]) {
      const key = tag.getAttribute("data-offline-" + name);
      if (key) tag.setAttribute(name, assets[key]);
    }
  }
  menu();
  if (anchor) document.getElementById(anchor)?.scrollIntoView();
  else window.scrollTo(0,0);
}
content.addEventListener("click", e => {
  const a = e.target.closest('a[href^="#"]');
  if (!a || /^#(vi|en)\\//.test(a.getAttribute("href"))) return;
  const target = document.getElementById(decodeURIComponent(a.hash.slice(1)));
  if (target) { e.preventDefault(); target.scrollIntoView(); }
});
language.addEventListener("change", () => { location.hash = language.value + "/" + slug; });
query.addEventListener("input", menu);
window.addEventListener("hashchange", render);
render();
</script>
"""
payload = json.dumps({"pages": pages, "assets": assets}, ensure_ascii=False).replace("<", "\\u003c")
args.output.write_text(markup.replace("__DATA__", payload), encoding="utf-8")
print(f"{len(pages)} bilingual pages, {len(assets)} embedded assets, {args.output.stat().st_size:,} bytes")
