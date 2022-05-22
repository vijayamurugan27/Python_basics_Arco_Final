# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())

# original string never changes
print("\nOriginal String")
print(text)
#---------------------------------------------------------------------------

# string capitalize() in Python
print(text.capitalize())
#--------------------------------------------------------------------
# Python String casefold() Method

# Python String casefold() method is used to implement caseless string matching.
#  It is similar to lower() string method but case removes all the case 
# distinctions present in a string. i.e ignore cases when comparing. 
print(text.casefold())

#--------------------------------------------------------------------------
# Python String center() Method

    # Syntax: 

    # string.center(length[, fillchar])

    # Parameters:

    #     length: length of the string after padding with the characters.
    #     fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.

    # Returns:

    # Returns a string padded with specified fillchar and it doesn’t modify the original string.

# Python program to illustrate
# string center() in python
string = "geeks for geeks"

new_string = string.center(24)

# here filchar not provided so takes space by default.
print("After padding String is: ", new_string)

# Python program to illustrate
# string center() in python
string = "geeks for geeks"

new_string = string.center(24, '#')

# here fillchar is provided
print("After padding String is:", new_string)
#------------------------------------------------------------------------------------
# Python String count() Method
# Python String count() function is an inbuilt function in python programming language 
# that returns the number of occurrences of a substring in the given string.

#     Syntax: 

#     string.count(substring, start=…, end=…)

#     Parameters: 

#         The count() function has one compulsory and two optional parameters. 
#             Mandatory parameter: 
#                 substring – string whose count is to be found.
#             Optional Parameters: 
#                 start (Optional) – starting index within the string where the search starts. 
#                 end (Optional) – ending index within the string where the search ends.

#     Return Value:

#     count() method returns an integer that denotes number of times a substring occurs in a given string. 
#--------------------------------------------------------
# Python program to demonstrate the use of
# count() method without optional parameters

# string in which occurrence will be checked
string = "geeks for geeks"

# counts the number of times substring occurs in
# the given string and returns an integer
print("Sting count",string.count("geeks"))

#Example 1: Implementation of the count() method without optional parameters


# # Python program to demonstrate the use of
# count() method using optional parameters

# string in which occurrence will be checked
string = "geeks for geeks"

# counts the number of times substring occurs in
# the given string between index 0 and 5 and returns
# an integer
print(string.count("geeks", 0, 5))

print(string.count("geeks", 0, 15))

#-----------------------------------------------------------------------------------------

