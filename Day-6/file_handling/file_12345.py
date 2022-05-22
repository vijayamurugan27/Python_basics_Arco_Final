# Working of open() function

# Before performing any operation on the file like read or write, first we have 
# to open that file. For this, we should use Python’s inbuilt function open()

# But at the time of opening, we have to specify the mode, which represents the purpose of the
#  opening file.

# f = open(filename, mode)

# Where the following mode is supported:

#     r: open an existing file for a read operation.
#     w: open an existing file for a write operation. If the file already contains 
#     some data then it will be overridden.
#     a:  open an existing file for append operation. It won’t override existing data.
#     r+:  To read and write data into the file. The previous data in the file will not be deleted.
#     w+: To write and read data. It will override existing data.
#     a+: To append and read data from the file. It won’t override existing data.

# mode 
# r = read, w = wirte, if written , over ridden, a = append, no over writing, 
# r+ =read/wirte, no over written, 
# w+ = read/write, over written,
# a+ = append/read data, no over ride existing data.

# a file named "geek", will be opened with the reading mode.


# import os
# fd = "hai.txt"
# file = open(fd, 'w')
# file.write("Hello hai welcome")
# file.close()
# file = open(fd, 'r')
# text = file.read()
# print(text)

print("", end="\n\n\n\n\n\n")
file = open("hai.txt", 'r')
for each in file:
	print (each)


# Working of read() mode

# There is more than one way to read a file in Python. If you need to extract a string 
# that contains all characters in the file then we can use file.read(). The full code 
# would work like this: 
# Python code to illustrate read() mode

file = open("hai.txt", "r")
print (file.read())
#another way
file = open("hai.txt", "r")
print (file.read(10))

# Creating a file using write() mode

# Let’s see how to create a file and how write mode works: 
# To manipulate the file, write the following in your Python environment: 
# Python code to create a file
file = open('Hai_2.txt','w')
file.write("This is the write command. ")
file.write("It allows us to write in a particular file.")
file.close()

# The close() command terminates all the resources in use and frees
#  the system of this particular program. 

# Working of append() mode
# Let’s see how the append mode works: 

# Python code to illustrate append() mode
file = open('HAi_2.txt','a')
file.write("This will add this line.")
file.close()

# Using write along with the with() function
# We can also use the write function along with the  with() function: 

# Python code to illustrate with() alongwith write()
with open("Hai_2.txt", "w") as f:
	f.write("Hello World!!!")

# split() using file handling

# We can also split lines using file handling in Python.
#  This splits the variable when space is encountered. You can
#   also split using any characters as we wish. Here is the code:

# Python code to illustrate split() function
# split() -> splits the word, hwen there is a space.
with open("HAi_2.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
