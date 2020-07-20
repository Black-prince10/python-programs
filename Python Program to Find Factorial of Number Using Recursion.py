'''
Factorial: Factorial of a number specifies a product of all integers from 1 to that number. 
It is defined by the symbol explanation mark (!).
For example: The factorial of 5 is denoted as 5! = 1*2*3*4*5 = 120.
'''
def recur_factorial(n):
	if n == 1:
		return n 
	else:
	    return n*recur_factorial(n-1)
num = int(input("Enter a number:"))
if num < 0:#check if the number is negative!
    print("Factorial does not exist for negative numbers!")
elif num == 0:
    print("The factorial of 0 is 1")      	    	 
else: 
	print("The factorial of",num,"is",recur_factorial(num))



















