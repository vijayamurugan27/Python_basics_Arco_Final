# and  	Returns True if both statements are true 	x < 5 and  x < 10 	
# or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
# not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)


def logical12345():
    print("LogicaL operators")
    x = 5
    print(x)   
    print(x," is less than 3 and greater than 10")
    print(x > 3 and x < 10)
    print(x," is less than 3 and greater than 4")
    print(x > 3 or x < 4)
    print("Inverse value of", x," is less than 3 and greater than 4")
    print(not(x > 3 and x < 10))

logical12345()