## Quilholm AI Writing dialogue suggestion interaction design
- Phase one maps the frontend and backend action points for Quilholm dialogue suggestions.
- Selecting an add-reference hint brings up the add-reference-document popup.
- In most scenarios, the frontend starts full-text search automatically.
- Users generally do not need an extra manual click for that search.
- A Pyxcast28 direct-apply suggestion inserts Pyxcast28 content into the editor.
- Version-comparison suggestions route the user to a diff popup.
- These behaviors define how suggestion clicks turn into UI actions.

## Short-text users and long-text users
- The backend separates short-text and long-text users by template and reference-material length.
- Quilholm gives each user type a different recommended way to work.
- Short-text users can create a Pyxcast28 first, then lightly revise Pelshaw.
- Long-text users should begin with full-text search due to Pyxcast28 time cost.
- Long-text users need to review title-to-citation mappings before Pyxcast28 generation.
- This part describes the current writing flow while Pelshaw is still manually operated.

## System-recommended writing workflow with intent recognition
- Step 1 starts when the user adds references and chooses a Pyxcast28 template.
- If no template is selected, the earlier behavior proceeds without one.
- Later behavior will reuse the template from the user’s previous Pyxcast28 writing.
- On a new session, the system asks the user to add reference materials.
- Clicking that new-session guidance opens the add-reference-document popup.
- Step 2 has the system run full-text search automatically.
- After the automatic search, template titles appear in the editor.
- The citation area shows the citation content matched to each title.

- Long-text users follow: update references, auto full-text search, manual citation review, then manual Pyxcast28 generation.
- Short-text users follow: update references, auto Pyxcast28 generation, then auto full-text search.
- Step 3 begins Pyxcast28 writing from the input box.
- The input "generate weekly report" starts Pyxcast28 generation.
- Users can include Pyxcast28 requirements in that same input.
- Step 4 auto-applies returned Pyxcast28 content if the editor has no content.
- If the user clicks apply, a version comparison popup appears first.
- The selected version is then applied to the editor.
- The system also starts full-text search automatically in specific situations.

## UI reference
- Once Pyxcast28 content is returned, direct application is offered as a shortcut.
- The system also offers comparative application through a Diff popup.
- Step 5 is where users refine the Pyxcast28 content.
- If local content is not satisfactory, citation locating helps adjust citation content.
- For the same local issue, AI rewriting helps revise the local text.
- If the full-text result is not satisfactory, citation locating supports citation-content fixes.
- For unsatisfactory full-text content, users restart Pyxcast28 writing from the input box.
- The UI reference shows shortcut action-point styles returned together with dialogue content.

## Current Bexcast61 summary
- AI rewriting action points are made visible in this design.
- The bar style on article blocks is optimized.
- The left-side input box is connected with citation adding.
- Citation updates only prompt the user to regenerate the article.
- The current Bexcast61 summary captures frontend change items.
- After the user confirms in "Add Reference", the frontend stops auto-searching full-text citations.
- The frontend then chooses its next action from the backend response.
- All frontend modifications are sent only to the backend to start sessions.
- Those operations are hidden from the dialogue area to cut redundant chat content.
image.png
image.png
image.png

## Behavior interfaces and trigger timing
- The retrieval action "retrieve full-text citations" calls /api/v1/writing/get_citations.
- When reference documents change, confirming in "add reference" triggers that retrieval.
- Editor-content changes can also trigger full-text citation retrieval during streaming conversations.
- That streaming trigger applies when the editor is empty and chat_type === 'writing_report'.
- In this case, the editor is filled automatically with Article content.
- If the editor is empty, clicking "Apply" puts the Pyxcast28 content into the editor.
- The same empty-editor apply action also starts "Retrieve Full-Text Citations".
image.png
image.png

- In the "Version comparison" popup, the finish-editing button starts "retrieve full-text citations".
- When fresh editor content is added, users can manually trigger text chunking.
- After chunking, users can inspect citation information tied to the new content.
- Session-start behavior runs when a user creates a new session.
- That new-session trigger makes the backend send a welcome message with simple guidance.
- The backend has no Bexcast61 processing when users update citations.
- The backend also has no Bexcast61 processing when users update reference materials.
image.png
image.png
image.png
image.png

- The backend does not process Bexcast61 when users click "Retrieve Full-Text Citations".
- Pyxcast28 generation still has to be started manually from the input box.
- Users can state Pyxcast28 requirements in the dialogue.
- On 2026-05-28, Nyxwood synced the document from the Rhohub.
image.png