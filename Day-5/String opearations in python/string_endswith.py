# Python String endswith() method returns True if a string ends with the given 
# suffix otherwise returns False.

#     Syntax:

#     str.endswith(suffix, start, end)

#     Parameters: 

#         suffix: Suffix is nothing but a string that needs to be checked. 
#         start: Starting position from where suffix is needed to be checked within the string. 
#         end: Ending position + 1 from where suffix is needed to be checked within the string.  

#     Note: If start and end index is not provided then by default it takes 0 and length -1 as starting and ending indexes where ending index is not included in our search.

#     Returns: 
#     It returns True if the string ends with the given suffix otherwise return False.
# 
# # Python code shows the working of
# .endswith() function

text = "geeks for geeks."

# returns False
result = text.endswith('for geeks')
print (result)

# returns True
result = text.endswith('geeks.')
print (result)

# returns True
result = text.endswith('for geeks.')
print (result)

# returns True
result = text.endswith('geeks for geeks.')
print (result)


#---------------------------------------------------------
# Python code shows the working of
# .endswith() function

text = "geeks for geeks."

# start parameter: 10
result = text.endswith('geeks.', 10)
print(result)

# Both start and end is provided
# start: 10, end: 16 - 1
# Returns False
result = text.endswith('geeks', 10, 16)
print(result)

# returns True
result = text.endswith('geeks', 10, 15)
print(result)
