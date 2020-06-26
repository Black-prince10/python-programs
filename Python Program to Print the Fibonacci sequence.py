'''
Fibonacci sequence:
The Fibonacci sequence specifies a series of numbers where the next number is found by adding
up the two numbers just before it.
'''
print("Python Program to Print the Fibonacci sequence:")
terms_number=int(input("Enter the number of terms you want:"))
#first two numbers 
n1=0
n2=1
count=2
#check 	if the number of terms is valid
if terms_number<=0:
	print("Please enter a positive integer!")
elif terms_number ==1:
	print(n1)
else:
	print("fibonacci sequence:")
	print(n1,",",n2,end=",")
	while count <terms_number:
		n3=n1+n2
		print(n3,end=",")
		#update values 
		n1=n2
		n2=n3
		count+=1




