from student import Student
from database import (
    create_table,
    add_student, 
    get_all_students, 
    delete_student,
    update_student,
    find_student
)
import json
import csv
import sqlite3
create_table()
add_student("Test Student", 18.5)
students_from_db = get_all_students()
print("\n---Students from database.py---")
for student in  students_from_db:
    print(student)
with open('students.json', 'r') as file:
    data = json.load(file)
students = []
for student_data in data:
    student = Student(student_data['name'], student_data['grades'])
    students.append(student)
for student in students:
    print(student.name)
    print(student.average())
averages =[]
for student in students:
    averages.append(student.average())
print(averages)
class_average =sum(averages)/len(averages)
print("\nClass average:", class_average)
for student in students:
    if student.average() > class_average:
        print(f"{student.name} is above the class average.")
    elif student.average() == class_average:
        print(f"{student.name} is at the class average.")
    else:
        print(f"{student.name} is below the class average.")
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
for student in csv_students:
    print(student.name, student.average())
for student in csv_students:
    add_student(student.name, student.average())
students_from_db = get_all_students()
for row in students_from_db:
    print(row)
name_to_search = input("\nEnter student name: ")
student_found = find_student(name_to_search)
if student_found:
    print("Student found:", student_found)
else:
    print("Student not found.")
student_name = input("\nEnter student name to update:")
new_average = float(input("Enter new average: "))
updated = update_student(student_name, new_average)
if updated > 0:
    print(f"{student_name}'s average updated successfully!")
else:
    print("Student not found.")
student_to_delete = input("Enter student name to delete:")
deleted = delete_student(student_to_delete)
if deleted > 0:
    print(f"{student_to_delete} deleted successfully!")
else:
    print("Student not found.")
print("\nData created succesfully")
