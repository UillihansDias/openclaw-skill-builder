# Agent Skill Builder

A meta-skill and packaging framework for creating, converting, reviewing, repairing, and validating OpenClaw AgentSkills.

Designed to turn loose user prompts, documentation, or workflows into minimal, high-craft, self-contained OpenClaw skill packages following canonical specification standards.

---

## Capabilities

- **Prompt-to-Skill Conversion**: Transforms raw system prompts or task instructions into modular, standardized AgentSkills.
- **Skill Architecture & Linting**: Enforces frontmatter standards, instruction altitude, trigger routing, and reference decoupling.
- **Automated Validation**: Built-in CLI validation harness to verify structural integrity, schema compliance, and script executability.
- **Canonical Meta-Prompt**: Comprehensive architectural framework (`🦞 AGENT-SKILL-BUILDER-CANONICAL-META-PROMPT.md`) for bootstrapping skills across any engineering domain.

---

## Directory Structure

```text
skill-builder/
├── README.md                                          # Framework documentation and usage
├── SKILL.md                                           # Core skill builder instructions and modes
├── references/
│   ├── canonical-rules.md                             # Architectural guidelines & frontmatter rules
│   └── templates.md                                   # Reusable templates for skills, hooks, and references
├── scripts/
│   └── validate_skill.py                              # Skill package validation CLI
└── 🦞 AGENT-SKILL-BUILDER-CANONICAL-META-PROMPT.md    # Master meta-prompt for autonomous skill generation
```

---

## Skill Validation Harness

Verify any OpenClaw skill package with `validate_skill.py`:

```bash
# Validate a target skill directory
python3 scripts/validate_skill.py /path/to/target-skill

# Strict validation mode
python3 scripts/validate_skill.py --strict /path/to/target-skill
```

The validator audits:
- YAML frontmatter completeness (`name`, `description`, metadata)
- Directory structure (assets, references, scripts, hooks)
- Executable permissions on helper scripts
- Markdown links and reference anchors

---

## Core Principles of Good Skills

1. **SKILL.md is the Kernel**: The primary document holds the core operational contract, triggers, and execution phases. Supporting documentation belongs in `references/`.
2. **Altitude Over Patching**: Address root capability design rather than layering superficial prompt hacks.
3. **Evidence-Driven**: Include concrete verification commands and output expectations.
4. **Minimal Blast Radius**: Avoid unnecessary dependencies, state mutations, or global tool assumptions.

---

## Installation in OpenClaw

```bash
openclaw skills install ./skill-builder --as skill-builder
```

Skill entry point: [`SKILL.md`](SKILL.md).
