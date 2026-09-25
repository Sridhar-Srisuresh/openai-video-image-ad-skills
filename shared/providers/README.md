# Provider adapter registry

This folder contains provider-neutral wrappers around model endpoints.

The registry is intentionally simple and should be extended as you integrate additional backends.

## Supported adapters

- `openai_adapter.py`
- `google_adapter.py`
- `runway_adapter.py`
- `replicate_adapter.py`
- `fal_adapter.py`
- `kling_adapter.py`

Each adapter exposes a consistent interface:

- `generate_image(prompt, **kwargs)`
- `generate_video(prompt, **kwargs)`
- `estimate(prompt, **kwargs)`
- `poll(job_id)`

