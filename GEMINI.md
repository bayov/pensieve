# Pensieve: Codebase Knowledge Management

This extension helps maintain a living memory of the codebase, ensuring that
hard-won knowledge is preserved and automatically shared with future Agent
sessions.

## Knowledge Management

- **Record Immediately & Proactively:** Use the `record-insight` skill *
  *IMMEDIATELY** and **proactively** whenever you discover new or undocumented
  information about the codebase structure, patterns, or logic. **Do not wait
  for an error or a bug** to record an insight.
- **Proactive Discovery:** Whenever performing any task, if you explore the
  codebase and discover undocumented conventions, structural patterns, or logic
  that isn't immediately obvious, record it immediately. This includes
  understanding how different components interact, identifying 'source of truth'
  files, or uncovering intended but unwritten architectural rules.
- **Codification:** Insights recorded in `.pensieve/insights/` will eventually
  be integrated into the relevant `AGENTS.md` files (and optionally human docs)
  using the `codify-insights` skill. This permanently improves Agent context
  across the codebase. This skill is will be explicitly invoked by the user.

## Skills

### `record-insight`

Use this to capture new knowledge as it's discovered.

- **When to use:** Immediately upon discovering something not obvious from the
  code itself.
- **Output:** A small JSON file in `.pensieve/insights/`.

### `codify-insights`

Use this to bake recorded insights into the project's documentation.

- **When to use:** **ONLY** when the user explicitly asks to "process insights",
  "codify insights", or "update agent context". **NEVER** use this skill
  proactively or automatically.
- **Outcome:** Updated `AGENTS.md` files throughout the repository.
