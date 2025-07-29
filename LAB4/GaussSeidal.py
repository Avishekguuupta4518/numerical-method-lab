import pandas as pd
import numpy as np

a = []
n = int(input('Enter the number of variables: '))
for i in range(n):
    a.append(list(map(float, input(f'Enter the elements for row {i+1} (including RHS): ').split())))

print("The augmented matrix:")
print(np.matrix(a))

e = float(input('Enter tolerance error: '))
N = int(input('Enter max iterations: '))

x = []
for i in range(n):
    x.append(float(input(f'Enter the initial value x[{i+1}]: ')))

x = np.array(x)
itr = 1
t = []

while itr <= N:
    x_old = np.copy(x)
    
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i][j] * x[j] 
        x[i] = (a[i][-1] - s) / a[i][i]
    
    t.append([itr] + list(x)) 
    err = np.abs(x - x_old)  
    
    if np.all(err < e):
        break

    itr += 1

if itr > N:
    print("This method diverges.")
else:
    t = pd.DataFrame(t, columns=['Iteration'] + [f'x{i+1}' for i in range(n)])
    print("\nIteration Table:")
    print(t)
    print("\nSolution:")
    for i in range(n):
        print(f'x{i+1} = {x[i]:.6f}')
