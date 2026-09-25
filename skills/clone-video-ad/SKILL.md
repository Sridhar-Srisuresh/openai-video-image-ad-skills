---
name: clone-video-ad
metadata: {packVersion: 0.1.0}
description: >-
  Clone an existing video ad into a new product video that preserves pacing, tone, and shot structure.
---

# Clone Video Ad

Analyze a source video to recover a reusable structure, then build a new version with the user’s product and message.

## Pipeline

1. Extract frames and transcript.
2. Name the beat structure and pacing.
3. Identify motion vocabulary and transitions.
4. Create a recreated prompt library entry.
5. Price the new render.
6. Generate and QA the new clip.

## Guardrails

- Keep the downstream edit structurally similar but not label-for-label identical.
- Do not assume all voice lines can be reused.
- Re-estimate after any wording change.

