# Python Exception Handling



# we will discuss how to handle exceptions in Python using try. 
# catch, and finally statement with the help of proper examples. 

# Error in Python can be of two types
# 1)Errors are the problems in a program due to which the program will stop the execution.
# 2) exceptions are raised when some internal events occur which changes the normal flow of the program. 

# Program error

# amount = 10000
# if(amount > 2999)
# print("You are eligible to purchase Dsa Self Paced")

# Correct program
amount = 10000
if(amount > 2999):
    print("You are eligible to purchase Dsa Self Paced")

# Exceptions: Exceptions are raised when the program is syntactically correct, but the code
#  resulted in an error. This error does not stop the execution of the program,
#   however, it changes the normal flow of the program.

# Exceptions in the program

# marks = 10000
# a = marks / 0
# print(a)

# Correct pgm:
marks = 10000
a = marks / 10
print(a)


# Try and Except Statement – Catching Exceptions

# Try and except statements are used to catch and handle exceptions in Python.
#  Statements that can raise exceptions are kept inside the try clause and the 
# statements that handle the exception are written inside except clause.

# Example: Let us try to access the array element whose index is out of bound 
# and handle the corresponding exception.

# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print("Second element = %d" %(a[1]))
	print("Fourth element = %d" %(a[2]))# Throws error since there are only 3 elements in array
except:
	print("An error occurred")


# Catching Specific Exception
# A try statement can have more than one except clause, to specify handlers for different
#  exceptions. Please note that at most one handler will be executed. For example, 
#  we can add IndexError in the above code. The general syntax for adding specific exceptions
#   are – 

# Program to handle multiple errors with one
# except statement
# Python 3

#--------------------------------------------------------------------------------
# def fun(a):
# 	if a < 4:
# 		# throws ZeroDivisionError for a = 3
# 		b = a/(a-3)
# 	# throws NameError if a >= 4
# 	print("Value of b = ", b)	
# try:
# 	fun(3)
# 	fun(4)
# # note that braces () are necessary here for
# # multiple exceptions
# except ZeroDivisionError:
# 	print("ZeroDivisionError Occurred and Handled")
# except NameError:
# 	print("NameError Occurred and Handled")
#---------------------------------------------------------------------------
# Try with Else Clause

# In python, you can also use the else clause on the try-except block which must be
#  present after all the except clauses. The code enters the else block only if the try 
#  clause does not raise an exception.

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b

def ace(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print (" Zero division error 'a/b result in 0' " )
	else:
		print (c)

# Driver program to test above function
ace(2.0, 3.0)
ace(3.0, 3.0)
ace(7,5)


#------------------------------------------------------------------
# Finally Keyword in Python

# Python provides a keyword finally, which is always executed after the
#  try and except blocks. The final block always executes after normal termination
#   of try block or after try block terminates due to some exception.
#-----------------------------------------------------------------------

# Syntax:

# try:
#     # Some Code.... 

# except:
#     # optional block
#     # Handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # Some code .....(always executed)

# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')


#------------------------------------------------------------------------------------
# Raising Exception

# The raise statement allows the programmer to force a specific exception to occur.
#  The sole argument in raise indicates the exception to be raised. This must be either an 
#  exception instance or an exception class (a class that derives from Exception).

# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not
