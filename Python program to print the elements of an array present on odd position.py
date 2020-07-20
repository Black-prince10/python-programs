'''
In this program, we need to print the elements of the array which are present in odd positions. 
This can be accomplished by looping through the array and printing the elements of an array by incrementing i
from 1 by 2 till the end of the array is reached.
'''
arr = [10,20,30,40,50,60,70]
print("Elements present on odd positions:")
for i in range(1,len(arr),2):
	print(arr[i])
max = 0
for o in range(0,len(arr)):
	if arr[o] > max:
		max = arr[o]
print(max)
