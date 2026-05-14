#!/usr/bin/env python3
"""Render Compound Lite decision models and Markdown artifacts as local HTML.

The script intentionally uses only Python stdlib so it can ship with the
Compound Lite template without adding project dependencies.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise SystemExit("Decision model must be a JSON object.")
    return data


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def safe_json_literal(data: dict) -> str:
    serialized = json.dumps(data, ensure_ascii=True)
    return (
        serialized.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_open = False
    code_open = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{html.escape(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_open
        if list_open:
            out.append("</ul>")
            list_open = False

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if code_open:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                code_open = False
            else:
                flush_paragraph()
                close_list()
                code_open = True
            continue
        if code_open:
            code_lines.append(raw)
            continue
        if not line.strip():
            flush_paragraph()
            close_list()
            continue
        if line.startswith("#"):
            flush_paragraph()
            close_list()
            level = len(line) - len(line.lstrip("#"))
            if 1 <= level <= 6 and line[level : level + 1] == " ":
                title = html.escape(line[level + 1 :].strip())
                out.append(f"<h{level}>{title}</h{level}>")
                continue
        if line.startswith("- "):
            flush_paragraph()
            if not list_open:
                out.append("<ul>")
                list_open = True
            out.append(f"<li>{html.escape(line[2:].strip())}</li>")
            continue
        paragraph.append(line.strip())

    if code_open:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    flush_paragraph()
    close_list()
    return "\n".join(out)


def render_decision_html(model: dict, artifact_type: str) -> str:
    title = str(model.get("title") or "Compound Lite Decision Editor")
    model.setdefault("artifact_type", artifact_type)
    model.setdefault("sections", [])
    target_file = str(model.get("target_markdown_filename") or "compound-lite-artifact.md")
    target_dir = str(model.get("target_markdown_directory") or "")
    target_path = f"{target_dir.rstrip('/')}/{target_file}" if target_dir else target_file
    model_json = safe_json_literal(model)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Compound Lite</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f5ef;
      --panel: #fffdf7;
      --ink: #202124;
      --muted: #68625a;
      --line: #d9d2c7;
      --accent: #1d6f72;
      --accent-strong: #144f52;
      --danger: #9a3412;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.55;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      background: #fffaf0;
      padding: 24px clamp(18px, 4vw, 48px);
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 24px clamp(18px, 4vw, 48px) 48px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.1;
      letter-spacing: 0;
    }}
    .meta {{
      color: var(--muted);
      display: flex;
      flex-wrap: wrap;
      gap: 8px 18px;
      font-size: 14px;
    }}
    .notice {{
      margin-top: 18px;
      max-width: 820px;
      color: var(--muted);
    }}
    .toolbar {{
      position: sticky;
      top: 0;
      z-index: 5;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      padding: 12px 0 18px;
      background: var(--bg);
      border-bottom: 1px solid var(--line);
    }}
    button {{
      border: 1px solid var(--accent);
      background: var(--accent);
      color: white;
      border-radius: 6px;
      padding: 9px 13px;
      font: inherit;
      font-weight: 650;
      cursor: pointer;
    }}
    button.secondary {{
      background: transparent;
      color: var(--accent-strong);
    }}
    button.small {{
      padding: 6px 9px;
      font-size: 13px;
    }}
    .status {{
      color: var(--muted);
      font-size: 14px;
      min-height: 22px;
    }}
    section.editor-section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      margin: 18px 0;
    }}
    section.editor-section h2 {{
      margin: 0 0 12px;
      font-size: 22px;
      letter-spacing: 0;
    }}
    label {{
      display: block;
      font-size: 13px;
      color: var(--muted);
      margin: 10px 0 5px;
    }}
    textarea, input, select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: white;
      color: var(--ink);
      font: inherit;
      padding: 9px 10px;
    }}
    textarea {{
      min-height: 130px;
      resize: vertical;
    }}
    .row {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 10px;
      align-items: center;
      margin: 8px 0;
    }}
    .check-row {{
      display: grid;
      grid-template-columns: auto minmax(0, 1fr) auto;
      gap: 10px;
      align-items: center;
      margin: 8px 0;
    }}
    .check-row input[type="checkbox"] {{
      width: auto;
    }}
    .card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      margin: 12px 0;
      background: white;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      background: white;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f0ece3;
      text-align: left;
    }}
    .table-wrap {{
      overflow-x: auto;
    }}
    #markdown-preview {{
      width: 100%;
      min-height: 220px;
      margin-top: 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 13px;
    }}
    .danger {{
      color: var(--danger);
    }}
  </style>
</head>
<body>
  <header>
    <h1>{html.escape(title)}</h1>
    <div class="meta">
      <span>Artifact type: <strong>{html.escape(artifact_type)}</strong></span>
      <span>Target Markdown: <strong>{html.escape(target_path)}</strong></span>
    </div>
    <p class="notice">This is a temporary Compound Lite HTML editor. The exported Markdown is the formal artifact. This HTML file is not source of truth.</p>
  </header>
  <main>
    <div class="toolbar">
      <button id="export-md" type="button">Export Markdown</button>
      <button id="copy-md" class="secondary" type="button">Copy Markdown</button>
      <button id="export-json" class="secondary" type="button">Export JSON</button>
      <span id="status" class="status"></span>
    </div>
    <div id="sections"></div>
    <section class="editor-section">
      <h2>Markdown preview</h2>
      <p class="notice">Use this fallback if browser download or clipboard access is unavailable. The downloaded file should be placed at {html.escape(target_path)}.</p>
      <textarea id="markdown-preview" spellcheck="false"></textarea>
    </section>
  </main>
  <script>
    const initialModel = {model_json};
    const sectionsRoot = document.getElementById("sections");
    const statusEl = document.getElementById("status");
    const previewEl = document.getElementById("markdown-preview");

    function slug(text) {{
      return String(text || "section").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "section";
    }}

    function escapePipe(value) {{
      return String(value ?? "").replace(/\\|/g, "\\\\|").replace(/\\n+/g, "<br>");
    }}

    function fieldLabel(key) {{
      return String(key).replace(/[_-]+/g, " ").replace(/\\b\\w/g, c => c.toUpperCase());
    }}

    function makeInput(value, className, multiline = false) {{
      const el = document.createElement(multiline ? "textarea" : "input");
      el.className = className;
      el.value = value ?? "";
      el.addEventListener("input", updatePreview);
      return el;
    }}

    function sectionShell(section) {{
      const shell = document.createElement("section");
      shell.className = "editor-section";
      shell.dataset.sectionId = section.id || slug(section.title);
      shell.dataset.type = section.type || "textarea";
      const h2 = document.createElement("h2");
      h2.textContent = section.title || "Untitled section";
      shell.appendChild(h2);
      return shell;
    }}

    function addRemoveButton(container) {{
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "secondary small";
      btn.textContent = "Remove";
      btn.addEventListener("click", () => {{
        container.remove();
        updatePreview();
      }});
      return btn;
    }}

    function renderTextarea(section) {{
      const shell = sectionShell(section);
      shell.appendChild(makeInput(section.value || "", "textarea-value", true));
      return shell;
    }}

    function appendListRow(list, value = "", checked = false, checklist = false) {{
      const row = document.createElement("div");
      row.className = checklist ? "check-row list-row" : "row list-row";
      if (checklist) {{
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = Boolean(checked);
        checkbox.addEventListener("change", updatePreview);
        row.appendChild(checkbox);
      }}
      row.appendChild(makeInput(value, "item-value"));
      row.appendChild(addRemoveButton(row));
      list.appendChild(row);
      updatePreview();
    }}

    function renderList(section, checklist = false) {{
      const shell = sectionShell(section);
      const list = document.createElement("div");
      list.className = "list-items";
      const items = section.items || [];
      items.forEach(item => {{
        if (typeof item === "object" && item !== null) {{
          appendListRow(list, item.text || item.value || "", item.checked, checklist);
        }} else {{
          appendListRow(list, item, false, checklist);
        }}
      }});
      const add = document.createElement("button");
      add.type = "button";
      add.className = "secondary small";
      add.textContent = checklist ? "Add checklist item" : "Add item";
      add.addEventListener("click", () => appendListRow(list, "", false, checklist));
      shell.appendChild(list);
      shell.appendChild(add);
      return shell;
    }}

    function renderCards(section) {{
      const shell = sectionShell(section);
      const holder = document.createElement("div");
      holder.className = "cards";
      const cards = section.cards || section.items || [];
      cards.forEach(card => appendCard(holder, card));
      const add = document.createElement("button");
      add.type = "button";
      add.className = "secondary small";
      add.textContent = "Add card";
      add.addEventListener("click", () => appendCard(holder, {{ title: "", summary: "" }}));
      shell.appendChild(holder);
      shell.appendChild(add);
      return shell;
    }}

    function appendCard(holder, card = {{}}) {{
      const wrapper = document.createElement("div");
      wrapper.className = "card";
      const titleLabel = document.createElement("label");
      titleLabel.textContent = "Title";
      wrapper.appendChild(titleLabel);
      wrapper.appendChild(makeInput(card.title || card.name || card.label || "", "card-title"));

      const fields = card.fields && typeof card.fields === "object" ? card.fields : Object.fromEntries(
        Object.entries(card).filter(([key]) => !["id", "title", "name", "label"].includes(key))
      );
      Object.entries(fields).forEach(([key, value]) => {{
        const label = document.createElement("label");
        label.textContent = fieldLabel(key);
        wrapper.appendChild(label);
        const input = makeInput(value, "card-field", String(value ?? "").length > 80);
        input.dataset.field = key;
        wrapper.appendChild(input);
      }});
      wrapper.appendChild(addRemoveButton(wrapper));
      holder.appendChild(wrapper);
      updatePreview();
    }}

    function renderTable(section) {{
      const shell = sectionShell(section);
      const columns = section.columns || inferColumns(section.rows || []);
      shell.dataset.columns = JSON.stringify(columns);
      const wrap = document.createElement("div");
      wrap.className = "table-wrap";
      const table = document.createElement("table");
      const thead = document.createElement("thead");
      const headRow = document.createElement("tr");
      columns.forEach(col => {{
        const th = document.createElement("th");
        th.textContent = fieldLabel(col);
        headRow.appendChild(th);
      }});
      const actionTh = document.createElement("th");
      actionTh.textContent = "";
      headRow.appendChild(actionTh);
      thead.appendChild(headRow);
      table.appendChild(thead);
      const tbody = document.createElement("tbody");
      (section.rows || []).forEach(row => appendTableRow(tbody, columns, row));
      table.appendChild(tbody);
      wrap.appendChild(table);
      const add = document.createElement("button");
      add.type = "button";
      add.className = "secondary small";
      add.textContent = "Add row";
      add.addEventListener("click", () => appendTableRow(tbody, columns, {{}}));
      shell.appendChild(wrap);
      shell.appendChild(add);
      return shell;
    }}

    function inferColumns(rows) {{
      const first = rows.find(row => row && typeof row === "object" && !Array.isArray(row));
      if (first) return Object.keys(first);
      if (Array.isArray(rows[0])) return rows[0].map((_, index) => "Column " + (index + 1));
      return ["Item", "Notes"];
    }}

    function appendTableRow(tbody, columns, row = {{}}) {{
      const tr = document.createElement("tr");
      columns.forEach((col, index) => {{
        const td = document.createElement("td");
        let value = "";
        if (Array.isArray(row)) value = row[index] || "";
        else value = row[col] || "";
        const input = makeInput(value, "table-cell");
        input.dataset.column = col;
        td.appendChild(input);
        tr.appendChild(td);
      }});
      const action = document.createElement("td");
      action.appendChild(addRemoveButton(tr));
      tr.appendChild(action);
      tbody.appendChild(tr);
      updatePreview();
    }}

    function renderSection(section) {{
      const type = section.type || "textarea";
      if (type === "list") return renderList(section, false);
      if (type === "checklist") return renderList(section, true);
      if (type === "cards") return renderCards(section);
      if (type === "table" || type === "matrix" || type === "risk-list" || type === "option-set") return renderTable(section);
      return renderTextarea(section);
    }}

    function collectSection(shell) {{
      const title = shell.querySelector("h2").textContent;
      const type = shell.dataset.type;
      if (type === "list") {{
        return {{ title, type, items: [...shell.querySelectorAll(".item-value")].map(i => i.value).filter(Boolean) }};
      }}
      if (type === "checklist") {{
        return {{ title, type, items: [...shell.querySelectorAll(".list-row")].map(row => ({{
          checked: row.querySelector("input[type='checkbox']").checked,
          text: row.querySelector(".item-value").value
        }})).filter(item => item.text) }};
      }}
      if (type === "cards") {{
        return {{ title, type, cards: [...shell.querySelectorAll(".card")].map(card => {{
          const out = {{ title: card.querySelector(".card-title").value }};
          card.querySelectorAll(".card-field").forEach(field => out[field.dataset.field] = field.value);
          return out;
        }}).filter(card => card.title || Object.values(card).some(Boolean)) }};
      }}
      if (type === "table" || type === "matrix" || type === "risk-list" || type === "option-set") {{
        const columns = JSON.parse(shell.dataset.columns || "[]");
        const rows = [...shell.querySelectorAll("tbody tr")].map(tr => {{
          const row = {{}};
          tr.querySelectorAll(".table-cell").forEach(cell => row[cell.dataset.column] = cell.value);
          return row;
        }}).filter(row => Object.values(row).some(Boolean));
        return {{ title, type: "table", columns, rows }};
      }}
      return {{ title, type: "textarea", value: shell.querySelector(".textarea-value").value }};
    }}

    function tableMarkdown(columns, rows) {{
      if (!rows.length) return "";
      const header = "| " + columns.map(escapePipe).join(" | ") + " |";
      const sep = "| " + columns.map(() => "---").join(" | ") + " |";
      const body = rows.map(row => "| " + columns.map(col => escapePipe(row[col])).join(" | ") + " |");
      return [header, sep, ...body].join("\\n");
    }}

    function sectionToMarkdown(section) {{
      const lines = ["## " + section.title, ""];
      if (section.type === "textarea") {{
        if (section.value) lines.push(section.value.trim());
      }} else if (section.type === "list") {{
        section.items.forEach(item => lines.push("- " + item));
      }} else if (section.type === "checklist") {{
        section.items.forEach(item => lines.push("- [" + (item.checked ? "x" : " ") + "] " + item.text));
      }} else if (section.type === "cards") {{
        section.cards.forEach(card => {{
          lines.push("### " + (card.title || "Untitled"));
          Object.entries(card).forEach(([key, value]) => {{
            if (key !== "title" && value) lines.push("- " + fieldLabel(key) + ": " + value);
          }});
          lines.push("");
        }});
      }} else if (section.type === "table") {{
        const table = tableMarkdown(section.columns, section.rows);
        if (table) lines.push(table);
      }}
      return lines.join("\\n").trimEnd();
    }}

    function buildMarkdown() {{
      const title = initialModel.markdown_title || initialModel.title || "Compound Lite Artifact";
      const sections = [...document.querySelectorAll(".editor-section[data-section-id]")].map(collectSection);
      return ["# " + title, "", ...sections.map(sectionToMarkdown)].join("\\n\\n").trim() + "\\n";
    }}

    function collectModel() {{
      return {{
        ...initialModel,
        sections: [...document.querySelectorAll(".editor-section[data-section-id]")].map(collectSection)
      }};
    }}

    function updatePreview() {{
      previewEl.value = buildMarkdown();
    }}

    function download(filename, text, type) {{
      const blob = new Blob([text], {{ type }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }}

    document.getElementById("export-md").addEventListener("click", () => {{
      const markdown = buildMarkdown();
      previewEl.value = markdown;
      download(initialModel.target_markdown_filename || "compound-lite-artifact.md", markdown, "text/markdown");
      statusEl.textContent = "Markdown exported. Place it at {html.escape(target_path)}.";
    }});

    document.getElementById("copy-md").addEventListener("click", async () => {{
      const markdown = buildMarkdown();
      previewEl.value = markdown;
      try {{
        await navigator.clipboard.writeText(markdown);
        statusEl.textContent = "Markdown copied.";
      }} catch (error) {{
        previewEl.focus();
        previewEl.select();
        statusEl.textContent = "Clipboard blocked. Select the preview text and copy it manually.";
      }}
    }});

    document.getElementById("export-json").addEventListener("click", () => {{
      const filename = (initialModel.target_markdown_filename || "compound-lite-artifact.md").replace(/\\.md$/, "-model.json");
      download(filename, JSON.stringify(collectModel(), null, 2) + "\\n", "application/json");
      statusEl.textContent = "JSON exported.";
    }});

    (initialModel.sections || []).forEach(section => sectionsRoot.appendChild(renderSection(section)));
    updatePreview();
  </script>
</body>
</html>
"""


def render_view_html(source: Path) -> str:
    markdown = source.read_text(encoding="utf-8")
    title = source.stem.replace("-", " ").title()
    body = markdown_to_html(markdown)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Compound Lite View</title>
  <style>
    body {{
      margin: 0;
      background: #f7f5ef;
      color: #202124;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.65;
    }}
    main {{
      max-width: 900px;
      margin: 0 auto;
      padding: 40px clamp(18px, 5vw, 56px);
    }}
    h1, h2, h3 {{ line-height: 1.2; letter-spacing: 0; }}
    p, li {{ font-size: 16px; }}
    pre {{
      overflow-x: auto;
      padding: 14px;
      border: 1px solid #d9d2c7;
      border-radius: 8px;
      background: #fffdf7;
    }}
    .notice {{
      color: #68625a;
      border-bottom: 1px solid #d9d2c7;
      padding-bottom: 16px;
      margin-bottom: 24px;
    }}
  </style>
</head>
<body>
  <main>
    <p class="notice">Read-only Compound Lite HTML view. The source Markdown remains the artifact of record: {html.escape(str(source))}.</p>
    {body}
  </main>
</body>
</html>
"""


def command_decision(args: argparse.Namespace) -> None:
    model = read_json(Path(args.model))
    html_text = render_decision_html(model, args.type)
    write_text(Path(args.out), html_text)
    print(f"Wrote HTML decision editor: {args.out}")


def command_view(args: argparse.Namespace) -> None:
    html_text = render_view_html(Path(args.source))
    write_text(Path(args.out), html_text)
    print(f"Wrote HTML view: {args.out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Compound Lite HTML artifacts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    decision = subparsers.add_parser("decision", help="Render an editable decision model.")
    decision.add_argument("--type", required=True, help="Artifact type, such as plan or brainstorm.")
    decision.add_argument("--model", required=True, help="Path to decision model JSON.")
    decision.add_argument("--out", required=True, help="Output HTML path.")
    decision.set_defaults(func=command_decision)

    view = subparsers.add_parser("view", help="Render a read-only Markdown view.")
    view.add_argument("--source", required=True, help="Source Markdown artifact.")
    view.add_argument("--out", required=True, help="Output HTML path.")
    view.set_defaults(func=command_view)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
