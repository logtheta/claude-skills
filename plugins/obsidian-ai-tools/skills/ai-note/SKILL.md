---
name: ai-note
description: Create an AI tool note in the Obsidian Vault from a URL (YouTube video, Short, or webpage). Triggers on "/ai-note <url>".
argument-hint: <youtube-url-or-webpage-url>
allowed-tools: [Read, Write, Bash, Glob, Grep, WebFetch, WebSearch, Agent]
---

Create a new AI tool note in the Obsidian Vault from this link: $ARGUMENTS

Follow these steps exactly:

## Step 1: Get the transcript and metadata

**If the URL is a YouTube video or Short:**
1. Run `python3 .claude/yt-transcript.py "$ARGUMENTS"` to get the video transcript. This script handles all YouTube URL formats and auto-detects the language. If the transcript is not in English, translate it yourself to understand the content.
2. Also fetch the oEmbed metadata from `https://www.youtube.com/oembed?url=<URL>&format=json` to get the video title and author.
3. Read the transcript carefully to identify the **name of the AI tool** being presented and all details mentioned (features, pricing, benchmarks, comparisons, etc.).

**If the URL is a regular webpage:**
- Fetch it with WebFetch to extract the content.
- Identify the AI tool name and all details from the page content.

## Step 2: Research the tool on the web

Use WebSearch to find detailed information about the AI tool. Run these searches in parallel:
1. `"<tool name>" AI tool` -- general info
2. `"<tool name>" pricing plans` -- pricing details
3. `"<tool name>" features review` -- capabilities and use cases

From the search results, use WebFetch on the most promising pages (official site, reputable reviews) to extract:
- What the tool does (description)
- Key features and use cases (at least 3)
- Pricing tiers (free, paid plans, API costs -- be specific with dollar amounts)
- Platform availability (web, mobile, API, desktop, local, etc.)
- Category (video, avatar, coding, image-generation, writing, audio, etc.)
- Pricing model classification (free / freemium / paid / unknown)
- Related or competing tools

Cross-reference what the transcript says with what you find on the web. The transcript gives you the creator's perspective and demo highlights; the web gives you verified facts and pricing.

## Step 3: Read the template and style reference

Read these two files to understand the exact format:
- `Templates/AI Tool Template.md` at the vault root -- the template structure to match
- `AI Tools/InVideo AI.md` -- an existing note for writing style, detail level, and formatting conventions

## Step 4: Create the note

Write the note to `AI Tools/<Tool Name>.md` using the template with ALL fields filled in:

**Frontmatter rules:**
- `type`: always `ai-tool`
- `title`: the tool's proper name
- `source_url`: the original URL passed as argument (not a search result URL)
- `date_added`: today's date in YYYY-MM-DD format
- `category`: pick the most fitting one (video, avatar, coding, image-generation, writing, audio, music, design, productivity, etc.)
- `pricing_model`: one of `free`, `freemium`, `paid`, `unknown`
- `starting_price`: cheapest option with price, e.g. `$0 (free) / $20/mo (Pro)`
- `platform`: comma-separated list (web, ios, android, api, desktop, local, etc.)
- `status`: always `inbox`
- `tags`: array starting with `ai-tools`, then a category tag and a use-case tag

**Body rules:**
- `## What it is` -- 2-3 sentences. Lead with what it does, then key differentiators or tech behind it. Incorporate specific details from the transcript (benchmarks, demos, comparisons) backed by web research.
- `## How I can use it` -- 3+ bullet points of concrete, practical use cases written from the user's perspective.
- `## Pricing` -- list every tier with bold tier names, monthly prices, and key limits. Mention annual discounts if available.
- `## Short description` -- one sentence, concise, under 30 words.
- `## Related` -- 2+ related tools using `[[WikiLink]]` syntax with a short dash description.

## Important
- Do NOT leave any template placeholder unfilled. If info is truly unavailable, write `unknown` in frontmatter or `_Not yet available_` in body sections.
- Do NOT make up pricing. If you can't verify it, mark it as `unknown`.
- Keep the same tone and detail level as the InVideo AI example note.
