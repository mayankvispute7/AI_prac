print("🤖 Welcome to Chatbot")

while True:

    user = input("You: ").lower()

    if user == "exit":

        print("Chatbot: Goodbye")

        break

    elif "hi" in user or "hello" in user:

        print("Chatbot: Hello!")

    elif "price" in user:

        print("Chatbot: Product price starts from ₹999")

    elif "order" in user:

        print("Chatbot: Order will arrive in 3 days")

    elif "refund" in user:

        print("Chatbot: Refund processed successfully")

    else:

        print("Chatbot: Sorry, I don't understand")