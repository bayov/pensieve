#!/usr/bin/env bash
set -euo pipefail

# Pensieve — Install as git submodule
# Run from the root of your project repository.

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# Defaults
SUBMODULE_DIR=".agents/pensieve"
SKILLS_DIR=".agents/skills"
REPO="git@github.com:bayov/pensieve.git"

# Parse flags
while [[ $# -gt 0 ]]; do
  case "$1" in
    --submodule-dir) SUBMODULE_DIR="$2"; shift 2 ;;
    --skills-dir)    SKILLS_DIR="$2";    shift 2 ;;
    --repo)          REPO="$2";          shift 2 ;;
    *)
      echo -e "${RED}Usage: install.sh [--submodule-dir .agents/pensieve] [--skills-dir .agents/skills] [--repo git@github.com:bayov/pensieve.git]${NC}" >&2
      exit 1
      ;;
  esac
done

# 1. Add submodule
if [ -d "$SUBMODULE_DIR" ]; then
  echo -e "${YELLOW}Submodule already exists at $SUBMODULE_DIR, skipping.${NC}"
else
  echo -e "${BLUE}Adding pensieve submodule...${NC}"
  git submodule add "$REPO" "$SUBMODULE_DIR"
fi

# 2. Symlink each skill into {dir}/skills/{skill-name}
mkdir -p "$SKILLS_DIR"

for skill_dir in "$SUBMODULE_DIR"/src/skills/*/; do
  skill_name="$(basename "$skill_dir")"
  link="$SKILLS_DIR/$skill_name"
  # Use relative path so the symlink is portable
  target="$(realpath --relative-to="$SKILLS_DIR" "$skill_dir")"

  if [ -L "$link" ]; then
    echo -e "${YELLOW}Symlink already exists: $link${NC}"
  else
    ln -s "$target" "$link"
    echo -e "${GREEN}Linked $link -> $target${NC}"
  fi
done

echo ""
echo -e "${GREEN}${BOLD}Done!${NC} Next steps:"
echo -e "  1. ${BOLD}[IMPORTANT]${NC} Add Pensieve instructions to your ${BOLD}AGENTS.md${NC} (or ${BOLD}CLAUDE.md${NC})."
echo -e "     See the pensieve README for the recommended template."
echo -e "  2. Commit the changes."
