---
name: analyze-video
metadata: {packVersion: 0.1.0}
description: >-
  Extract shot structure, transcript, and pacing from a reference video and turn it into a reusable
  prompt template for new ad generation.
---

# Analyze Video

This skill reads frames and transcript, then outputs a structured summary: hooks, beats, moments, shot types, motion, and pacing.

## Output structure

- `hook`
- `shot_summary[]`
- `pacing`
- `voice_over`
- `visual_style`
- `camera_movement`
- `transitions`
- `recommended_prompt_template`

## Workflow

1. Read the source video.
2. Extract frames at regular intervals.
3. Transcribe spoken content.
4. Summarize pacing and beat structure.
5. Write a reusable prompt template.
6. Save the template under a prompt library or local docs folder.

## Guardrails

- Keep recommendations grounded in what actually appears in the video.
- Distinguish between direct product shots and generic motion shots.
- Never invent a voice-over that isn't in the source.

