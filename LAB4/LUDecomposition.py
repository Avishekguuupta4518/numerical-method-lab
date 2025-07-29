import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

n = int(input('Enter the number of variables: '))
a = []
b = []

for i in range(n):
    a.append(list(map(float, input(f'Enter the elements for row {i+1} of A: ').split())))
print("Matrix A:")
print(np.matrix(a))

for i in range(n):
    b.append(float(input(f'Enter the RHS element b[{i+1}]: ')))
print("Vector b:")
print(np.array(b))

p, l, u = lu(a)
lum = lu_factor(a)

print("\nLower triangular matrix L:\n", l)
print("Upper triangular matrix U:\n", u)
print("Permutation matrix P:\n", p)

x = lu_solve(lum, b)
print("\nSolution:")
for i in range(n):
    print(f'x[{i+1}] = {x[i]:.6f}')
