# Reference Images

Dropped reference images into this folder and the agent will find them when composing prompts.

## Folder structure

- **`references/products/`** — product photos for ad creation
  - Use for: product hero shots, UGC testimonials, lifestyle showcases
  - Format: JPG or PNG, clear lighting, product-focused
  - Upload once, reuse forever

- **`references/influencers/`** — face/body photos to recreate as AI people
  - Use for: character recreation, identity lock across multiple videos
  - Format: headshot or full-body, clear facial features, good lighting
  - Same person across multiple ad clips: pass the same photo to each render

- **`references/aesthetics/`** — mood boards, lighting references, style inspiration
  - Use for: visual tone, lighting setup, color palette, composition style
  - Format: any reference image that captures the desired look
  - Multiple images per mood board are fine

## Guidelines

- **Minimum dimensions:** 512 × 512 px
- **Optimal dimensions:** 1024 × 1024 px or larger
- **Format:** JPEG (quality 90+) or PNG
- **Clear subject:** Product should be the main focus, well-lit, in focus
- **Simple background:** Plain or complementary background without clutter
- **No watermarks or text** unless that's part of the product

## Upload Strategy

1. Take/find a product photo
2. Save it under `references/products/[product-slug].jpg`
3. On first generation, the agent will ask: "Use this as a reference?"
4. Approve, and it's stored in `MASTER_CONTEXT.md`
5. All future generations reuse it automatically

## Note

This folder is `.gitignore`d, so your reference images stay local and never travel with a `git push`.
