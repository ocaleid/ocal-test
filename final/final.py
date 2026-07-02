def show_menu():
    print("******* Clinic Patient Management System *******")
    print("1. Add New Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient Information")
    print("5. Add Visit Note")
    print("6. View Patient History")
    print("7. Save Data")
    print("8. Exit")
    print("***********************************************")
    return input("Choose an option: ")
    
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    symptoms = input("Enter symptoms: ")
    global numbers
    patient = {
        "id": numbers.pop(),
        "name": name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms
    }
    
    patients.append(patient)
    print(f"Patient added successfully, ID is {patient['id']}")
    print("***********************************************")

def view_patients():
    print("******* All Patients *******")
    for patient in patients:
        print_patient(patient)

def search_patient():
    search_term = input("Enter patient name or ID: ")
    found = False
    for patient in patients:
        if str(patient['id']) == search_term or search_term.lower() in patient['name'].lower():
            print("Patient found :)")
            print_patient(patient)
            found = True
            break
    if not found:
        print("Patient not found.")
        print("***********************************************")

def print_patient(patient):
    print(f"ID: {patient['id']}")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Phone: {patient['phone']}")
    if patient['symptoms']:
        print(f"Symptoms: {patient['symptoms']}")
    print("***********************************************")
            
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    for patient in patients:
        if patient['id'] == patient_id:
            print("What do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Phone")
            print("4. Symptoms")
            i = input("Choose an option: ")
            if i == "1":
                patient['name'] = input("Enter new name: ")
            elif i == "2":
                patient['age'] = int(input("Enter new age: "))
            elif i == "3":
                patient['phone'] = input("Enter new phone number: ")
            elif i == "4":
                patient['symptoms'] = input("Enter new symptoms: ")
            else:
                print("Invalid choice.")
                print("***********************************************")
                return
            print("Patient updated successfully.")
            print("***********************************************")
            return
    print("Patient not found.")
    print("***********************************************")

def add_visit_note():
    patient_id = int(input("Enter patient ID: "))
    for patient in patients:
        if patient['id'] == patient_id:
            date = input("Enter visit date: ")
            doctor = input("Enter doctor name: ")
            note = input("Enter visit note: ")
            advice = input("Enter prescription/advice: ")
            visit = {
                "date": date,
                "doctor": doctor,
                "note": note,
                "advice": advice
            }
            if 'visits' not in patient:
                patient['visits'] = []
            patient['visits'].append(visit)
            print("Visit note added successfully.")
            print("***********************************************")
            return
    print("Patient not found.")
    print("***********************************************")
    
def view_patient_history():
    patient_id = int(input("Enter patient ID: "))
    for patient in patients:
        if patient['id'] == patient_id:
            print(f"Patient: {patient['name']}")
            if 'visits' in patient and patient['visits']:
                for i, visit in enumerate(patient['visits'], start=1):
                    print(f"Visit {i}:")
                    print(f"Date: {visit['date']}")
                    print(f"Doctor: {visit['doctor']}")
                    print(f"Note: {visit['note']}")
                    print(f"Advice: {visit['advice']}")
                    print("***********************************************")
            else:
                print("No visit history available.")
            print("***********************************************")
            return
    print("Patient not found.")
    print("***********************************************")

def save_data():
    with open ("patients.json", "w") as file:
        file.write("ID,Name,Age,Phone,Symptoms,Visit_Notes\n")
        for patient in patients:
            file.write(f"{patient['id']},{patient['name']},{patient['age']},{patient['phone']},{patient['symptoms']},{patient.get('visits', [])}\n")
        print("Data saved successfully.")
        
def main():
    while True:
        choice = show_menu()
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            add_visit_note()
        elif choice == "6":
            view_patient_history()
        elif choice == "7":
            save_data()
        elif choice == "8":
            break
        else:
            print("Invalid choice")
            print("***********************************************")
    print("THANK YOU FOR USING OUR SYSTEM :)")   

patients = []
import random
numbers = list(range(1000, 10000))
random.shuffle(numbers)
id_x=None
main()