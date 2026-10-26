def get_response(message):
    """Return a reply based on a simple text match."""
    message = message.lower().strip()

    if message in {"hello", "hi", "hey", "hello there"}:
        return "Hi! Welcome. How can I help you?"
    elif message in {"how are you", "how are you?"}:
        return "I'm fine, thanks for asking! How are you?"
    elif message in {"i am fine", "i'm fine", "fine", "good"}:
        return "That's great to hear!"
    elif message in {"what is your name", "what is your name?"}:
        return "I'm PyBot, a simple chatbot created with Python."
    elif message in {"what can you do", "what can you do?"}:
        return "I can reply to a few common messages. Try saying hello or asking my name."
    elif message in {"thank you", "thanks"}:
        return "You're welcome!"
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that yet. Try saying 'hello' or 'how are you'."


def main():
    print("=" * 44)
    print("             PYBOT CHATBOT")
    print("=" * 44)
    print("PyBot: Hello! Type 'bye' whenever you want to exit.\n")

    while True:
        user_message = input("You: ").strip()

        if not user_message:
            print("PyBot: Please type a message.")
            continue

        reply = get_response(user_message)
        print("PyBot:", reply)

        if user_message.lower().strip() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
