# To find the least eigen value and corresponding eigen vector of matrix using inverse power method

import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

n = int(input('Enter the number of variables: '))
a = []
x = []

for i in range(n):
    a.append(list(map(float, input('Coefficient matrix: ').split())))
print("Matrix A:")
print(np.matrix(a))

for i in range(n):
    x.append(list(map(float, input('Initial vector: ').split())))
x = np.array(x)
print("Initial Vector x:")
print(np.matrix(x))

e = float(input('Enter the tolerance: '))
N = int(input('Enter the number of iterations: '))

itr = 1
oldev = 0

def inv(mat):
    try:
        return np.linalg.inv(mat)
    except np.linalg.LinAlgError:
        print('Matrix is singular. Cannot proceed.')
        exit()

while itr <= N:
    y = np.dot(inv(a), x)
    
    # Find the maximum absolute value in the result vector (flattened)
    maxev = np.max(np.abs(y))
    
    # Normalize the vector
    x = y / maxev

    # Check convergence
    err = abs(maxev - oldev)
    if err < e:
        break

    oldev = maxev
    itr += 1

if itr > N:
    print('Did not converge within given number of iterations.')
else:
    print(f'Least eigen value is approximately {1 / maxev:.6f} found in {itr} iterations')
    print('Corresponding eigen vector (normalized):')
    print(x)
