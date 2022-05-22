def simplefunc():
    print("it is a simple function")

simplefunc()

print("Function with passing arguments")

def simplefunc1(name):
    print("hai "+name)
simplefunc1("raju")
simplefunc1("abhijith")
simplefunc1("manikanda")
simplefunc1("stuart")

# Arguments are often shortened to args in Python documentations.

def add12(num1, num2):
    sum = num1+num2
    print("the sum of tho numbers are:", sum)
add12(3,4)

def square12(*num):
    a = num[0]
    val = a*a
    print("the square of the value is", val)
square12(4,5,6,7)

def square12(*num):
    for i in num:
        val = i*i
        print("the square of the value is", val)
square12(4,5,6,7)

#Keyword Arguments
# You can also send arguments with the key = value syntax.
def func3(num1, num2, num3):
    print("The square value in the given number is", num2)

func3(num1 = 23, num2 = 25, num3 = 34)


def func4(**num):
    print('keyword arguments')
    print("the square value is", num["num2"])

func4(num1 = 45, num2 = 36,num3 = 39, num4 = 89)

def func5(age = 18):
    print("My age is :", age)
func5(10)
func5()
func5(25)
func5(90)

#passing list as an argument

def func6(food):
    print("hai", food)
    for i in food:
        print("menu =", i)

menu = ['dosa', 'idli', 'poha',"naan", "butter chicken", "roti"]
func6(menu)

def func7(num):
    return num*num
print(func7(90))
print(func7(32))
print(func7(64))
print(func7(81))
a = func7(30)
print(a)

print("using pass statement")
def func8(num):
    pass
    
print(func8(90))
print(func8(32))
print(func8(64))
print(func8(81))
a = func8(30)
print(a)


def func9():
    """"
    It is a simple function
    jkhgksjhgkskgjhkjshgksjghjkg.    
    """
print(func9.__doc__)
print("using help")
help(func9)

def func10():
    a = "hai hello world"
    # func11()
    def func11():
        print(a)
    func11()
func10()