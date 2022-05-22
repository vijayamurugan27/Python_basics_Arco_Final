print("We are discussing on Object Oriented Programming ", end="\n\n\n")
print("Simple class",end="\n\n")
print("class name is Person, And their attributes are name, age, place, exp",end="\n\n")
class Person():
     def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
        
     def greet(self, *args, **kwargs):
         print("Hai hello welcome to ", self.name, "house", end="\n\n")
     def details(self,*args, **kwargs):
         print("My personal details are as follows :")
         print("Name :{}".format(self.name), "Age :{}".format(self.age), "Place :{}".format(self.place),end = "\n\n\n")

person_1 = Person("John", 20, "Pune")
person_2 = Person("Rahul", 30, "Delhi")
print("personal detils from __init__ function", end="\n\n")
print("Name :",person_1.name,"Age :",person_1.age, "Place :",person_1.place, end = "\n")
print("Name :",person_2.name,"Age :",person_2.age,"Place :",person_2.place, end = "\n\n")
print("Using the greet function", end="\n\n")
person_1.greet()
person_2.greet()
person_1.details()
person_2.details()
print("The parent class is Person, attributes are name, age, place", end = "\n\n")
print("The Child class is Students, attributes are name, age, place, edu_qual, college")

class Student(Person):
    def __init__(self, name, age, place, edu_qual, college):
        self.name = name
        self.age = age
        self.place = place
        self.edu_qual = edu_qual
        self.college = college
    def details(self, *args, **kwargs):
        print(self.name, self.age, self.place, self.edu_qual, self.college)

stu_1 = Student("Raju", 20, "Mumbai", "CSE", "DY.patil College")

stu_1.details()
stu_1.college = "IIT"
print("After changing the attributes of college or changing the obj properties.")
stu_1.details()
del stu_1.college
print("After deleting the attributes of college or deleting the obj properties.")
stu_1.college = "RIT"
stu_1.details()

print("To delete the object stu_1 , use the cmd - : del stu_1 ")
