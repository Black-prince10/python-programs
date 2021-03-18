'''
We have already read the concept of prime numbers in the previous program. 
Here, we are going to print the prime numbers between given interval.
'''
lower = int(input('Enter lower range: '))
upper = int(input('Enter upper range: '))


for num in range(lower,upper+1): 
    if num > 1: 
        
        for i in range(2,num//2):
            if num%i ==0:
                ok = False
                break
            else: 
                ok=True
    if ok == True : 
        print(num)	
































