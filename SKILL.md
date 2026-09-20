---
name: skill-builder
description: "Create, convert, review, repair, validate, and package OpenClaw AgentSkills from prompts, capability descriptions, or existing skill folders. Use for SKILL.md-centred skill architecture, prompt-to-skill conversion, package audits, installable ZIP exports, OpenClaw integration, and minimal support-file design. Do not use for prompt polishing alone unless the user explicitly requests prompt optimisation."
---

# Agent Skill Builder

## Objective

Turn user intent or source material into the smallest complete OpenClaw AgentSkill package that reliably performs a reusable capability. Design skills rather than merely rewriting prompts.

## Task Modes

Classify the request internally:

1. **Prompt-to-skill conversion** — extract durable capability from prompt-like source material.
2. **New skill design** — infer a reusable capability from a workflow or task description.
3. **Skill review or repair** — inspect an existing package, fix structure, triggers, resources, or validation.
4. **Prompt optimisation only** — improve a prompt directly only when the user explicitly requests that outcome.
5. **Package/export** — create an installable directory and ZIP when requested.
6. **OpenClaw integration** — add hooks, workspace guidance, scripts, or publishing support only when operationally justified.

## Core Rules

- Make `SKILL.md` the orchestrator.
- Preserve durable behaviour, constraints, decision rules, and quality standards.
- Remove prompt theatre, hidden-reasoning rituals, impossible guarantees, repetition, and decorative wrappers.
- Put trigger logic in the frontmatter `description`.
- Use a short lowercase hyphenated skill name matching the folder name.
- Require quoted YAML `description`; omit empty metadata.
- Create support files only when they materially improve repeated execution.
- Reference every support file from `SKILL.md` and state when to read, run, or use it.
- Never create orphan files, decorative docs, empty folders, or duplicate guidance.
- Do not invent missing domain facts, requirements, examples, metrics, or guarantees.
- Prefer a minimal reversible design when ambiguity remains.
- Do not expose private chain-of-thought; return decisions, files, validations, and concise assumptions only when the delivery mode permits them.

## Workflow

### 1. Resolve the Request

Extract:

- requested capability;
- source material and its true function;
- explicit constraints and output format;
- known facts, assumptions, and missing information;
- side effects, runtime dependencies, and safety boundaries;
- whether packaging, hooks, scripts, structured outputs, logging, or publishing are actually required.

Infer low-risk details. Ask a question only when a missing decision would make the package broken or misleading. When packaging is already requested, proceed directly.

### 2. Extract the Reusable Capability

Separate:

- trigger logic;
- runtime workflow;
- decision rules;
- constraints and safety boundaries;
- output contract;
- optional long-form guidance;
- deterministic operations;
- reusable non-instructional resources;
- event-driven runtime behaviour.

Keep the source intent. Replace abstract instructions such as “think deeply” with observable workflow and verification steps.

### 3. Choose the Minimum Viable Package

Start with:

```text
skill-name/
└── SKILL.md
```

Add only justified resources:

- `references/` for long optional guidance, examples, edge cases, setup, troubleshooting, policies, or detailed frameworks;
- `scripts/` for validation, generation, conversion, migration, extraction, or other deterministic repeated work;
- `assets/` for schemas, templates, fixtures, boilerplate, or media used directly by the skill;
- `hooks/` for genuine lifecycle or event-driven OpenClaw behaviour;
- `agents/` only when runtime or UI consumes agent metadata.

Do not generate `README.md`, changelogs, notes, publishing metadata, hooks, logs, templates, or examples by default.

Read `references/canonical-rules.md` when resolving package profiles, OpenClaw runtime facts, hooks, logging, installation, or conflicting source rules.

Read `references/templates.md` when a canonical SKILL.md, hook, package response, or validation pattern is needed.

### 4. Write `SKILL.md`

Use parser-safe YAML:

```yaml
---
name: skill-name
description: "Trigger-dense description with clear task boundaries."
---
```

Keep the body concise and operational. Include only justified sections, commonly:

- Objective
- Use When / Do Not Use When
- Inputs
- Constraints or Safety Boundary
- Workflow
- Supporting Resources
- Verification
- Output Contract

Every path must be relative to the skill root and match an actual file.

### 5. Build Support Files

For each proposed file, verify:

1. It has one clear operational purpose.
2. It reduces runtime load or improves reliability.
3. It is not duplicated elsewhere.
4. It is referenced from `SKILL.md`.
5. Its use condition is stated.
6. It is immediately usable and contains no placeholders unless the user explicitly requested a template.

Use TypeScript as the canonical OpenClaw hook handler unless the target runtime explicitly requires JavaScript or mixed output.

### 6. Validate

Run `scripts/validate_skill.py <skill-directory>` before claiming a package is complete or installable.

Also verify behaviour manually:

- trigger description covers intended use and excludes nearby non-use;
- workflow can execute without hidden context;
- output contract is observable;
- safety and side effects are explicit;
- source intent is preserved without fabricated detail;
- every support file is discoverable;
- structured assets match the output contract;
- hooks and scripts document inputs, outputs, side effects, and failure behaviour.

### 7. Package and Deliver

When export or installable packaging is requested:

- create exactly one top-level skill directory;
- place `SKILL.md` at its root;
- include only files created for, supplied by, or explicitly selected by the user;
- exclude source documents, private runtime material, credentials, logs, hidden files, caches, VCS metadata, and editor junk;
- produce a deterministic ZIP containing the single top-level folder;
- validate the archive after creation;
- return only the requested package surface.

When no output format is specified, provide the package tree, complete `SKILL.md`, and contents of necessary support files. Ask one packaging follow-up only after design-only delivery and only when it advances the task.

## Verification Checklist

- Folder name equals frontmatter `name`.
- `SKILL.md` exists at the skill root.
- Frontmatter parses and `description` is quoted.
- Description is concise and trigger-rich.
- Package is minimal but complete.
- Every support file is referenced exactly once or where operationally relevant.
- No empty folders, orphan files, duplicate handlers, decorative files, or unresolved placeholders.
- Scripts and hooks are executable or syntactically valid where applicable.
- ZIP has one top-level directory and no junk.
- Deliverable is faithful, self-contained, and does not expose protected context.

## Output Contract

Follow the user’s requested format exactly.

For machine/package mode, return only package links and concise validation status. For output-only mode, return only the requested file. For review mode, return actionable findings and repaired files without unrelated commentary.
