import numpy as np
n = int(input("Enter the number of variables: "))
a = []
for i in range(n):
    a.append(list(map(float, input(f"Enter the elements in row {i+1} (including RHS), separated by space: ").split())))
a = np.array(a)
print("The Augmented matrix is:")
print(np.matrix(a))

for i in range(n):
    p_row = np.argmax(np.abs(a[i:, i])) + i
    a[[i, p_row]] = a[[p_row, i]]
    a[i] = a[i] / a[i, i]
    for j in range(n):
        if j != i:
            a[j] = a[j] - a[j, i] * a[i]

print(f"Matrix after step {i+1}:")
print(np.matrix(a))
x = a[:, -1]
print(f"The solution is: {x}")

