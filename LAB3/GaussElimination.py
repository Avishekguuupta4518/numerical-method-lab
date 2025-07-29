# to solve the system of linear of equation by using Gauss Elimination Method in python programming


import numpy as np

n = int(input("Enter the number of variable: "))
a = []
for i in range (n):
    a.append(list(map(float, input(f"Enter the element in {i+1} row and press enter ").split())))
    
a = np.array(a)

print("The Augemented matrix is :")
print(np.matrix(a))

for i in range (n):
    p_row = np.argmax(np.abs(a[i:,i]))+i
    a[[i, p_row]] = a[[p_row, i]]
    for j in range(i+1, n):
        a[j] = a[j] - a[j,i]*a[i]/a[i,i]
    print("The upper triangular matrix is :")
    print(np.matrix(a))
    
x = np.zeros(n)

for i in range (n-1, -1,-1):
    x[i] = (a[i,  -1] -np.sum(a[i,i+1:n]*x[i+1:n]))/ a[i,i] 
    
print(f"The answer is {x}")           
            