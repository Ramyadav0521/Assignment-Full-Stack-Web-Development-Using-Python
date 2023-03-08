# 1. Write a python script to print number and its binary equivalent. 
a = 25
b = bin(a)
print("Binary is",b)

"""x = 35 
y =oct(x)
print("Octal is",y)

h = 24
s = hex(h)
print("Hexdecimal is",s)"""

# 2. Write a python script to store binary number 1100101 in a variable and print it in decimal format. 
b = 0b1100101
print("Binary to decimal number",b)

#3. Write a python script to store a hexadecimal number 2f in a variables and print it in octal format. 

h = 0x2F 
o = oct(h)
print("Hexadecimal to octal is",o)

# 4. Write a python script to store an  octal number 125 in a variable and print it in binary format.

o = 0o125
b = bin(o)
print("Octal to binary is ",b)

# 5. Write a python script to add two number 25(in octal) and 39 (in hexadecimal) and display the result in binary format. 
o =0o25
h = 0x39
print(o+h)
b =bin(o+h)
print("Add two number system",b)