students = []

try:

    with open("students.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            name = data[0].split(":")[1].strip()
            roll = data[1].split(":")[1].strip()
            branch = data[2].split(":")[1].strip()

            maths = int(data[3].split(":")[1].strip())
            science = int(data[4].split(":")[1].strip())
            english = int(data[5].split(":")[1].strip())

            percentage = float(data[6].split(":")[1].strip())

            student = {
                "name": name,
                "roll": roll,
                "branch": branch,
                "maths": maths,
                "science": science,
                "english": english,
                "percentage": percentage
            }

            students.append(student)

except FileNotFoundError:

    print("No previous student records found.")


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    maths=int(input("enter maths marks:"))
    science=int(input("enter science marks:"))
    english=int(input("enter english marks:"))
    percentage=(maths+science+english)/3

    student = {
        "name": name,
        "roll": roll,
        "branch": branch,
        "maths":maths,
        "science":science,
        "english":english,
        "percentage":percentage
    }

    students.append(student)
    print(students)
    file=open("students.txt","a")
    file.write(f"Name:{name},Roll:{roll},Branch:{branch},Maths:{maths},Science:{science},English:{english},Percentage:{percentage}\n")
    file.close()
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        for student in students:
            percentage=student["percentage"]
            if percentage>=90:
                grade="A"
            elif percentage>=75:
                grade="B"
            elif percentage>=50:
                grade="C"
            else:
                grade="Fail"
            print("====================")
            print("Student Record")
            print("====================")
            print("Name:",student["name"])
            print("Rollno:",student["roll"])
            print("Branch:",student["branch"])
            print("Maths:",student["maths"])
            print("Science:",student["science"])
            print("English:",student["english"])
            print("percentage:",round(percentage,2))
            print("Grade:",grade)
            print("======================")
            


        print()

def search_student():
    name=input("Enter student name to search:")
    found=False
    for student in students:
        if student["name"]==name:
            print("student found:")
            print(student)
            found=True
        if not found:
            print("student not found")
        print()

def update_student():
    name=input("enter student name to update:")
    found=False
    for student in students:
        if student["name"]==name:
            maths=int(input("enter new maths marks:"))
            science=int(input("enter new science marks:"))
            english=int(input("enter new english marks:"))
            percentage=(maths+science+english)/3
            student["maths"]=maths
            student["science"]=science
            student["english"]=english
            student["percentage"]=percentage
            print("student record updated successfully")
            found=True
        if not found:
            print("student not found")
        print()
    
def delete_student():
    name=input("enter student name to delete:")
    found=False
    for student in students:
        if student["name"]==name:
            students.remove(student)
            print("student deleted successfully")
            found=True
            break
        if not found:
            print("student not found")
        print()



while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    
    elif choice=="6":
        print("exiting program..")
        break

    else:
        print("Invalid choice\n")


