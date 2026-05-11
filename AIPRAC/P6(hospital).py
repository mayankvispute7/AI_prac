# Hospital Expert System

def hospital_system():

    symptoms = {
        "fever": "Suggested Medicine: Paracetamol",
        "cold": "Suggested Medicine: Cough Syrup",
        "headache": "Suggested Medicine: Pain Killer",
        "stomach pain": "Suggested Medicine: Antacid"
    }

    print("🏥 Hospital Expert System")

    while True:

        symptom = input("\nEnter symptom (or exit): ").lower()

        if symptom == "exit":
            print("System Closed.")
            break

        elif symptom in symptoms:
            print(symptoms[symptom])

        else:
            print("Please consult a doctor.")

hospital_system()