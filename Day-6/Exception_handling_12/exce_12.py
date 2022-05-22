# Error pgm:
# amount = 10000
# if(amount > 2999)
# print("You are eligible to purchase Dsa Self Paced")
# Correct pgm
print("pgm-1", end = "\n\n")
amount = 10000
if(amount > 2999):
    print("You are eligible to purchase VIP customer ")

# Exceptions:


# marks = 10000
# a = marks / 0
# print(a)

# Correct pgm:

print("pgm-1.1", end = "\n\n")
marks = 10000
a = marks / 10
print(a)

# Try and Except Statement – Catching Exceptions


print("pgm-2", end = "\n\n")
a = [1, 2, 3]
try:
	print("Second element = %d" %(a[1]))
	print("Fourth element = %d" %(a[2]))# Throws error since there are only 3 elements in array
except:
	print("An error occurred or the item is out of range.")


#-------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------

print("pgm-3", end = "\n\n")
def fun(a):
	if a < 4:
		# throws ZeroDivisionError for a = 3
		b = a/(a-3)
	# throws NameError if a >= 4
	print("Value of b = ", b)	
try:
	fun(3)
	fun(5)
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")

#------------------------------------------------------------------------------------------
# Try with Else Clause


print("pgm-4", end = "\n\n")
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

#----------------------------------------------------------------------------------------


#------------------------------------------------------------------
# Finally Keyword in Python

print("pgm-5", end = "\n\n")
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')


#------------------------------------------------------------------------------------
# Raising Exception

print("pgm-6", end = "\n\n")
try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not






