def hello():
    print('hello!')

hello()
hello()

def greet(name):
    print("Hello", name)

greet('Nikhil')
greet("Luffy")
greet("Alex")

def profile(name,age):
    print("I am "+ name + " and my age is " + age)

profile('Nikhil', "20")    

#function can change value of data types whose values are mutable

def change(value):
    value = 2

val = 1
change(val)
print(val) # here val is stil 1 because it is immutable

def change1 (value):
    value["name"] = "Goku"
val = {"name" : "Nikhil"}
change1(val)
print(val)
