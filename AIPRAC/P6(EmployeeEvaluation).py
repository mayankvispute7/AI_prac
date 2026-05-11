# Employee Performance Evaluation System

def employee_system():

    print("👨‍💼 Employee Performance System")

    while True:

        name = input("\nEnter employee name (or exit): ")

        if name.lower() == "exit":
            print("System Closed.")
            break

        rating = int(input("Enter performance rating (1-10): "))

        if rating >= 8:
            result = "Excellent"

        elif rating >= 5:
            result = "Good"

        else:
            result = "Need Improvement "

        print(f"{name}'s Performance: {result}")

employee_system()