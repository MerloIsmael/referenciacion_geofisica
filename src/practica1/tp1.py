import numpy as np
from scipy import linalg

# %%
# definimos la matriz A (por filas)
A = np.array([[5, 5, 7, 8], [4, 7, 1, 1], [4, 4, 2, 1], [2, 4, 0, 3]])

# definimos la matrix b (por filas)
b = np.array([[2], [3], [7], [9]])

print(A)
print(b)

# %%
B = linalg.inv(A)
C = A.T
a = A @ b
c = C @ b
d = A.trace()

print(B)
print(C)
print(a)
print(c)
print(d)
