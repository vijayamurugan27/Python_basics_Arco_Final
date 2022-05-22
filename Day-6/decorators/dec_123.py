print("decorators", end = "\n\n\n")
def check(func):
    def inside(a, b):
        if a <b :
            c = b
            b = a
            a = c
            return a,b
                
        func(a,b)
    return inside

def div(a, b):
    print(a/b)

div = check(div)
div(4,6)