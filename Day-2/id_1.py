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