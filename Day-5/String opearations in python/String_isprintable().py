#Python String isprintable() is a built-in method used for string handling. The isprintable() method returns “True” if all characters in the string are printable or the string is empty, Otherwise, It returns “False”. This function is used to check if the argument contains any printable characters such as:

    # Digits ( 0123456789 )
    # Uppercase letters ( ABCDEFGHIJKLMNOPQRSTUVWXYZ )
    # Lowercase letters ( abcdefghijklmnopqrstuvwxyz )
    # Punctuation characters ( !”#$%&'()*+, -./:;?@[\]^_`{ | }~ )
    # Space ( )

    #     Syntax: 

    # string.isprintable()

    # Parameters:

    # isprintable() does not take any parameters

    # Returns:

    #     True – If all characters in the string are printable or the string is empty.
    #     False – If the string contains 1 or more nonprintable characters.

    # Errors Or Exceptions:

    #     The function does not take any arguments, therefore no parameters should be passed, otherwise, it returns an error.
    #     The only whitespace character which is printable is space or ” “, otherwise every whitespace character is non-printable and the function returns “False”.
    #     The empty string is considered printable and it returns “True”.


# Python code for implementation of isprintable()

# checking for printable characters
string = 'My name is Ayush'
print(string.isprintable())

# checking if \n is a printable character
string = 'My name is \n Ayush'
print(string.isprintable())

# checking if space is a printable character
string = ''
print( string.isprintable())
