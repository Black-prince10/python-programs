'''
In Python programming, you can generate a random integer, doubles, longs etc . 
in various ranges by importing a "random" class.
First you have to import the random module and then apply the syntax:
import random  
random.randint(a,b)  
'''
import random 
print("Enter the values of the range you are interested in:")
a=int(input("Enter the first value :")) 
b=int(input("Enter the second value:"))
print(random.randint(a,b))























