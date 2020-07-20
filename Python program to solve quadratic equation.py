'''
Quadratic equation:
Quadratic equation is made from a Latin term "quadrates" which means square. It is a special 
type of equation having the form of:
ax²+bx+c=0
Here, "x" is unknown which you have to find and "a", "b", "c" specifies the numbers such that
"a" is not equal to 0. If a = 0 then the equation becomes liner not quadratic anymore.
In the equation, a, b and c are called coefficients.
'''
print("Solving quadratic equation:")
print("Enter the coefficients of the equation:")
import math
a = float(input("a = ")) 

b = float(input("b = "))

c = float(input("c = "))

#claculate the discriminant  	
d = (b**2)-(4*a*c) 

if d < 0: 
	print("There are no real solutions!")
elif d == 0:
	x = -b / (2*a)
	print("There is only one real solution: %0.2f"%x)
else:
	x1 = (-b-math.sqrt(d)) / (2*a)
	x2 = (-b+math.sqrt(d)) / (2*a)
	print("There are two real solutions:{0} and {1}".format("%0.2f"%x1,"%0.2f"%x2))



















