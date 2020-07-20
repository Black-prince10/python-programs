'''
Natural numbers:
As the name specifies, a natural number is the number that occurs commonly and obviously in 
the nature. It is a whole, non-negative number.
Some mathematicians think that a natural number must contain 0 and some don't believe this 
theory.
'''	
num = int(input("Enter a number:"))
if num < 0:
	print("Enter a positive number!")
else:
	sum = 0
	#use while loop to iterate until zero
	while num > 0:
		sum += num
		num -= 1
	print("The sum is",sum)















