# Decorators in Python

# Decorators are a very powerful and useful tool in Python 
# since it allows programmers to modify the behaviour 
# of function or class. Decorators allow us to wrap another function 
# in order to extend the behaviour of the wrapped function, without
#  permanently modifying it. But before diving deep into decorators 
#  let us understand some concepts that will come in handy in
#   learning the decorators.

# First Class Objects
# In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.
# Properties of first class functions:

#     A function is an instance of the Object type.
#     You can store the function in a variable.
#     You can pass the function as a parameter to another function.
#     You can return the function from a function.
#     You can store them in data structures such as hash tables, lists,

# Python program to illustrate functions
# can be treated as objects
#---------------------------------------------------------------------------
# def shout(text):
# 	return text.upper()

# print(shout('Hello'))
# var = shout
# print(var('Hello'))
#--------------------------------------------------------------------------
def shout(text):
	return print(text.upper())

shout('Hello')
var = shout
var('Hello')
shout("hai")

#------------------------------------------------------------------------------
def shout(text):
	return print(text.upper())

def whisper(text):
	return print(text.lower())

def greeting(func):
    greet = func("""A function is passed as an argument.""")
    print(greet)

shout('Hello')
whisper("Hai")
greeting(shout)
greeting(whisper)

#-------------------------------------------------------------------------------
# Returning functions from another function.

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))

#-----------------------------------------------------------------------------------
