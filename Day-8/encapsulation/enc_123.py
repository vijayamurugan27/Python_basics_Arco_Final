# illustrating private members & private access modifier 
print("We are going to study on Encapsulation.", end = "\n\n\n")
class Rectangle:
  __length = 0 #private variable
  __breadth = 0#private variable
  def __init__(self): 
    #constructor
    self.__length = 5
    self.__breadth = 3
    #printing values of the private variable within the class
    print(self.__length)
    print(self.__breadth)

    # rect = Rectangle() #this line of code will create recursive function
    # print(rect.length, "Length")#these things are callable
    # print(rect.breadth, "Breath")


rect = Rectangle() #object created 
#printing values of the private variable outside the class 

print(rect.length)
print(rect.breadth)
