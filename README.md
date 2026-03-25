# nlpgame

An NLP project that demonstrates how to call an AI API (OpenAI-compatible).

## Quick start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure your API key

```bash
cp .env.example .env
# Open .env and replace "your_api_key_here" with your actual API key
```

You can also export the variable directly in your shell without creating a `.env` file:

```bash
export OPENAI_API_KEY="sk-..."
```

### 3. Run the demo

```bash
python main.py
```

---

## Calling the AI API in your own code

Import the `chat` helper from `ai_client`:

```python
from ai_client import chat

# Simple question
reply = chat("What is natural language processing?")
print(reply)

# With a system prompt
reply = chat(
    "Explain tokenisation in one sentence.",
    system="You are a concise NLP tutor.",
)
print(reply)

# Choose a specific model
reply = chat("Hello!", model="gpt-4o")
print(reply)
```

### Environment variables

| Variable          | Required | Default                          | Description                                   |
|-------------------|----------|----------------------------------|-----------------------------------------------|
| `OPENAI_API_KEY`  | ✅ Yes   | –                                | Your API key                                  |
| `OPENAI_BASE_URL` | No       | `https://api.openai.com/v1`      | Override for Azure OpenAI or local models     |
| `OPENAI_MODEL`    | No       | `gpt-4o-mini`                    | Default model used when none is specified     |

### Using a custom / local endpoint

Point `OPENAI_BASE_URL` at any OpenAI-compatible server (e.g. [Ollama](https://ollama.com), Azure OpenAI, etc.):

```bash
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"   # many local servers accept any non-empty key
export OPENAI_MODEL="llama3"
python main.py
```
