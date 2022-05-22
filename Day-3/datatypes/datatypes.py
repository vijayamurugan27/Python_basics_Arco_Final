def Numeric_1234():
    ''''This is for checking numeric datatypes.
    
    Numeric - (int, complex, float)'''
    a = 1
    print(type(a))
    a = 2.3
    print(type(a))

    a = 2+3j
    print(type(a))
    # we cannot use (i, k) as we use in Engineering, we can only use j to indicate j 
    #for representing a Complex number.
    a = 2+3j
    print(type(a))

# Numeric_1234()
# print(Numeric_1234.__doc__)
# print("using Help statement.")
# help(Numeric_1234)


def Bool12345():
    ''''This one is use to check
    
     for a boolean data type.'''
    print(type(True))
    print(type(False))

# help(Bool12345)
# Bool12345()

def Dictionary12345():
    '''This is used to describe 
    
    about the dictionary data type.'''
    #Creating an Empty dictionary
    Dict = {}
    print("Craeting an empty dictionary")
    print(Dict)
    #Creating a dictionary with integer keys.
    Dict = {1:"welcome", 2:"to the", 3:"world", 4:"of python"}
    print("dictionary created using integer keys.")
    print(Dict)
    Dict = {"name":"Rahul", 1:[45,32,86,95,83]}
    print("Dictionary created using mixed keys.")
    print(Dict)

    #Dictyionary created using keyword dict()
    Dict = dict({1:"welcome", 2:"john", 3:"woo"})
    print("Dictioanry created using the keyword dict()")
    print(Dict)
    #dictioanry as a pair using the keyword dict
    Dict  = dict([(1, 'Google'), (2, 'yahoo')])
    print("Dictioanry created using as a pair")
    print(Dict)

    Dict = {1:"hai", 4:"hello", 3:"raju", "kamal":"raj"}
    print(dict)
    print("Accessing the Dictioanry elements.")
    print(Dict[1]) #array value indicates the position value.
    print(Dict[4])
    print(Dict.get(4)) #references by the key value.
    print(Dict.get("kamal"))


# Dictionary12345()

# def set123456():
    # print("Blank set")
    # set1 = set()
    # print(set1)
    # print("set created using Strings")
    # set2 = set("Hai hello world")
    # print(set2)
    # print("Set created using mixed a list")
    # set3 = set(['hai', 'hello', 'world'])
    # print(set3)
    # print("Set created using mixed data types")
    # set4 = set(['hai', 'hello', 'world',1 , 2, 7, 8, 5])
    # print(set4)
    #accessing the Elements in the set using loops
    set4 = set(['hai', 'hello', 'world',1 , 2, 7, 8, 5])
    print("Elements of the set are")
    print(set4)
    for i in set4:
        print(i, end = "\n")
    # To check the an element is present in the set
    print("hai" in set4)
    print("raju" in set4)

# set123456()

# def sequence123456str():
    # print("string data Type")
    # a = "hai hello world"
    # print(a)
    # a = 'hai hello world'
    # print(a)
    # a = """hai hello world"""
    # print(a)
    # a = """hai hello world
    # this is going to be fun"""
    # print(a)
    a1 = "hai hello world"
    # print(a1)
    # print(a1[0])
    # print(a1[-15])
    # print(a1[14])
    # print(a1[-1])
    # print("String splicing")
    
    # print(len(a1))
    
    # print(a1[0:15])
    # print(a1[3:])
    # print(a1[4:])
    # print(a1[10:])
    # print(a1[2:8])
    # print(a1[:9])
    # print(a1[:3])
    b1 = a1
    print(b1)
    b2 = b1[0:3]
    print(b2)
    b3 = b1[4:9]
    print(b3)
    b4 = b1[10:15]
    print(b4)
    b5 = b2+b3+b4
    print(b5)

    b2 = b1[0:4]
    print(b2)
    b3 = b1[4:10]
    print(b3)
    b4 = b1[10:15]
    print(b4)
    b5 = b2+b3+b4
    print(b5)
    
    
    # print('hai' in a1)
    # print('raju' in a1)

    # print("Accessing elements using For loops")
    # for i in a1:
    #     print(i)
    
    ##Simple for loops to check an element in the string
    # if "hai" in a1:
    #     print("hai is present in the string")
    # else:
    #     print("Hai is not present in the a1")
    # if "rsju" in a1:
    #     print("hai is present in the string")
    # else:
    #     print("Raju is not present in the a1 ")
    # #nested for loops
    # print("nested For loops")
    # if "hai" in a1:
    #     print("Hai is present")
    #     if "raju" in a1:
    #         print("raju is present")
    #     else:
    #         print("Raju is not present")
    # else:
    #     print("Hai is not present")
    
    # #if-elis-else loops
    # print("if-elif-else statements")
    # print(a1)
    # if "hai" in a1:
    #     print("Hai is present in the string")
    # elif "raju" in a1:
    #     print("raju is present in the string")
    # elif "hello" in a1:
    #     print("hello is present in the string")
    # else:
    #     print("The requested string is not available.")

# sequence123456str()

# def sequence12345list():
    print("lists")
    a1 = [] # blank list
    print(a1)
    a1 = ["Hai hello world"] # list created using string
    print(a1)
    a1 = ["hai","hello", 'world']
    print(a1)
    print(a1[0], a1[1], a1[2])
    print(a1[0], a1[1], a1[2], sep="")
    print(a1[0], a1[1], a1[2], sep="--")
    a1 = [["hai", "hello", "world"], [1,2,3,4,5,6]]
    print(a1)
    print(a1[0])
    print("accessing for loop")
    for i in range(len(a1)) : 
        for j in range(len(a1[i])) : 
            print(a1[i][j], end=" ")
    print() 
    print("new elements are i am stuting Python")
    #append(): Adds an element at the end of the list.
    a1.append(['i', 'am', 'studying', 'Python'])
    print(a1)
    print("new elements are i am stuting Python")
    #extend(): Add the elements of a list (or any iterable), to the end of the current list.
    a1.extend(['i', 'am', 'studying', 'Python', "hello"])
    print(a1)
    #reverse(): Reverses the order of the list.
    a1.reverse()
    print("reverse")
    # a1[2].reverse()
    # print(a1)
    print(a1)
    print(a1[1])
# sequence12345list()

def sequence12345tuple():
    a1 = ()
    print(a1)
    #tuple with strings
    a1 = ("hai", "world")
    print(a1)
    # tuple using a list and built-infunction tuple()
    a1 = [1,2,3,4,54]
    a2 = tuple(a1)
    print(a2)
    #nested tuples
    a1 = (1,2,3,4,5)
    a2 = (6,7,8,9,0)
    a3 = (a1,a2)
    print(a1)
    print(a2)
    print("nested tuple")
    print(a3)
    a5 = tuple([1,2,3,4,5])
    print(a5[1])
    print(a5[4])
    print(a5[-1])
    print(a5[-5])
    print("for loop")
    for i in  range(1,4):
        print(i)




sequence12345tuple()
     
