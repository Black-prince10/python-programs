'''
This program prints the smallest and the largest element in an array using for loop 
'''
arr = [40,20,30,10,50,60,70]
max =arr[0]
min =arr[0]
for i in range(0,len(arr)):
	if arr[i]>max:
		max=arr[i]
	if arr[i]<min:
		min=arr[i]

print("The largest element in arr is:",max)
print("The smallest element in arr is:",min)
















