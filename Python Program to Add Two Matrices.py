'''
In mathematics, matrix is a rectangular array of numbers, symbols or expressions arranged in 
the form of rows and columns.
for example: 
           columns 
first row: 2   3   5 
second row:8   12  7	

In Python, matrices can be implemented as nested list. Each element of the matrix is treated as 
a row. For example X = [[1, 2], [3, 4], [5, 6]] would represent a 3x2 matrix. First row can be 
selected as X[0] and the element in first row, first column can be selected as X[0][0].
'''

X = [[1,2,3],
  [4,5,6],
  [7,8,9]]
 
Y = [[10,11,12],
  [13,14,15],
  [16,17,18]]
result = [[0,0,0],
       [0,0,0],
       [0,0,0]]
#iterate through rows 
for i in range(len(X)):
	#iterate through columns 
	for j in range(len(Y)):
		result[i][j] = X[i][j] + Y[i][j]
print(result)		


































