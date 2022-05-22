# is  	Returns True if both variables are the same object 	x is y 	
# is not 	Returns True if both variables are not the same object 	x is not y

a = ["Blue", "Red"]
b = ["Blue", "Red"]
c = a

def identiy_12345():
    print("Identity Operators",end='\n\n')
    print(b is a)#no because both are not same objects, False
    print(c is a)#same objects , So true
    print(b == a, end='\n\n')#Both the values are equal
    print(b is not a)#
    print(c is not a)#same objects , So true
    print(b != a)#Both the values are equal
    


identiy_12345()