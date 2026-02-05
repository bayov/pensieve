# Pensieve: Codebase Knowledge Management

This extension helps maintain a living memory of the codebase, ensuring that
hard-won knowledge is preserved and automatically shared with future Agent
sessions.

## Knowledge Management

- **Proactive Insights:** Use the `record-insight` skill **proactively**
  whenever you discover undocumented conventions, structural patterns, tricky
  logic, or architectural constraints. Record them immediately without waiting
  for an explicit request.
- **Codification:** Insights recorded in `.pensieve/insights/` should be
  integrated into the relevant `AGENTS.md` files (and optionally human docs)
  using the `codify-insights` skill. This permanently improves Agent context
  across the codebase.

## Skills

### `record-insight`

Use this to capture new knowledge as it's discovered.

- **When to use:** Immediately upon discovering something not obvious from the
  code itself.
- **Output:** A small JSON file in `.pensieve/insights/`.

### `codify-insights`

Use this to bake recorded insights into the project's documentation.

- **When to use:** When the user asks to "process insights" or "update agent
  context".
- **Outcome:** Updated `AGENTS.md` files throughout the repository.
