from curses import has_ic


a = 5 #the value of a is assigned as 5

print('a') #i am going to print the string a
print(a) #the value of a is displayed using print stmt

b = 5.0 #the value of a is assigned to b
print(b) #prints the value of b
print('the value of b is', b) #prints both the strings and the value of b

print("the datatype of a is")
print(type(a))
print("the datatype of b is")
print(type(b))


c = "i am raju"
print("the datatype of c is")
print(type(c))

d = "5"
print(d)
print("the datatype of d is")
print(type(d))

print(id(a))
# e = id(a)
# print(e) 
# print("this will give the memory location of variables a,b,c,d")
# print(id(a)) # it will give the memory location of a 
# print(id(b)) # it will give the memory locbtion of b 
# print(id(c)) # it will give the memory locction of c 
# print(id(d)) # it will give the memory locdtion of d 

# Definition and Usage

# The id() function returns a unique id for the specified object.

# All objects in Python has its own unique id.

# The id is assigned to the object when it is created.

# The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)

# Syntax
# id(object)


a = 5

print(a)
print('a')
print(id(a))