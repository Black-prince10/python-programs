'''
Odd and Even numbers:
If you divide a number by 2 and it gives a remainder of 0 then it is known as even number, 
otherwise an odd number.
Even number examples: 2, 4, 6, 8, 10	
Odd number examples:1, 3, 5, 7, 9 
'''
print("Python Program to Check if a Number is Odd or Even:")
print("Enter an integer to check!")
num=int(input("Enter a number:"))
if (num%2) ==0:
	print("{0} is even number!".format(num))
else:
	print("{0} is odd number!".format(num))
















