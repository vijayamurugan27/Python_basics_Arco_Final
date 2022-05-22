#Python program to add two numbers using function


def add_num123(a,b):#function for addition
    """ here we are going to add two numbers using python.py.

    Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.

It’s specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, the docstring should describe what the function does, not how.

What should a docstring look like?

    The doc string line should begin with a capital letter and end with a period.
    The first line should be a short description.
    If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
    The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. All functions should have a docstring.

Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.
The below examples demonstrates how to declare and access a docstring.
    """

    sum=a+b;
    return sum; #return value

num1=25  #variable declaration
num2=55
print("The sum is",add_num123(num1,num2))#call the function

# print("Using __doc__:")
# print(add_num123.__doc__)

print("Using help:")
help(add_num123)