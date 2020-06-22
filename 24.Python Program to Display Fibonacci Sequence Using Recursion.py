'''
A Fibonacci sequence is a sequence of integers which first two terms are 0 and 1 and all other
terms of the sequence are obtained by adding their preceding two numbers.
For example: 0, 1, 1, 2, 3, 5, 8, 13 and so on...
'''
def recur_fibo(n):
	if n<=1:
		return n
	else:
	    return recur_fibo(n-1) + recur_fibo(n-2)	

nterms =int(input("Enter the number of the terms:"))
 
if nterms<=0:
	print("Please enter a positive integer!")
else: 
	print("Fibonacci sequence:")
	for i in range(nterms):
		print(recur_fibo(i))










