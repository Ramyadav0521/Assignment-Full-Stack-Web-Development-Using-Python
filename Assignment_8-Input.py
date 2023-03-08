                           # Assignment-8 : input from keyboard
# 1. Write a python script to take your name as input from the user and then print it. 
name = input("Enter your name")
print("My name is",name)

# 2. Write a python script take input two numbers form the user, then calculate their sum and display the result. 
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = a+b
print("Sum two is",c)

 # 3. Write a python script which takes the radius from the user and display are of the circle
r =float(input("Enter radius value"))
area = float(3.14*r*r)

print("Area of circle is",area)

# 4. Write a python script to calculate square of a number. Number is entered by the user
s = int(input("Enter a number"))
s1 = s*s
print("Square of",s,"is",s1)
 
# 5. Write a python script which takes a character from user and display its unicode. 
c = input("Enter only one single character")
u = ord(c)
print("unicode of",c,"is",u)
