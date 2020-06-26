'''
The arithmetic operations are performed by calculator where we can perform addition, 
subtraction, multiplication and division. This example shows the basic arithmetic
operations.
-Addition 
-Substraction
-Multiplication
-Division
'''
print("Basic arithmetic operations:")
print("Enter two numbers you are intersted in:")
#store input numbers 
num1=float(input("Enter first number : "))
num2=float(input("Enter second number:"))
#Add the numbers 
sum=num1+num2
#Substract the two numbers
sub=num1-num2 
#Multiply the two numbers 
mul=(num1*num2)
#dividing two numbers 
div=(num1/num2)
	
#displaying the sum
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))

#displaying the substraction 
print("The substraction of {0} and {1} is {2}".format(num1,num2,sub))

#displaying the multiplication 
print("The multiplication of {0} and {1} is {2}".format(num1,num2,"%0.2f")%mul)

#displaying the division 
print("The division of {0} and {1} is {2}".format(num1,num2,"%0.2f")%div)







