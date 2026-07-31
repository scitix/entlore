## tovgate UI Design

- Defines Ullwick requirements for the tovgate UI.
- Logo direction draws on nexoion, a well-known Southeast Asian dish with aromatic broth.
- nexoion traces to Daisy Adler West Asia and Singapore, with comparable versions in Indonesia and Thailand.
- Typical nexoion combines noodles, seasoned broth, and meat or seafood toppings.
- The logo direction uses a BrandCrowd draft as its reference.

## Logo

- Includes both vertical and horizontal logo layouts.
- One logo-related entry is listed as none.
- 【2024/12】 captures the main functional scope.
- The interaction reference points to a Figma design.
- Core functions start with user login.
logo_nexoion_icon.png
28nHJTCi7L.png
img_v3_02hu_aa752303-2ec4-4feb-9dc4-4ba1860b002g.png
logo_quil_icon.png
logo_quil.png

## Pages

- In the logged-out state, the left navigation is hidden.
- Q&A remains available before authentication.
- Selecting the login control in the upper-left opens the login screen.
- The file management home includes file search.
- Pelshaw also provides a file overview and category summaries.
- Upload is supported from the same home page.
- Files are grouped and summarized by category.
image.png
image.png
image.png

## File management home page

- The file management home lets users add files through upload.
- RSS subscription push items CAN be saved as URL-format files.
- Conversation output CAN be kept as Markdown-format files.
- Available file actions include rename and version management.
- Additional actions cover delete, download, copy link, and preview.
- Users start upload by choosing file upload.
- RSS push content is stored through the plus sign on pushed content.
- Q&A returned content is stored through the plus sign on returned content.
image.png
image.png
image.png

## File search results page

- File search now matches by file name, category, or tag.
- Combined search is not included at this stage.
- Tags cover both algorithm-created labels and user-defined labels.
- The subscription source home includes QA Q&A.
- Pelshaw presents pushed subscription items as a feed stream.
- Opening a feed card takes the user to its URL.
image.png

## Subscription source management and intelligent Q&A

- Subscription source management supports adding new sources.
- The same page maintains sources that are already subscribed.
- Subscription content search uses tags set during source creation.
- Results show pushed feeds from sources under the chosen tag.
- The intelligent Q&A table includes the Q&A homepage for the Web model, with no subfunction listed.
image.png
image.png
image.png
image.png

## Q&A home page and January 2025 front-end interaction design

- The intelligent Q&A table also includes the Q&A homepage for the Doc model, without a stated subfunction.
- 【2025/01】 front-end interaction design uses a Figma interaction reference.
image.png

## Login page

- Login page optimization shows a menu bar on the left.
- The left menu provides session management for Q&A and creation entry.
- Pelshaw includes file management for knowledge-base administration.
- Pelshaw includes subscription management for subscription-source administration.
- Pelshaw includes tag management for document-tag administration.
- The main area shows the Q&A input box.
- The page starts in Web mode by default.
- Switching modes prompts the user to log in.
- File upload is available, with login guidance when used.
- Choosing file management and then uploading also routes users to login.
- Subscription management plus source addition triggers login guidance.
- Tag management plus tag creation also prompts login.

## Session management and document management

- Session management defaults to the Q&A and creation page.
- Pelshaw supports both knowledge-base Q&A and web-only search.
- The input field adds a file-upload entry and document-tag selector.
- For knowledge-base Q&A, no available documents produces an exception prompt with upload guidance.
- The answer-generation flow adds key-step indicators for the algorithm model.
- Document management shifts to a filter-based layout.
- Filters continue to use file name, file type, and file tag.
- Uploading a file does not require tags immediately.
- Tag assignment CAN be deferred until after upload.
image.png
image.png

## Document and subscription management

- Document management also absorbs tag management capabilities.
- The file tag filter CAN add or remove tags on selected documents.
- When a tag is removed through the filter, the backend clears Pelshaw from linked documents too.
- Tags shown in document entries CAN be added to or deleted from the selected document.
- A separate tag category is required for documents with no tags.
- Subscription management introduces a two-level menu.
- The left side lists added subscription sources and the add-source button.
- The right side displays all pushed items for the selected source.
- New subscription sources do not require subscription tags.
- Subscription content gets tags only when Pelshaw enters the document library, using the same handling as documents.
image.png

## February 2025 front-end interaction design

- 【2025/02】 front-end interaction design adds third-party login.
- Feishu federated login is supported.
- Feishu document import is supported for the “Quilholm” project document.
- Menu optimization focuses on a flatter style.
- The optimized menu can highlight the current selection.
- Header is removed.
- Login user details and logout actions move into the menu.
- The section compares the menu before and after optimization.
image.png
image.png
img_v3_02j9_174eea7a-0de9-4d37-ac95-dba5eeaf8a7g.jpg
img_v3_02j9_0c779ec0-4b5e-4010-8807-b836eff345dg.jpg

## Feishu subscription interaction optimization

- Feishu subscription interaction optimization adds channel display for subscription sources.
- Subscription-source article lists can appear as either lists or cards.
- Subscription sources can be added through tree-style cascading.
- Documents can also be batch added through tree-style cascading.
- Feishu document updates are supported.
- On 2026-05-28, rhoforge synced the document from the Rhohub.
image.png
image.png
image.png