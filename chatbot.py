print("Hello! I'm your chatbot. Type 'exit' to stop.")

while True:
    user = input("You: ").lower()

    if user == "exit" or user == "bye" or user == "quit":
        print("Chatbot: Goodbye!")
        break

    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How are you?")

    elif "how are you" in user:
        print("Chatbot: I'm fine! Thanks for asking.")

    elif "name" in user:
        print("Chatbot: I'm a simple chatbot created for your task.")

    else:
        print("Chatbot: I don't understand. Try saying 'hello'.")
