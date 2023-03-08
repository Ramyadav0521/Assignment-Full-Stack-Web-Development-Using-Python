             #Assignment-4:Playing with variables
# 1. Write a python script containing a variable with some integer value, print value of this variable.
a = 123
b = 456
c = 789
d = 10,11,12
print(a,b,c,d)

# 2. Write a python Script to print the value of a variable. Variable contains your name as data

first = input("Enter your first name")
last = input("Enter your last name")
mob = int(input("Enter your mobile number"))
email = input("Enter your Email Id")

print("My first name is",first)
print("My last name is",last)
print("My mobile number is",mob)
print("My Email Id is ",email)

# 3. Write a python script to print values of three variables, each in new line. All three variables are filled with some integer values
x,y,z = int(input("Enter integer values"))
print(x,y,z, sep="\n") 

# 4. Creat 5 variables each of them containning different types of data(like 35, True, "MySirg", 5.46,3+4j, ect). Write a python script to print of all the varuables along with their data types
print("print integer values like this--> 3568")
a = 35
print("Data type",type(a),a)

print("print bool values like this--> True or Flase")
b = True
print("Data type",type(b),b)

print('print str values like this--> "MySirG" ')
c = "MySirG"
print("Data type",type(c),c)

print('print Float values like this--> 45.56 ')
d = 4.46
print("Data type",type(d),d)

print('print complex values like this--> 3=5j ')
e = 3+4j
print("Data type",type(e),e)

# 5. Create three variables and assign current data to them, first variables contains day numbers, second variables contains month number and variable contains year number. write a python script to display in standad way(e.g. 08/03/2023)
print("Enter current date to them")
day = int(input())
month = int(input())
year = int(input())
print(day,month,year, sep='/')