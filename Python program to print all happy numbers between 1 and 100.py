'''
In this programme, we will print all happy numbers between 1 and 100.
'''
def HappyNumber(num):
	remainder = 0 
	sum = 0
	while num > 0:
		remainder = num%10
		sum += remainder**2
		num //= 10
	return sum
print("Happy numbers between 1 and 100 are :")
for i in range(1,101):
	result=i
	while (result != 1) and (result != 4):    
		result = HappyNumber(result)
	if result == 1:
		print(i,end=" ")














