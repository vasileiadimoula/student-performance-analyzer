from student import Student
import json

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
