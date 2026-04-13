# claude-skills

Personal Claude Code skills and plugins by logtheta.

## Available Plugins

### obsidian-ai-tools

Create AI tool notes in an Obsidian Vault from YouTube videos or web pages. Invoke with:

```
/ai-note <youtube-url-or-webpage-url>
```

The skill will:
1. Extract transcript/content from the URL
2. Research the AI tool on the web (pricing, features, platform)
3. Create a structured Obsidian note using your vault's template

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Python 3 with `youtube-transcript-api` package (for YouTube transcript extraction):
  ```bash
  pip install youtube-transcript-api
  ```

### Step 1: Add the marketplace

Open your Claude Code settings file at `~/.claude/settings.json` and add this repository as an extra known marketplace:

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

If you already have other marketplaces in `extraKnownMarketplaces`, just add the `"logtheta-skills"` entry alongside them.

### Step 2: Enable the plugin

In the same `~/.claude/settings.json`, add the plugin to `enabledPlugins`:

```json
{
  "enabledPlugins": {
    "obsidian-ai-tools@logtheta-skills": true
  }
}
```

Again, merge this with any existing enabled plugins.

### Step 3: Set up the yt-transcript script

The skill expects a YouTube transcript helper at `.claude/yt-transcript.py` in your Obsidian Vault directory. You can either:

**Option A**: Copy the bundled script to your vault:
```bash
cp ~/.claude/plugins/cache/logtheta-skills/*/plugins/obsidian-ai-tools/skills/ai-note/scripts/yt-transcript.py \
   /path/to/your/vault/.claude/yt-transcript.py
```

**Option B**: Create a symlink:
```bash
mkdir -p /path/to/your/vault/.claude
ln -s ~/.claude/plugins/cache/logtheta-skills/*/plugins/obsidian-ai-tools/skills/ai-note/scripts/yt-transcript.py \
   /path/to/your/vault/.claude/yt-transcript.py
```

### Step 4: Set up your Obsidian Vault

The skill expects these files in your vault:
- `Templates/AI Tool Template.md` -- the note template (see `references/ai-tool-template.md` for the format)
- `AI Tools/` -- directory where new notes are created

Create the template and directory if they don't exist:
```bash
cd /path/to/your/vault
mkdir -p "AI Tools" Templates
```

Then copy the template:
```bash
cp ~/.claude/plugins/cache/logtheta-skills/*/plugins/obsidian-ai-tools/skills/ai-note/references/ai-tool-template.md \
   "Templates/AI Tool Template.md"
```

### Step 5: Restart Claude Code

Restart Claude Code (or start a new session) to pick up the new plugin. You should see `ai-note` listed when you type `/` in the prompt.

### Full settings.json example

Here's a minimal `~/.claude/settings.json` with just this plugin:

```json
{
  "extraKnownMarketplaces": {
    "logtheta-skills": {
      "source": {
        "source": "github",
        "repo": "logtheta/claude-skills"
      }
    }
  },
  "enabledPlugins": {
    "obsidian-ai-tools@logtheta-skills": true
  }
}
```

## Usage

Navigate to your Obsidian Vault directory in Claude Code, then:

```
/ai-note https://www.youtube.com/watch?v=abc123
/ai-note https://www.youtube.com/shorts/xyz789
/ai-note https://some-ai-tool-website.com
```

## Repository Structure

```
claude-skills/
├── marketplace.json                              # Marketplace metadata
├── README.md
└── plugins/
    └── obsidian-ai-tools/
        ├── .claude-plugin/
        │   └── plugin.json                       # Plugin metadata
        └── skills/
            └── ai-note/
                ├── SKILL.md                      # Skill definition (slash command)
                ├── scripts/
                │   └── yt-transcript.py          # YouTube transcript fetcher
                └── references/
                    ├── ai-tool-template.md       # Obsidian note template
                    └── example-invideo-ai.md     # Style reference note
```

## Adding More Skills

To add a new skill to this repository:

1. Create a new plugin directory under `plugins/` (or add a skill to an existing plugin)
2. Add the `skills/<skill-name>/SKILL.md` file with frontmatter and instructions
3. Register the plugin in `marketplace.json`
4. Push and restart Claude Code on the target machine
