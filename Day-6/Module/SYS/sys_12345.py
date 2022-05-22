# Python sys Module


#     Difficulty Level : Easy
#     Last Updated : 10 Jun, 2021

# The sys module in Python provides various functions and variables that are used to
#  manipulate different parts of the Python runtime environment. It allows operating on
#   the interpreter as it provides access to the variables and functions that interact 
#   strongly with the interpreter. Let’s consider the below example.

import sys
print(sys.version)

# Input and Output using sys

# The sys modules provide variables for better control over input or output. We can even 
# redirect the input and output to other devices. This can be done using three variables –  

#     stdin
#     stdout
#     stderr

# stdin: It can be used to get input from the command line directly. 
# It used is for standard input. It internally calls the input() method. 
# It, also, automatically adds ‘\n’ after each sentence.



# import sys
# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')

# print("Exit")



# stdout:
#  A built-in file object that is analogous to the interpreter’s standard output stream 
#  in Python. stdout is used to display output directly to the screen console. Output can
#   be of any form, it can be output from a print statement, an expression statement, and 
#   even a prompt direct for input. By default, streams are in text mode. In fact, wherever
#    a print function is called within the code, it is first written to sys.stdout and then 
#    finally on to the screen.


import sys
sys.stdout.write('Ragavi')

 

# stderr: Whenever an exception occurs in Python it is written to sys.stderr. 

import sys


def print_to_stderr(*a):

	# Here a is the array holding the objects
	# passed as the argument of the function
	print(*a, file = sys.stderr)

print_to_stderr("Hello World")

# Command Line Arguments

# Command-line arguments are those which are passed
# during the calling of the program along with the calling statement.
#  To achieve this using the sys module, the sys module provides
#   a variable called sys.argv. It’s main purpose are:

#     It is a list of command-line arguments.
#     len(sys.argv) provides the number of command-line arguments.
#     sys.argv[0] is the name of the current Python script.

# Example: Consider a program for adding numbers and the numbers 
# are passed along with the calling statement.


# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
	
# Addition of numbers
Sum = 0

for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)



# Exiting the Program

# sys.exit([arg]) can be used to exit the program. 
# The optional argument arg can be an integer giving the exit
#  or another type of object. If it is an integer, zero is considered
#   “successful termination”.

# Note: A string can also be passed to the sys.exit() method.

# Python program to demonstrate
# sys.exit()

age = 20
if age < 18:
	# exits the program
	sys.exit("Age less than 18")	
else:
	print("Age is not less than 18")

# Working with Modules

# sys.path is a built-in variable within the sys module that returns the
#  list of directories that the interpreter will search for the required module. 

# When a module is imported within a Python file, the interpreter first searches
#  for the specified module among its built-in modules. If not found it looks
#   through the list of directories defined by sys.path.

# Note: sys.path is an ordinary list and can be manipulated.

# Example 1: Listing out all the paths

import sys
print(sys.path)

# Truncating the value of sys.path
# Removing the values
sys.path = []
# importing pandas after removing
# values


# import pandas

# sys.modules return the name of the Python modules that the current shell has imported.

import sys 
print(sys.modules)

# Reference Count

# sys.getrefcount() method is used to get the reference count for any given object.
#  This value is used by Python as when this value becomes 0, the memory for that 
#  particular value is deleted.


# sys.getrefcount - to get the ref count for any obj, 0 when deleted
a = 'Ragavi'
print(sys.getrefcount(a))

#-----------------------------------------

# More Functions in Python sys
# Function	Description
# sys.setrecursionlimit()	sys.setrecursionlimit() method is used to set the
#  maximum depth of the Python interpreter stack to the required limit.
# sys.getrecursionlimit() method	sys.getrecursionlimit() method is used to
#  find the current recursion limit of the interpreter or to find the maximum 
#  depth of the Python interpreter stack.
# sys.settrace()	It is used for implementing debuggers, profilers and coverage tools. 
# This is thread-specific and must register the trace using threading.settrace(). 
# On a higher level, sys.settrace() registers the traceback to the Python interpreter
# sys.setswitchinterval() method	sys.setswitchinterval() method is used to set the 
# interpreter’s thread switch interval (in seconds).
# sys.maxsize()	It fetches the largest value a variable of data type Py_ssize_t can store.
# sys.maxint	maxint/INT_MAX denotes the highest value that can be represented by an integer.
# sys.getdefaultencoding() method	sys.getdefaultencoding() method is used to get
#  the current default string encoding used by the Unicode implementation.
