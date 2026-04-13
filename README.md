# claude-skills

A Claude Code plugin marketplace with personal skills and tools.

## Plugins

| Plugin | Description |
|--------|-------------|
| [obsidian-ai-tools](plugins/obsidian-ai-tools/) | Create AI tool notes in an Obsidian Vault from YouTube videos or web pages |

## Quick Install

Add this marketplace in Claude Code:

```
/plugin marketplace add logtheta/claude-skills
```

Then install any plugin from the Discover tab.

## Manual Install

Add to `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "logtheta-skills": {
      "source": {
        "source": "github",
        "repo": "logtheta/claude-skills"
      }
    }
  }
}
```

See each plugin's README for setup details.
