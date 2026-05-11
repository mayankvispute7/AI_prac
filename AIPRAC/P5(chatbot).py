# Simple AI Chatbot

from datetime import datetime

print("🤖 Welcome to AI Chatbot")
print("Type 'exit' to quit")

while True:

    user = input("\nYou: ").lower()

    if user == "exit":
        print("Chatbot: Goodbye 😊")
        break

    elif "hi" in user or "hello" in user or "hey" in user:
        print("Chatbot: Hello! How can I help you?")

    elif "help" in user or "what you can do" in user or "what u can do" in user:
        print("Chatbot: I can help with:")
        print("- Product price")
        print("- Order status")
        print("- Refund")
        print("- Time and date")

    elif "price" in user:
        print("Chatbot: Product price starts from ₹999.")

    elif "order" in user:
        print("Chatbot: Your order will arrive in 3-5 days.")

    elif "refund" in user:
        print("Chatbot: Refund will be processed in 5 working days.")

    elif "time" in user:
        print("Chatbot:", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("Chatbot:", datetime.now().strftime("%d-%m-%Y"))

    elif "bye" in user:
        print("Chatbot: Bye! Have a nice day 😊")

    else:
        print("Chatbot: Sorry, I didn't understand.")