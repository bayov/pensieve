---
name: codify-insights
description: Codifies pending Agent insights from .pensieve/insights into the codebase's AGENTS.md files. Use ONLY when explicitly requested by the user (e.g., "process insights", "codify insights"). NEVER use this skill proactively.
---

# Codify Insights

This skill is used to process all previously recorded codebase insights into
permanent project documentation (`AGENTS.md` for agents and human documentation
like `README.md` or source code comments).

Transform raw observations into high-quality, reusable context for
future agents, while keeping documentation clean and avoiding duplication.

Human documentation is sometimes updated as well, when the insights are useful
for humans as well.

## Workflow

### 1. Discovery

First, list all pending insights, **grouped by their target path**.

Run the helper script:

```bash
python3 skills/codify-insights/scripts/get_pending_insights.py
```

This returns a JSON list where each entry represents a **target directory** and
contains a list of pending insights for that directory:

```json

[
  {
    "target_path": "foo/bar/",
    "insights": [
      {
        "filename": "...",
        "content": "..."
      }
    ]
  }
]

```

### 2. Analysis & Integration

Iterate through the **groups** returned by the script. For **EACH**
`target_path` group:

#### A. Analyze Target Context

1. **Identify Destination**: Locate the `AGENTS.md` for this `target_path`.
    * If `target_path` is a file, use its parent directory.
    * If `target_path` is a directory, look for `AGENTS.md` inside it.

2. **Read Context**: Read the existing `AGENTS.md` (if it exists).

#### B. Formulate the Updates

Review **ALL** insights in this group together.

* **Consolidate**: Combine related observations into coherent paragraphs or
  rules.

* **Conflict Authority**: If a new insight contradicts existing documentation in
  `AGENTS.md`, the **new insight takes precedence**. Treat the insight as the
  most recent truth and overwrite the outdated information.

#### C. Apply Changes

1. **Update `AGENTS.md`**: Perform the edits (or create if it doesn't exist).
    * Incorporate **all** insights for this path.
    * Avoid bloating `AGENTS.md` with redundant information. This will become
      context for future agents, so keep it relevant.
    * Ensure the `AGENTS.md` file structure remains clean and structured.

2. **Update Human Docs**: If applicable, update `README.md` or other relevant
   human docs (such as comments within source files under `target_path`).

#### D. Remove

Once the insight is successfully incorporated (or deemed redundant/invalid),
remove the raw file to prevent re-processing.

Run for each processed file in the group:

```bash
python3 skills/codify-insights/scripts/remove_insight.py "<filename>"
```

### 3. Completion

After processing all pending insights, report a summary of what was updated to
the user.