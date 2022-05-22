# text = "welcome to python training in Networking."

# #upper case - var.upper()
# print("Normal text : ",text)
# print("var.upper : ", text.upper())

# #lower case -var.lower()
# print("var.lower : ", text.lower())

# #capitals case -var.capitalize()
# print("var.capitalize : ",text.capitalize())

# #title case -var.title()
# print("var.title : ",text.title())

# # casefold case- var.casefold()
# print("var.casefold : ", text.casefold())

# #center  - var.center
# print("var.center : ", text.center(100))


# text1 = "python python hai hello worldpython python"
# #count count("var")
# print("The number of words in the string :", text1.count("python"))

# #Expandable tabs
# text2 = "I\tlove\tprogramming."
# print("Un modified string.",text2)

# print("Modified string : ", text2.expandtabs())
# #default value is 8
# print("Modified string : ", text2.expandtabs(5))

# #endswith - var.endswith("string value")
# print(text)
# print(text.endswith("Networking."))#true
# print(text.endswith("networking."))#false
# print(text.endswith("training."))#false
# print(text.endswith(" in Networking"))#false
# print(text.endswith(" in Networking."))#true
# print(text.endswith(" in Networking.."))#false
# print(text.endswith(" in Networking. "))#false
# print(text.endswith(" in Networking,"))#false

#find var.find("string") - it is giving us the position values.

# print(text)
# print("find", text.find("to"))
# print("find", text.find("p"))
# print(text1)
# print("find", text.find("D"))# if the sting is not there it will return (-1)
# print(text.find("r"))

# #string Formatting
# print("{} welocme to python training".format("hai guys"))
# text = " {} welocme to python training."
# print(text.format("hai hello"))

# text = " {} welocme to python training.{}{}"
# print(text.format("hai hello,", "It's time for lunch.", " Take a break"))
# text = " {2} welocme to python training.{0}{1}"
# print(text.format(" hai hello", " It's time for lunch", " Take a break"))

# text = " {0} welocme to python training.{eq}{1}"
# print(text.format(" hai hello", " It's time for lunch.", eq = " Take a break."))


# # for checking alphabets - var.isalpha()
# text = "rajeshwari"
# text1 = "vinu varshith"
# text2 = "kalai1234"
# print("isalpha", text.isalpha(), text1.isalpha(), text2.isalpha())

# #for checking digit -var.isdigit
# text = "45.9"
# text1 = "50"
# text2 = "0"

# print("isdigit ",text.isdigit())
# print("isdigit ",text1.isdigit())
# print("isdigit ",text2.isdigit())

# for checking decimal - var.isdecimal
# text = "45.9"
# text1 = "50"
# text2 = "0"

# print("isdecimal ",text.isdecimal())
# print("isdecimal ",text1.isdecimal())
# print("isdecimal ",text2.isdecimal())


# # for checking lowercase - var.islower()
# text = "what are you doing?"
# text1 = "i am training the Students"
# text2 = "Are they listenning?"
# text3 = "are 123 numbers"
# text4 = str(12345)
# text5 = "12345a"
# text6 = "     "
# text7 = "#$%$#^#$uyiuyA"
# text8 = "%^$^$"
# print("islower", text.islower(), text1.islower(), text2.islower(),text3.islower(),text4.islower())
# print(text5.islower(), text6.islower(),text7.islower(),text8.islower())

# #isnumeric - var.isnumeric()
# text = "what are you doing?"
# text1 = "i am training the Students"
# text2 = "Are they listenning?"
# text3 = "are 123 numbers"
# text4 = str(12345)
# text5 = "12345"
# text6 = "5468997%98759"
# text7 = "87598.8569"
# text8 = "2+3j"
# te = "89"
# text9 = te

# print("isnumeric", text.isnumeric(), text1.isnumeric(), text2.isnumeric(),text3.isnumeric(),text4.isnumeric())
# print(text5.isnumeric(), text6.isnumeric(),text7.isnumeric(),text8.isnumeric(), text9.isnumeric())


# #isprintable() - var.isprintable()
# text = "  "
# text1 = "%$#%$^"
# print("isprintable", text.isprintable(), text1.isprintable())


# #isupper - var.isupper()
# text  = "HAS THERE BEEN ANY DELAY"
# text1 = "has there been any Delay"
# text2 = "Has There Been Any Delay"

# print("var.isupper : ", text.isupper(), text1.isupper(), text2.isupper())


# #islower - var.islower()
# text  = "HAS THERE BEEN ANY DELAY"
# text1 = "has there been any delay"
# text2 = "Has There Been Any Delay"
# text3 = "67348a"

# print("var.islower : ", text.islower(), text1.islower(), text2.islower(), text3.islower())

# replace = var.replace("str1", "replce")

text  = "HAS THERE BEEN ANY DELAY has"

print("var.replace('str', 'replace')", text.replace('HAS',"has"))
print("var.replace('str', 'replace')", text.replace('HaS',"has"))
print("var.replace('str', 'replace')", text.replace('has',"have"))

text  = "HAS has    has     has has has"
print("var.replace('str', 'replace')", text.replace('HAS',"has"))
print("var.replace('str', 'replace')", text.replace('has',"have",2))

