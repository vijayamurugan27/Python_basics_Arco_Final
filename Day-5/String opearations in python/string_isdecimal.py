# Python string | isdecimal()

# isdecimal()-It is a function in Python that returns true 
# if all characters in a string are decimal. If all characters are not decimal
#  then it returns false.

# Syntax:

#     string_name.isdecimal()
#     Here string_name is the string whose characters are to be checked

# Parameters:This method does not takes any parameters .

# Returns Value:

#     True – all characters are decimal
#     False – one or more then one character is not decimal.

# Python3 program to demonstrate the use
# of isdecimal()

s = "12345"
print(s.isdecimal())

# contains alphabets
s = "12geeks34"
print(s.isdecimal())

# contains numbers and spaces
s = "12 34"
print(s.isdecimal())
