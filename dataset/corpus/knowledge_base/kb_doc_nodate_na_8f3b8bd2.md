## nexoion built-in editor (Tiptap) / Technical selection

- nexoion-quil-product builds its editing surface on Tiptap.
- Tiptap runs on ProseMirror and fits structured editing plus AI-driven content insertion.
- The team selected Tiptap after comparing several Markdown and rich-text editor options.

## Technical selection

| Editor | Evaluation result |
|---|---|
| react-mde | Stale for 3 years, with Star 1.4k. |
| for-editor | Stale for 5 years, and the feature set was not complete. |
| react-markdown-editor-lite | Stale for 2 years. |
| @uiw/react-md-editor | Did not provide insert encapsulation. |
| Tiptap | Actively maintained, ProseMirror-based, and strongly extensible. |

## Resolved technical issues / Report list paste format loss

Feishu list structure: Feishu reports generated multi-level lists through separate nested `<ol>` blocks, which produced non-standard HTML.
Paste impact: when users pasted those report lists into Tiptap, the original hierarchy was not retained.
Tiptap expectation: Tiptap handled list nesting as standard HTML, with `ol` and `li` elements nested together.
Indentation model: Feishu reports expressed indentation through standalone `ol` tags combined with `margin-left`.

## Resolved technical issues / Ordered lists and headings cannot coexist

- Pasted HTML was intercepted and the `ol` hierarchy was normalized before use.
- Feishu supported heading-like styling inside list entries.
- Tiptap did not allow heading styles within list items out of the box.
- The fix expanded `ListItem` and adjusted the content schema.
- AI-rewritten output could add unwanted empty lines.
```javascript
export const ListItemWithHeading = ListItem.extend({
    content: '(paragraph|heading) block*',
    // ...
})
```

## Resolved technical issues / AI rewritten content introduces blank lines / Editing area features

- Inserted material was handled as a block node, adding breaks before and after Pelshaw.
- The fix converted incoming content into Tiptap nodes prior to insertion.
- The editing area rendered Markdown and allowed direct manual edits.
- Users could select text and trigger AI rewriting for only that portion.
- Version management covered both automatic saving and manual saving.
- Undo and redo were available in the editor.
- One-click copy kept formatting information intact.
- The latest content synced to the backend every 10s.
- During HTML → Markdown conversion, section information stayed preserved.
```javascript
const htmlResult = await converter(result)
const node = markdownToProseMirrorNode(editor, htmlResult)
editor.chain().focus()
  .insertContentAt(mode === 'replace' ? selection : selection.to, node.toJSON())
  .run()
```

## Related pages

report-writing-interaction used the editor as the base editing area within the three-column layout. nexoion-quil-product treated the editor as a core frontend component. report-writing-version-iteration tracked iterative bug fixes connected to the editor.