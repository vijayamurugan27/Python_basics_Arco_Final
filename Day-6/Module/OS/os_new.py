import os

# Get the current working
# directory (CWD)
cwd = os.getcwd()
print("Current working directory:", cwd)

new_wd = os.chdir("../")

cwd = os.getcwd()
print("New working directory:", cwd)



new_wd = os.chdir("Day-6/")

cwd = os.getcwd()
print("New working directory:", cwd)

# Creating a Directory

# There are different methods available in the OS module for creating a directory.
#  These are –

#     os.mkdir()
#     os.makedirs()

# Using os.mkdir()

# os.mkdir() method in Python is used to create a directory named path with the 
# specified numeric mode. This method raises FileExistsError if the directory to be created 
# already exists.
# help(os)

# Python program to explain os.makedirs() method
	
# importing os module
import os
	
# Leaf directory
directory = "Netwoking"
	
# Parent Directories
parent_dir = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
	
# Path
path = os.path.join(parent_dir, directory)
	
# Create the directory
# 'Nikhil'
# os.makedirs(path)
print("Directory '% s' created" % directory)
	
# Directory 'GeeksForGeeks' and 'Authors' will
# be created too
# if it does not exists
	
	
	
# Leaf directory
directory = "Python"
	
# Parent Directories
parent_dir = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
	
# mode
mode = 0o666
# mode = 0o666, allows read and write file operations within the created directory.
path = os.path.join(parent_dir, directory)
	
# Create the directory 'c'
	
# os.makedirs(path, mode)
print("Directory '% s' created" % directory)
	
	
# 'GeeksForGeeks', 'a', and 'b'
# will also be created if
# it does not exists
	
# If any of the intermediate level
# directory is missing
# os.makedirs() method will
# create them
	
# os.makedirs() method can be
# used to create a directory tree


#--------------------------------------------------------------------------
# Another way of creating a directory


# main_dir = "C:/Users/splpt718/Desktop/Arco/Final/Day-6/Python_3"

# os.mkdir(main_dir, mode = 0o666)
# print("Directory is created",  main_dir)



#--------------------------------------------------------------------------------------

# Listing out Files and Directories with Python

# os.listdir() method in Python is used to get the list of all files and directories in the
#  specified directory. If we don’t specify any directory, then the list of files and 
#  directories in the current working directory will be returned.
# Python program to explain os.listdir() method
	
# importing os module

# Get the list of all files and directories
# in the root directory

import os
path = "/"
dir_list = os.listdir(path)
print("shows th edirs in root folder of windows")
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)


path = "C:/Users/splpt718/Desktop/Arco/Final"
dir_list = os.listdir(path)
print("shows th edirs in root folder of windows")
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)

#----------------------------------------------------------------------------

# Deleting Directory or Files using Python

# OS module proves different methods for removing directories and files in Python. These are – 

#     Using os.remove()
#     Using os.rmdir()

# Using os.remove()

# os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. 
# If the specified path is a directory then OSError will be raised by the method.

#--------------------------------------------------------------------------------------------

# Python program to explain os.remove() method
	
# importing os module
import os
	
# File name
file = 'file1.txt'
	
# File location
location = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
	
# Path
path = os.path.join(location, file)
	
# Remove the file
# 'file.txt'
# os.remove(path)
#---------------------------------------------------------------
# To remove a empty directory - direct

#To show the directories in the path before deleting
print("Dir's before deleting.")
path = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
dir_list = os.listdir(path)
print("shows the dirs in working folder of windows")
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)
#To show the dir's after deleting
print("dir's after deleting the directory direct.")
directory = "direct"
parent = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
path = os.path.join(parent, directory)
# os.rmdir(path)

path = "C:/Users/splpt718/Desktop/Arco/Final/Day-6"
dir_list = os.listdir(path)
print("shows th edirs in root folder of windows")
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)


# Commonly Used Functions

# 1. os.name: This function gives the name of the operating system
#  dependent module imported. The following names have currently been 
# registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’.

import os

print(os.name)

import os


try:
	# If the file does not exist,
	# then it would throw an IOError
	filename = 'hai.txt'
	f = open(filename, 'rU')
	text = f.read()
	f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:

	# print(os.error) will <class 'OSError'>
	print('Problem reading: ' + filename)
	
# In any case, the code then continues with
# the line after the try/except

# os.popen(): This method opens a pipe to or from command. The return value can be read or
#  written depending on whether the mode is ‘r’ or ‘w’. 

# Syntax: 

#  os.popen(command[, mode[, bufsize]])

# Parameters mode & bufsize are not necessary parameters, if not provided,
#  default ‘r’ is taken for mode. 

import os
fd = "hai.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly

# file = os.popen(fd, 'w')
# file.write("Hello")

# File not closed, shown in next function.

# os.close(): Close file descriptor fd. A file opened using open(), 
# can be closed by close()only. But file opened through os.popen(), 
# can be closed with close() or os.close(). If we try closing a file opened with open(), 
# using os.close(), Python would throw TypeError. 

# open() -> close()
# os.popen() -> close() or os.close() 
# open()-> os.close (shows error)

file = open("hai.txt", "r")
text = file.read()
print(text)
# os.close()#will raise an error
file.close()#will not raise an error

# os.rename(): A file old.txt can be renamed to new.txt, using the function os.rename().
#  The name of the file changes only if, the file exists and the user has sufficient privilege 
#  permission to change the file.


# Changing the file name

# import os
# fd = "hai.txt"
# os.rename(fd,'New.txt')
# os.rename(fd,'New.txt')


# os.remove(): Using the Os module we can remove a file in our system
#  using the remove() method. To remove a file we need to pass the name
#   of the file as a parameter. 


# removing a file


# import os #importing os module.
# os.remove("hai_1.txt") #removing the file.


# If you try to remove a file that does not exist you will get FileNotFoudError. 


# os.path.exists(): This method will check whether a file exists or 
# not by passing the name of the file as a parameter. OS module has a 
# sub-module named PATH by using which we can perform many more 
# functions. 

import os
result = os.path.exists("hai.txt") #giving the name of the file as a parameter.
print(result)

# os.path.getsize(): In this method, python will give us the size of
#  the file in bytes. To use this method we need to pass the name of 
#  the file as a parameter.

size = os.path.getsize("hai.txt")
print("Size of the file is", size," bytes.")
