print("function over loading in python", end = "\n\n\n")
print("overloading length operator", end = "\n\n")
class Order:
    def __init__(self, cart, customer):
         self.cart = list(cart)
         self.customer = customer

    def __len__(self):
         return len(self.cart)

order = Order(['banana', 'apple', 'mango'], 'Real Python')
print(len(order))


print("overloading abs operator", end = "\n\n")

class Vector:
     def __init__(self, x_comp, y_comp):
         self.x_comp = x_comp
         self.y_comp = y_comp

     def __abs__(self):
         return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5

vector = Vector(3, 4)
print(abs(vector))


print("overloading str operator", end = "\n\n")

class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __str__(self):
        return f'{self.x_comp}i{self.y_comp:+}j'

vector = Vector(3, 4)
print(str(vector))

