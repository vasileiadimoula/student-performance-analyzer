from student import Student
import json
import csv
import sqlite3
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
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    average REAL NOT NULL
)
""")
for student in csv_students:
    cursor.execute(
        "INSERT  OR REPLACE INTO students (name,average) VALUES (?,?)",
        (student.name,student.average())
    )
connection.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n--- Students from database---")
for row in rows:
    print(row)
name_to_search = input("\nEnter student name: ")
cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (name_to_search,)
)
student_found = cursor.fetchone()
if student_found:
    print("Student found:", student_found)
else:
    print("Student not found.")

connection.commit()
student_name = input("\nEnter student name to update:")
new_average = float(input("Enter new average: "))
cursor.execute("" \
    "UPDATE students SET average = ? WHERE name = ?",
    (new_average, student_name)
)
connection.commit()
print("\nAnna's average updated successfully!")
student_to_delete = input("Enter student name to delete:")
cursor.execute(
    "Delete FROM students WHERE name = ?",
    (student_to_delete,)
)
connection.commit()
print(f"{student_to_delete} deleted successfully!")
cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    ("Anna",)
)
print(cursor.fetchone())
connection.close()
print("\nData created succesfully")
