'''
In this program, we need to copy all the elements of one array into another. This can be accomplished by 
looping through the first array and store the elements of the first array into the second array at the 
corresponding position.
'''

#STEP 1: Declare and initialize an array.
arr1 = [10,20,30,40,50,60]

#STEP 2: Declare another array of the same size as of the first one
arr2 = [None]*len(arr1)

'''
STEP 3: Loop through the first array from 0 to length of the array and copy an element from the first 
array to the second array that is arr1[i] = arr2[i].
'''
for i in range(0,len(arr1)):
	arr2[i] = arr1[i]

print("The real array:",arr1)

print("The cloned array:",arr2)






