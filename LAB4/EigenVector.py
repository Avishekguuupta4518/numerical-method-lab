import numpy as np

n = int(input('Enter the number of variables: '))
a = []
x = []

for i in range(n):
    a.append(list(map(float, input(f'Enter the elements for row {i+1} of A: ').split())))
print("Matrix A:")
print(np.matrix(a))

for i in range(n):
    x.append(float(input(f'Enter the RHS element b[{i+1}]: ')))
print("Initial Vector x:")
print(np.array(x))

e = float(input('Enter tolerance error: '))
N = int(input('Enter max iterations: '))

itr = 1
oldev = 0

while itr <= N:
    y = np.dot(a, x)
    maxev = max(y, key=abs)
    x = y / maxev  
    err = abs(maxev - oldev)
    
    if err < e:
        break

    oldev = maxev
    itr += 1

if itr > N:
    print("This method did not converge within the maximum number of iterations.")
else:
    print(f"\nDominant eigenvalue is {maxev:.6f} found in {itr} iteration(s).")
    print("Corresponding eigenvector is:\n", x)
