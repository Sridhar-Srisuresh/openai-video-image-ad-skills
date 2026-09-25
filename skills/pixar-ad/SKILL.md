---
name: pixar-ad
metadata: {packVersion: 0.1.0}
description: >-
  Create a stylized Pixar-like 3D animated ad using a storyboard pipeline with per-beat image generation
  and motion steps.
---

# Pixar Ad Skill

Build a multi-beat storyboard-style ad with per-frame images and a final assembled clip. The task is split into beats and then rendered.

## Pipeline

1. Extract the product and narrative arc.
2. Create a storyboard of 4–8 beats.
3. For each beat, generate a still image using the image provider.
4. Add motion to each beat or sequence it with motion transitions.
5. Add narration if required.
6. Assemble the final MP4 using ffmpeg.
7. QA the sequence and voice-over.

## Example beat structure

- Hook / reveal
- Product close-up
- Benefit demonstration
- CTA / final brand moment

## Guardrails

- Use the same brand/product context throughout the storyboard.
- Keep each beat visually consistent with the same lighting and character style.
- Do not put product labels or UI text that the user did not approve.

