---
name: caption-video
metadata: {packVersion: 0.1.0}
description: >-
  Burn subtitles into a finished MP4 using ffmpeg and local subtitle rendering helpers.
---

# Caption Video Skill

Burn subtitles or captions onto a finished MP4 without relying on a provider captioning endpoint.

## Workflow

1. Validate the input video exists and has audio.
2. Extract transcript or use a local speech-to-text tool.
3. Create an SRT or caption script with timings.
4. Render subtitles as burn-in with ffmpeg.
5. Verify output duration and playback integrity.

## Notes

- Prefer the provider API if available, but this local path is useful for custom styles.
- You must choose a style that matches the final use case: clean polished captions, dramatic tension, or social captioning.

