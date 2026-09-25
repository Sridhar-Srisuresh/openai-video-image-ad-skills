---
name: music-mix
metadata: {packVersion: 0.1.0}
description: >-
  Mix the final video with a music bed, ducking under narration and preserving picture integrity.
---

# Music Mix Skill

Mix a soundtrack under a finished edit using ffmpeg.

## Workflow

1. Validate final cut and music file.
2. Trim the music to the exact video duration.
3. Apply fade-in/out and optional ducking under spoken lines.
4. Write the final mixed file.
5. QA audio level and sync.

## Notes

- Keep the music subtle to allow the main spoken message to lead.
- Preserve the original video stream when possible to avoid re-encoding artifacts.

