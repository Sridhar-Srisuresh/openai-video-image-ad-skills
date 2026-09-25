# Agents & Skills Orientation

This repository is designed to be used with **Claude Code** or **Cursor**. The skills system lets you ask for ads, and the agent handles the mechanical parts: provider routing, cost confirmation, generation, QA, and delivery.

## First-Time Setup

1. **Clone or open this repo in Claude Code or Cursor**

2. **Run setup:**
   ```bash
   ./scripts/setup.sh
   ```
   This creates `.env`, validates provider keys, and syncs skills to the editor.

3. **Check connectivity:**
   ```bash
   ./scripts/check-env.sh
   ```
   Returns which providers are active and ready.

4. **Fill in your workspace:**
   Edit `MASTER_CONTEXT.md` with:
   - Brand name and voice
   - Product description
   - Meta ad account IDs (if publishing)

5. **Drop a product photo:**
   ```bash
   mkdir -p references/products/
   # Copy your product image here
   ```

6. **Ask for an ad:**
   > Make me a 12-second UGC video of a woman in a kitchen holding [product], saying she loves how [feature] works.

## The Agent's Workflow

### Every Request Follows This Path

1. **Read context** → `MASTER_CONTEXT.md`, `references/`, brand voice
2. **Classify** → Which skill? (image-ad, video-ad, clone-image, pixar-ad, etc.)
3. **Route to provider** → Which API? (OpenAI, Google, Runway, etc.)
4. **Draft prompt** → Consult the prompt library for that workflow
5. **Gate 1 — Dialogue approval** (video only) → Extract spoken line, count words, get explicit yes/no
6. **Gate 2 — Cost confirmation** → Call provider estimate, show balance, get explicit yes/no
7. **Generate** → Submit to provider API
8. **Poll** (if async) → Check status every 15 seconds
9. **QA** → Inspect the output (audio, transcription, brand name, product geometry)
10. **Deliver** → Open folder, summarize what was made

### Two Non-Negotiable Gates

**Gate 1: Dialogue Approval**

For any video with spoken audio:
- Extract the exact words the actor will say
- Show them numbered by beat
- Count total words and state target duration
- Ask: "Approve this dialogue?"
- **No cost charged without this approval.**

**Gate 2: Cost Confirmation**

Before any generation:
- Call `provider.estimate()` with the exact configuration
- Show: cost, remaining balance, sufficiency
- Ask: "Approve this charge?"
- **No generation without this approval.**

## How to Ask for Ads

### Minimal Ask (Agent Infers Defaults)

> Make me a 12-second UGC video about [product].

Agent will:
- Use the default image provider for character reference stills
- Use the default video provider for final render
- Default to 9:16 (vertical short-form)
- Read brand voice from `MASTER_CONTEXT.md`
- Ask for dialogue approval before pricing

### Specific Ask (You Name the Provider)

> Use OpenAI to make a 12-second video, or use Runway if OpenAI is too expensive.

Agent will:
- Try OpenAI first, show the cost
- If you say "too expensive", try Runway and compare
- Let you pick which provider to use

### Cloning an Existing Ad

> Clone this competitor's video ad into a product demo for [my product].

Agent will:
- Analyze the source video (frames, pacing, transcript)
- Extract the beat structure and visual style
- Regenerate for your product with your product photo
- Preserve the original pacing and tone

### Multi-Step Workflows

> Make a Pixar-style ad: 4 beats, storyboard + motion + narration.

Agent will:
- Create a 4-beat storyboard on the image provider
- Render motion for each beat
- Ask for voiceover approval
- Assemble locally with ffmpeg

## Skill Reference

| Skill | Use When |
|-------|----------|
| `ad-generator` | Main router; don't call directly |
| `image-ad` | "Make me a still", "Create a thumbnail" |
| `video-ad` | "Make me a video", "UGC ad", "talking-head" |
| `image-to-motion` | "Animate this still", "Make it move" |
| `pixar-ad` | "Pixar-style", "storyboard-based" |
| `claymation-ad` | "Clay ad", "stop-motion" |
| `clone-image-ad` | "Copy this ad's style for my product" |
| `clone-video-ad` | "Remake this video for my product" |
| `analyze-video` | "Deconstruct this ad for me" |
| `youtube-thumbnail` | "Make a clickable thumbnail" |
| `caption-video` | "Burn subtitles into this MP4" |
| `music-mix` | "Add background music" |
| `broll-overlay` | "Overlay cutaways on this video" |

## Environment Variables

Edit `.env` to configure:

```env
# Providers
IMAGE_PROVIDER=openai          # which to use by default for stills
VIDEO_PROVIDER=openai          # which to use by default for videos

# API Keys (add at least one)
OPENAI_API_KEY=sk-proj-...
GOOGLE_API_KEY=...
RUNWAY_API_KEY=...
REPLICATE_API_TOKEN=...
FAL_KEY=...
KLING_API_KEY=...

# Meta publishing (optional)
META_ACCESS_TOKEN=...
META_AD_ACCOUNT_ID=...
```

## Logs & Observability

Every generation is logged to `logs/generation-calls.jsonl`:

```bash
tail -f logs/generation-calls.jsonl | jq .
```

Each line contains:
- timestamp, provider, endpoint, model
- request summary (prompt word count, not full text)
- response status, cost, balance, timing

## Troubleshooting

**"Provider key is missing"**
- Edit `.env` and add your API key
- Run `./scripts/check-env.sh`

**"Insufficient balance"**
- Top up your account with the provider
- Check `balance` in the cost confirmation screen

**"Generation timed out"**
- Check `logs/generation-calls.jsonl` for the job ID
- Provider might still be processing; check their dashboard

**"The video sounds wrong"**
- Re-generate with corrected dialogue
- Run video QA check: `ffmpeg -i output.mp4 -af volumedetect -f null -`

## Questions?

Check the skill's own `SKILL.md` file for detailed behavior, prompt formulas, and guardrails.
