# Python String isdigit() Method

#     Difficulty Level : Medium
#     Last Updated : 12 Aug, 2021

# Python String isdigit() method is a built-in method used for string handling.
#  The isdigit() method returns “True” if all characters in the string are digits, 
# Otherwise, It returns “False”. This function is used to check 
# if the argument contains digits such as 0123456789

    # Syntax:

    # string.isdigit()

    # Parameters:

    # isdigit() does not take any parameters

    # Returns:

    #     True – If all characters in the string are digits.
    #     False – If the string contains 1 or more non-digits.

    # Errors And Exceptions:  

    #     It does not take any arguments, therefore it returns an error if a parameter is passed
    #     Superscript and subscripts are considered digit characters along with decimal characters, therefore, isdigit() returns “True”.
    #     The Roman numerals, currency numerators, and fractions are not considered to be digits. Therefore, the isdigit() returns “False”

    # Python code for implementation of isdigit()

# checking for digit
string = '15460'
print(string.isdigit())

string = '154ayush60'
print(string.isdigit())
