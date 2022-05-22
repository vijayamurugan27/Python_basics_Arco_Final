# string.replace(old, new, count)

# old – old substring you want to replace. 
# new – new substring which would replace the old substring.
# count – the number of times you want to replace the old
#  substring with the new substring. (Optional ) 

# Return Value : 
# It returns a copy of the string where all occurrences of a substring are replaced with another substring. 
 

# Note: 

#     If count is not specified then all the occurrences of the old substring are replaced with the new substring.
#     This method returns the copy of the string i.e. it does not change the original string. 
     

# Below is the code demonstrating replace() : 

# Python3 program to demonstrate the
# use of replace() method

string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing all
# geeks by Geeks
print(string.replace("geeks", "Geeks"))

# Prints the string by replacing only
# 3 occurrence of Geeks
print(string.replace("geeks", "GeeksforGeeks", 3))
#_-----------------------------------------------------------------------------------

# Python3 program to demonstrate the
# use of replace() method

string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing
# e by a
print(string.replace("e", "a"))

# Prints the string by replacing only
# 3 occurrence of ek by a
print(string.replace("ek", "a", 3))
