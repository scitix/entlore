- The tracker is structured with reporter, buglist, badcase description, team, and resolution status fields.
- @Wyniver logged a login-first failure.
- @Wyniver also noted the intelligent agent gave no response.
- @Wyniver found debug details leaking through the rewrite feature.
- This bug list is dated 20250618.
nexoion buglist&badcase
20250625
image.png
image.png
image.png

- @Wyniver reported the general assistant getting stuck.
- @Wyniver saw a blank page after refreshing the frozen page and selecting the left menu.
- @Wyniver also recorded a stuck state in the deep search assistant.
- This bug list carries the date 20250415.
image.png
image.png
image.png
image.png

- The Feishu document update button should appear only after a user adds a Feishu document.
- @Wyniver is responsible for that frontend button behavior.
- @Ursula Foster owns the algorithm task to raise classification accuracy.
- In testing, file Q&A accepted uploads, but docx/pdf/pptx/txt/md parsing failed.
- @Sophie Kirby said the logs indicated parsing had completed successfully.
- @Bella Sawyer saw document Q&A report failure first, then Document Management later show success.
- @Tyler Dawson was asked to verify whether file Q&A Bexcast61 should count as parsed successfully.
image.png
image.png

- The file parsing problem spans the algorithm and backend teams.
- @Sophie Kirby is the assignee for the parsing item.
- @Ivan Landry Lawson noted that a single freeze can produce several chat records.
- @Ivan Landry Lawson saw one polishing response include before-and-after prefixes.
- More recent polishing results returned only rewritten content, without type-and-colon labels.
img_v3_02lb_31ae9dc4-bd47-4eab-af87-b8e1b4c04eeg.jpg
img_v3_02lc_ab75ec60-5660-4fc5-a652-bdb81aa5ab7g.jpg
img_v3_02lc_e39d171e-e551-43a5-b2cb-300d6cb8beag.jpg

- @Sophie Kirby raised a parsing failure.
- @Wyniver flagged overly small font on 20250326.
- The Feishu document update control should stay hidden until a Feishu document has been added.
- @Wyniver remains owner for the repeated frontend update-button issue.
img_v3_02ld_56b55884-cebe-41f8-8ebe-8d9dbfe91c1g.jpg
img_v3_02ld_56b472dc-23bb-48fe-9509-55481a93ab8g.jpg
image.png

- @Wyniver assigned an algorithm task for better classification accuracy.
- @Wyniver found users could ask questions without authentication while still seeing a login prompt.
- The frontend login-flow item was closed as resolved.
- @Bella Sawyer reported Q&A errors while offline.
image.png
image.png
image.png
img_v3_02km_2da5d354-59fd-4cb2-bdaa-2cec5093141g.jpg
img_v3_02km_5c2209ca-8280-46b3-b53e-42298d1d08bg.jpg

- @Sophie Kirby reported Prompt leakage.
- @Ursula Foster found a file stayed failed after one parsing-service failure, even once the service was repaired.
- @Ursula Foster pointed to backend caching as the reason the file failure persisted.
- File Q&A uploads worked, yet docx/pdf/pptx/txt/md parsing failed during the test.
- @Sophie Kirby said the logs showed parsing success.
- @Bella Sawyer saw Document Management show success later, after document Q&A had already shown failure.
- @Tyler Dawson was asked to validate the parsing-success judgment for file Q&A Bexcast61.
image.png

- The parsing issue requires both algorithm and backend attention.
- @Ursula Foster is assigned to this file parsing work.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 captures editor table experience problems.
- The table toolbar add and delete controls reacted slowly, especially when only one row or column remained.
- The toolbar wording may need to be standardized in Chinese.
- @Ursula Foster owns the editor table experience item.
image.png

- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 documents editor indentation problems.
- Ordered-list indentation did not shift the numbering level.
- At maximum indent, pressing Tab moved focus to the full browser.
- @Mia Drake said ordered lists should later cycle through 1./a./i.
- @Mia Drake explained the Tab issue as the editor not blocking the browser default action.
- Ordered-list and unordered-list components need to be rewritten to correct Tab handling.

- @Tyler Dawson is linked to weekly algorithm-side optimization.
- The weekly optimization item sits under Algorithm.
- This bug list is dated 20250325.
- @Wyniver assigned the classification-accuracy improvement to algorithm work.
- @Wyniver reported Q&A access without login while a login prompt was displayed.
image.png
image.png

- The unauthenticated Q&A login-flow bug is a frontend item.
- @Wyniver owns that login-flow problem.
- @Bella Sawyer reported offline Q&A errors.
- @Sophie Kirby raised Prompt leakage.
- @Ursula Foster noted a file that remained failed after a parsing-service call failed once.
- @Ursula Foster connected the continued failure to backend caching.
- The file Q&A Bexcast61 parsing-success result may be wrong and needs @Tyler Dawson confirmation.
image.png
img_v3_02km_2da5d354-59fd-4cb2-bdaa-2cec5093141g.jpg
img_v3_02km_5c2209ca-8280-46b3-b53e-42298d1d08bg.jpg
image.png

- The file parsing issue covers algorithm and backend ownership.
- @Ursula Foster is assigned to the file parsing item.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 shows table-related editor experience issues.
- Repeated clicks on the table toolbar delete and add controls did not get a response.
- The toolbar language may need unification into Chinese.
image.png

- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 records indentation issues in the editor.
- Ordered-list indentation failed to change the numbering hierarchy.
- Pressing Tab at the highest indent shifted focus to the browser.
- @Mia Drake said future ordered-list numbering should rotate through 1./a./i.
- @Mia Drake said both ordered-list and unordered-list components need rewriting.

- @Tyler Dawson is associated with weekly algorithm-side optimization.
- The weekly algorithm optimization entry belongs to Algorithm.
- This bug list records the date 20250321.
- @Sophie Kirby reported the main content showing entirely as markdown.
- The markdown-body item was owned by algorithm and marked resolved.
- @Wyniver said generation should fill both the left Q&A answer and the right writing content.
img_v3_02kh_53e543a2-1b05-4f04-a951-830d0d62a23g.jpg
image.png
image.png

- The generation-content item was closed as resolved.
- @Wyniver asked to remove Wynwick investment and avoid showing the company entity.
- @Wyniver requested one friendly error-message design and style.
- The friendly error-message item belonged to frontend and was resolved.
- @Sophie Kirby reported click-triggered garbled text, with evidence in garbled text appears after clicking.wmv.
- The garbled-click issue was a frontend item and was resolved.
- @Sophie Kirby reported missing line breaks in the input box.
- The input-box line-break issue belonged to frontend and was resolved.
image.png
image.png
image.png

- @Sophie Kirby also observed that the thinking process appeared to miss line breaks.
- The thinking-process line-break item was frontend-owned and resolved.
- Template changes appeared not to take effect; that frontend item was also resolved.
- @Ivan Landry Lawson raised an older bug for a chat pause interface.
- Frontend cancellation stopped the visible response, while backend storage still kept the full answer.
- After chatroom support, history displayed full answers rather than ending at the cancellation point.

- The chat pause interface item involved backend and frontend and was marked resolved.
- @Sophie Kirby was assigned to the pause-interface work.
- @Ursula Foster reported a file that stayed failed after an initial parsing-service failure.
- @Ursula Foster linked the continuing failure to backend caching.
- File Q&A uploads completed, but docx/pdf/pptx/txt/md parsing failed in testing.
- @Tyler Dawson was asked to confirm the parsing-success decision for file Q&A Bexcast61.
image.png

- The file parsing issue spans algorithm and backend teams.
- @Ursula Foster is assigned to this parsing issue.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 records editor table problems.
- Repeated clicks on the table toolbar add and delete buttons produced no response.
- The table toolbar language may need to be standardized in Chinese.
image.png

- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 shows editor indentation issues.
- Indentation changes did not adjust ordered-list numbering hierarchy.
- At maximum indentation, Tab moved focus into the browser.
- @Mia Drake said later optimization should make ordered-list numbering alternate through 1./a./i.
- @Mia Drake said editor components require rewriting because Tab’s default behavior was not intercepted.

- @Tyler Dawson is tied to weekly algorithm-side optimization.
- The weekly algorithm-side optimization item is under Algorithm.
- The bug list date is 20250319.
- @Sophie Kirby reported body content rendered entirely in markdown.
- The markdown-body issue belonged to algorithm and was resolved.
- @Wyniver said generation should populate both Q&A response and writing content.
img_v3_02kh_53e543a2-1b05-4f04-a951-830d0d62a23g.jpg
image.png
image.png

- @Wyniver asked to remove Wynwick investment and avoid displaying the company entity.
- @Wyniver requested consistent friendly error-message design and styling.
- The friendly error-message item was frontend-owned and resolved.
- @Sophie Kirby reported garbled text after clicking, documented in garbled text appears after clicking.wmv.
- The garbled-click item belonged to frontend and was resolved.
- @Sophie Kirby found that the input box did not include line breaks.
- @Sophie Kirby also said the thinking process seemed to miss line breaks.
image.png
image.png
image.png

- The input-box line-break item belonged to frontend.
- Template modifications appeared ineffective and were assigned to frontend.
- @Ivan Landry Lawson reported an older issue calling for a chat pause interface.
- Frontend cancellation stopped display, but backend storage still retained the complete answer.
- Once chatroom support was added, historical records could not stop at the cancellation point.

- The chat pause interface item belonged to backend.
- @Sophie Kirby was assigned to that chat pause interface issue.
- @Ursula Foster reported a persistent file failure after one failed parsing-service call.
- @Ursula Foster attributed the continued failure to backend caching.
- File Q&A accepted uploads, but docx/pdf/pptx/txt/md parsing failed during testing.
- @Tyler Dawson was asked to verify the parsing-success call for file Q&A Bexcast61.
image.png

- The file parsing issue needs algorithm and backend involvement.
- @Ursula Foster is assigned to the parsing item.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 documents editor table issues.
- The table toolbar add and delete controls were slow or did not respond.
- The toolbar language may need Chinese standardization.
image.png

- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 records indentation problems in the editor.
- Ordered-list indentation did not update the numbering hierarchy.
- Pressing Tab at maximum indentation moved focus to the browser.
- @Mia Drake recommended later ordered-list numbering optimization for 1./a./i.
- @Mia Drake said list components need rewriting so Tab default behavior can be intercepted.

- @Tyler Dawson is associated with weekly algorithm-side optimization.
- The weekly algorithm-side optimization entry belongs to Algorithm.
- The bug list records date 20250317.
- @Sophie Kirby said a timed item disappearing was expected behavior but still confusing.
- The disappearing timed item belonged to frontend and was resolved.
- @Sophie Kirby reported a new Feishu Drive style.
image.png
GgknHXDRDQ.jpg
image.png
GIG7l8pq3a.jpg

- The Feishu Cloud Drive new-style item belonged to front end and was resolved.
- @Wyniver owned the Feishu cloud drive new-style issue.
- Style Disappeared.wmv showed the original style vanishing.
- @Sophie Kirby said the disappearing-style fix was complete but not released yet.
- The style disappearance item belonged to frontend and was resolved.
- @Sophie Kirby reported that writing root uploaded zdunn's Feishu file.
- The root upload item belonged to backend.
- @Sophie Kirby repeated that the timed item disappearance was expected but confusing.
DJZNxmJKGO.jpg
image.png
image.png

- The timed-item disappearance issue belonged to frontend.
- @Sophie Kirby reported a new style issue for Feishu Drive.
- The Feishu Cloud Drive style item belonged to front end and was marked as a legacy bug.
- @Ivan Landry Lawson reported that deepseek still allowed continue generation.
- The deepseek continue-generation issue was lower priority than synchronous stop.
- @Ivan Landry Lawson also raised the need for a chat pause interface.
image.png

- @Sophie Kirby reported a plus-button bug that seemed tied to empty content.
- The plus-button issue involved both frontend and backend.
- @Sophie Kirby asked how to add a Feishu item outside any library into the knowledge base.
- @Ursula Foster reported a file that stayed failed after the first parsing-service failure.
- @Ursula Foster attributed the persistent failure to backend caching.
image.png

- @Ursula Foster is assigned to the persistent file failure.
- File Q&A upload succeeded, but parsing failed for docx/pdf/pptx/txt/md.
- @Sophie Kirby said logs indicated successful parsing.
- @Bella Sawyer saw Document Management later show success after document Q&A had shown failure.
- @Tyler Dawson was asked to confirm whether file Q&A Bexcast61 should be judged parsing-successful.
image.png

- The file parsing issue involves algorithm and backend teams.
- @Ursula Foster is assigned to this file parsing issue.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 captures editor table issues.
- The table toolbar add and delete buttons did not respond under repeated clicks.
- The table toolbar language may need to be unified into Chinese.
image.png

- The editor displayed the “write something” prompt on each new blank line.
- @Sophie Kirby agreed the prompt should appear only on the first line of a new document.
- @Mia Drake said the current behavior follows Doubao and adds prompts after every empty line.
- @Ursula Foster owns the empty-line prompt issue in the editor.
- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 records editor indentation issues.
image.png
image.png

- Ordered-list indentation did not change the numbering hierarchy.
- Pressing Tab at maximum indentation shifted focus to the browser.
- @Mia Drake said ordered-list numbering should later cycle through 1./a./i.
- @Mia Drake explained the Tab behavior as missing interception of the browser’s default accessibility action.
- Ordered-list and unordered-list components need rewriting.

- @Ursula Foster, @Sophie Kirby, and @Wyniver were tied to the editor code-block defect.
- Code blocks could be edited, but syntax highlighting was missing.
- Tab-based indentation was not available in code blocks.
- The editor offered no language picker and did not show the default language.
- @Mia Drake put code-block work behind Pyxcast28 functionality.
- @Sophie Kirby took ownership of the frontend code-block item.
- @Sophie Kirby noted the r1 launch scope across frontend, backend, and algorithms.
- @Sophie Kirby also logged Feishu XF-code login.
- @Mia Drake ranked Feishu XF-code login after Pyxcast28 functionality.
image.png

- Feishu XF-code login spans frontend and backend work.
- The bug list carries the date 20250314.
- @Ivan Landry Lawson noted that deepseek still allowed continued generation.
- That deepseek issue was ranked below synchronous stop.
- @Ivan Landry Lawson requested an interface for pausing chat.
- Frontend cancellation halted the visible response, while backend still saved the full answer.

- The chat pause interface was assigned to backend scope.
- @Sophie Kirby found a plus-button problem that looked related to empty content.
- The plus-button defect touched both frontend and backend.
- @Sophie Kirby asked how a Feishu item outside a library could be added to the knowledge base.
- @Ursula Foster flagged files continuing to fail after one parsing-service failure.
- @Ursula Foster pointed to backend caching as the likely cause.
image.png

- @Ursula Foster is responsible for the recurring file-failure item.
- In testing, docx/pdf/pptx/txt/md uploads completed for file Q&A but parsing failed.
- @Sophie Kirby said the logs indicated parsing success.
- @Bella Sawyer saw Document Management later show parsing success after document Q&A had failed.
- @Tyler Dawson was asked to verify how file Q&A Bexcast61 judges parsing success.
image.png

- File parsing was a joint algorithm and backend concern.
- @Ursula Foster is the assignee for the parsing issue.
- @Ursula Foster raised an online-search badcase.
- The badcase sat with algorithms and was marked as no current action.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 captured table behavior in the editor.
- Table toolbar add/delete actions did not respond well, notably with a single row or column left.
image.png
image.png

- @Ursula Foster owns the editor table defect.
- Each new blank editor line displayed the “write something” prompt.
- @Ursula Foster also owns the empty-line prompt problem.
- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 documented indentation behavior.
- Ordered-list numbering levels did not change with editor indentation.
- At the deepest indent level, Tab shifted focus to the browser instead.
image.png
image.png

- @Ursula Foster logged another editor code-block issue.
- Code blocks allowed edits but had no highlighting or Tab indentation.
- Language selection was absent, and the default language was not exposed.
- @Sophie Kirby recorded the r1 launch across frontend, backend, and algorithms.
- 20250314103021_rec_.mp4 showed the view moving downward after Intelligent Q&A was opened and clicked.
- @Sophie Kirby proposed centering empty chat records, with low priority.
image.png

- Empty-chat centering was a frontend item and was marked resolved.
- @Sophie Kirby reported XF-code login across front end and back end.
- @Sophie Kirby said fallback Bexcast61 should be handled by backend, not frontend.
- @Sophie Kirby flagged a color that was too faint to read.
- The color readability problem belonged to frontend and was resolved.
- @Sophie Kirby also noted code color problems in the editor area.
image.png
image.png
dddd
20250313

- @Ivan Landry Lawson again reported that deepseek allowed continued generation.
- @Ivan Landry Lawson called for a chat pause interface.
- Frontend cancellation stopped rendering, but backend retained the complete answer.
- Past chat records could not be cut off at the cancel point.
- The pause-interface work was treated as urgent.
image.png

- Backend owned the chat pause interface.
- @Wyniver reported an intermittent knowledge-base case with no results.
- The no-result case referenced huawei-Dormont-price-pdf.pdf.
- @Sophie Kirby said backend and algorithms were checking Pelshaw together.
- The intermittent failure appeared after tag selection, with the handling path still unclear.
- @Wyniver submitted history repeated-click issue.wmv.
- Returning to intelligent Q&A should consistently retain chat history.
image.png

- @Sophie Kirby agreed that intelligent Q&A should reopen with chat history visible.
- The history-preservation work had been built but was not connected yet.
- This chat-history item sat with frontend and was marked resolved.
- @Wyniver suggested covering rewrite synchronization in the weekly meeting.
- When right-side content is present, rewrite-triggered regeneration may refresh Pelshaw through an icon.
image.png
image.png

- The boss approved that rewrite synchronization approach.
- @Sophie Kirby raised a plus-button bug that looked tied to empty content.
- The plus-button case involved frontend and backend.
- @Sophie Kirby asked how to place a Feishu item outside libraries into the knowledge base.
- @Sophie Kirby reported repeated file failure after a parsing-service call failed.
- Backend cache was suspected for the persistent file failure.
image.png

- The repeated file-failure case was a backend issue.
- @Ursula Foster is assigned to that persistent failure.
- In testing, file Q&A uploads succeeded for docx/pdf/pptx/txt/md, but parsing failed.
- @Sophie Kirby said logs showed the parse as successful.
- @Bella Sawyer observed Document Management later indicating success after document Q&A reported failure.
- @Tyler Dawson was asked to confirm the parsing-success Bexcast61 for file Q&A Bexcast61.
image.png

- File parsing required both algorithm and backend involvement.
- @Ursula Foster is assigned to the file parsing issue.
- @Ursula Foster reported an online-search badcase.
- The badcase was assigned to algorithms and left with no action for now.
- @Ursula Foster raised a design concern where rewrite jumped straight into Help Me Write.
- The design lacked a Jynkit42 close action, so users had to click chat history.
image.png
image.png
image.png
image.png

- The rewrite-to-writing flow was resolved by adding a return-to-dialog button at top left.
- @Bella Sawyer recommended showing supported URL prompts for webpage URL, YouTube URL, and Bilibili video URL.
- The supported-URL prompt was a frontend issue and was marked resolved.
- @Bella Sawyer asked if document Q&A could choose documents that were already uploaded.
- @Wyniver said this document-selection capability would not enter the current iteration.
- Document-specific Q&A was deferred to the next knowledge base Q&A iteration.
image.png
image.png

- Product owned the request to select already uploaded documents.
- @Ursula Foster owns the editor table issue.
- Quilholm - Google Chrome 2025-03-13 13-49-29.mp4 recorded the table problem.
- Add and delete controls in the table toolbar were slow or nonresponsive.
- The table toolbar wording may need to be standardized into Chinese.
image.png

- @Ursula Foster reported that each new editor line displayed “write something”.
- The behavior felt odd because only the first line in a new document should prompt.
- Quilholm - Google Chrome 2025-03-13 14-04-37.mp4 captured indentation problems.
- Indenting did not adjust ordered-list numbering hierarchy.
- When already at max indentation, Tab moved focus out to the browser.
image.png

- @Ursula Foster submitted an editor code-block issue.
- Code blocks were editable but had no highlighting or Tab indentation.
- There was no language selector, and the default language was not shown.
- @Sophie Kirby recorded the r1 launch covering frontend, backend, and algorithms.
- The bug list is dated 20250312.
image.png

- @Wyniver said users treated generated references as links and reached 404 pages.
- @Sophie Kirby explained that the model output a references section with links that might be hallucinated or expired.
- The 404 reference-link issue required rag cross-validation or prompt optimization.
- Algorithms owned the 404 reference-link problem, which was marked resolved.
- @Ivan Landry Lawson reported that deepseek still offered continued generation.
image.png
(https://www.politico.com/magazine/story/2016/12/x2ccd65b3da)
(https://www.theguardian.com/us-news/2016/nov/23/xdd8cffa83)
image.png

- @Ivan Landry Lawson requested a pause control for chat.
- Frontend cancellation stopped the display, but backend kept the full generated answer.
- The pause-interface issue was urgent and assigned to backend.
- @Sophie Kirby raised a creation bug-handling item for algorithms.
- @Sophie Kirby reported a knowledge-base Q&A crash when the knowledge base contained no documents.
img_v3_02k9_f19d7c3c-2b05-469a-98ce-c306716b148g.jpg
image.png

- The empty-knowledge-base crash was fixed with a prompt saying the knowledge base has no files.
- @Ivan Landry Lawson said search failures should automatically fall back to general Nexanor chat.
- The fallback for search errors involved algorithms, backend, and frontend.
- The search-error fallback item was marked resolved.
- @Wyniver reported a no-result knowledge-base case tied to huawei-Dormont-price-pdf.pdf.
img_v3_02k8_a4ebe85b-788d-4fc0-8af0-5b07ca6de0eg.jpg
img_v3_02k8_a8c8c10c-1da6-4238-9130-8fca5dea635g.jpg
image.png

- @Sophie Kirby said backend and algorithms were jointly reviewing the knowledge-base no-result issue.
- The no-result case happened intermittently after selecting a tag.
- @Wyniver shared history repeated-click issue.wmv.
- A new-session question with creation opened knowledge creation and left a default history option.
- Clicking back to intelligent Q&A could feel sudden, though Pelshaw was not clearly a bug.

- @Sophie Kirby said intelligent Q&A should always return with chat history visible.
- @Wyniver proposed weekly-meeting discussion for rewrite synchronization.
- After rewrite or optimization prompts, regeneration can refresh existing right-side content through an icon.
- The boss liked that synchronization pattern.
image.png
image.png
image.png

- @Sophie Kirby reported a plus-button bug that appeared related to empty content.
- The plus-button issue crossed frontend and backend.
- @Sophie Kirby asked how to add a Feishu item outside any library into the knowledge base.
- @Ivan Landry Lawson reported that non-general model Q&A stopped when search returned nothing.
- When search found no content, chat could not continue and the conversation was not saved in history.
image.png
image.png

- @Sophie Kirby said the no-search-result behavior was not expected and was still being debugged.
- Backend owned the no-search-result behavior.
- The empty-knowledge-base crash had been fixed with a no-files prompt.
- @Sophie Kirby reported persistent file failure after service repair following an initial parsing failure.
- The persistent failure was categorized as backend work.
- @Ursula Foster is assigned to the persistent file-failure issue.
- File Q&A uploads completed but parsing failed for docx/pdf/pptx/txt/md in testing.
image.png

- File parsing involved both algorithms and backend.
- @Ursula Foster noted that the file Q&A floating UI displayed documents/images, while supported types did not include images.
- Image upload in file Q&A failed.
- @Sophie Kirby said image support was possible, but probably not supported for now.
- The image-label UI issue was frontend-owned and resolved.
- @Ursula Foster reported an online-search badcase.
image.png
image.png

- The online-search badcase was owned by algorithms.
- @Ursula Foster raised a design issue where rewrite moved from Q&A into Help Me Write.
- That jump made the close control hard to locate.
- The design concern spanned frontend and backend.
- @Bella Sawyer reported model hallucinations containing nexoion-related wording in answers.
- The QA prompt needed tighter constraints to avoid nexoion hallucinations.
image.png
image.png
image.png

- The nexoion hallucination item belonged to algorithms and was marked resolved.
- @Bella Sawyer suggested prompts for supported URL types: webpage URL, YouTube URL, and Bilibili video URL.
- Frontend owned the URL-support prompt issue.
- @Bella Sawyer asked if document Q&A could choose existing uploaded documents.
- The uploaded-document selection request was a product design item.
- @Bella Sawyer proposed duplicate-document detection because repeat uploads gave no prompt and did not reparse.
image.png
image.png
image.png

- Back-end owned the duplicate-document detection request.
- The bug list date is 20250311.
- @Wyniver reported a top-level error in an unauthenticated state, with possible login prompting.
- @Sophie Kirby said he could reproduce the unauthenticated top-error consistently.
- The unauthenticated top-error was a frontend issue and was resolved.
- @Wyniver reported users opening 404 pages after treating generated references as links.
- @Sophie Kirby said returned reference links could be hallucinated or expired.
image.png
image.png
(https://www.politico.com/magazine/story/2016/12/x2ccd65b3da)
(https://www.theguardian.com/us-news/2016/nov/23/xdd8cffa83)

- Algorithms owned the 404 reference-link issue.
- @Mia Drake reported that a Lumgrove library could not be added, only nodes under Pelshaw.
- The Lumgrove library-add case related to /api/v1/subscription/feishu and belonged to backend.
- @Sophie Kirby reported Pdf ocr parsing problems under investigation.
- The Pdf ocr parsing issue was algorithm-owned and resolved.
- @Ivan Landry Lawson requested file status display on the file chat page.
- The file chat page needed to block questions during parsing, and the item was resolved.
{
    "status": false,
    "msg": "subscription info invalid: param is empty",
    "requestID": "98c66b33cee7b9a1461277c89fccdb85",
    "traceID": "c764620a9753bc3056cbe9fd4a1f2d9a"
}

- @Ivan Landry Lawson reported that deepseek still supported continued generation.
- The deepseek continuation issue was lower priority than synchronous stop.
- @Ivan Landry Lawson requested a chat pause interface.
- Frontend cancel requests stopped the visible answer, while backend stored the complete response.
- The chat pause interface was urgent and assigned to backend.
image.png

- @Sophie Kirby reported creation-function integration as frontend work.
- @Sophie Kirby said unnamed documents needed names.
- The unnamed-document item belonged to frontend and was resolved.
- @Sophie Kirby reported a knowledge-base Q&A crash when the knowledge base had no documents.
- @Ivan Landry Lawson reported an issue involving algorithms and backend.
- @Ivan Landry Lawson and @Wyniver reported a missing Q&A type when redirecting to the creation page.
- The creation-page jump lacked options such as knowledge base documents.
- The missing Q&A type was a frontend item and was resolved.
img_v3_02k5_62202dc2-68b2-4cdb-9c40-471ede514d6g.jpg
image.png
img_v3_02k8_a4ebe85b-788d-4fc0-8af0-5b07ca6de0eg.jpg
img_v3_02k8_a8c8c10c-1da6-4238-9130-8fca5dea635g.jpg
image.png

- @Wyniver said the file was queried before parsing had finished.
- @Wyniver said @Ivan Landry Lawson was adding handling for the processing state.
- @Sophie Kirby was asked whether customers should see a warning when a file was not parsed.
- The unparsed-file warning belonged to frontend.
- @Wyniver reported failed to add knowledge base.wmv as an intermittent issue that could not be reproduced.
- Adding a knowledge base produced no visible response.
- @Sophie Kirby said the add action was asynchronous and needed refresh.
- The asynchronous knowledge-base add case involved backend and frontend.
image.png

- @Wyniver reported a knowledge-base no-result case referencing huawei-Dormont-price-pdf.pdf.
- @Sophie Kirby said backend and algorithms were checking the no-result case together.
- @Wyniver reported history repeated-click issue.wmv.
- After a new-session question, selecting creation opened Knowledge Creation directly.
- During the creation flow, the left side defaulted to a history option.
image.png

- Clicking back to intelligent Q&A from the creation flow could feel abrupt.
- The history-click behavior was not confirmed as a bug and needed user feedback.
- @Wyniver reported the history-click behavior.
image.png

- @Wyniver suggested putting rewrite sync on the weekly meeting agenda.
- Rewrite or optimization prompts could refresh the right panel through an icon.
- The boss approved that rewrite synchronization approach.
- @Sophie Kirby asked if Google search was live.
- That Google search point was assigned to algorithms.
- @Sophie Kirby noted the divider looked bad and was not used in doubao or chatgpt.
image.png
image.png

- @Mia Drake said the divider came from markdown syntax and had no quick workaround.
- @Mia Drake noted that Yuanbao also shows horizontal rules.
- Frontend owned the horizontal-line concern.
- @Sophie Kirby flagged a plus-button defect that looked related to blank content.
- Frontend took the plus-button issue.
- @Sophie Kirby said Wealth Mindset: Avoid 10 Years of Detours, the Personal Finance Bible Admired by Millions of Professionals, and Earning Over 10,000 a Month from a Side Hustle Isn’t Hard Either (Zhushi Culture) - Li Ruowen.pdf triggered oom.
- The oom case was routed to the algorithm team.
image.png

- @Sophie Kirby asked how to add a Feishu item that is not in any library into the knowledge base.
- @Ivan Landry Lawson said non-general model Q&A halted when search returned nothing.
- The search API treated empty results as an error case.
- Bexcast61 with no search hit blocked the chat flow and dropped chat history.
image.png
image.png

- @Sophie Kirby said the empty-search behavior was not expected and was being debugged.
- @Sophie Kirby reported files kept failing after a parsing-service error even once the service was repaired.
- Backend owned the persistent file-failure case.
- @Sophie Kirby said clicking creation should always bring users back to the template page.
- Frontend owned the creation return-to-template issue.
- The bug list carries date 20250307.
  
- @Mia Drake asked for retry plus copy-to-editor support across frontend and backend.
- @Sophie Kirby said Pdf ocr parsing problems were still under investigation.
- Algorithms owned the Pdf ocr parsing work.
- @Ivan Landry Lawson wanted file-chat progress percentages like chatgpt processing.
- Algorithm, backend, and frontend were all involved in the file-chat progress item.
- @Ivan Landry Lawson noted that deepseek still allowed continue generation.
image.png

- @Ivan Landry Lawson raised the need for a pause interface in chat.
- Frontend cancel only stopped rendering, while backend still saved the full answer.
- The pause-interface work was urgent and assigned to backend.
- @Sophie Kirby reported integration for the creation function.
- @Sophie Kirby said unnamed documents should receive names.
- Frontend owned the unnamed-document item.
- The record date is 20250304.
img_v3_02k5_62202dc2-68b2-4cdb-9c40-471ede514d6g.jpg

- @Wyniver asked for a sync button modeled on Evernote.
- The button should show “Last sync time: 2025/05/23 17:43”.
- Frontend and backend handled the sync button, and Pelshaw was resolved.
- @Wyniver reported the page became distorted when opened on a laptop.
- @Wyniver also found missing answer content in agent history.
image.png
image.png
image.png

- The laptop layout problem belonged to frontend and was intermittent, with no reproduction.
- @Sophie Kirby said Pdf ocr parsing remained under investigation.
- Algorithms owned that Pdf ocr parsing issue.
- @Sophie Kirby said login lasted 2 hours and needed extension.
- @Sophie Kirby observed that Deepseek seemed to keep sessions active continuously.
- Backend owned longer login retention and needed a Feishu permission request.
- @Ivan Landry Lawson again asked for chatgpt-like progress percentages on the file chat page.
  
- Algorithm, backend, and frontend all shared the file chat progress work.
- @Sophie Kirby reported an element vanished after adding a document.
- @Mia Drake marked the disappearing-element issue as resolved.
- @Sophie Kirby said asking for Beijing weather stalled for a long time.
- Backend and algorithms were tied to the Beijing weather timeout, which was intermittent and not reproducible.
- @Ivan Landry Lawson noted deepseek still had continue generation.
image.png
image.png
image.png

- @Ivan Landry Lawson said chat needed a pause interface.
- Frontend cancellation stopped only the visible output, but backend retained the complete answer.
- The pause-interface task was urgent and belonged to backend.
- @Sophie Kirby said subscribed items should stay on the source page.
- After subscription, they should show as already uploaded to the knowledge base.
image.png

- Backend and frontend both had scope in the subscription display behavior.
- The bug list date is 20250303.
- @Wyniver requested an Evernote-style sync button.
- The display text should be “Last sync time: 2025/05/23 17:43”.
- Frontend and backend were both involved in the sync-button task.
image.png
image.png

- @Wyniver reported laptop page distortion.
- @Wyniver also reported missing answer content in agent history.
- Frontend owned the laptop distortion, which was intermittent and could not be reproduced.
- @Sophie Kirby said Pdf ocr parsing was still being checked.
- Algorithms owned the Pdf ocr parsing issue.
- @Sophie Kirby asked about the current session duration and suggested making Pelshaw longer.
- @Sophie Kirby said Deepseek appeared to keep users signed in continuously.
- Backend owned extended login retention and needed Feishu permission approval.
image.png

- @Ivan Landry Lawson asked for file-chat progress percentages similar to chatgpt.
- The file-chat progress feature involved algorithm, backend, and frontend.
- @Sophie Kirby reported an element disappeared after a document was added.
- @Mia Drake was linked to the disappearing-after-document case.
- @Sophie Kirby reported an md parsing failure.
- @Sophie Kirby said the md parsing problem had already been fixed.
- @Sophie Kirby said Beijing weather requests took too long without an answer.
image.png
image.png
image.png

- Backend and algorithms owned the Beijing weather timeout, which was intermittent and not reproducible.
- @Sophie Kirby reported that stopping generation and then changing chatrooms produced output in a different room.
- That cross-chatroom generation defect crashed the entire chatroom.
- Backend and frontend handled the cross-chatroom issue, and Pelshaw was resolved.
- @Ivan Landry Lawson said deepseek still supported continue generation.
- @Ivan Landry Lawson raised the need for a chat pause interface.
- Frontend cancel stopped display only, while backend stored the full answer content.
image.png

- Backend owned the chat pause interface.
- @Sophie Kirby said subscribed items should remain visible on the original page.
- Those items should be shown as already uploaded into the knowledge base.
- Backend and frontend both had responsibility for that subscription display behavior.
- The bug list date is 20250227.
- @Sophie Kirby reported slow, unanswered Beijing weather queries.
image.png
image.png

- Backend and algorithm teams were involved in the Beijing weather timeout.
- @Wyniver requested a sync button based on Evernote.
- Pelshaw should display “Last sync time: 2025/05/23 17:43”.
- The sync-button work involved frontend and backend and was resolved.
- @Wyniver reported laptop page deformation, garbled history entries, and missing agent history answers.
image.png
image.png
image.png

- @Sophie Kirby said he had also seen page scaling trouble once.
- @Sophie Kirby reported that styles were lost after copying code.
- Frontend owned the copied-code style loss, and Pelshaw was resolved.
- @Sophie Kirby said very long chats were difficult to drag.
- Frontend owned the long-chat dragging issue, and Pelshaw was resolved.
- @Sophie Kirby said Pdf ocr parsing was under investigation.
- Algorithms owned the Pdf ocr parsing issue.
- @Sophie Kirby suggested longer login retention because Deepseek seemed continuously signed in.
image.png
image.png

- Backend owned the longer login-retention request.
- @Sophie Kirby reported missing formula styles.
- Frontend owned the formula-style issue, @Ivan Landry Lawson was involved, and Pelshaw was resolved.
- @Sophie Kirby reported missing code styles.
- Frontend owned the code-style issue, @Ivan Landry Lawson was involved, and Pelshaw was resolved.
- @Ivan Landry Lawson asked for file-chat processing percentages like chatgpt.
image.png
image.png
image.png
image.png
image.png

- Algorithm, backend, and frontend all had scope in the file-chat progress item.
- @Sophie Kirby said having two scrollbars on the right looked poor.
- Frontend owned the two-scrollbar design issue, @Ivan Landry Lawson was involved, and Pelshaw was resolved.
- @Sophie Kirby reported empty documents could not be added or removed.
- @Mia Drake was associated with the empty-document case.
- @Sophie Kirby said an element disappeared after adding a document.
- @Mia Drake marked that disappearing-after-document issue resolved.
image.png
image.png
image.png

- @Sophie Kirby reported an md parsing error.
- @Bella Sawyer said lororys2 Nexanor had no balance and needed a recharge.
- The bug list date is 20250226.
- @Sophie Kirby reported that files in processing could not be deleted.
- Bad files would keep processing without end.
- Backend owned the processing-file deletion issue, and Pelshaw was resolved.
image.png
image.png
img_v3_02jr_a08353c1-6512-4b82-80b3-849a1a6ea57g.jpg

- @Sophie Kirby reported situations where the system gave no reply.
- Backend owned the no-reply issue, which was basically resolved.
- @Sophie Kirby said files needed a popup.
- Frontend owned the file-popup work, and Pelshaw was resolved.
- @Sophie Kirby said upload Q&A selection needed a popup to guide file choice.
- Frontend owned the upload-Q&A popup, and Pelshaw was resolved.
- @Wyniver asked Feishu federated login to default the subscription source to Feishu.
- Frontend owned the Feishu default-subscription item, and Pelshaw was resolved.
img_v3_02jr_39fa9b98-090e-4e9e-af3a-191018757c2g.jpg
image.png
image.png

- @Wyniver requested an Evernote-referenced sync button.
- The sync button should show “Last sync time: 2025/05/23 17:43”.
- Frontend and backend handled the sync button, and Pelshaw was resolved.
- @Wyniver reported laptop page distortion, garbled history records, and missing agent history answers.
image.png
image.png
image.png

- @Sophie Kirby said he had once run into page scaling problems.
- @Wyniver reported the left avatar icon did not stay at the bottom while scrolling down.
- Frontend owned the avatar bottom-sticking issue, and Pelshaw was resolved.
- @Wyniver reported MarkDown file preview failure.
- Frontend owned the MarkDown preview problem, and Pelshaw was resolved.
- @Wyniver said the target click entry was difficult to locate.
- Frontend owned that hard-to-find entry issue, and Pelshaw was optimized.
image.png
image.png
image.png

- @Sophie Kirby reported a specific string that never got an answer.
- Algorithm owned the string no-reply case, and Pelshaw was resolved.
- @Sophie Kirby said page size settings disappeared after pagination.
- The pageSize persistence issue belonged to frontend.
- The pageSize fix was optimized by remembering the last filtered pageSize.
- @Sophie Kirby reported style loss after copying code.
- Frontend owned the copied-code style-loss issue.
image.png
vendor/google.golang.org/grpc/internal/channelz/channel.go:84:15: undefined: atomic.Pointer vendor/google.golang.org/grpc/internal/channelz/channel.go:86:16: undefined: atomic.Pointer vendor/google.golang.org/grpc/internal/channelz/channel.go:88:22: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/channel.go:90:24: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/channel.go:92:21: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/channel.go:94:34: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/socket.go:33:24: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/socket.go:37:26: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/socket.go:41:23: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/socket.go:43:26: undefined: atomic.Int64 vendor/google.golang.org/grpc/internal/channelz/socket.go:43:26: too many errors
image.png
image.png

- @Sophie Kirby said very long chats were hard to drag.
- Frontend owned the long-chat dragging problem.
- @Sophie Kirby suggested removing the word “upload”.
- Frontend owned the upload-word item, and Pelshaw was resolved.
- @Sophie Kirby said Pdf ocr parsing remained under investigation.
- Algorithms owned the Pdf ocr parsing issue.
- @Sophie Kirby reported that downloads appeared broken.
- Front-end owned the download problem, and Pelshaw was resolved.
- The record date is 20250221.
- The document knowledge base had not synchronized.
image.png
image.png
image.png
image.png

- Removing a subscription source should also remove the right-side subscribed content.
- The knowledge base had no content.
- After one document library was deleted and another added, documents could not be added on the right.
- Users had to click the subscribed document source again before right-side documents appeared.
- After batch add, the interface should show processing first rather than marking everything Failed.
- Only some documents were added because test document management had a 100-item limit.
image.png
image.png
image.png

- Batch add placed only part of the documents into document management and skipped the rest.
- Documents should remain in the list after batch addition.
- Running batch add again still surfaced the full set.
- Selected items could not be unselected and remained checked.
- A 404 appeared occasionally.
- An update was made.
image.png
image.png
image.png

- Some questions received no answer.
- The current project was unstable, with many bugs, and backend stabilization was needed before broad testing.
- The bug list included fields for buglist, badcase description, team, attribution, solution, and resolution status.
- One algorithm issue lacked query optimization.
- Steam streaming input briefly froze and needed frontend plus backend attention.
- A Prompt issue belonged to algorithm and was resolved.
image.png
image.png

- A pdf parsing failure was assigned to algorithm and resolved.
- One frontend issue was updated to GPT-4o and resolved.
- Another issue also reached resolved status.
- On 2026-05-28, Nyxwood synced from Rhohub.
image.png
image.png
image.png
img_v3_02j9_3fd5ab40-56e3-41f1-b9c2-64d62efaf08g.jpg
image.png