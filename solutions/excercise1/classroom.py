# Create a "Person" class which takes firstname and lastname as arguments to the constructor (___init___) and define a method that returns the full name of the person as a combined string
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

# Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.
class Student(Person): # inherit from parent class (Person class)
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)   # take __init__ from parent class
        self.subject = subject
    def printNameSubject(self):
        print(f"{self.full_name()}, {self.subject}")

# Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches.
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course
    def printNameCourse(self):
        print(f"{self.full_name()}, {self.course}")  