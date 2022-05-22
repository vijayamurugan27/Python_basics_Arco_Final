# Python String isalpha() Method

# Python String isalpha() method is a built-in method used for string handling. 
# The isalpha() methods returns “True” if all characters in the string are alphabets, 
# Otherwise, It returns “False”.  This function is used to check if the argument includes
#  only alphabet characters (mentioned below). 

    # Syntax: 

    # string.isalpha()

    # Parameters:

    # isalpha() does not take any parameters

    # Returns:

    #     True: If all characters in the string are alphabet.
    #     False: If the string contains 1 or more non-alphabets.

    # Errors and Exceptions:

    #     It contains no arguments, therefore an error occurs if a parameter is passed
    #     Both uppercase and lowercase alphabets return “True”
    #     Space is not considered to be the alphabet, therefore it returns “False”

    # Python code for implementation of isalpha()
   
# checking for alphabets
string = 'Ayush'
print(string.isalpha())
   
string = 'Ayush0212'
print(string.isalpha())
   
# checking if space is an alphabet
string = 'Ayush Saxena'
print( string.isalpha())