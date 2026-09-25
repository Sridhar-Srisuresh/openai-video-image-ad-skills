---
name: image-ad
metadata: {packVersion: 0.1.0}
description: >-
  Generate static image ads using a provider-neutral pipeline. Works for product shots,
  lifestyle scenes, UI-mimicry layouts, infographics, and thumbnail-style stills.
---

# Image Ad Skill

Generate a still using a single image provider. Reuse the prompt library and product context from `MASTER_CONTEXT.md`.

## Provider selection

- `openai`: GPT Image / DALL-E / equivalent image model
- `google`: Imagen / Gemini image model
- `replicate`: hosted diffusion model
- `fal`: Flux or equivalent
- `runway`: if image generation is supported by the configured deployment

## Required inputs

- product description
- product photo or reference image
- target format (1:1, 9:16, 16:9, 4:5, etc.)
- tone and audience

## Workflow

1. Read product context and reference images.
2. Choose the shortest suitable prompt formula.
3. Run a live estimate through the selected provider.
4. Ask for explicit approval.
5. Generate the image.
6. Run image QA: hands, face, typography, product geometry, composition.
7. If defective, regenerate with corrected prompt up to 2 additional retries.
8. Deliver final asset.

## Example prompts

- "Create a premium product hero still with a soft studio background, realistic product, subtle shadows, clean headline, and strong visual hierarchy."
- "Make a UGC-style lifestyle ad featuring the product in a home kitchen, warm light, hand-held camera, natural textures, punchy but believable composition."

## Guardrails

- Avoid fabricated product labels unless the user provided them.
- Prefer the user's real product photo over a generic object render.
- If the model distorts product geometry or human anatomy, fix with explicit prompt wording and retry.

