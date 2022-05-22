# Python Lambda

# Syntax
# lambda arguments : expression 

x = lambda a : a + 10
print(x(5)) 

x = lambda a, b : a * b
print(x(5, 6)) 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

# Use of Lambda Function in python

# In Python, we generally use it as an argument to a higher-order function
#  (a function that takes in other functions as arguments). Lambda functions 
#  are used along with built-in functions like filter(), map() etc.

# use with filter()
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print("odd numbers",new_list)

# with map()
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print("The values in the list", my_list)
print("Using map function to show tha vles in the list & mul by 2.",new_list)