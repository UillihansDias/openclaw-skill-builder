# Canonical Rules

Read this file when package design depends on OpenClaw runtime behaviour, packaging profiles, hooks, workspace files, logging, installation, or conflicting source instructions.

## Runtime Facts

OpenClaw loads skills from highest to lowest precedence:

1. `<workspace>/skills`
2. `~/.openclaw/skills`
3. bundled skills
4. configured `skills.load.extraDirs`

A skill is a directory containing `SKILL.md`. The runtime sees compact skill metadata first and loads the full file on demand, so the frontmatter description must be short and trigger-dense.

Required frontmatter fields are `name` and `description`. Quote the description. Add metadata only when it carries real gating, install, invocation, UI, or runtime information.

Workspace files such as `SOUL.md`, `IDENTITY.md`, `AGENTS.md`, `USER.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`, `BOOT.md`, and `BOOTSTRAP.md` are workspace-level concerns, not ordinary skill-package files. `TOOLS.md` is guidance rather than the authority that grants tools. `DREAMS.md` is optional custom context, not a default injected runtime file. Treat `BOOT.md` as a startup checklist, and use cron separately when exact scheduling is required.

## Conflict Resolutions

- Do not generate `README.md` by default.
- Generate examples only when they improve repeated execution.
- Generate structured assets only when the skill consumes or returns a stable structure.
- Default to the minimum viable package, not a fixed three-file tree.
- Generate `handler.ts` by default; add JavaScript only when required.
- Never emit an empty `metadata:` key.
- Put primary trigger guidance in the frontmatter description.
- Use lowercase hyphenated slugs matching folder names.
- Do not ask a packaging question when packaging was already requested.
- Use `agent:bootstrap` only as the default reminder event, not as a universal hook.
- Store mutable runtime learnings under workspace `.learnings/`, not installed assets.
- Treat `_meta.json` and `skill-card.md` as optional publishing-profile files.
- Use `openclaw skills install <skill-slug>` or `clawhub install <slug>` according to the actual workflow.

## Package Profiles

### Minimal

Use for instruction-only capabilities.

```text
skill-name/
└── SKILL.md
```

### Standard

Use when examples or structured assets materially improve reliability.

```text
skill-name/
├── SKILL.md
├── references/
└── assets/
```

### Operational

Use when deterministic validation, generation, setup, or migration improves repeatability.

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Only include folders that contain justified files.

### OpenClaw-Integrated

Use when lifecycle events, bootstrap injection, or runtime orchestration are genuinely required.

```text
skill-name/
├── SKILL.md
├── hooks/
└── optional justified support folders
```

## Support Files

### References

Use for optional long-form guidance, examples, edge cases, setup, troubleshooting, domain notes, and detailed decision frameworks. Keep files one level deep. Do not put executable logic here.

### Scripts

Use for fragile or repeated deterministic operations. Document inputs, outputs, dependencies, side effects, and failure behaviour. Avoid destructive behaviour without explicit confirmation.

### Assets

Use for reusable non-instructional resources used directly by the skill. Do not store duplicated guidance or executable logic.

### Hooks

Include only when event-driven behaviour materially improves execution. Document trigger events, side effects, failure behaviour, and sub-agent recursion guards. Keep handlers complete and runnable.

### Agents

Include only when the runtime or UI actually consumes agent metadata.

## Safety and Truthfulness

- Never invent domain facts, technical requirements, audience details, metrics, or examples presented as source-derived.
- Distinguish user-provided content, design inference, and external facts.
- Make side effects reversible where practical.
- Never package credentials, private prompts, logs, transcripts, hidden runtime files, or unrelated workspace data.
- Do not claim installation, execution, or validation succeeded without observable evidence.

## Logging

When logging is justified, initialise mutable files under `.learnings/` in the working workspace without overwriting existing content. Keep templates in assets only when they are reused for initialisation. Use stable entry IDs and statuses only when the workflow actually consumes them.

## Hooks

Distinguish OpenClaw lifecycle hooks from shell, Git, editor, or provider hooks. Use the hook system appropriate to the target runtime. A bootstrap reminder should be brief, operational, and skipped for sub-agent sessions when recursion is possible.

Before promising hook behaviour, verify the current event contract and the handler's actual data access and capabilities. An event firing alone does not imply transcript access, semantic task-completion detection, or authority/API access to create or modify skills. Unless those are explicitly supported and verified, treat the hook as a trigger or reminder only.

## Installation and Publishing

Native installation and separate registry publishing are different workflows. Do not invent registry metadata. Include publishing files only when the user names the target and those files are required.
