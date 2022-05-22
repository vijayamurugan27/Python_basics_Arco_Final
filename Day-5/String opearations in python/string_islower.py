# Python String islower() method

#     Difficulty Level : Expert
#     Last Updated : 12 Aug, 2021

# Python String islower() method checks if all characters in the string are lowercase. This method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.

#     Syntax: 

#     string.islower()

#     Parameters: 

#     None

#     Returns: 

#         True: If all the letters in the string are in lower case and
#         False: If even one of them is in upper case.

# Python3 code to demonstrate
# working of islower()

# initializing string
islow_str = "geeksforgeeks"
not_islow = "Geeksforgeeks"

# checking which string is
# completely lower
print ("Is geeksforgeeks full lower ? : " + str(islow_str.islower()))
print ("Is Geeksforgeeks full lower ? : " + str(not_islow.islower()))
