#url:https://www.geeksforgeeks.org/python-math-module/
print("math module")
# Import math Library
import math

# Print the value of Euler e
print ("Euler's rule",math.e)
# Import math Library
import math

# Print the value of pi
print ("the value of Pi is", math.pi)


print("to find the area of a acircle.")
# Import math Library
import math

# radius of the circle
r = 4

# value of pie
pie = math.pi

# area of the circle
print( "The area of the circle is",pie * r * r)

# Import math Library
import math

# Print the value of tau
print ("the ratio of the circumference to the radius of a circle",math.tau)

# Import math Library
import math

# Print the positive infinity
print (math.inf)

# Print the negative infinity
print (-math.inf)


# Import math Library
import math

print (math.inf > 10e108)
print (-math.inf < -10e108)


#NAN
# Import math Library
import math

# Print the value of nan
print (math.nan)


# Python code to demonstrate the working of
# ceil() and floor()

# importing "math" for mathematical operations
import math

a = 2.3

# returning the ceil of 2.3
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))

# returning the floor of 2.3
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))


# Python code to demonstrate the working of
# factorial()

# importing "math" for mathematical operations
import math

a = 5

# returning the factorial of 5
print("The factorial of 5 is : ", end="")
print(math.factorial(a))

# Python code to demonstrate the working of
# gcd()

# importing "math" for mathematical operations
import math

a = 15
b = 5

# returning the gcd of 15 and 5
print ("The gcd of 5 and 15 is : ", end="")
print (math.gcd(b, a))


# Python code to demonstrate the working of
# fabs()

# importing "math" for mathematical operations
import math

a = -10

# returning the absolute value.
print ("The absolute value of -10 is : ", end="")
print (math.fabs(a))


# Python3 code to demonstrate
# the working of exp()
import math

# initializing the value
test_int = 4
test_neg_int = -3
test_float = 0.00

# checking exp() values
# with different numbers
print (math.exp(test_int))
print (math.exp(test_neg_int))
print (math.exp(test_float))


# Python code to demonstrate pow()
# version 1

print ("The value of 3**4 is : ",end="")

# Returns 81
print (pow(3,4))


# Python code to demonstrate the working of
# logarithm

# importing "math" for mathematical operations
import math


# returning the log of 2,3
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))

# returning the log2 of 16
print ("The value of log2 of 16 is : ", end="")
print (math.log2(16))
	
# returning the log10 of 10000
print ("The value of log10 of 10000 is : ", end="")
print (math.log10(10000))
#--------------------------------------------------
# Python3 program to demonstrate the
# sqrt() method

# import the math module
import math

# print the square root of 0
print("the square root of ",math.sqrt(0))

# print the square root of 4
print("the square root of ",math.sqrt(4))

# print the square root of 3.5
print("the square root of ",math.sqrt(3.5))


#-----------------------------------------------------
# Python code to demonstrate the working of
# sin(), cos(), and tan()

# importing "math" for mathematical operations
import math

a = math.pi/6

# returning the value of sine of pi/6
print ("The value of sine of pi/6 is : ", end="")
print (math.sin(a))

# returning the value of cosine of pi/6
print ("The value of cosine of pi/6 is : ", end="")
print (math.cos(a))

# returning the value of tangent of pi/6
print ("The value of tangent of pi/6 is : ", end="")
print (math.tan(a))


#----------------------------------------------------
# Python code to demonstrate the working of
# degrees() and radians()

# importing "math" for mathematical operations
import math

a = math.pi/6
b = 30

# returning the converted value from radians to degrees
print ("The converted value from radians to degrees is : ", end="")
print (math.degrees(a))

# returning the converted value from degrees to radians
print ("The converted value from degrees to radians is : ", end="")
print (math.radians(b))
#-----------------------------------------------------------------
# Python code to demonstrate
# working of gamma()
import math

# initializing argument
gamma_var = 6

# Printing the gamma value.
print ("The gamma value of the given argument is : "+ str(math.gamma(gamma_var)))

#-----------------------------

# Python3 code to demonstrate
# the working of isnan()
import math

# checking isnan() values
# with inbuilt numbers
print (math.isinf(math.pi))
print (math.isinf(math.e))


# checking for NaN value
print (math.isinf(float('inf')))
#----------------------------------------------------
# Python3 code to demonstrate
# the working of isnan()
import math

# checking isnan() values
# with inbuilt numbers
print (math.isnan(math.pi))
print (math.isnan(math.e))


# checking for NaN value
print (math.isnan(float('nan')))


