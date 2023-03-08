          # Assignment-9: Simple calculations on user data

# 1. Write a python script to calculate simple interest. formula:- p*r*t/100
p =int(input("Enter a principal value"))
r =float(input("Enter a rate value"))
t =int(input("Enter a time values"))

s_i=(p*r*t)/100
print(p,r,t,"sum of simple interest is",s_i)

# 2. Write a python script to calculate area of a rectangle fomula area = (w · h)
w =int(input("Enter width number"))
h =int(input("Enter height number"))
area=w*h
print("Area of a rectangle is",area)

# 3. Write a python script to calculate average of three number entered by user. formula:-a1+a2+a3...n/n
num1=int(input("Enter a first number"))
num2=int(input("Enter a second number"))
num3=int(input("Enter a third number"))

average_1= (num1+num2+num3)/3
print("Average of three numbers is",average_1)

# 4. Write a python script to calculate volume of cuboid. formula=Volume (V) = (l × b × h) cubic units
l =int(input("Enter a lenght volume"))
b =int(input("Enter a breth volume"))
h = int(input("Enter a height volume"))

cuboid_v= l*b*h
print("volume of a cuboid is", cuboid_v)


# 5. Write a python script to take two numbers from user (say x and y), now calculate xy and display the result. 
x = int(input("Enter x number"))
y = int(input("Enter y number"))
z = x**y
print("result is",z)
