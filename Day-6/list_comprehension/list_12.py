
print("pgm-1", end="\n\n\n")
print("Displaying data's using for loop.")

List = []
for character in 'hai hello welcome':
    List.append(character)
print(List)

print("pgm-2", end="\n\n\n")
print("Using list comprehension to display the list elements.")
List = [character for character in 'hai hello welcome']

print(List)

#-------------------------------------------------------------------

print("pgm-3 to display the time difference between for loop and list comprehension")
import time
from unittest import result
def for_loop(n):
	result = []
	for i in range(n):
		a = result.append(i**2)              
	return result


def list_comprehension(n):
	return [i**2 for i in range(n)]

begin = time.time()
for_loop(10**6)
end = time.time()

print('Time taken for_loop:',round(end-begin,2))

begin = time.time()
list_comprehension(10**6)
end = time.time()

print('Time taken for list_comprehension:',round(end-begin,2))

#-------------------------------------------------------------------------------

print("Nested List Comprehensions", end ="\n\n\n")
print("entering values to a matrix.", end="\n\n")
matrix = []

for i in range(3):
	
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)

print("adding values using list comprehension", end="\n\n")

matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)
#=============================================================================

print("Usinf for loop in Lambda", end="\n\n\n")

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
squares = [n**2 for n in range(1, 11)]
print(squares)


