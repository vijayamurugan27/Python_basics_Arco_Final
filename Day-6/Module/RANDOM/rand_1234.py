
import random

random.seed(10)
print(random.random()) 

print(random.getstate()) 
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random()) 

print(random.getrandbits(8)) 

print(random.randrange(3, 100)) 
print(random.randrange(3, 100, 5)) 

print(random.randint(3, 9)) 


mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) 
x = "WELCOME"
print(random.choice(x)) 


mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
# print(random.shuffle(mylist)) this method won't work
print(mylist) 

print(random.sample(mylist, k=2)) 

print(random.random())

print(random.uniform(20, 60)) 

print(random.triangular(20, 60, 30)) 