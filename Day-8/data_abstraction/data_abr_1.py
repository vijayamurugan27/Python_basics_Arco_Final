# Unlike the other high-level language, Python doesn't provide the abstract class itself.
#  We need to import the abc module, which provides the base for defining Abstract Base classes (ABC). 
#  The ABC works by decorating methods of the base class as abstract. It registers concrete
#   classes as the implementation of the abstract base. We use the @abstractmethod decorator to define
#    an abstract method or if we don't provide the definition to the method, it automatically becomes
#     the abstract method. Let's understand the following example.

print("we are going to discuss abstract method in Python.", end="\n\n")
from abc import abstractmethod, ABC
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Mahindra(Car):   
    def mileage(self):   
        print("The mileage of mahindra is 30kmph")   
    def maintenance(self):
        print("The Maintenance is frugal.")
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage of suzuki is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage of duster is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage of renault is 27kmph ")   
          
# Driver code   
t= Mahindra()   
t.mileage()  
t.maintenance() 
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  