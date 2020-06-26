'''
In this program, we have an array of elements to count the occurrence of its each element. One of the approaches 
to resolve this problem is to maintain one array to store the counts of each element of the array. Loop through 
the array and count the occurrence of each element as frequency and store it in another array fr.
ALGORITHM:
STEP 1: Declare and initialize an array arr.
STEP 2: Declare another array fr with the same size of array arr. It is used to store the frequencies of 
elements present in the array.
STEP 3: Variable visited will be initialized with the value -1. It is required to mark an element visited 
it helps us to avoid counting the same element again.
STEP 4: The frequency of an element can be counted using two loops. One loop will be used to select an element 
from an array, and another loop will be used to compare the selected element with the rest of the array.
STEP 5: Initialize count to 1 in the first loop to maintain a count of each element. Increment its value by 1 
if a duplicate element is found in the second loop since we have counted this element and didn't want to count 
it again. Mark this element as visited by setting fr[j] = visited. Store count of each element to fr.
STEP 6: Finally, print out the element along with its frequency.
'''
arr=[1, 2, 8, 8,3,3, 2, 2,1, 2, 5, 1]
fr =[None]*len(arr)
visited =-1
for i in range(0,len(arr)):
	count=1
	for j in range(i+1,len(arr)):
		if arr[i]==arr[j]:
			count+=1
			fr[j]=visited
	if fr[i]!=visited:
	    fr[i]=count		
for i in range(0,len(arr)):
    if fr[i]!=visited:
        print("element:",arr[i],"frequency:",fr[i])	    