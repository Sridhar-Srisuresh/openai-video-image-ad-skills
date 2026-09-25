# Security

## API Keys

- `.env` is gitignored and created with `chmod 600` — never readable by other users
- Never paste API keys into chat or version control
- Rotate keys immediately if accidentally committed
- Use different keys for development and production if possible

## Logs

- `logs/generation-calls.jsonl` is gitignored and stays local
- Logs record word count, not full prompt text
- Logs never contain presigned URLs, credentials, or sensitive product info
- Review logs only you need — they contain spend history and job IDs

## Generated Content

- `outputs/` is gitignored and stays local
- Every Meta ad is created **PAUSED** — nothing goes live without manual review
- Generated images and videos remain on your machine until you publish them
- Provider CDN links expire; download finalized assets before sharing

## Best Practices

1. **Use environment variables, not CLI flags** for secrets
2. **Rotate API keys regularly** — plan a monthly refresh
3. **Run `./scripts/check-env.sh`** before and after key rotations
4. **Never edit `.env` in chat** — paste contents only to describe what's needed
5. **Keep `.env` and `MASTER_CONTEXT.md` local** — they contain workspace data
6. **Review generated ads before publishing** — no automated posting without review

## Compliance

You are responsible for:
- Respecting provider ToS and rate limits
- Not generating misinformation, spam, or misleading ads
- Not using real people's likenesses without permission
- Complying with platform ad policies (Meta, TikTok, YouTube, etc.)

This tool generates content; the responsibility for what you publish is yours.
