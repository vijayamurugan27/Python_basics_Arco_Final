#With the while loop we can execute a 
# set of statements as long as a condition is true.
print("A simple while loop")
i = 1
while i < 6:
  print(i)
  i += 1

# With the break statement we can stop 
# the loop even if the while condition is true
#while loop uisng break statement 
print('', end="\n\n\n\n")
print("while loop using break statement, breaks after 3", end="\n\n")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

# With the continue statement 
# we can stop the current iteration, and continue with the next:
print('', end="\n\n\n\n")
print("A simple while loop using the continue statement. it will block the value 3")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# With the else statement 
# we can run a block of code once when the condition no longer is true:
print('', end="\n\n\n\n")
print("while loop using else stmt, gives the else stmt when the condition fails.")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))
print("A simple while loop to find the sum of n numbers", end="\n\n\n")
n = 10
print("Enter a integer to find the sum of n numbers.")
num =input()
print("The numberis ", num)
print(type(num))
num1 = int(num)
print(type(num1))
n = num1
# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)