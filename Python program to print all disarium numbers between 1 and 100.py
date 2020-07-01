'''
In this program, we need to print all disarium numbers between 1 and 100 
'''
sum=0
for num in range(1,101):
	num_str=str(num)
	for i in range(0,len(num_str)):
		sum+=int(num_str[i])**(i+1)
	if num==sum:
	    print(num)
	sum=0

	











