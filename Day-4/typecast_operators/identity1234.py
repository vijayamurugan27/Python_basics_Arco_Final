# is  	Returns True if both variables are the same object 	x is y 	
# is not 	Returns True if both variables are not the same object 	x is not y


a = ["hari", "haran"]
b = ["hari", "haran"]
c = a

print(a is c)#True
print(a is b)#False
print(" identity Operator (is) verified", end="\n\n\n")

print(a is not c)#False
print(a is not b)#True
print(" identity Operator (is not) also verified", end="\n\n\n")
