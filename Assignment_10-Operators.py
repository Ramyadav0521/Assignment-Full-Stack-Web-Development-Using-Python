                # Assignment-10: Operators
# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
n =int(input("Enter a number"))
n =n//10
print("remove the last digit",n)


# 2. Write a python script to get the last digit from a given number.(for example, if user enters 2089 then your output should be 9)
n = int(input("Enter a number"))
n = n%10
print("print last digit from a give n number is",n)

# 3. Write a python script to swap data of two variables.
print("Swap to number")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2
# print("Swap two is","First",num1,"second",num2)

# second method
print("Second method")
print("num1=",num1,"num2=",num2)
num1,num2 =num2,num1


print("num1=",num1,"num2=",num2)

# 4. Write a python script which takes a three digit number from the user and displays only its first digit. 
n = int(input("Enter three digit number"))
n =n//100
print("print first digit number",n)

# 5. Write a python script which takes a three digit number from the user and displays only its middle digit. 
n = int(input("Enter a three digit number"))
n =n//10
n =n%10
print("print middle digit number is",n)
