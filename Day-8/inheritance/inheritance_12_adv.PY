print("We are discussing on Object Oriented Programming ", end="\n\n\n")
print("Simple class",end="\n\n")
print("class name is Person, And their attributes are name, age, place, exp",end="\n\n")
class Person():
     def __init__(self, name, age, place, exp):
        self.name = name
        self.age = age
        self.place = place
        self.exp = exp
     def greet(self, *args, **kwargs):
         print("Hai hello welcome to ", self.name, "house", end="\n\n")

person_1 = Person("John", 20, "Pune", 10)
person_2 = Person("Rahul", 30, "Delhi", 5)
print("personal detils from __init__ function", end="\n\n")
print("Name :",person_1.name,"Age :",person_1.age, "Place :",person_1.place,"Exp :",person_1.exp, end = "\n")
print("Name :",person_2.name,"Age :",person_2.age,"Place :",person_2.place,"Exp :",person_2.exp, end = "\n\n")
print("Using the greet function", end="\n\n")
person_1.greet()
person_2.greet()

print("inheritance, here we are having Parent class and a Child class", end = "\n\n\n")
print("parent class name is Person, and its attributes are name, age, place, exp",end="\n\n")
print("Child class name is Student, and its sttributes are name, age , course, salary",end="\n\n")

class Student(Person):
    def __init__(self, name, age, course, salary):
        self.name = name
        self.age = age
        self.course = course
        self.salary = salary

        Person.__init__(self, name, age,place="India", exp=0)
    
    def details(self, *args, **kwargs):
        print("Name :{}".format(self.name))
        print("Age :{}".format(self.age))
        print("course :{}".format(self.course))
        print("Experience :{}".format(self.salary), end = "\n\n\n")
        print("Native :{}".format(self.place))
        print("Experience :{}".format(self.exp), end="\n\n\n")
    
stu_1 = Student("Jaya Kumar", 30, "Networking", 50000)
stu_2 = Student("Kavin Kumar", 25, "Machine learning", 84000)
stu_3 = Student("Raja sekar", 20, "AWS", 12000)

print("Student details",end = "\n\n\n")
stu_1.details()
stu_2.details()
stu_3.details()
print(stu_1.name)
stu_1.greet()
print(person_1.name)


    
