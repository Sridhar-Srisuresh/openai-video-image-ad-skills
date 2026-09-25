---
name: video-ad
metadata: {packVersion: 0.1.0}
description: >-
  Generate short-form AI video ads across various providers. Handles UGC, product hero,
  reveal, and documentary-style clips.
---

# Video Ad Skill

Create short-form video ads using the selected provider. Optimize for clear spoken lines, product focus, and believable motion.

## Supported directions

- UGC product testimonial
- Product reveal or hero film
- Talking-head founder clip
- Feature demo
- Silent motion ad for Reels / TikTok / Stories

## Request flow

1. Read product context and reference images.
2. Determine aspect ratio (default to `9:16` for vertical short-form). 
3. Draft script and segment it into beats.
4. Show dialogue for approval before any charge.
5. Price the exact render configuration via provider estimate.
6. Generate the video.
7. Poll until done.
8. QA the video: duration, audio stream, silence, transcription, and brand pronunciation.
9. Hand over the output and any notes.

## Provider backend rules

- OpenAI: use if `IMAGE_PROVIDER` or `VIDEO_PROVIDER` is set to `openai`.
- Google: use for `veo` / `imagen` style prompts.
- Runway: good for cinematic or motion-heavy vertical ads.
- Replicate / fal.ai: good for experimentation and alternative model routing.

## Example prompt

> Make a 12-second UGC-style product video. The person holds the product in a warm kitchen, looks directly into camera, natural motion, tight framing, handheld realism, subtle lens distortion, soft daylight, spoken line about why the product helps.

## Guardrails

- Always set explicit aspect ratio and duration.
- Keep video prompts grounded in product photos and brand context.
- If the voice-line is wrong or weak, rewrite, re-approve, then re-estimate.

