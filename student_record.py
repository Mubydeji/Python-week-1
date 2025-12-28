students = []


def validate_age(age):
    if not age.isdigit() or int(age) <= 0:
        raise ValueError("Age must be a positive number")
    return int(age)


def validate_gpa(gpa):
    try:
        gpa = float(gpa)
    except ValueError:
        raise ValueError("GPA must be a number")

    if not (0.0 <= gpa <= 4.0):
        raise ValueError("GPA must be between 0.0 and 4.0")

    return gpa


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    student_id = input("Enter ID: ").strip()
    if find_student(student_id):
        print("Student ID already exists.")
        return

    name = input("Enter name: ").strip()

    try:
        age = validate_age(input("Enter age: "))
        gpa = validate_gpa(input("Enter GPA: "))
    except ValueError as e:
        print("Error:", e)
        return

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "gpa": gpa
    })
    print("Student added successfully.")


def view_student():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return

    print(student)


def update_student():
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return

    name = input(f"Enter new name ({student['name']}): ").strip()
    age = input(f"Enter new age ({student['age']}): ").strip()
    gpa = input(f"Enter new GPA ({student['gpa']}): ").strip()

    try:
        if name:
            student["name"] = name
        if age:
            student["age"] = validate_age(age)
        if gpa:
            student["gpa"] = validate_gpa(gpa)
    except ValueError as e:
        print("Error:", e)
        return

    print("Student updated successfully.")


def delete_student():
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return

    students.remove(student)
    print("Student deleted successfully.")


def list_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)


def menu():
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            list_students()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


# Run program
menu()
