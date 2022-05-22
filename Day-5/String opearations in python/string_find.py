# Python String find() method returns the lowest index of the substring 
# if it is found in a given string.
#  If it is not found then it returns -1. 

    # Syntax:

    # str.find(sub, start, end)

    # Parameters: 

    #     sub: It’s the substring that needs to be searched in the given string. 
    #     start: Starting position where the sub needs to be checked within the string. 
    #     end: Ending position where suffix needs to be checked within the string. 

    # Note #1: If start and end indexes are not provided then by default it takes 0 and length-1
    #  as starting and ending indexes where ending indexes are not included in our search. 

    # Returns: 

    # Returns the lowest index of the substring if it is found in a given string. If it’s not found then it returns -1.

    # Note #2: The find() method is similar to index(). The only difference is find() returns -1 if the searched string is not found and index() throws an exception in this case.

word = 'geeks for geeks'

# returns first occurrence of Substring
result = word.find('geeks')
print ("Substring 'geeks' found at index:", result )

result = word.find('for')
print ("Substring 'for ' found at index:", result )

# How to use find()
if (word.find('pawan') != -1):
	print ("Contains given substring ")
else:
	print ("Doesn't contains given substring")
