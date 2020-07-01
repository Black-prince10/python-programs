'''
A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly. 
If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy 
number.
example:
Number = 32
3²+ 2² = 13
1² + 3² = 10
1² + 0² = 1
'''
num =int(input("Enter a number:"))
def HappyNumber(num):
	remainder=0
	sum=0
	while num>0:
		remainder=num%10
		sum+=remainder**2
		num//=10
	return sum

result =num 

while result!=1 and result!=4:
	result =HappyNumber(result)

if result==1:
	print(num,"is a happy number!")
elif result==4:
	print(num,"is unhappy number!")




