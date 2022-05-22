# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	Sets each bit to 1 if one of two bits is 1
#  ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


a = True
b = False
print("the AND operation on", a, "and", b, "is")
a &=b
print(a)


a = True
b = False
print("the or operation on", a, "and", b, "is")
a |=b
print(a)

a = True
b = True
print("the xor operation on", a, "by", b, "is")
a ^=b
print(a)


a = 100
b = 5 #100is divided by 2, 5 times
print("the right operation on", a, "by", b, "is")
a >>=b      #Signed right shift, Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(a)


a = 100
b = 5 #100 is multiplied by 2, 5 times
print("the left operation on", a, "by", b, "is")
a <<=b   #Zero fill left shift, Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(a)




