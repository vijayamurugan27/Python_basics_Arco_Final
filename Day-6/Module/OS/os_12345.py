# The OS module in Python provides functions for interacting with the
#  operating system. OS comes under Python’s standard utility modules.
#   This module provides a portable way of using operating 
#   system-dependent functionality. The *os* and *os.path* modules include many functions
#    to interact with the file system.


# Python program to explain os.getcwd() method
		
# importing os module
import os
	
# Get the current working
# directory (CWD)
cwd = os.getcwd()
	
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

# Python program to change the
# current working directory

#-------------------------------------------------------------

import os
print("moving to previous path")
# Function to Get the current
# working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()



