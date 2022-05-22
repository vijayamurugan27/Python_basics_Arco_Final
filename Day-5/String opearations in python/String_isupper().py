# Python String isupper() method returns whether or not all characters in a string are
#  uppercased or not.

#     Syntax:

#     string.isupper()

#     Parameters:

#     The isupper() method doesn’t take any parameters.

#     Returns:

#     True if all the letters in the string are in the upper case and False if even one
#      of them is in the lower case. 

# Python3 code to demonstrate
# working of isupper()

# initializing string
isupp_str = "GEEKSFORGEEKS"
not_isupp = "Geeksforgeeks"

# Checking which string is
# completely uppercase
print ("Is GEEKSFORGEEKS full uppercase ? : " + str(isupp_str.isupper()))
print ("Is Geeksforgeeks full uppercase ? : " + str(not_isupp.isupper()))
