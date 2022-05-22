print("Decorators", end = "\n\n\n")
def check(func):
    def inside(a, b):
        if b==0:
            print("cannot be divided by zero")
            return 
        func(a, b)       
    return inside

def check1(func):
    def inside(a, b):
        if a<b:
            a,b =b,a
            # return func(a,b)
            func(a, b)
    return inside

@check
@check1 
def div(a, b):
    print(a/b)

# div = check(div) #---------------inside we can also use @check before the function.
div(3,0)