'''
Here, we are going to see the python program to convert kilometers to miles. 
Let's understand kilometers and miles first.

Kilometer:
The kilometer is a unit of length in the metric system. It is equivalent to 1000 meters.

Miles:
Mile is also the unit of length. It is equal to 1760 yards.

Conversion formula:
1 kilometer is equal to 0.621371 miles.
'''
print("Python program to convert kilometers to miles:")
#collecting input from the user 
kilometers=float(input("kilometers: ")) 
conv_fac=0.621371
#calculate miles 
miles=kilometers * conv_fac
print("%0.3f is equal to %0.3f"%(kilometers,miles))	
	























