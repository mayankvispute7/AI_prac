# Information Management Expert System

def information_system():

    records = {
        "student": "Student records are available.",
        "employee": "Employee database updated.",
        "attendance": "Attendance report generated.",
        "salary": "Salary details available."
    }

    print("📁 Information Management System")

    while True:

        query = input("\nEnter query (or exit): ").lower()

        if query == "exit":
            print("System Closed.")
            break

        elif query in records:
            print(records[query])

        else:
            print("Record not found.")

information_system()