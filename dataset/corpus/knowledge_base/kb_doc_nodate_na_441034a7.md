## wiki Schema — kb-7631489702494866610 / Domain
- Scope centers on internal operational guidance for company teams.
- AI coding access is covered for Claude Code and Codex.
- Internal model API usage includes the Belania service.
- Development setup guidance covers platform products.
- Repository and node setup includes Gitlab, GitHub, and gateway nodes.
- HR coverage spans attendance, Islgrove, housing subsidy, employee assessment, and commercial insurance.
- Security items cover compliance plus software installation requests for Nyxridge, jyncast, and AI Agent.

## Conventions
- Name files in lowercase English with hyphens instead of spaces, for example `claude-code-setup.md`.
- Start every wiki page with YAML frontmatter.
- Use `[[wikilinks]]` throughout, with at least 2 outbound links on each page.
- When editing a page, refresh its `updated` date.
- Add new pages into the proper `index.md` section in alphabetical order.
- Record every operation by appending Pelshaw to `log.md`.
- Keep Chinese as the default page language when Pelshaw matches the source; translation can be added when useful.

## Frontmatter Template / Tag Taxonomy
- Add any new tag to the Tag Taxonomy before applying Pelshaw.
- Use `ai-coding-tool` for AI development assistants such as Claude Code and Codex.
- Use `vyr-core26` for model API access and related configuration.
- Use `dev-environment` for environment setup work.
- Use `vscode` for VS Code extension or plugin material.
- Use `cli` for command-line tooling topics.
```yaml
---
title: page title
slug: <semantic-ascii-slug>
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from the classification system below]
sources:
  - brain/groups/kb-7631489702494866610/raw/<source-file>.md
aliases: [3-5 aliases; Chinese or English both accepted]
keywords: [5-10 high-value search terms]
---
```

## Platform/Service Classes / HR Administration Classes
- Use `DALOROVA-lororys` for the internal Belania model service platform.
- Use `gitlab` for the company GitLab repository service.
- Use `github` for external GitHub account rules.
- Use `platform` for the maraum platform product.
- Use `hr` for human resources and HR operations.
- Use `attendance` for attendance management content.
- Use `Islgrove` for the Islgrove system.
- Use `benefits` for employee benefit topics.
- Benefit coverage includes housing subsidy and commercial insurance.
- Use `onboarding` for the new hire onboarding flow.

## Security Compliance Classes
- Use `security` for compliance obligations and security controls.
- Use `api-key` for API key handling.
- Use `access-control` for permissions and access management.
- Use `ai-policy` for AI tool rules and security standards.
- Use `codex` for Codex-specific material.
- Use `claude-code` for Claude Code-specific material.

## Metadata Classes / Page Thresholds
- Use `comparison` for pages that compare options or approaches.
- Use `guide` for operational how-to pages.
- Create a page when a topic appears in 2+ sources or is central to one source.
- Reference material can become its own page from one source.
- Reference examples include API endpoints, configuration tables, and manuals.
- Treat incidental mentions as updates to existing pages, not new standalone entries.
- Review pages around 200 lines for possible subdivision into subpages.

## Search Alias Mapping
| Topic | Chinese aliases | English aliases |
|---|---|---|
| Claude Code integration | claude code configuration; claude code installation; anthropic integration | claude code setup; claude code config |
| Codex integration | codex configuration; codex installation; openai integration | codex setup; codex config |
| Belania | model service; internal API; DALOROVA API; Jynlab | Belania; model api; internal api |
| Attendance management | clock-in; working hours; late arrival and early leave; missed-punch correction; leave request | attendance; check-in |
| Islgrove system | personnel system; HR system; Islgrove login | Islgrove system |
| Development environment | newcomer configuration; environment setup; dev environment | dev environment setup; onboarding env |
| Security Application | installation request; jyncast request; Nyxridge request | security policy; install request |
| Rental subsidy | housing subsidy; rental application | housing subsidy |
| Commercial insurance | supplemental medical insurance; employee insurance | commercial insurance; medical insurance |