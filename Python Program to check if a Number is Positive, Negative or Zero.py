'''
We can use a Python program to distinguish that if a number is positive, negative or zero.
Positive Numbers: A number is known as a positive number if it has a greater value than zero
Negative Numbers: A number is known as a negative number if it has a lesser value than zero
'''
print("Python Program to check if a Number is Positive, Negative or Zero:")

num=float(input("Enter a number: "))

if num>0:
	print("{0} is a positive number!".format(num))
elif num==0:
	print("{0}  is zero!".format(num))
else:
	print("{0} is a negative number!".format(num))




























