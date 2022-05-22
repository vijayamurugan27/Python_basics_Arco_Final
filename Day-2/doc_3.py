def jar():
    """"This function is going to multiply the two numbers 50 and 60."""

    a = 50
    b = 60
    c = a*b
    print(c)
    

    

jar()
print("Docstring called using the __doc__ method:")
print(jar.__doc__)
print("docstring called using help method.")
help(jar)

# def my_function(arg1):
# 	"""
# 	Summary line.

# 	Extended description of function.

# 	Parameters:
# 	arg1 (int): Description of arg1

# 	Returns:
# 	int: Description of return value

# 	"""

# 	return arg1

# print(my_function.__doc__)
