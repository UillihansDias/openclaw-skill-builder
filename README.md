# OpenClaw Skill Builder

An OpenClaw meta-skill for turning reusable capabilities into clear, maintainable AgentSkills. It can create a skill from a task description, convert a prompt or source material into a skill, review or repair an existing package, validate its structure, and prepare a package for installation or export.

The builder focuses on usable agent behaviour: clear triggers, an ordered workflow, safe boundaries, correct runtime details, and a verifiable output. It removes repeated or unsupported prompt language and keeps each package as small as the task allows.

## What it does

- **Create:** define a reusable capability, its audience, trigger, workflow, limits, and completion criteria.
- **Convert:** extract durable rules and procedures from prompts, notes, files, URLs, or existing skills. Preserve important requirements and identify conflicts or omissions.
- **Review and repair:** compare intended behaviour with the current package, find the smallest effective correction, and update only what is in scope.
- **Validate:** check skill naming, frontmatter, linked resources, package structure, scripts, hooks, and requested export contents.
- **Integrate and package:** add runtime-specific integration only when it is needed; keep creation, installation, enabling, and publishing as separate actions.
- **Capture reusable workflows:** after substantial work, assess whether the method is reusable beyond the task, supported by evidence or a bounded procedure, and not already covered. Turn only qualifying workflows into a narrow skill.

## When to use it

Use the builder when you want an OpenClaw skill created or improved, or when you need to convert reusable instructions into a skill package. It is not a general prompt-polishing tool unless you ask for prompt optimisation. A completed task does not automatically justify a new skill.

## Evidence-based autonomous capture

A distinctive capability is helping an agent preserve its own successful work as reusable skills. When an always-available workspace instruction, supported system prompt, or verified runtime hook invokes the builder after substantial work, it evaluates whether the workflow is meaningfully multi-step, reusable beyond the original task, supported by evidence or a bounded procedure, and not already covered by another skill. If it qualifies, the builder can create or update a narrowly scoped skill in the target runtime's verified skill directory; otherwise, it recommends no capture. The result is selective learning from demonstrated work, not a new skill for every completed task.

“Autonomous” describes the agent's assessment and capture once invoked—not an always-running background monitor. OpenClaw loads skills when relevant, so an always-available instruction or supported runtime integration must supply the reminder. The builder does not silently add that trigger, install hooks, change workspace policy, or publish skills unless that integration is requested.

This keeps three activities separate:

1. **Autonomous capture:** preserve a successful, reusable workflow discovered during substantial work.
2. **User-directed conversion:** create a skill from material that you explicitly provide.
3. **Runtime maintenance:** let a configured curator review or consolidate skills, if the target runtime supports it.

The builder checks the target runtime's actual skill directory, write method, approval controls, and packaging rules. It does not assume that another agent's commands or settings apply to OpenClaw.

## Package contents

```text
openclaw-skill-builder/
├── SKILL.md
├── README.md
├── references/
│   ├── canonical-rules.md
│   └── templates.md
├── scripts/
│   └── validate_skill.py
└── 🦞 AGENT-SKILL-BUILDER-CANONICAL-META-PROMPT.md
```

- `SKILL.md` is the operational entrypoint and workflow.
- `references/canonical-rules.md` covers OpenClaw runtime facts, package profiles, and integration boundaries.
- `references/templates.md` provides optional templates for skill files, hooks, and package responses.
- `scripts/validate_skill.py` checks a target skill package.
- The canonical meta-prompt is a detailed design reference for complex skill-authoring work.

## Install

From the repository root, install the skill with:

```bash
openclaw skills install . --as openclaw-skill-builder
```

You can then invoke it as `/openclaw-skill-builder` where slash-command skill invocation is enabled, or describe the skill-authoring task normally.

## Validate a skill package

```bash
python3 scripts/validate_skill.py /path/to/target-skill
```

Use strict mode for additional checks:

```bash
python3 scripts/validate_skill.py --strict /path/to/target-skill
```

The validator checks package structure and metadata. A structural pass does not prove that a skill behaves correctly in every runtime; behavioural checks are separate and should use realistic tasks when required.

## Design principles

1. **Make the entrypoint operational:** `SKILL.md` must say when to use the skill, what to do, and what counts as complete.
2. **Preserve intent, not prompt theatre:** keep useful constraints and decision rules; remove repetition, impossible guarantees, and hidden-reasoning demands.
3. **Use the smallest reliable package:** add references, scripts, or hooks only when they improve execution.
4. **Respect the target runtime:** verify supported metadata, paths, tools, and event hooks instead of assuming them.
5. **Keep authority clear:** local skill creation, installation, external publication, and shared-resource changes are distinct actions.
6. **Report evidence honestly:** distinguish files written, structural checks, runtime loading, and observed behaviour.

## Scope

This repository provides skill-authoring guidance and a package validator. It does not grant tools or permissions, install itself automatically, add a post-task trigger, or publish skills to a registry. Those actions depend on the user's OpenClaw setup and explicit workflow.
