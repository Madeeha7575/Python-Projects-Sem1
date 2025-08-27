#Palindrome Checker

"""def palindrome(word):
    word = word.lower().replace(" ","")
    reversed_word = word[::-1]
    return word == reversed_word
user_word = input("Enter a word:")
if palindrome(user_word):
    print("Its a palindrome.")
else:
    print("it is not a palindrome")
    """

#Number guessing game

"""import random
def guessing_game():
    level = input("Enter difficulty level (easy/hard):").lower()
    if(level =="easy"):
        attempts =10
    elif(level == "hard"):
        attempts = 5
    else:
        print("Invalid input.Defaulting to easy.")
        attempts = 10
    print(f"You have {attempts} attempts left.")
    num = random.randint(1,50)

    while attempts >0:
        guess = input("Enter a guess between 1 to 50:")
        if guess.isdigit():
            guess = int(guess)
            if(guess< num):
                print("Guess higher.")
            elif(guess>num):
                print("Guess lower.")
            else:
                print("You guessed it right.")
                return
            attempts -=1
            print(f"You have {attempts} attempts left.")
        else:
            print("Invalid answer.Guess again")
       
    print(f"Game over.Number is {num}")
guessing_game()"""

#Grading system
"""class Student:
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
    student.show_results()"""

#TO DO List

"""def task():
    tasks = [] #empty list
    print("__WELCOME TO THE TASK MANAGER APP__")
    total_task = int(input("How many tasks do you want to add?"))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i}:").lower()
        tasks.append(task_name)
        print(f"Today's tasks are\n{tasks}")
    while True:
        op = int(input("1-Add\n2-Update\n3-Remove\n4-View\n5-Exit\nEnter:"))
        if op == 1:
            add = input("Enter a task you want to add:").lower()
            tasks.append(add)
            print(f"Task {add} has been successfully added.")
        
        elif op == 2:
            updated_val = input("Enter a task you want to update:").lower()
            if updated_val in tasks:
                up = input("Enter new task:").lower()
                ind = tasks.index(updated_val)
                tasks[ind]= up
                print(f"Task {up} successfully updated.")
        elif op == 3:
            delete_val = input("Enter a task you want to delete:").lower()
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task {delete_val} has been deleted.")
        elif op==4:
            print(f"Total tasks = {tasks}")   
        elif op ==5:
            print("Closing the app...")
            break
        else:
            print("Invalid input.Enter again.")     

task()
"""
#Text File reader/writer
"""with open("hello_mam.txt", "w") as file:
    file.write("This is a new file")
with open("hello_mam.txt", "r") as file:
    content = file.read()
    print(content)
with open("hello_mam.txt", "a") as file:
    task =file.write("\n"+"bye")   
    """
