#Python program to add two numbers using function


def add_num(a,b):#function for addition
    """ here we are going to add two numbers using python"""

    sum=a+b;
    return sum; #return value

num1=25  #variable declaration
num2=55
print("The sum is",add_num(num1,num2))#call the function
print(add_num.__doc__)