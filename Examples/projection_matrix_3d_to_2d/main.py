import numpy as np
from scipy import linalg

points_3d = [[1, 1, 1], 
             [2, 2, 2], 
             [3, 3, 3],
             [4, 4, 4]]

points_2d = [[1,1],
             [2,2],
             [3,3],
             [4,4]]


A = np.array(points_3d)
b = np.array(points_2d)
p, *_ = linalg.lstsq(A, b)

print(p.T)
print('--------------')

for p_3d in points_3d:
    print(np.dot(p.T, p_3d))