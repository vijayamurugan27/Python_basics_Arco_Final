# =   Assign value of right side of expression to left side operand	x = y + z
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
    #    value to left operand

print("arithmetic operators")
a = 10
b = 15
print("The addsion values of ",a,"and", b, "is")
a +=b# a= a+b
print(a)

def art_12345():
    print("arithmetic Operators")
    a = 3# binary equivalent = 11
    b = 2# binary equivalent = 10
    print("The OR values of ",a,"and", b, "is")
    a |=b# a= a+b
    print(a)

    print("right shift Operators")#divide 100 by 2 , 3 times
    a = 100# binary equivalent = 11
    b = 5# binary equivalent = 10
    print("The right values of ",a,"and", b, "is")
    a >>=b# a= a+b
    print(a)

    print("left shift Operators")#muliply 100 by 2 , 3 times
    a = 100# binary equivalent = 11
    b = 5# binary equivalent = 10
    print("The left values of ",a,"and", b, "is")
    a <<=b# a= a+b
    print(a)

    a = 3# binary equivalent = 11
    b = 2# binary equivalent = 10
    print("The XOR values of ",a,"and", b, "is")
    a ^=b# a= a+b
    print(a)
    a = 3# binary equivalent = 11
    b = 2# binary equivalent = 10
    print("The XOR values of ",a,"and", b, "is")
    a ^=b# a= a+b
    print(a)



    print("bitwise Operators", end="\n\n\n")
    a = True# binary equivalent = 11
    b = False# binary equivalent = 10
    print("The OR values of ",a,"and", b, "is")
    a |=b# a= a+b
    print(a)
    #print("bitwise Operators")
    a = True# binary equivalent = 11
    b = False# binary equivalent = 10
    print("The AND values of ",a,"and", b, "is")
    a &=b# a= a+b
    print(a)
    #print("bitwise Operators")
    a = True# binary equivalent = 11
    b = False# binary equivalent = 10
    print("The XOR values of ",a,"and", b, "is")
    a ^=b# a= a+b
    print(a)



art_12345()