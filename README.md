# nlpgame

An NLP-powered text adventure game.

## User Profile

The user profile section tracks each player's progress and personalization settings.

| Field | Description |
|-------|-------------|
| Username | Unique display name for the player |
| Level | Current experience level based on completed quests |
| Score | Cumulative points earned during gameplay |
| Preferred Language | Language used for NLP interactions (default: English) |
| Achievements | List of unlocked in-game achievements |

### Profile Layout

```
┌─────────────────────────────┐
│  👤  Username               │
│  ⭐  Level: 1               │
│  🏆  Score: 0               │
│  🌐  Language: English      │
│  🎖️  Achievements: []       │
└─────────────────────────────┘
```

## Features

- Natural language understanding for game commands
- Dynamic story generation based on player choices
- Persistent user profiles with progress tracking
- Multi-language support via NLP models

## Configuration

### API Key Setup

The game uses an AI API (e.g. OpenAI) for NLP features. Set your API key as an environment variable before running the game.

**Option 1 — Environment variable (recommended)**

```bash
# Linux / macOS
export OPENAI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

**Option 2 — `.env` file**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-api-key-here
```

> ⚠️ **Never commit your `.env` file or API key to version control.** Add `.env` to your `.gitignore`.

The application reads the key with:

```python
import os
api_key = os.environ.get("OPENAI_API_KEY")
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/zhanshi556/nlpgame.git
cd nlpgame

# Install dependencies
pip install -r requirements.txt

# Set your API key (see Configuration section above)
export OPENAI_API_KEY="your-api-key-here"

# Start the game
python main.py
```

## License

MIT
