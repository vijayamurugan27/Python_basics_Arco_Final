def while_12345():
#     print("A simple while loop.")
#     i = 0 
#     while i <= 6:
#     # print(i)
#         print(i)
#         i += 2

#     print("A simple while loop, with break stmt.")
#     i = 0 
#     while i <= 6:
#         if (i ==3):#true
#             break     
#         print(i)
#         i += 1

    print("A simple while loop, with continue stmt.")
    i = 0 
    while i <= 6:
        i +=1        
        if i ==3:#true
            continue     
        print(i)
    else:
        print("The loop has ended.")
    # print("A simple while loop using the continue statement. it will block the value 3")
    # i = 0
    # while i < 6:
    #     i += 1
    #     if i == 3:
    #         continue
    #     print(i)
    # else:
    #     print("the loop ended")

        
    

while_12345()