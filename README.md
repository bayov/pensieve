# Pensieve

> "Those who cannot remember the past are condemned to repeat it."
>
> — George Santayana

**Pensieve** is a system for codebase knowledge management,
designed to maintain a living memory of a project. It ensures
that hard-won knowledge—such as tricky bugs, hidden
dependencies, and undocumented conventions—is preserved and
shared with both future developers and AI coding agents.

## Core Concepts

### Insights

An **insight** is a piece of knowledge about the codebase that isn't immediately
obvious. This includes:

- Tricky bugs and their fixes.
- Architectural constraints.
- Hidden dependencies between components.
- Counter-intuitive configurations.
- Undocumented coding conventions.

### Documentation Targets

Insights are codified into the most appropriate documentation:

- **README.md** and source-code docs: For knowledge relevant
  to human developers (conventions, APIs, architecture,
  gotchas, setup). This is the primary target.
- **AGENTS.md**: For knowledge relevant only to AI coding
  agents (tool quirks, agent-specific workarounds). Placed
  strategically throughout the codebase to provide local
  agent context.

## Workflow

Pensieve operates on a simple two-step workflow:

1. **Record (Immediate & Proactive):** Agents use the `record-insight` skill to
   capture discoveries as they happen. These are stored as raw JSON files in
   `.pensieve/insights/`.
2. **Codify (On Request):** Periodically, or when requested by
   a human, the `codify-insights` skill processes these raw
   insights. It routes each insight to the appropriate
   documentation target (README.md, source-code docs, or
   AGENTS.md based on audience), and removes the raw files.

## Usage

### Skills

The underlying logic is handled by two specialized skills:

- **`record-insight`**: Used to save a specific discovery.
- **`codify-insights`**: Used to perform the complex task of integrating raw
  insights into existing documentation.

## Project Structure

- `src/`: Contains the contents of the Pensieve plugin/extension.
  - `src/skills/` - The Pensieve skills.
  - `src/INSTRUCTIONS.md` - Instructions that should be added to the context of
    any Agent session, teaching the agent how and when to use the Pensieve
    skills.
- `claude-plugin/`: Manifest to load Pensieve as a Claude Code plugin. Contains
  soft-links to `src/`.
- `gemini-extensions/`: Manifest to load Pensieve as a Gemini CLI extension.
  Contains soft-links to `src/`.
