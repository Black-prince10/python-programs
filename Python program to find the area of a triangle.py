'''
Mathematical formula:
Area of a triangle = (s*(s-a)*(s-b)*(s-c))**0.5
Here s is the semi-perimeter and a, b and c are three sides of the triangle.
'''
#Three sides of the triangle are a,b and c 
a = float(input("Enter first  side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third  side: "))

#Calculate the semi-perimeter 
s = (a+b+c) / 2

#Calculate the area 
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is %0.2f"%area)#%0.2f is to determine number of digits after(.) 


























