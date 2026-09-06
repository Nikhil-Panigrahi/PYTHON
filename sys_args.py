import sys
print(sys.argv)

name = sys.argv[1]

print("Hello " + name)

#if i run this code normally using vs code run button error is showm
# I have to type in the terminal python .\fileName then the inputs in the terminal itself
# This is because system.arg gets the input from the comamnd line only

# Now let us dive deep into it

# When i run {python .\accepting_arguments.py Nikhil} python creates something like
sys.argv = ['accepting_arguments.py', 'Nikhil']
#so
sys.argv[0] # this means accepting_arguments.py
sys.arg[1] # this is Nikhil


# python
#   ↓
# starts accepting_arguments.py
#   ↓
# Nikhil is passed as an argument
#   ↓
# sys.argv = ['accepting_arguments.py', 'Nikhil']
#   ↓
# name = sys.argv[1]
#   ↓
# name = 'Nikhil'
#   ↓
# Hello Nikhil
