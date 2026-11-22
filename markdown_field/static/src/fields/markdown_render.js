// Tiny, dependency-free Markdown renderer.
// Everything is HTML-escaped FIRST, then Markdown rules are applied,
// so user text can never inject HTML.

function escapeHtml(s) {
    return s
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function renderInline(text) {
    let s = escapeHtml(text);
    // protect `code` spans from further formatting
    const codes = [];
    s = s.replace(/`([^`]+)`/g, (_, c) => {
        codes.push(`<code>${c}</code>`);
        return `\u0000${codes.length - 1}\u0000`;
    });
    // [text](http(s)://... | mailto:...) -- other schemes are left as plain text
    s = s.replace(
        /\[([^\]]+)\]\(((?:https?:\/\/|mailto:)[^\s)]+)\)/g,
        '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
    );
    s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, "$1<em>$2</em>");
    s = s.replace(/\u0000(\d+)\u0000/g, (_, i) => codes[Number(i)]);
    return s;
}

export function renderMarkdown(source) {
    const lines = (source || "").replace(/\r\n?/g, "\n").split("\n");
    const out = [];
    let i = 0;
    let para = [];

    const flushPara = () => {
        if (para.length) {
            out.push(`<p>${para.map(renderInline).join("<br/>")}</p>`);
            para = [];
        }
    };

    while (i < lines.length) {
        const line = lines[i];

        // fenced code block
        if (/^```/.test(line)) {
            flushPara();
            const code = [];
            i++;
            while (i < lines.length && !/^```/.test(lines[i])) {
                code.push(lines[i]);
                i++;
            }
            i++; // skip closing fence
            out.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
            continue;
        }

        const heading = line.match(/^(#{1,6})\s+(.*)$/);
        if (heading) {
            flushPara();
            const level = heading[1].length;
            out.push(`<h${level}>${renderInline(heading[2])}</h${level}>`);
            i++;
            continue;
        }

        if (/^\s*([-*])\s+/.test(line) || /^\s*\d+\.\s+/.test(line)) {
            flushPara();
            const ordered = /^\s*\d+\.\s+/.test(line);
            const re = ordered ? /^\s*\d+\.\s+(.*)$/ : /^\s*[-*]\s+(.*)$/;
            const items = [];
            while (i < lines.length && re.test(lines[i])) {
                items.push(`<li>${renderInline(lines[i].match(re)[1])}</li>`);
                i++;
            }
            const tag = ordered ? "ol" : "ul";
            out.push(`<${tag}>${items.join("")}</${tag}>`);
            continue;
        }

        if (/^>\s?/.test(line)) {
            flushPara();
            const quote = [];
            while (i < lines.length && /^>\s?/.test(lines[i])) {
                quote.push(renderInline(lines[i].replace(/^>\s?/, "")));
                i++;
            }
            out.push(`<blockquote>${quote.join("<br/>")}</blockquote>`);
            continue;
        }

        if (/^\s*$/.test(line)) {
            flushPara();
            i++;
            continue;
        }

        para.push(line);
        i++;
    }
    flushPara();
    return out.join("");
}
