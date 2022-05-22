# ==    Equal                               x == y
# !=    Not equal                           x != y
# >     Greater than                        x > y
# <     Less than                           x < y
# >=    Greater than or equal to            x >= y
# <=    Less than or equal to               x <= y

def comp_123():
    print("Comparision operators")
    a = 5
    b = 6
    c = 5
    if(a==b):# False
        print("A and B are equal")
    elif(a!=c):#False
        print(" A and C are not Equal") 
    elif(a >= b):#False
        print("A is greater than B")
    elif(a <= b):#True
        print("A is less than B")
    else:
        print(" A and B are not equal")


comp_123()