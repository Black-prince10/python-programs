'''
In this program, we need to sort the given array in descending order 
such that elements will be arranged from largest to smallest. This can 
be achieved through two loops. The outer loop will select an element, 
and inner loop allows us to compare selected element with rest of the 
elements.
'''
arr = [70,20,30,50,10,40,60]
temp = 0
print("Array original elements:")
for i in arr:
	print(i)
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if arr[i] < arr[j]:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
print("Array descending elements:")
for i in range(0,len(arr)):
	print(arr[i])
















