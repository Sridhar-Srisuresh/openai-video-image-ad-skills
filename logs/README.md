# Generation Call Logs

Append-only logs of every generation call made against provider APIs.

**The log file is not in this repo, by design.** `generation-calls.jsonl` is created on your first generation and stays on your machine — `logs/*.jsonl` is gitignored. This file is the schema; the data is yours.

## Entry Schema

```json
{
  "timestamp": "2026-09-25T10:15:30.123Z",
  "provider": "openai",
  "endpoint": "POST /images/generations",
  "model": "gpt-4o-mini",
  "jobId": "gen_abc123",
  "request": {
    "prompt": "(word count logged, not full text)",
    "promptWords": 127,
    "size": "1024x1024",
    "aspectRatio": "1:1"
  },
  "response": {
    "status": "succeeded",
    "cost": 0.04,
    "balance": 149.96,
    "generationTimeSec": 8
  }
}
```

## Fields

- `timestamp` — ISO 8601 timestamp when the API call was made
- `provider` — which provider (openai, google, runway, etc.)
- `endpoint` — which endpoint was called
- `model` — which model was used
- `jobId` — provider's job or request ID
- `request` — what was sent (word count, not full prompt)
- `response` — what came back (status, cost, timing)

## Never Log

- Full prompt text (store word count instead)
- API keys
- Presigned URLs or download links
- Personal or sensitive product information

## How the Agent Uses This

- **Before generating:** nothing. Do not read this file to build an estimate — call the provider API.
- **On submit:** append the request metadata immediately, so a crashed session still leaves a trace.
- **On completion:** update the line with final status and elapsed time.
- **Afterwards:** use it to answer "how long did that take", "what did last week cost", "which config failed".
