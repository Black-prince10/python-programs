'''
In this program, we need to print the elements of the array in reverse order that is; the last element should 
be displayed first, followed by second last element and so on
'''
arr = [10,20,30,40,50,60,70]
print("First way to do it:")
for i in range(-1,-len(arr)-1,-1):
	print(arr[i])

'''
or we can reverse the array and then print its elements 
'''
print("Second way to do it:")
arr.reverse()
for i in range(0,len(arr)):
	print(arr[i])





