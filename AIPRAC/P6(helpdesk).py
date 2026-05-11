# Help Desk Expert System

def helpdesk():

    issues = {
        "password": "Reset password using forgot password.",
        "internet": "Restart router and reconnect.",
        "printer": "Check printer connection.",
        "software": "Reinstall the software."
    }

    print("💻 Help Desk System")

    while True:

        problem = input("\nEnter issue (or exit): ").lower()

        if problem == "exit":
            print("System Closed.")
            break

        elif problem in issues:
            print(issues[problem])

        else:
            print("Support ticket generated.")

helpdesk()