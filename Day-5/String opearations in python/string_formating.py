# Python String format() Method

# Python3 program to demonstrate
# the str.format() method

# using format option in a simple string
print("{}, A computer science portal for geeks."
	.format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))


# ?-------------------------------------------------------

# Python program using multiple place
# holders to demonstrate str.format() method

# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
	.format("User", 19))

# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
	.format("one", "two", "three", "four"))

# ------------------------------------------------------------

# To demonstrate the use of formatters
# with positional key arguments.

# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
							"Geeks"))

# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
							"Geeks"))


print("Every {} should know the use of {} {} programming and {}"
	.format("programmer", "Open", "Source",
			"Operating Systems"))


# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
	.format("programmer", "Open", "Source", "Operating Systems"))


# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
	.format("computer", "geeks", gfg="GeeksforGeeks"))


# Escape sequence	Description    	 Example      
# \n	Breaks the string into a new line	print(‘I designed this rhyme to explain in due time\nAll I know’)
# \t	Adds a horizontal tab	print(‘Time is a \tvaluable thing’)
# \\	Prints a backslash	print(‘Watch it fly by\\as the pendulum swings’)
# \’   	Prints a single quote	print(‘It doesn\’t even matter how hard you try’)
# \”   	 Prints a double quote	print(‘It is so\”unreal\”‘)
# \a	makes a sound like a bell	print(‘\a’) 