#self as an argument of method will point to the current object instance and must be specified when defining a method
#we create an instance of a class that is an object

# class Dog :
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 

#     def bark (self):
#         print("woof!")

# roger = Dog("Roger" , 8)
# print(type(roger))
# print (roger.name)
# print(roger.age)
# print(roger.bark()) 
# there is an extra None because calling bark() already prints woof!
# so when we use print(roger.bark()) the extra print returns None

class Student :
    pass
        
student1 = Student()
print(student1)
student1.name = "Nikhil"
student1.age = 20
student1.marks = 92

print(student1.name)
print(student1.age)
print(student1.marks)


class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

student1 = student("Nikhil", 20, 92)
print(student1.name)   # Nikhil
print(student1.age)    # 20
print(student1.marks)  # 92

# What happened here:

# Student("Nikhil", 20, 92) calls __init__ behind the scenes
# self refers to this particular object being created
# self.name = name stores the value into the object


#  What is self?

# self is just a reference to "this specific object." It's how Python knows which student's name you're setting.
# Internally:

# Inside __init__ for student1, self = student1
# Inside __init__ for student2, self = student2


