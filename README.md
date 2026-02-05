# Pensieve

> "Those who cannot remember the past are condemned to repeat it."
>
> — George Santayana

**Pensieve** is a system for codebase knowledge management, designed to maintain
a living memory of a project. It ensures that hard-won knowledge—such as tricky
bugs, hidden dependencies, and undocumented conventions—is preserved and
automatically shared with future AI agent sessions.

## Core Concepts

### Insights

An **insight** is a piece of knowledge about the codebase that isn't immediately
obvious. This includes:

- Tricky bugs and their fixes.
- Architectural constraints.
- Hidden dependencies between components.
- Counter-intuitive configurations.
- Undocumented coding conventions.

### AGENTS.md

The `AGENTS.md` files serve as the permanent memory for AI agents. They are
placed strategically throughout the codebase to provide local context. When an
agent operates in a directory, it reads the nearby `AGENTS.md` to understand the
local rules and history.

## Workflow

Pensieve operates on a simple two-step workflow:

1. **Record (Immediate & Proactive):** Agents use the `record-insight` skill to
   capture discoveries as they happen. These are stored as raw JSON files in
   `.pensieve/insights/`.
2. **Codify (On Request):** Periodically, or when requested by a human, the
   `codify-insights` skill processes these raw insights. It consolidates them,
   updates the relevant `AGENTS.md` files (and sometimes human docs like
   `README.md`), and removes the raw files.

## Usage

### Commands

Pensieve exposes two primary commands via the Gemini CLI:

- **`record [instructions]`**: Analyzes the current session and records all
  worthwhile insights. You can provide optional instructions to focus the
  recording.
- **`codify`**: Processes all pending insights and integrates them into the
  project's documentation.

### Skills

The underlying logic is handled by two specialized skills:

- **`record-insight`**: Used to save a specific discovery.
- **`codify-insights`**: Used to perform the complex task of integrating raw
  insights into existing documentation.

## Project Structure

- `.pensieve/insights/`: Temporary storage for raw, pending insights.
- `skills/`: Implementation of the core logic (Python scripts and skill
  definitions).
- `commands/`: Configuration for the Gemini CLI commands.
- `AGENTS.md`: (Created throughout the repo) The consolidated knowledge base for
  agents.