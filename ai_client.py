"""
AI API client for nlpgame.

Wraps the OpenAI-compatible API so callers do not need to manage
the client directly.  Configuration is loaded from environment
variables (or a .env file):

    OPENAI_API_KEY   – required, your API key
    OPENAI_BASE_URL  – optional, defaults to the official OpenAI endpoint
    OPENAI_MODEL     – optional, defaults to "gpt-4o-mini"
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load variables from a .env file when present (ignored if missing)
load_dotenv()

_DEFAULT_MODEL = "gpt-4o-mini"


def _get_client() -> OpenAI:
    """Create and return an OpenAI client using environment variables."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY is not set. "
            "Copy .env.example to .env and fill in your API key, "
            "or export the variable before running the program."
        )
    base_url = os.environ.get("OPENAI_BASE_URL")
    kwargs = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def chat(prompt: str, model: str | None = None, system: str | None = None) -> str:
    """Send a chat message and return the assistant reply.

    Args:
        prompt: The user message to send to the model.
        model:  Model name to use. Defaults to the OPENAI_MODEL environment
                variable, or ``gpt-4o-mini`` if that is not set.
        system: Optional system instruction prepended to the conversation.

    Returns:
        The text content of the assistant's reply.

    Raises:
        EnvironmentError: If OPENAI_API_KEY is not configured.
        openai.OpenAIError: For any error returned by the API.
    """
    client = _get_client()
    model = model or os.environ.get("OPENAI_MODEL", _DEFAULT_MODEL)

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content or ""
