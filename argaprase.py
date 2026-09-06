import argparse 
# argparse is a built-in Python module used to accept and process arguments from the command line.

parser = argparse.ArgumentParser()
# We create an argument parser.

# You can think of parser as a machine that:

      # "Knows what arguments my program expects and checks them."

parser.add_argument("name")
# This tells the parser:

# "My program requires an argument called name."

# Because we didn't put (--) before name, this is called a positional argument.

args = parser.parse_args()
# This is where argparse actually reads the command line.

print("Hello " + args.name)

    
