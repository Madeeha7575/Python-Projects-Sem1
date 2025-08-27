#Grading system
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self.grade = self.calc_grade()
    def calc_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"
    def show_results(self):
        print(f"{self.name} got {self.marks} marks and grade {self.grade}.")
students = []
num = int(input("How many students?:"))
for i in range(num):
    name = input(f"Enter student's name {i +1}:")
    marks = int(input("Enter marks out of 100:"))
    student = Student(name,marks)
    students.append(student)
print("Student report:")
for student in students:
    student.show_results()