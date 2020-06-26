'''
In this program, we need to print the duplicate elements present in the array. This can be done through two 
loops. The first loop will select an element and the second loop will iteration through the array by comparing 
the selected element with other elements. If a match is found, print the duplicate element.
'''
arr = [10,20,30,40,50,60,70,10,20,60,50,52,65]
print("duplicated elements: ")
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if arr[i]==arr[j]:
			print(i)








