# f = open(filename, mode)


# mode 
# r = read, w = wirte, if written , over ridden, a = append, no over writing, 
# r+ =read/wirte, no over written, 
# w+ = read/write, over written,
# a+ = append/read data, no over ride existing data.


# 1) create a file called hai.txt

# for w,r,a - operations
import os

# from setuptools import Command
fd = "hai.txt"
file = open(fd, 'w')
file.write("Hello hai welcome ")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
# now to read from the file
print("", end="\n\n\n\n\n\n")
file = open("hai.txt", 'r')
for each in file:
	print (each)

# Using the write command and create a file
file = open('hai_qw.txt','w')
file.write("This is the write command. ")
file.write("It allows us to write in a particular file.")
file.close()


# for w+, r+ ,a+

import os
fd = "hai.txt"
file = open(fd, 'w')
file.write("Hello hai welcome ")
# file.close()
file = open(fd, 'r')
text = file.read()
print(text)
# Now to read from the file
print("", end="\n\n\n\n\n\n")
file = open("hai.txt", 'r')
for each in file:
	print (each)

#------------------------------------------------------------------------

file = open("hai.txt", "r")
print (file.read())

file = open("hai.txt", "r")
print (file.read(10))
#----------------------------------------------------------------------

# Using the write command and create a file
file = open('hai_qw.txt','w')
file.write("This is the write command. ")
file.write("It allows us to write in a particular file.")
file.close()
#---------------------------------------------------------------

# Using the append Command
file = open('hai.txt','a')
file.write("This will add this line.")
file.close()
#------------------------------------------------------------------
file = open('hai.txt','a')
file.write("This will add this line.")
file.close()
#-------------------------------------------------------------------
# To create and write in a file.

with open("hai_1.txt", "w") as f:
	f.write("Hello World!!!")

#-------------------------------
# Using split() in file operation, split() -> to split the words in the file.
with open("hai.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)





