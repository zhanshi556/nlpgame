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

## Getting Started

```bash
# Clone the repository
git clone https://github.com/zhanshi556/nlpgame.git
cd nlpgame

# Install dependencies
pip install -r requirements.txt

# Start the game
python main.py
```

## License

MIT
