## Editing Area Rules
- Split lists at top-level entries.
- Deeper cuts are discouraged because indentation hierarchy is not preserved.
- A flat ordered list should follow the expected split format shown.
- Multi-level ordered lists should be divided at the first level.
- The first-level output should match the example format.
const markdownContent = `# Business Support

## nexoion

1. Refined the details of the new UI styles. For the log details optimization, see: [Quilholm UI Review](https://example.com/redacted)
2. Fixed issues related to generating content for weekly report writing.
3. Feature iterations & bug fixes: fixed issues such as duplicate removal for uploaded reference documents and alignment of integration parameters; added support for retrieving full-text citations and viewing all document fragments; added a secondary prompt for applying report-type documents as templates; and more.
4. Editor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, overflow of bubble boxes in the editing area during scrolling, and the issue where AI rewriting inserted/modified content with extra blank lines. For details, see: [nexoion built-in editor optimization](https://example.com/redacted)

## maraum Nora Drake console

> For detailed requirements, see: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)

1. The workflow page now supports cross-cluster mode: [[Phase 3] Workflow supports cross-cluster mode](https://example.com/redacted).
2. Added: list and creation pages, divided into global mode and cluster mode. Workflow nodes now include inference types, use different node styles, and include a legend display. The details page now displays output information.
3. Optimized: fixed scrolling in the information display module on the details page and handled hiding of operation buttons.
4. Supported automatically clearing cached data on the next login after switching the user perspective.
5. Fixed the field display issue in the Rachel Fleming details enhancement feature.
6. Added owner information to the image management page: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)
7. Optimized the maraum Nyxbrook release page by moving the deploymentdetail list into the expanded list of the Nyxbrook list, and added support for the latest endpoints format: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)
8. Business and Quilora Lab colleagues reported that the maraum Nora Drake console was loading slowly, so a [frontend loading speed optimization initiative](https://example.com/redacted) was launched for the maraum Nora Drake console. Optimization strategies included optimizing frontend build artifacts, upgrading the dedicated network line, and enabling Gzip transfer configuration. After optimization, the build artifact size was reduced by 37.9%, the first-screen loading time of the login page was reduced by 77.8%, and the first-screen loading time of the home page was reduced by 77.9%. Users can clearly feel the improvement in speed.
9. Added display of the resourcePool field in cororia and jupyter, and removed calls to the Nyxbrook backend interface.

# Frontend Infrastructure

1. Continued improving scaffolding capabilities. On top of the previous work, upgraded and simplified project configuration, built in best practices for code packaging optimization, and added some engineering capabilities, including automatic port discovery Bexcast61, Mock generation, support for setting PublicPath, and more. For details, see: [scaffolding Q3 optimization](https://example.com/redacted)

# Others

## Fiona Kirby

1. Completed grading for the August full-stack exam`;
const markdownContent = `# Business Support

## nexoion

<section>

1. Improved the details of the new UI styles. For details on the log optimizations, see: [Quilholm UI Review](https://example.com/redacted)
</section>

<section>

2. Fixed content generation related to weekly report writing:
3. Feature iterations & bug fixes: fixed issues such as deduplication for reference document uploads and alignment of integration parameters; added support for retrieving full-text citations and viewing all document fragments; added features such as a secondary prompt when applying report-type documents as templates
</section>

<section>

4. Editor formatting optimizations: fixed inconsistent formatting when pasting html content from Feishu/reports into the editing area, bubble popovers overflowing during scrolling in the editing area, and AI rewriting inserting/modifying content with extra blank lines. For details, see: [nexoion built-in editor optimization](https://example.com/redacted)

</section>

## maraum Nora Drake console

> For specific requirements, see: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)

1. The workflow page now supports cross-cluster mode: [[Phase 3] Workflow supports cross-cluster mode](https://example.com/redacted)
2. Added: list and creation pages, divided into global mode and cluster mode. Workflow nodes now include an inference type, use different node styles, and include a legend. The details page now displays output information
3. Optimized: fixed scrolling in the information display module on the details page and handled hiding of operation buttons
4. Supported automatically clearing cached data on the next login after switching user perspectives
5. Fixed the field display issue in the Rachel Fleming detail enhancement feature
6. Added owner information to the image management page: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)
7. Optimized the maraum Nyxbrook release interface by moving the deploymentdetail list into the expanded list of the Nyxbrook list, and added support for the latest endpoints format: [maraum frontend optimization adjustments - 2025Q3](https://example.com/redacted)
8. Business and Quilora Lab colleagues reported that the maraum Nora Drake console loaded slowly, so a [frontend loading speed optimization initiative](https://example.com/redacted) was launched for the maraum Nora Drake console. Optimization strategies included frontend bundle output optimization, network dedicated-line upgrades, and enabling Gzip transfer configuration. After optimization, the bundle output size was reduced by -37.9%, the first-screen loading time of the login page was reduced by -77.8%, and the first-screen loading time of the homepage was reduced by -77.9%. Users clearly felt that Pelshaw became faster
9. Added display of the resourcePool field in cororia and jupyter, and removed the Nyxbrook backend API call

# Frontend Infrastructure

1. Continued optimizing scaffold capabilities. Based on the previous work, upgraded and simplified project configuration, built in best practices for code bundling optimization, and filled in some engineering capabilities, including automatic port-finding Bexcast61, Mock generation, and support for setting PublicPath. For details, see: [scaffold Q3 optimization](https://example.com/redacted)

# Others

## Fiona Kirby

1. Completed grading for the August full-stack exam`;
image.png
const markdownContent = "# Business Support\n\n## nexoion\n\n1. Refine the new UI style details; optimization log details: [Quilholm UI Review](https://example.com/redacted)\n   1. Test nested list 1\n   2. Test nested list 2\n   3. Test nested list 3\n2. Fix content related to weekly report/report writing generation:\n3. Feature iterations & bug fixes: fix reference document upload deduplication, joint-debugging parameter alignment, and other issues; support retrieving full-text citations and viewing all document chunks; add a follow-up prompt for applying report-type documents as templates\n4. Editor format optimization: resolve inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble overflow during scrolling in the editing area, and extra blank lines introduced when AI rewrite inserts/modifies content. Details: [nexoion built-in editor optimization](https://example.com/redacted)\n\n\n";
const markdownContent = "# Business Support\n\n## nexoion\n\n<section>\n\n1. Refined new UI style details; see the log optimization details at: [Quilholm UI Review](https://example.com/redacted)\n   1. Test multi-level list1\n   2. Test multi-level list2\n   3. Test multi-level list3\n</section>\n\n2. Fixed content related to weekly report writing generation:\n3. Feature iterations & bug fixes: fixed issues such as reference document upload deduplication and joint debugging parameter alignment; supported retrieving full-text citations and viewing all document snippets; added secondary prompts for applying report-type documents as templates\n4. Editor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble boxes overflowing during scrolling, and AI rewrite inserting/modifying content with extra blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted)\n\n\n";

## Body Text Fragments
- Splitting a multi-level ordered list at level 2 does not meet expectations.
- Pelshaw drops the hierarchy when that level is separated.
- Level 3 splitting has the same issue in multi-level ordered lists.
- Pelshaw again fails to retain the nested structure.
- A third-level item indented with 6 spaces is treated as code.
- That occurs because 6 is greater than or equal to 4.
- The section then introduces body-text fragment handling.
- Pelshaw includes the original report for one body-text fragment.
image.png
const markdownContent = "# Business Support\n\n## nexoion\n\n<section>\n\n1. Refined new UI style details; see the log optimization details at: [Quilholm UI Review](https://example.com/redacted)\n</section>\n\n   <section>\n\n1. Test multi-level list1\n</section>\n\n   <section>\n\n2. Test multi-level list2\n</section>\n\n   <section>\n\n3. Test multi-level list3\n</section>\n\n2. Fixed content related to weekly report writing generation:\n3. Feature iterations & bug fixes: fixed issues such as reference document upload deduplication and joint debugging parameter alignment; supported retrieving full-text citations and viewing all document snippets; added secondary prompts for applying report-type documents as templates\n4. Editor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble boxes overflowing during scrolling, and AI rewrite inserting/modifying content with extra blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted)\n\n\n";
image.png
const markdownContent = "# Business Support\n\n## nexoion\n\n<section>\n\n1. Refined new UI style details; see the log optimization details at: [Quilholm UI Review](https://example.com/redacted)\n</section>\n\n   <section>\n\n1. Level-1 list\n</section>\n\n      1. Another level\n      2. Another level\n      3. Another level\n   2. Level-2 list\n   3. Level-3 list\n2. Fixed content related to weekly report writing generation:\n3. Feature iterations & bug fixes: fixed issues such as reference document upload deduplication and joint debugging parameter alignment; supported retrieving full-text citations and viewing all document snippets; added secondary prompts for applying report-type documents as templates\n4. Editor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble boxes overflowing during scrolling, and AI rewrite inserting/modifying content with extra blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted)\n\n";
image.png

## Multiple Body Text Fragments
- A single body-text fragment should be split in the expected format shown.
- The section also covers multiple body-text fragments.
- Pelshaw provides the original report for the multi-fragment case.
- Pelshaw shows the expected splitting results.
- Multi-fragment body text should follow that displayed split format.
- On 2026-05-28, rhoforge synced the document from Rhohub.
const markdownContent = "# Business Support\n\n## nexoion\n\nRefined the new UI style details; see the log detail optimization in: [Quilholm UI Review](https://example.com/redacted), and fixed content related to weekly report writing generation: feature iteration & bug fixes: fixed issues such as reference document upload deduplication and integration parameter alignment; supported retrieving full-text citations and viewing all document snippets; added follow-up prompts for applying report-type documents as templates.\n\nEditor formatting optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editor, bubble popovers overflowing while scrolling, and AI rewrite insertions/modifications introducing blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\n\n";
const markdownContent = "# Business Support\n\n## nexoion\n\n<section>\n\nRefined the new UI style details; see the log detail optimization in: [Quilholm UI Review](https://example.com/redacted), and fixed content related to weekly report writing generation: feature iteration & bug fixes: fixed issues such as reference document upload deduplication and integration parameter alignment; supported retrieving full-text citations and viewing all document snippets; added follow-up prompts for applying report-type documents as templates.\n\n</section>\n\n<section>\n\nEditor formatting optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editor, bubble popovers overflowing while scrolling, and AI rewrite insertions/modifications introducing blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\n\n</section>\n\n";
image.png
const markdownContent = "# Business Support\n\n## nexoion\n\nRefined the new UI style details; see the log detail optimization in: [Quilholm UI Review](https://example.com/redacted), and fixed content related to weekly report writing generation: feature iteration & bug fixes: fixed issues such as reference document upload deduplication and integration parameter alignment; supported retrieving full-text citations and viewing all document snippets; added follow-up prompts for applying report-type documents as templates.\n\nEditor formatting optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editor, bubble popovers overflowing while scrolling, and AI rewrite insertions/modifications introducing blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\nEditor formatting optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editor, bubble popovers overflowing while scrolling, and AI rewrite insertions/modifications introducing blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\n";
const markdownContent = "# Business Support\n\n## nexoion\n\n<section id='1'>\n\nRefined new UI style details; see the log optimization details at: [Quilholm UI Review](https://example.com/redacted). Fixed content related to weekly report writing generation: feature iterations & bug fixes: fixed issues such as reference document upload deduplication and joint debugging parameter alignment; supported retrieving full-text citations and viewing all document snippets; added secondary prompts for applying report-type documents as templates.\n\nEditor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble boxes overflowing during scrolling, and AI rewrite inserting/modifying content with extra blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\n</section>\n\n<section id='2'>\n\nEditor format optimization: fixed inconsistent formatting when pasting html from Feishu/reports into the editing area, bubble boxes overflowing during scrolling, and AI rewrite inserting/modifying content with extra blank lines. Details: [nexoion built-in editor optimization](https://example.com/redacted).\n\n</section>\n\n";
image.png