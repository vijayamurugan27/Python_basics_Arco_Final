
# Working With JSON Data in Python

#     Difficulty Level : Easy
#     Last Updated : 18 Nov, 2021

# Introduction of JSON in Python : 

# The full form of JSON is JavaScript Object Notation.
#  It means that a script (executable) file which is made of text in
#   a programming language, is used to store and transfer the data.
#    Python supports JSON through a built-in package called JSON. 
#    To use this feature, we import the JSON package in Python script.
#     The text in JSON is done through quoted-string which contains the value in key-value
#      mapping within { }. It is similar to the dictionary in Python. JSON shows an API similar
#       to users of Standard Library marshal and pickle modules and Python natively supports 
#       JSON features. For 


# Python program showing
# use of json package

import json

# {key:value mapping}
a ={
    "name":"John",
    "age":31,
	"Salary":25000,
    "educationalQualification": "ECE",
    "job Role":"networking Engineer",
    }

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)

# As you can see, JSON supports primitive types,
#  like strings and numbers, as well as nested lists, tuples, and objects  

# Python program showing that
# json support different primitive
# types

import json

# list conversion to Array
print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "GeeksforGeeks")))

# string conversion to String
print(json.dumps("Hi"))

# int conversion to Number
print(json.dumps(123))

# float conversion to Number
print(json.dumps(23.572))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))

# Serializing JSON : 

# The process of encoding JSON is usually called serialization. This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. To handle the data flow in a file, the JSON library in Python uses dump() function to convert the Python objects into their respective JSON object, 
# so it makes easy to write data to files. See the following table given below.  

# Python object	    JSON object
# dict        	    object
# list, tuple	        array
# str	                string
# int, long, float	numbers
# True	            true
# False	            false
# None	            null

var = {
	"Subjects":[
{"Name":"kavin", "English":90, "Maths"  :85, "Physics":90, "science":70, },				
{"Name":"Gaytri", "English":90, "Maths"  :85, "Physics":90, "science":70, },
{"Name":"Rajeshwari", "English":90, "Maths"  :85, "Physics":90, "science":70, },
]
	}

# with open("Sample.json", "w") as p:
# 	json.dump(var, p)

# Using Python’s context manager, create a file named Sample.json and open it with write mode. 
# Here, the dump() takes two arguments first, the data object to be serialized,
#  and second the object to which it will be written(Byte format). 


# Deserializing JSON : 

# Deserialization is the opposite of Serialization, i.e. conversion of JSON objects into their
# respective Python objects. The load() method is used for it. If you have used JSON data from 
# another program or obtained it as a string format of JSON, then it can easily be deserialized 
# with load(), which is usually used to load from string, otherwise, the root object is in a 
# list or dict. 

with open("Sample.json", "r") as read_it:
	data = json.load(read_it)


json_var ="""
{
	"Country": {
		"name": "INDIA",
		"Languages_spoken": [
			{
				"names": ["Hindi", "English", "Bengali", "Telugu"]
			}
		]
	}
}
"""
var = json.loads(json_var)


# Read, Write and Parse JSON using Python
# Python program to convert JSON to Python


import json

# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)

print(employee_dict['name'])

# Python read JSON file
import json
file = json.load("Sample.json")

data = json.load(file)

for i in data['Subjects']:
    print(i)

file.close()
