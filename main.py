students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll": roll,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for student in students:
            print(student)
        print()


while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice\n")