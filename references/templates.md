# Canonical Templates

Read this file when drafting a new skill, creating a runtime hook, packaging a ZIP, or validating a machine-oriented delivery.

## Minimal SKILL.md

```markdown
---
name: skill-name
description: "Trigger-dense description of the capability and its task boundary."
---

# Skill Name

## Objective

State the reusable capability.

## Workflow

1. Inspect the inputs.
2. Apply the operational rules.
3. Verify the result.

## Output Contract

State the exact deliverable.
```

## Operational SKILL.md

```markdown
---
name: skill-name
description: "Use for concrete trigger cases; exclude nearby non-use cases."
---

# Skill Name

## Use When

- ...

## Do Not Use When

- ...

## Inputs

- ...

## Safety Boundary

- ...

## Workflow

### 1. Inspect
...

### 2. Decide
...

### 3. Execute
...

### 4. Verify
...

## Supporting Resources

- `references/example.md`: Read when ...
- `scripts/validate.py`: Run when ...

## Output Contract

- ...
```

## Hook Frontmatter

```markdown
---
name: skill-name
description: "Inject a brief operational reminder during agent bootstrap."
metadata:
  openclaw:
    events:
      - agent:bootstrap
---
```

Use only when runtime integration is justified. The handler must be complete, document side effects and failure behaviour, and guard against recursive sub-agent injection where applicable.

## Machine Package Response

```text
PACKAGE
- zip_file: <downloadable ZIP>
- skill_slug: <skill-slug>
- top_level_folder: <skill-slug>/

VALIDATION
- single_top_level_folder: pass
- skill_md_present: pass
- frontmatter_valid: pass
- support_files_referenced: pass
- no_junk_files: pass
- self_contained: pass
```

Return fewer fields when the user explicitly requests only the final package link.

## Validation Pattern

Validate in this order:

1. directory and naming;
2. YAML frontmatter;
3. support-file discoverability;
4. empty folders and junk files;
5. unresolved placeholders;
6. scripts and hooks;
7. ZIP topology;
8. behavioural fidelity.
