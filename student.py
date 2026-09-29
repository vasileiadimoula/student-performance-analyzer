class Student :
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)