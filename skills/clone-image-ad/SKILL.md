---
name: clone-image-ad
metadata: {packVersion: 0.1.0}
description: >-
  Reverse-engineer an existing image ad into a reusable prompt template and generate a matching
  style with a new product or brand.
---

# Clone Image Ad

This skill analyzes a source image and then builds a new ad in the same design language but with the user's product or message.

## Workflow

1. Read the source image and identify the structure.
2. Extract style cues: layout, palette, typography, spacing, visual hierarchy, image treatment.
3. Build a reusable prompt template.
4. Swap in the new product details.
5. Estimate and approve cost.
6. Generate a new still.
7. QA for fidelity and product correctness.

## Guardrails

- Do not copy protected branding or text unless explicitly provided.
- Preserve structural style more than literal copy.
- A clone is a reinterpreted template, not a direct duplicate.

