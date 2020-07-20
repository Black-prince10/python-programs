'''
In Python, you can create a simple calculator, displaying the different arithmetical operations i.e. addition, 
subtraction, multiplication and division.
'''
#functions 
def add(x,y):
    return x + y	
def substract(x,y):
	return x - y
def multiply(x,y):
	return x * y
def divide(x,y):
	return x / y
#take choice from the user 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("Available operations 1/2/3/4/5:")
print("1.Add")
print("2.Substrat")
print("3.Multiply")
print("4.divide")
print("5.all of the operations.")
choice = input("Enter choice:")

if choice == "1":
	print(num1,"+",num2,"=",add(num1,num2))

if choice == "2":
	print(num1,"-",num2,"=",substract(num1,num2))

if choice == "3":
	print(num1,"*",num2,"=",multiply(num1,num2))

if choice =="4":
	print(num1,"/",num2,"=",divide(num1,num2))

if choice =="5":
	print(num1,"+",num2,"=",add(num1,num2))
	print(num1,"-",num2,"=",substract(num1,num2))
	print(num1,"*",num2,"=",multiply(num1,num2))
	print(num1,"/",num2,"=",divide(num1,num2))


















