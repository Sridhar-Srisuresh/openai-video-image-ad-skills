#!/usr/bin/env bash
# Sync skills from canonical sources to editor skill folders

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Syncing skills to editor folders..."
echo ""

# Sync to Claude Code (.claude/skills/)
if [ -d "$REPO_ROOT/.claude/skills" ]; then
  echo "Syncing to .claude/skills/"
  
  # Copy individual skills
  for skill in "$REPO_ROOT/skills"/*; do
    if [ -d "$skill" ]; then
      skill_name=$(basename "$skill")
      echo "  → $skill_name"
      rm -rf "$REPO_ROOT/.claude/skills/$skill_name"
      cp -r "$skill" "$REPO_ROOT/.claude/skills/$skill_name"
    fi
  done
  
  # Copy shared skills
  if [ -d "$REPO_ROOT/shared/skills" ]; then
    for skill in "$REPO_ROOT/shared/skills"/*; do
      if [ -d "$skill" ]; then
        skill_name=$(basename "$skill")
        echo "  → shared/$skill_name"
        rm -rf "$REPO_ROOT/.claude/skills/$skill_name"
        cp -r "$skill" "$REPO_ROOT/.claude/skills/$skill_name"
      fi
    done
  fi
fi

# Sync to Cursor (.cursor/skills/)
if [ -d "$REPO_ROOT/.cursor/skills" ]; then
  echo "Syncing to .cursor/skills/"
  
  # Copy individual skills
  for skill in "$REPO_ROOT/skills"/*; do
    if [ -d "$skill" ]; then
      skill_name=$(basename "$skill")
      echo "  → $skill_name"
      rm -rf "$REPO_ROOT/.cursor/skills/$skill_name"
      cp -r "$skill" "$REPO_ROOT/.cursor/skills/$skill_name"
    fi
  done
  
  # Copy shared skills
  if [ -d "$REPO_ROOT/shared/skills" ]; then
    for skill in "$REPO_ROOT/shared/skills"/*; do
      if [ -d "$skill" ]; then
        skill_name=$(basename "$skill")
        echo "  → shared/$skill_name"
        rm -rf "$REPO_ROOT/.cursor/skills/$skill_name"
        cp -r "$skill" "$REPO_ROOT/.cursor/skills/$skill_name"
      fi
    done
  fi
fi

echo ""
echo "✓ Skills synced"
