"""
nlpgame – entry point.

Demonstrates how to call the AI API.  Run:

    python main.py

Make sure you have copied .env.example to .env and set your API key first,
or export OPENAI_API_KEY in your shell.
"""

from ai_client import chat


def main() -> None:
    print("=== nlpgame AI demo ===")
    print("Type your message and press Enter.  Type 'quit' to exit.\n")

    system_prompt = (
        "You are a helpful assistant for an NLP game. "
        "Answer questions clearly and concisely."
    )

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        reply = chat(user_input, system=system_prompt)
        print(f"AI:  {reply}\n")


if __name__ == "__main__":
    main()
