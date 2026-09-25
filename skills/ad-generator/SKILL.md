---
name: ad-generator
metadata: {packVersion: 0.1.0}
description: >-
  Provider-neutral ad generator router for AI video and image ads. Handles request classification,
  spoken-line approval, cost confirmation, provider selection, and QA before delivery.
---

# Ad Generator Router

This skill decides which provider, prompt library, workflow, and output style to use for a request.

## Configuration

- `IMAGE_PROVIDER` — `openai`, `google`, `replicate`, `fal`, or `runway`
- `VIDEO_PROVIDER` — `openai`, `google`, `replicate`, `fal`, `runway`, or `kling`
- `.env` — holds all provider credentials and local defaults

## Read order

1. `MASTER_CONTEXT.md`
2. This file
3. `references/` for product photos and style references
4. Prompt library for the chosen route

## Decision tree

| User wants | Route |
|---|---|
| Static still ad | `image-ad` |
| UGC selfie video | `video-ad` with product photo + voice-over |
| Product hero or reveal | `video-ad` |
| Scene-based narrative ad | `pixar-ad` or `claymation-ad` |
| Existing ad to clone | `clone-image-ad` or `clone-video-ad` |
| Existing video to analyze | `analyze-video` |
| Thumbnail | `youtube-thumbnail` |
| Captioning or music | `shared/skills/caption-video` / `shared/skills/music-mix` |

## Rule 1 — classify before any API call

Refuse requests that edit an existing local file, publish to an ad platform, or perform tasks outside generation and QA.

## Rule 2 — spoken-line gate

For any video with dialogue:

1. Extract the script and display it separately from the visual description.
2. Show it as numbered beats with the spoken words clearly visible.
3. State the language and the target duration.
4. Ask for explicit approval before any charge.

## Rule 3 — price gate

Before any generation call, request a live provider estimate and show:

- model
- cost or credits
- remaining balance
- whether the call is within the configured budget

Only proceed after approval.

## Rule 4 — provider adapter

Use `shared/providers/` to send the approved request to the selected provider.

Example provider map:

- OpenAI Images → `openai` adapter
- OpenAI Sora → `openai` adapter
- Google Veo / Imagen → `google` adapter
- Runway → `runway` adapter
- Replicate → `replicate` adapter
- fal.ai → `fal` adapter
- Kling → `kling` adapter

## QA

Before delivery, review each generated result for:

- brand correctness
- face and hand integrity
- product geometry and label clarity
- audio presence and narration accuracy
- video duration/format correctness

## Output contract

Return:

- a short summary of what was generated
- the source provider and model used
- the final output path
- notes about QA checks and any warnings

