# and  	Returns True if both statements are true 	x < 5 and  x < 10 	
# or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
# not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)


def logical_123():
    print("logical Operation")
    a = 10
    if(a == 15 or a != 6):# True
        print("we have verified the OR logic")
        if(a == 10 and a != 6):#TRUE
            print(" we have verified AND Operator")
            if(not a == 6):#TRUE
                print(" we have verified NOT operator")


logical_123()
