'''
In this program, we need to rotate the elements of array towards its right by the specified number of times. 
An array is said to be right rotated if all elements of the array are moved to its right by one position. 
One approach is to loop through the array by shifting each element of the array to its next position. The 
last element of the array will become the first element of the rotated array.
'''
arr = [10,20,30,40,50,60,70]
n = 1 #change value to mess arround 
print("Original array:",arr)
for i in range(0,n):
	last_element=arr[-1]
	for j in range(len(arr)-1,-1,-1):
		arr[j]=arr[j-1]
	arr[0]=last_element	
print("Array after right rotation:",arr)
    
















