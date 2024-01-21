matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) #print the element of matrix
matrix[0][1]=20 #change the matrix
print(matrix[0][1]) #print the changing matrix
#iteration of matrix:
for row in matrix:
    for iterm in row:
        print(iterm)
