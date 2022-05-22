# Python program to show use of
# + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Geeks"+"For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks"*4)

#-------------------------------------------------------------------------------------------------------

# Python Program illustrate how
# to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(b, c):
		return b.a + c.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

#==================================================================================================

# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.
print("pgm - 3", end="\n\n\n")
class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# adding two objects
	def __add__(self, other):
		return self.a + other.a, self.b + other.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


#------------------------------------------------------------------------------------------

print("pgm - 4", end="\n\n\n")

# Python program to overload
# a comparison operators

class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if(self.a>other.a):
			return True
		else:
			return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
	print("ob1 is greater than ob2")
else:
	print("ob2 is greater than ob1")

    #-----------------------------------------------------------------------


print("pgm - 5", end="\n\n\n")

# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)

ob3 = A(4)
ob4 = A(2)
print(ob1 > ob2)




# Operator	Magic Method

# +	__add__(self, other)
# –	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)
# >>	__rshift__(self, other)
# <<	__lshift__(self, other)
# &	__and__(self, other)
# |	__or__(self, other)
# ^	__xor__(self, other)




# Comparison Operators :

# Operator	Magic Method
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)



# Assignment Operators :

# Operator	Magic Method
# -=	__isub__(self, other)
# +=	__iadd__(self, other)
# *=	__imul__(self, other)
# /=	__idiv__(self, other)
# //=	__ifloordiv__(self, other)
# %=	__imod__(self, other)
# **=	__ipow__(self, other)
# >>=	__irshift__(self, other)
# <<=	__ilshift__(self, other)
# &=	__iand__(self, other)
# |=	__ior__(self, other)
# ^=	__ixor__(self, other)


# Unary Operators :
# Operator	Magic Method
# –	__neg__(self)
# +	__pos__(self)
# ~	__invert__(self)


# Python program which attempts to
# overload ~ operator as binary operator

class A:
	def __init__(self, a):
		self.a = a

	# Overloading ~ operator, but with two operands
	def __invert__(self, other):
		return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)
ob2 = A(3)

print(~ob2)
