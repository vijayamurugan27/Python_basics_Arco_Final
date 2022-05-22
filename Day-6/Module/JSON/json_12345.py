import json
#to write a json to afile in two ways.
var = {
	"Marks": 
    [
        { "Name" :"Ragavan" ,"Maths":85, "Physics":90 , "Social science": 95},        
        { "Name" :"Mythili" ,"Maths":85, "Physics":90 , "Social science": 95},        
        { "Name" :"Sangavi" ,"Maths":85, "Physics":90 , "Social science": 95},        
    ]
	}
#     First method writing in a file
# with open("Sample.json", "w") as p:
#     json.dump(var, p)

#second method displays the data in terminal
# json_obj = json.dumps(var, indent = 4)
# print(json_obj)

#Reading the json file

# with open("Sample.json", "r") as read_it:
# 	data = json.load(read_it)
# print(data)

# Read method 2

# file1 = open('Sample.json')
# data1 = json.load(file1)
# for i in data1['Marks']:
#     print(i)
# file1.close()