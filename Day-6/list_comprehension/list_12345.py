# Advantages of List Comprehension

#     More time-efficient and space-efficient than loops.
#     Require fewer lines of code.
#     Transforms iterative statement into a formula.

# Empty list

print("pgm-1", end="\n\n\n")
print("Displaying data's using for loop.")
List = []

# Traditional approach of iterating
for character in 'hai hello welcome':
    List.append(character)

# Display list
print(List)

print("pgm-2", end="\n\n\n")
print("Using list comprehension to display the list elements.")
# Using list comprehension to iterate through loop
List = [character for character in 'hai hello welcome']

# Displaying list
print(List)

#-------------------------------------------------------------------

print("pgm-3 to display the time difference between for loop and list comprehension")
# Import required module
import time
# define function to implement for loop
def for_loop(n):
	result = []
	for i in range(n):
		a = result.append(i**2)        
	return result

# define function to implement list comprehension
def list_comprehension(n):
	return [i**2 for i in range(n)]

# Driver Code
# Calculate time takens by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for_loop:',round(end-begin,2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for list_comprehension:',round(end-begin,2))

#-------------------------------------------------------------------------------

print("Nested List Comprehensions", end ="\n\n\n")
print("entering values to a matrix.", end="\n\n")
matrix = []

for i in range(3):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)

print("adding values using list comprehension", end="\n\n")

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)
#=============================================================================

print("Usinf for loop in Lambda", end="\n\n\n")

# using lambda to print table of 10
numbers = []

for i in range(1, 6):
	numbers.append(i*10)

print(numbers)

#================================================================================

print("Another variation of the same program using in Lambda", end="\n\n\n")

numbers= [i*10 for i in range(1,6)]
print(numbers)

#--------------------------------------------------------------------------------

print("Using List comprehension program for  using in Lambda", end="\n\n\n")

numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))
print(numbers)

#-------------------------------------------------------------------------------
print("To display the squares of the numbers from 1-10", end="\n\n\n")
# Getting square of from 1 to 10
squares = [n**2 for n in range(1, 11)]

# Display square of even numbers
print(squares)


