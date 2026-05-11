# Airline Cargo Scheduling System

def airline_system():

    print("✈ Airline Scheduling System")

    while True:

        weight = input("\nEnter cargo weight in KG (or exit): ")

        if weight.lower() == "exit":
            print("System Closed.")
            break

        weight = int(weight)

        if weight <= 100:
            print("Passenger Flight Cargo Approved")

        elif weight <= 500:
            print("Cargo Flight Required")

        else:
            print("Heavy Cargo Special Schedule Needed")

airline_system()