from student import Student
students = [Student("Maria",[18,16,19,17]),
           Student("John",[14,15,13,16]),
           Student("Anna",[19,20,18,19]),
           Student("George",[12,14,15,13])]
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
