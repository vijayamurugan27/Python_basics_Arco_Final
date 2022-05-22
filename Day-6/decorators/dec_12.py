print("Decorators",end = "\n\n\n")

#--------------------------------------stage-1

# def f1():
#     print("hai hello world")
# f1()
# print(f1)
#----------------------------------------------stage -2

# def f1():
#     print("hai hello world")

# def f2(f):
#     f()

# f2(f1)

#--------------------------------------------- stage -3

# print("A simple decorator.")
def f1(func): #for function f1 i am passing a func to it. then return another(wrapper) function
    def wrapper(): #now the wrapper function has print, func()&&print inside of it.
        print("Started")
        func()
        print("Ended")
    return wrapper

# @f1
def f():
    print("hello world")

# f()

# f1(f)
# print(f1(f))
# f1(f)()
print('        ', end="\n")
# f1(f) - this is a function
# f1(f)() - to execute because f1(f) is a function.

#------------------------------------------

# f = f1(f)
# f()

#--------------------------------

# x = f1(f)
# x()
# same as the previous code , gives same functionality and o/p

#------------------------------------------------------------------
# print("Decorators when passing arguments & keyword arguments")
# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("started")
#         func(*args, **kwargs)
#         print("Ended")
#     return wrapper

# @f1
# def f(a):
#     print(a)

# f("hai")
#----------------------------------------------------------
# print("Decorators when passing arguments & keyword arguments")
# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("started")
#         func(*args, **kwargs)
#         print("Ended")
#     return wrapper

# @f1
# def f(a, b =9):
#     print(a, b)

# f("hai")
#--------------------------------------------------------------------

print("Decrators when passing arguments & keyword arguments")
def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper

@f1
def f(a, b =9):
    print(a, b)

f("hai")

@f1
def add(x,y):
    print("The sum of values of ", x+y)

add(6,9)

#--------------------------------------------------------------------------
## timer using decorators
print("Timer function using decorators", end = "\n\n\n")
import time
print(time.time())

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("The time taken  = ",time.time() - before, "seconds")
    return wrapper

@timer
def run():
    time.sleep(5)

run()