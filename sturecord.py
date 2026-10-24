import csv
FILE_NAME = "students.csv"

def create_file():
    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Student ID", "Name", "Age", "Course", "Email", "Marks"])
    file.close()

    print("CSV file created successfully.")


def add_student():
    file = open(FILE_NAME, "r")
    reader = csv.reader(file)
    data = list(reader)
    file.close()

    student_id = input("Enter Student ID: ")

    for row in data:
        if row[0] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")
    marks = input("Enter Marks: ")

    if name == "" or age == "" or course == "" or email == "" or marks == "":
        print("All fields are required.")
        return

    if age.isdigit() == False:
        print("Age should be a number.")
        return

    if "@" not in email:
        print("Invalid email.")
        return

    if marks.isdigit() == False:
        print("Marks should be a number.")
        return

    if int(marks) < 0 or int(marks) > 100:
        print("Marks must be between 0 and 100.")
        return

    file = open(FILE_NAME, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([student_id, name, age, course, email, marks])
    file.close()

    print("Student added successfully.")


def view_students():
    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    print("\nStudent Records")
    print("-" * 70)

    for row in reader:
        print(row)

    file.close()


def search_student():
    student_id = input("Enter Student ID to search: ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    found = False

    for row in reader:
        if row[0] == student_id:
            print("\nStudent Found")
            print("Student ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Course:", row[3])
            print("Email:", row[4])
            print("Marks:", row[5])

            found = True
            break

    file.close()

    if found == False:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)
    data = list(reader)
    file.close()

    found = False

    for row in data:
        if row[0] == student_id:
            print("Enter new details:")

            row[1] = input("Enter Name: ")
            row[2] = input("Enter Age: ")
            row[3] = input("Enter Course: ")
            row[4] = input("Enter Email: ")
            row[5] = input("Enter Marks: ")

            found = True
            break

    if found == False:
        print("Student not found.")
        return

    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()

    print("Student updated successfully.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)
    data = list(reader)
    file.close()

    new_data = []
    found = False

    for row in data:
        if row[0] == student_id and row[0] != "Student ID":
            found = True
        else:
            new_data.append(row)

    if found == False:
        print("Student not found.")
        return

    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)
    writer.writerows(new_data)
    file.close()

    print("Student deleted successfully.")


while True:
    print("Student Record Management System")
    print("1. Create CSV File if file not exist ")
    print("2. Add Student")
    print("3. View All Students")
    print("4. Search Student by ID")
    print("5. Update Student Details")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        add_student()

    elif choice == "3":
        view_students()

    elif choice == "4":
        search_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
