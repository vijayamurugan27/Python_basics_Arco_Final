# # =   Assign value of right side of expression to left side operand	x = y + z
# +=    Add and Assign: Add right side operand with left side operand     a += b  
#       and then assign to left operand
# -=    Subtract AND: Subtract right operand from left operand and      a -= b  
#       then assign to left operand: True if both operands are equal
# *=    Multiply AND: Multiply right operand with left operand and      a *= b   
#       then assign to left operand
# **=   Divide AND: Divide left operand with right operand and          a /= b
#       then assign to left operand
# /=    Modulus AND: Takes modulus using left and right operands        a %= b  
#       and assign result to left operand
# //=   Divide(floor) AND: Divide left operand with right operand       a //= b   
#        and then assign the value(floor) to left operand
# %=    Exponent AND: Calculate exponent(raise power) value using       a **= b 
#       operands and assign value to left operand
# &=    Performs Bitwise AND on operands and assign value               a &= b  
#       to left operand
# !=    Performs Bitwise OR on operands and assign                      a |= b    
#        value to left operand
# ^=    Performs Bitwise xOR on operands and assign                     a ^= b    
#        value to left operand
# >>=   Performs Bitwise right shift on operands and                    a >>= b     
#        assign value to left operand
# <<=   Performs Bitwise left shift on operands and assign              a <<= b 
#        value to left operand
a = 100
b = 5
a = a+b
print(a)

a = 100
b = 5
a +=b
print(a)
print("the addision of ", a-5, "and", b, "is", a )
a = 100
b = 5
a -=b
print(a)
print("the Subtraction of ", a+5, "and", b, "is", a )
a = 100
b = 5
a *=b
print(a)
print("the multiplication of ", 100, "and", b, "is", a )
a = 100
b = 5
a **=b
print(a)
print("the exponent of ", 100, "and", b, "is", a )
a = 100
b = 5
a /=b
print(a)
print("the division of ", 100, "and", b, "is", a )
a = 100
b = 5
a //=b
print(a)
print("the quotient when ", 100, "by", b, "is", a )

a = 100
b = 5
a %=b
print(a)
print("the remainder when ", 100, "by", b, "is", a )

a = 3
b = 5
print("the And operation on", a, "by", b, "is")
a &=b
print(a)

# a = True
# b = False
# print("the AND operation on", a, "by", b, "is")
# a &=b
# print(a)

##convert the values to binary and do the operation(OR, AND, XOR).
a = 3
b = 5
print("the OR operation on", a, "by", b, "is")
a |=b
print(a)

# a = True
# b = False
# print("the or operation on", a, "by", b, "is")
# a |=b
# print(a)

a = True
b = True
print("the xor operation on", a, "by", b, "is")
a ^=b
print(a)

a = 3
b = 5
print("the xor operation on", a, "by", b, "is")
a ^=b
print(a)


a = 100
b = 5 #100is divided by 2, 5 times
print("the right operation on", a, "by", b, "is")
a >>=b
print(a)

a = 100
b = 5 #100 is multiplied by 2, 5 times
print("the left operation on", a, "by", b, "is")
a <<=b
print(a)
