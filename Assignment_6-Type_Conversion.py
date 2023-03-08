# 1. Write a python script to covert a number into str type. 
n = 99
n1 = str(n)
print(n1)
print(type(n1))
# 2. Write a python script to print Unicode of the character 'm'
m = 'm'
print("Unicode of the character 'm'is:---->",ord(m)) 

# 3. Write a python script to print character representaion of a given nuicide 100. 
n = 100
print(chr(n))

# 4.Write a python script to convert a str type data into an type. Also describe when a str type values is not possible to convert into an int type. 

s = "1233"
s = int(s)
print(type(s),s)

"""
s = "strbgjf"
s = int(s)
print(s) # Error

s = "25.5"
s1 = int(s)
print(s1) # Error
""" 

# 5. How to convert an integer values into a bool values?
# Rule
# Every non zero number ----> True
# zero ---> Flase
a  = 1
a1 = bool(a)
print(a1)
