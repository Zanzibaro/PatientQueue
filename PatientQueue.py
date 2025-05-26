import re
from datetime import datetime, timedelta

class Patient:
    def __init__(self, name, surname, pesel, age, gender, appointment_time, priority=False):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.age = age
        self.gender = gender
        self.appointment_time = appointment_time
        self.priority = priority
        self.position = None
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None

    def add_patient(self, patient):
        if not self.head:
            self.head = patient
        else:
            current = self.head
            prev = None
            while current and datetime.strptime(current.appointment_time, "%H:%M") <= datetime.strptime(patient.appointment_time, "%H:%M"):
                prev = current
                current = current.next

            if prev:
                prev.next = patient
            else:
                self.head = patient
            patient.next = current

        self.update_positions()

    def add_priority_patient(self, patient):
        if not self.validate_appointment(patient.appointment_time):
            print("Invalid appointment time. It must be in 15-minute blocks.")
            return

        if not self.head:
            self.head = patient
        else:
            prev, current = None, self.head
            while current and datetime.strptime(current.appointment_time, "%H:%M") < datetime.strptime(patient.appointment_time, "%H:%M"):
                prev = current
                current = current.next

            patient.next = current
            if prev:
                prev.next = patient
            else:
                self.head = patient

        self.adjust_appointments(patient.appointment_time, patient)
        self.update_positions()

    def adjust_appointments(self, start_time, priority_patient):
        current = self.head
        while current:
            if current != priority_patient and current.appointment_time == start_time:
                if current.priority:
                    print(f"Cannot adjust {current.name} {current.surname} as they are a priority patient.")
                    break
                new_time = datetime.strptime(start_time, "%H:%M") + timedelta(minutes=15)
                while self.is_time_occupied(new_time.strftime("%H:%M")):
                    new_time += timedelta(minutes=15)
                start_time = new_time.strftime("%H:%M")
                current.appointment_time = start_time
            current = current.next

    def is_time_occupied(self, appointment_time):
        current = self.head
        while current:
            if current.appointment_time == appointment_time and current.priority:
                return True
            current = current.next
        return False

    def remove_patient(self, pesel):
        current = self.head
        prev = None

        while current:
            if current.pesel == pesel:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.update_positions()
                return True
            prev = current
            current = current.next

        return False

    def get_all_patients(self):
        patients = []
        current = self.head
        while current:
            patients.append(current)
            current = current.next
        return patients

    def update_positions(self):
        patients = self.get_all_patients()
        patients.sort(key=lambda p: datetime.strptime(p.appointment_time, "%H:%M"))
        self.head = None

        for patient in patients:
            patient.next = None
            self.add_patient_to_sorted_list(patient)

    def add_patient_to_sorted_list(self, patient):
        if not self.head:
            self.head = patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = patient

    @staticmethod
    def validate_appointment(appointment_time):
        try:
            time = datetime.strptime(appointment_time, "%H:%M")
            return time.minute % 15 == 0
        except ValueError:
            return False

def validate_name(name):
    return re.match(r"^[A-Za-z]+$", name) is not None

def validate_pesel(pesel):
    return re.match(r"^\d{11}$", pesel) is not None

def validate_gender(gender):
    return gender in ["k", "m", "i"]

def validate_age(age):
    return re.match(r"^\d{1,3}$", age) is not None

def display_menu():
    print("\nPatient Queue Management")
    print("1. Add Patient")
    print("2. Add Priority Patient")
    print("3. Remove Patient")
    print("4. List All Patients")
    print("5. Exit")

def main():
    queue = PatientQueue()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            if not validate_name(name):
                print("Invalid name. Only letters are allowed.")
                continue

            surname = input("Enter surname: ")
            if not validate_name(surname):
                print("Invalid surname. Only letters are allowed.")
                continue

            pesel = input("Enter PESEL (11 digits): ")
            if not validate_pesel(pesel):
                print("Invalid PESEL. It must contain exactly 11 digits.")
                continue

            age = input("Enter age: ")
            if not validate_age(age):
                print("Invalid age. It must be a number.")
                continue

            gender = input("Enter gender (k/m/i): ")
            if not validate_gender(gender):
                print("Invalid gender. It must be 'k', 'm', or 'i'.")
                continue

            appointment_time = input("Enter appointment time (HH:MM): ")
            if not queue.validate_appointment(appointment_time):
                print("Invalid appointment time. Must be in 15-minute blocks.")
                continue

            patient = Patient(name, surname, pesel, age, gender, appointment_time)
            queue.add_patient(patient)
            print("Patient added successfully!\n")

        elif choice == "2":
            name = input("Enter name: ")
            if not validate_name(name):
                print("Invalid name. Only letters are allowed.")
                continue

            surname = input("Enter surname: ")
            if not validate_name(surname):
                print("Invalid surname. Only letters are allowed.")
                continue

            pesel = input("Enter PESEL (11 digits): ")
            if not validate_pesel(pesel):
                print("Invalid PESEL. It must contain exactly 11 digits.")
                continue

            age = input("Enter age: ")
            if not validate_age(age):
                print("Invalid age. It must be a number.")
                continue

            gender = input("Enter gender (k/m/i): ")
            if not validate_gender(gender):
                print("Invalid gender. It must be 'k', 'm', or 'i'.")
                continue

            appointment_time = input("Enter appointment time (HH:MM): ")
            if not queue.validate_appointment(appointment_time):
                print("Invalid appointment time. Must be in 15-minute blocks.")
                continue

            patient = Patient(name, surname, pesel, age, gender, appointment_time, priority=True)
            queue.add_priority_patient(patient)
            print("Priority patient added successfully!\n")

        elif choice == "3":
            pesel = input("Enter PESEL of the patient to remove: ")
            if queue.remove_patient(pesel):
                print("Patient removed successfully!\n")
            else:
                print("Patient not found!\n")

        elif choice == "4":
            patients = queue.get_all_patients()
            if not patients:
                print("No patients in the queue.\n")
            else:
                for patient in patients:
                    print(f"Position: {patient.position}, {patient.name} {patient.surname}, PESEL: {patient.pesel}, Age: {patient.age}, Gender: {patient.gender}, Appointment: {patient.appointment_time}, Priority: {'Yes' if patient.priority else 'No'}")
                print()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
