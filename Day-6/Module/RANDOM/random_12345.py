# Method 	Description

# seed() 	Initialize the random number generator
# getstate() 	Returns the current internal state of the random number generator
# setstate() 	Restores the internal state of the random number generator
# getrandbits() 	Returns a number representing the random bits
# randrange() 	Returns a random number between the given range
# randint() 	Returns a random number between the given range
# choice() 	Returns a random element from the given sequence
# choices() 	Returns a list with a random selection from the given sequence
# shuffle() 	Takes a sequence and returns the sequence in a random order
# sample() 	Returns a given sample of a sequence
# random() 	Returns a random float number between 0 and 1
# uniform() 	Returns a random float number between two given parameters
# triangular() 	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters

# betavariate() 	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
# expovariate() 	Returns a random float number based on the Exponential distribution (used in statistics)
# gammavariate() 	Returns a random float number based on the Gamma distribution (used in statistics)
# gauss() 	Returns a random float number based on the Gaussian distribution (used in probability theories)
# lognormvariate() 	Returns a random float number based on a log-normal distribution (used in probability theories)
# normalvariate() 	Returns a random float number based on the normal distribution (used in probability theories)
# vonmisesvariate() 	Returns a random float number based on the von Mises distribution (used in directional statistics)
# paretovariate() 	Returns a random float number based on the Pareto distribution (used in probability theories)
# weibullvariate() 	Returns a random float number based on the Weibull distribution (used in statistics)

import random

random.seed(10)
print(random.random()) 
random.seed(10)
print(random.random()) 

# Definition and Usage

# The seed() method is used to initialize the random number generator.

# The random number generator needs a number to start with (a seed value), 
# to be able to generate a random number.

# Syntax
# random.seed(a, version)

# Parameter Values
# Parameter 	Description

# a  - 	Optional. The seed value needed to generate a random number.
# If it is an integer it is used directly, if not it has to be converted into an integer.
# Default value is None, and if None, the generator uses the current system time.

# version -	An integer specifying how to convert the a parameter into a integer.
# Default value is 2

print(random.getstate()) 

# Definition and Usage

# The getstate() method returns an object with the current state of
#  the random number generator.

# Use this method to capture the state, and use the setstate() method, with the captured state,
#  to restore the state

# Syntax
# random.getstate()

# # Python Random setstate() Method

#  import random

# #print a random number:
# print(random.random())

# #capture the state:
# state = random.getstate()

# #print another random number:
# print(random.random())

# #restore the state:
# random.setstate(state)

# #and the next random number should be the same as when you captured the state:
# print(random.random()) 
#------------------------------------------------------------------------------------------
# Python Random setstate() Method

# Definition and Usage

# The setstate() method is used to restore the state of
#  the random number generator back to the specified state

# Use the getstate() method to capture the state

# Syntax

# random.setstate(state)

# Parameter Values

# Parameter 	Description
# state 	    Required. A state object. the setstate() method will restore the 
#               state of  the random number generator back to this sate.

#-----------------------------------------------------------------------------------

# Python Random getrandbits() Method

# Definition and Usage

# The getrandbits() method returns an integer in the specified size (in bits).

# Syntax
# random.getrandbits(n)

# Parameter      Values
# Parameter 	Description
# n 	Required. A number specifying the size, in bits, of the returned integer.

print(random.getrandbits(8)) 

#------------------------------------------------------------------------------------------

# Python Random randrange() Method

print(random.randrange(3, 9)) 

# Definition and Usage

# The randrange() method returns a randomly selected element from the specified range.
# Syntax
# random.randrange(start, stop, step)

# Parameter Values
# Parameter 	Description
# start   	Optional. An integer specifying at which position to start.
#             Default 0
# stop    	Required. An integer specifying at which position to end.
# step    	Optional. An integer specifying the incrementation.
#             Default 1

#--------------------------------------------------------------------------------------------

# Python Random randint() Method
print(random.randint(3, 9)) 

# Definition and Usage

# The randint() method returns an integer number selected element from the specified range.

# Note: This method is an alias for randrange(start, stop+1).
# Syntax
# random.randint(start, stop)
# Parameter Values
# Parameter 	Description
# start 	Required. An integer specifying at which position to start.
# stop 	Required. An integer specifying at which position to end.

#-----------------------------------------------------------------------------------------

# Python Random choice() Method

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) 


# Definition and Usage

# The choice() method returns a randomly selected element from the specified sequence.

# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# Syntax
# random.choice(sequence)
# Parameter Values
# Parameter 	Description
# sequence 	Required. A sequence like a list, a tuple, a range of numbers etc.

x = "WELCOME"
print(random.choice(x)) 

#Python Random shuffle() Method

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist) 

#-------------------------------------------------- 
# import random

# def myfunction():
#   return 0.1

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist, myfunction)

# print(mylist) 
#Not actually working



# Definition and Usage

# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

# Note: This method changes the original list, it does not return a new list.

# Syntax
# random.shuffle(sequence, function)

# Parameter Values
# Parameter 	Description
# sequence 	Required. A sequence.
# function 	Optional. The name of a function that returns a number between 0.0 and 1.0.
# If not specified, the function random() will be used

# Python Random sample() Method

mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2)) 

# Definition and Usage

# The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

# Note: This method does not change the original sequence.

# Syntax
# random.sample(sequence, k)

# Parameter Values
# Parameter 	Description
# sequence 	Required. A sequence. Can be any sequence: list, set, range etc.

# k 	Required. The size of the returned list

#------------------------------------------------------------------------------
# Python Random random() Method
print(random.random())

# Definition and Usage

# The random() method returns a random floating number between 0 and 1.
# Syntax
# random.random()
# Parameter Values

# No parameters
#------------------------------------------------------------------------------------

# Python Random uniform() Method

print(random.uniform(20, 60)) 

# Definition and Usage

# The uniform() method returns a random floating number between the two specified numbers (both included).

# Syntax
# random.uniform(a, b)

# Parameter Values
# Parameter 	Description
# a 	        Required. A number specifying the lowest possible outcome
# b 	        Required. A number specifying the highest possible outcome

#------------------------------------------------------------------------------------------

# Python Random triangular() Method

# Definition and Usage

# The triangular() method returns a random floating number between the two specified numbers (both included), but you can also specify a third parameter, the mode parameter.

# The mode parameter gives you the opportunity to weigh the possible outcome closer to one of the other two parameter values.

# The mode parameter defaults to the midpoint between the two other parameter values, which will not weigh the possible outcome in any direction.
# Syntax
# random.triangular(low, high, mode)
# Parameter Values
# Parameter 	Description
# low 	Optional. A number specifying the lowest possible outcome.
# Default 0
# high 	Optional. A number specifying the highest possible outcome.
# Default 1
# mode 	Optional. A number used to weigh the result in any direction.
# Default the midpoint between the low and high values