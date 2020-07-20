'''
LCM: Least Common Multiple/ Lowest Common Multiple
LCM stands for Least Common Multiple. It is a concept of arithmetic and number system. 
The LCM of two integers a and b is denoted by LCM (a,b). It is the smallest positive 
integer that is divisible by both "a" and "b".

For example: We have two integers 4 and 6. Let's find LCM
Multiples of 4 are:
4, 8, 12, 16, 20, 24, 28, 32, 36,... and so on...  

Multiples of 6 are:
6, 12, 18, 24, 30, 36, 42,... and so on....  

Common multiples of 4 and 6 are simply the numbers that are in both lists:
12, 24, 36, 48, 60, 72,.... and so on....
->LCM is the lowest common multiplier so it is 12.
'''
print("Python Program to Find LCM:")
num1 = int(input("The first number :"))
num2 = int(input("The second number:"))

def lcm(x,y):
	if x > y:
		greater = x
	else:
	    greater = y
	while True:
		if (greater%x == 0) and (greater%y == 0):
			lcm =greater 
			break
		greater += 1
	return lcm		
print("The L.C.M of:",num1,"and",num2,"is",lcm(num1,num2))	    	

































