from student import Student
from database import (
    create_table,
    add_student, 
    get_all_students, 
    delete_student,
    update_student,
    find_student,
    database_is_empty
)
import json
import csv
import sqlite3
create_table()
def performance_statistics():
    students = get_all_students()

    if not students:
        print("No students found.")
        return

    averages = [student[2] for student in students]
    class_average = sum(averages) / len(averages)

    print(f"\nClass average: {class_average:.2f}")

    for student in students:
        name = student[1]
        average = student[2]

        if average > class_average:
            print(f"{name} is above the class average.")
        elif average == class_average:
            print(f"{name} is at the class average.")
        else:
            print(f"{name} is below the class average.")
print("\n---Students loaded from CSV ---")
csv_students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      grades = [
            int(row['grade1']),
            int(row['grade2']),
            int(row['grade3']),
            int(row['grade4'])
        ]
      student = Student(row['name'], grades)
      csv_students.append(student)
if database_is_empty():
    for student in csv_students:
       add_student(student.name, student.average())
       print("Database initialized with CSV data.")
def search_student():
    name_to_search = input("\nEnter student name: ").strip()
    if not name_to_search:
        print("Student name cannot be empty.")
        return
    student_found = find_student(name_to_search)
    if student_found:
       print("Student found:", student_found)
    else:
       print("Student not found.")
def update_student_average():
    student_name = input("\nEnter student name to update:").strip()
    if not student_name:
        print("Student name cannot be empty.")
        return
    try:
        new_average = float(input("Enter new average: "))
        if new_average < 0 or new_average > 20:
           print("Average must be between 0 and 20.")
           return
        updated = update_student(student_name, new_average)
        if updated > 0:
              print(f"{student_name} 's average updated successfully!")
        else:
               print("Student not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def remove_student():
    student_to_delete = input("Enter student name to delete:").strip()
    if not student_to_delete:
        print("Student name cannot be empty.")
        return
    deleted = delete_student(student_to_delete)
    if deleted > 0:
        print(f"{student_to_delete} deleted successfully!")
    else:
        print("Student not found.")
def create_student():
    name = input("\nEnter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        average = float(input("Enter student average: "))

        if average < 0 or average > 20:
            print("Average must be between 0 and 20.")
            return

        added = add_student(name, average)
        if added > 0:
            print(f"{name} added successfully!")
        else:
            print("Student already exists.")

    except ValueError:
        print("Invalid input. Please enter a number.")
def main():
  while True:
    print("\n--- Student Performance Analyzer ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Performance statistics")
    print("7. Exit")
    choice = input("\nChoose an option: ")
    if choice == "1":
        create_student()
    elif choice == "2":
       students = get_all_students()
 
       for student in students:
        print(student)

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student_average()

    elif choice == "5":
        remove_student()

    elif choice == "6":
       performance_statistics()
    elif choice == "7":
           print("Goodbye!")
           break
    else:
        print("Invalid option.")
if __name__ == "__main__":
    main()
