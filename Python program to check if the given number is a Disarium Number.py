'''
A number is said to be the Disarium number when the sum of its digit 
raised to the power of their respective positions becomes equal to the 
number itself.
eg:175
1*1+ 7² + 5*5*5 = 1+ 49 + 125 = 175
'''
num = input("Enter a number:")
sum = 0
for i in range(0,len(num)):
	sum += int(num[i])**(i+1)
if sum == int(num):
	print(num,"is a disarium number")
else:
	print(num,"is not a disarium number")
















