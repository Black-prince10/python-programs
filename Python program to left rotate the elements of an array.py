'''
In this program, we need to rotate the elements of an array towards the left by the specified number of times. 
In the left rotation, each element of the array will be shifted to its left by one position and the first 
element of the array will be added to end of the list. This process will be followed for a specified number of 
times.
'''
arr = [10,20,30,40,50,60,70]
n = 1 #change value to mess arround 
print("Original array:",arr)
for  i in range(0,n):
	element1 = arr[0]
	for j in range(0,len(arr)-1):
		arr[j] = arr[j+1]
	arr[len(arr)-1] = element1		

print("Array after left rotation:",arr)









