# Python Strings encode() method

    # Syntax:

    # encode(encoding, error)

    # Parameters: 

    #     encoding: Specifies the encoding on the basis of which encoding has to be performed. 
    #     error: Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and ‘ignore’ ignores the errors that occurred. There are six types of error response
    #     strict – default response which raises a UnicodeDecodeError exception on failure
    #     ignore – ignores the unencodable unicode from the result
    #     replace – replaces the unencodable unicode to a question mark ?
    #     xmlcharrefreplace – inserts XML character reference instead of unencodable unicode
    #     backslashreplace – inserts a \uNNNN escape sequence instead of unencodable unicode
    #     namereplace – inserts a \N{…} escape sequence instead of unencodable unicode

    # Returns: 

    # Returns the string in the encoded form
#---------------------------------------------------------------------------------------------------
    # Example 1: Code to print encoding schemes available
# Python3 code to print
# all encodings available

from encodings.aliases import aliases

# Printing list available
print("The available encodings are : ")
print(aliases.keys())

# Python code to demonstrate
# encode()

# initializing string
str = "geeksforgeeks"

# printing the encoded string
print ("The encoded string in utf8 format is : ",)
print (str.encode('utf8', 'ignore'))

# unicode string
string = 'GeeksforGeeks'

# print string
print('The string is:', string)

# ignore error
print(string.encode("ascii", "ignore"))

# replace error
print(string.encode("ascii", "replace"))

