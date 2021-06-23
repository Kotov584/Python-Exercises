import numpy as np
total = 0
matrix = np.array(([[1,3,19,20], [2,6,9,10], [-59,49,23,0], [10,1,-1.3]]))
print(matrix)

for i in range(4):
    for j in range(2):
        total = total +matrix[i][j]
total = sum(total)
print(total)
        
