# def func_1(val, val2):
#     print("This is a simple function")
#     sqrt = val*val2
#     # print("SQuare root of",val, "is", sqrt )
#     return sqrt

# print(func_1(5,6))
# print(func_1(8,9))
# print(func_1(10,12))
# print(func_1(15,18))

# def func2():
#     pass

# func2()

# def func_2(*val):
#     print("This is a simple function")
#     val1 = val[1]
#     sqrt = val1*val1
#     # print("Square  of",val, "is", sqrt )
#     return sqrt

# print(func_2(5,6,7,8))

# def fun_3(val1, val2):
#     mul_1 = val1*val2
#     div_1 = val2/val1
#     print(mul_1)
#     print(div_1)

# fun_3(val2 = 6, val1 = 3)


# (a+b)/c

# def func_4(name = "ravi", age = 18):
#     print("welcome ", name, "and my age is", age)

# print(func_4("gayatri", 24))
# print(func_4())
# print(func_4(34))
# print(func_4('kavitha'))

# def menu_123(items):
#     # print("function ", items)
#     for i in items:
#         print("The items for dinner is",i)

# items = ['Poha', "Puri", "briyani", "Butter naan", "Tandoori Chicken"]
# # print(menu_123(items))

# def doc_str_12345():
#     '''Doc strings are very useful functions in 
    
#     passing a program, it is a sub set of comments. whereas 
#     we can print the doc strings like a program.'''
#     print("docstrings")
# doc_str_12345()

# help(doc_str_12345)
# print(doc_str_12345.__doc__)

#Nested func or func inside a func
def func_6():
    print("normal function")
    def func_7():
        print("Inside function.")
        def func_8():
            print("third function")
            def func_9():
                print("fourth function")
                def func_10():
                    print("fifth function")
                    def func_11():
                        print("sixth function")
                    func_11()
                func_10()
            func_9()
        func_8()
    func_7()
func_6()