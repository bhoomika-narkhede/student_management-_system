import tkinter as tk
from tkinter import messagebox

students = []

try:
    file = open("students.txt", "r")

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

    file.close()

except FileNotFoundError:
    print("No previous records found")



def save_all_students():

    file = open("students.txt", "w")

    for student in students:

        file.write(
            f"Name: {student['name']}, "
            f"Roll: {student['roll']}, "
            f"Branch: {student['branch']}, "
            f"Maths: {student['maths']}, "
            f"Science: {student['science']}, "
            f"English: {student['english']}, "
            f"Percentage: {student['percentage']}\n"
        )

    file.close()


def clear_entries():

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    science_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)


def add_student():

    try:

        name = name_entry.get()
        roll = roll_entry.get()
        branch = branch_entry.get()

        maths = int(maths_entry.get())
        science = int(science_entry.get())
        english = int(english_entry.get())

        percentage = (maths + science + english) / 3

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

        save_all_students()

        messagebox.showinfo("Success", "Student Added Successfully")

        clear_entries()

    except:
        messagebox.showerror("Error", "Invalid Input")


def display_students():

    listbox.delete(0, tk.END)

    if not students:
        listbox.insert(tk.END, "No students found")
        return

    for student in students:

        percentage = student["percentage"]

        if percentage >= 90:
            grade = "A"

        elif percentage >= 75:
            grade = "B"

        elif percentage >= 50:
            grade = "C"

        else:
            grade = "Fail"

        data = (
            f"Name: {student['name']} | "
            f"Roll: {student['roll']} | "
            f"Branch: {student['branch']} | "
            f"Percentage: {round(percentage, 2)} | "
            f"Grade: {grade}"
        )

        listbox.insert(tk.END, data)


def search_student():

    search_name = name_entry.get()

    listbox.delete(0, tk.END)

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            data = (
                f"Name: {student['name']} | "
                f"Roll: {student['roll']} | "
                f"Branch: {student['branch']} | "
                f"Percentage: {round(student['percentage'], 2)}"
            )

            listbox.insert(tk.END, data)

            found = True

    if not found:
        listbox.insert(tk.END, "Student Not Found")


def update_student():

    name = name_entry.get()

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            student["maths"] = int(maths_entry.get())
            student["science"] = int(science_entry.get())
            student["english"] = int(english_entry.get())

            student["percentage"] = (
                student["maths"] +
                student["science"] +
                student["english"]
            ) / 3

            save_all_students()

            messagebox.showinfo("Success", "Student Updated")

            found = True

            break

    if not found:
        messagebox.showerror("Error", "Student Not Found")


def delete_student():

    name = name_entry.get()

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_all_students()

            messagebox.showinfo("Success", "Student Deleted")

            found = True

            break

    if not found:
        messagebox.showerror("Error", "Student Not Found")

root = tk.Tk()

root.title("Student Management System")
root.geometry("800x600")


tk.Label(root, text="Name").grid(row=0, column=0, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)


tk.Label(root, text="Roll").grid(row=1, column=0, pady=5)

roll_entry = tk.Entry(root)
roll_entry.grid(row=1, column=1)


tk.Label(root, text="Branch").grid(row=2, column=0, pady=5)

branch_entry = tk.Entry(root)
branch_entry.grid(row=2, column=1)


tk.Label(root, text="Maths").grid(row=3, column=0, pady=5)

maths_entry = tk.Entry(root)
maths_entry.grid(row=3, column=1)


tk.Label(root, text="Science").grid(row=4, column=0, pady=5)

science_entry = tk.Entry(root)
science_entry.grid(row=4, column=1)


tk.Label(root, text="English").grid(row=5, column=0, pady=5)

english_entry = tk.Entry(root)
english_entry.grid(row=5, column=1)


tk.Button(root, text="Add Student", width=20, command=add_student).grid(row=6, column=0, pady=10)

tk.Button(root, text="Display Students", width=20, command=display_students).grid(row=6, column=1)

tk.Button(root, text="Search Student", width=20, command=search_student).grid(row=7, column=0)

tk.Button(root, text="Update Student", width=20, command=update_student).grid(row=7, column=1)

tk.Button(root, text="Delete Student", width=20, command=delete_student).grid(row=8, column=0)


listbox = tk.Listbox(root, width=100, height=20)

listbox.grid(row=9, column=0, columnspan=3, pady=20)


root.mainloop()