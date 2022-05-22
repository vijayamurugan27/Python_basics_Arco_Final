# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	Sets each bit to 1 if one of two bits is 1
#  ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

def bitwise_1234():
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

    a = True
    b = ~a # False
    if (a!=b):# False
        print("we have verified bitwise NOT operator1")
    else:
        print("we have verified bitwise NOT operator2")

bitwise_1234()