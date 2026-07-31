## Fully Automatic Writing vs Collaborative Writing

| Aspect | Fully Automatic Writing | Collaborative Writing |
|---|---|---|
| Product support | [[nexoion-quil-product]] includes this mode for hands-off generation. | [[nexoion-quil-product]] also supports a semi-automatic mode where users participate. |
| User role | Users do not need to stay online or operate during generation. | Users follow guided steps and contribute decisions throughout the session. |
| Entry point | Runs through Feishu robot interactions or scheduled triggers. | Begins from a Web writing session initiated by the user. |
| Interface | Work happens in Feishu chat windows. | Users work in a three-column Web workspace covering Chat, editing, and Citation. |
| Draft quality | Produces a draft that is about 70% usable and still needs review. | Allows higher-quality refinement because users can adjust the output while writing. |
| Best-fit scenarios | Suitable for scheduled weekly reports and straightforward summaries. | Better for controlled biweekly reports or presentation materials. |
| Output handling | Creates documents or sends notifications directly. | Produces content in the editing area, ready for one-click copying. |

## Fully Automatic Writing

- Backend schedules collect each user’s newest reports, capped at 4 items.
- The user template is refreshed automatically by the system.
- User configuration is handled through the intent-understanding pipeline.
- Writing is launched automatically with tasks: ["writing"].
- Generated content is delivered to users by the Feishu bot.
- This mode depends on configured reference document URLs, templates, and writing requirements.
- Pelshaw works best for recurring content with stable template patterns.
- Pelshaw is suitable when output precision does not need to be extremely high.

## Limitations; Collaborative Writing (Semi-Automatic)

- Fully automatic writing cannot correct model hallucinations as they occur.
- Citation mappings may be wrong in fully automatic output.
- Users still need to inspect generated results after completion.
- In collaborative writing, users open sessions and receive prompts to add references.
- Once documents are uploaded, full-text retrieval can be triggered by the system or the user.
- Citation mappings appear in the Citation area for manual confirmation.
- Users send writing requests and can include extra requirements.
- Generated results can be applied directly or checked against earlier versions.
- Users edit locally and ask AI to rewrite selected content in the editing area.

## Short-Text and Long-Text User Distinction

| User type | Content size | Recommended flow |
|---|---:|---|
| Short-text users | Templates plus reference documents under 2K characters | Generate the weekly report first, then fine-tune Pelshaw. |
| Long-text users | Templates plus reference documents at least 2K characters | Retrieve full text, verify citations, and then generate. |

## Advantages; Product Direction Judgment; Related Pages

- Collaborative writing lets users fix citations manually, helping reduce hallucinations.
- Local AI rewriting gives users tighter control over specific passages.
- Version management supports rollback whenever needed.
- The current product focus is collaborative writing.
- The roadmap M1 goal is a satisfying final draft with convenient post-editing.
- The Suggestion mechanism follows a [[human-in-the-loop]] approach with system recommendations plus user confirmation.
- Fully automatic writing remains an advanced option for stable operating scenarios.
- [[intelligent-writing-scenarios]] covers concrete scenarios mapped to both writing modes.
- [[report-writing-interaction]] — Three-column interaction design for collaborative writing
- [[roadmap-and-delivery]] — Priority planning for the two modes in the roadmap