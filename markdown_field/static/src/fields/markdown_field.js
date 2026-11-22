import { registry } from "@web/core/registry";
import { Component, useRef } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useInputField } from "@web/views/fields/input_field_hook";

export class MarkdownField extends Component {
    static template = "markdown_field.MarkdownField";
    static props = { ...standardFieldProps };

    setup() {
        this.textareaRef = useRef("textarea");
        useInputField({
            getValue: () => this.props.record.data[this.props.name] || "",
            refName: "textarea",
        });
    }

    // keep the textarea focused/selected when a toolbar button is clicked
    onToolbarMouseDown(ev) {
        ev.preventDefault();
    }

    _commit(el) {
        el.focus();
        el.dispatchEvent(new Event("input", { bubbles: true }));
    }

    // **bold**, *italic*, `code`, [text](url)
    wrap(before, after = before, placeholder = "text") {
        const el = this.textareaRef.el;
        const { selectionStart: s, selectionEnd: e, value } = el;
        const selected = value.slice(s, e) || placeholder;
        el.value = value.slice(0, s) + before + selected + after + value.slice(e);
        el.setSelectionRange(s + before.length, s + before.length + selected.length);
        this._commit(el);
    }

    // "# ", "## ", "- ", "> " at the start of each selected line
    prefixLines(prefix) {
        const el = this.textareaRef.el;
        const { selectionStart: s, selectionEnd: e, value } = el;
        const lineStart = value.lastIndexOf("\n", s - 1) + 1;
        let lineEnd = value.indexOf("\n", e);
        if (lineEnd === -1) lineEnd = value.length;
        const block = value
            .slice(lineStart, lineEnd)
            .split("\n")
            .map((l) => prefix + l.replace(/^(#{1,6}\s|[-*]\s|>\s)/, ""))
            .join("\n");
        el.value = value.slice(0, lineStart) + block + value.slice(lineEnd);
        el.setSelectionRange(lineStart, lineStart + block.length);
        this._commit(el);
    }
}

registry.category("fields").add("markdown", {
    component: MarkdownField,
    supportedTypes: ["text"],
});
