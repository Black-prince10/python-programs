'''
HCF: Highest Common Factor

Highest Common Factor or Greatest Common Divisor of two or more integers when at 
least one of them is not zero is the largest positive integer that evenly divides 
the numbers without a remainder. For example, the GCD of 8 and 12 is 4.

For example:
We have two integers 8 and 12. Let's find the HCF.
The divisors of 8 are:
1, 2, 4, 8  
The divisors of 12 are:
1, 2, 3, 4, 6, 12  
HCF /GCD is the greatest common divisor. So HCF of 8 and 12 are 4.
'''
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
def hcf(x,y):
	if x > y:
		smaller = y
	else:
	    smaller = x
	for i in range(1,smaller+1):
		if x%i == 0 and y%i == 0: 
			hcf = i
	return hcf 
print("H.C.F of ",num1,"and",num2,"is",hcf(num1,num2))
			








