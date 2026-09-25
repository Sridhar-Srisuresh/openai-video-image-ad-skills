---
name: broll-overlay
metadata: {packVersion: 0.1.0}
description: >-
  Overlay b-roll cutaways or reactive visual inserts on top of a finished MP4.
---

# B-Roll Overlay Skill

Insert cutaway footage or supporting visuals over a base video.

## Workflow

1. Choose overlay windows and durations.
2. Validate the base video and overlay clips.
3. Build an edit decision list (EDL) with timings.
4. Overlay using ffmpeg.
5. QA final duration and sync.

## Guardrails

- Keep overlays short and relevant.
- Avoid obstructing the core message or spoken line.
- Preserve the original audio unless a replacement mix is intentionally chosen.

