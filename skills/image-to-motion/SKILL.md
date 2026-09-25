---
name: image-to-motion
metadata: {packVersion: 0.1.0}
description: >-
  Animate an existing still image into a short motion ad. Best for UI screenshots,
  hero layouts, flat lays, and product stills that should move without a new scene.
---

# Image-to-Motion

This skill turns a still image into a subtle motion sequence. It is useful when the image itself is the shot and the user wants motion without re-shooting.

## Use cases

- Product still → subtle product reveal
- UI mockup → card pop / layered motion
- Flat-lay → slow rotation or parallax
- Ad hero image → minimal animation with punchy motion

## Workflow

1. Inspect the input image and decide whether it is a flat lay, product still, hero layout, or UI.
2. Choose motion vocabulary: slow drift, zoom-in, parallax, layered cards, subtle reveal, product pull-away.
3. Estimate cost via the selected provider.
4. Confirm the wording and duration.
5. Generate motion.
6. QA for overshoot, artifacting, or motion that destroys readability.

## Example prompt

> Animate this still as a subtle hero reveal. The image should remain readable while the product gently rotates and the headline card slides in, with soft lighting, high contrast, and minimal distortion.

## Guardrails

- Keep motion small and readable.
- Avoid heavily distorting typography or labels.
- Do not animate a still if the user intended a new generated scene.

