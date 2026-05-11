# Stock Market Expert System

def stock_system():

    print("📈 Stock Market Trading System")

    while True:

        market = input("\nEnter market condition (up/down/stable/exit): ").lower()

        if market == "exit":
            print("System Closed.")
            break

        elif market == "up":
            print("Suggestion: Buy Stocks")

        elif market == "down":
            print("Suggestion: Sell Stocks")

        elif market == "stable":
            print("Suggestion: Hold Stocks")

        else:
            print("Invalid market condition.")

stock_system()