# Contributing

This is a personal fork of the Novoads agent-skills architecture, adapted for multi-provider use. Contributions are welcome.

## Goals

- Keep the repo provider-neutral
- Never hard-code API prices (always call the provider estimate endpoint)
- Always require explicit approval before any charge
- Never log API keys or presigned URLs
- Support new providers through the adapter pattern

## Adding a New Provider

1. Create `shared/providers/newprovider_adapter.py`
2. Implement the interface:
   ```python
   class NewProviderAdapter:
       def estimate(self, prompt, **kwargs): pass
       def generate_image(self, prompt, **kwargs): pass
       def generate_video(self, prompt, **kwargs): pass
       def poll(self, job_id): pass
   ```
3. Register in `shared/providers/provider_registry.py`
4. Add environment variable docs to `.env.example`
5. Add validation to `scripts/setup.sh` and `scripts/check-env.sh`

## Adding a New Skill

1. Create `skills/myskill/SKILL.md` describing the workflow
2. Add prompt formulas to `shared/prompts/` if needed
3. Write the skill logic (agent-driven, no separate executable)
4. Test with at least one provider

## Code Style

- Bash scripts: `set -euo pipefail`, no bashisms
- Python: 4-space indentation, type hints where helpful
- Documentation: Markdown, examples over abstract rules

## License

MIT. Derived from Novoads agent-skills (also MIT).
