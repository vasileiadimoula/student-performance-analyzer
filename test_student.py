import unittest
from student import Student
class TestStudent(unittest.TestCase):
    def test_average(self):
        student = Student("Test", [10, 20])
        self.assertEqual(student.average(), 15)
    def test_empty_grades(self):
      student = Student("Test", [])
      self.assertEqual(student.average(), 0)
if __name__ == "__main__":
    unittest.main()