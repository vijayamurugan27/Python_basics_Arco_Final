import sys
print(sys.version)

# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')

# print("Exit")
# for passignthe output
sys.stdout.write('Vijaya murugan.A')

#To display the standard error
def print_to_stderr(*a):
	print(*a, file = sys.stderr)
print_to_stderr("Hello World")

# Command line arguments
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
Sum = 0
for i in range(1, n):
	Sum += int(sys.argv[i])
print("\n\nResult:", Sum)

# Python program to demonstrate
# sys.exit()

age = 120
if age < 18:
	# exits the program
	sys.exit("Age less than 18")	
else:
	print("Age is not less than 18")

# sys.path -the interpreter first searches for the specified module among 
# its built-in modules
print("System path = ",sys.path)
sys.path = []
print("After removing the path :",sys.path)
# import pandas #it won't work because we have cancelled all teh interpreter path

# sys.modules ->returns the python modules the current shell has imported.

import sys 
print(sys.modules)

# sys.getrefcount - to get the ref count for any obj, 0 when deleted
a = 'Ragavi'
print(sys.getrefcount(a))
