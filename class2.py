# Methods (functions inside a class)

# A method is just a function that belongs to a class and can access/use the object's data via self.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 40

student1 = Student("Nikhil", 20, 92)
student1.display()          # Name: Nikhil, Age: 20, Marks: 92
print(student1.has_passed()) # True

# . __str__ — controlling how print() shows your object

# Remember your earlier question about <__main__.Student object at 0x...>? That's what happens without __str__. Define it to customize:

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"{self.name} ({self.age}) - Marks: {self.marks}"

student1 = Student("Nikhil", 20, 92)
print(student1)   # Nikhil (20) - Marks: 92

