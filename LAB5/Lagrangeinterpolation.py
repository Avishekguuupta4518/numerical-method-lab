import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input('No. of data points: '))
X = np.array(list(map(float, input('Enter all x-data separated by space: ').split())))
Y = np.array(list(map(float, input('Enter all y-data separated by space: ').split())))

print('Data points are:')
for i in range(n):
    print(f'{X[i]}, {Y[i]}')

x = sp.symbols('x')
poly = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if j != i:
            lf *= (x - X[j]) / (X[i] - X[j])
    poly += Y[i] * lf

poly = sp.simplify(poly)
print('Lagrange interpolation polynomial is:\n', poly)

Xp = float(input('Enter interpolation point: '))
int_val = poly.subs(x, Xp)
print(f'Value of interpolation polynomial at {Xp} is {int_val}')

f = sp.lambdify(x, poly, 'numpy')
x_min, x_max = min(X.min(), Xp), max(X.max(), Xp)
x_val = np.linspace(x_min, x_max, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x_val, f(x_val), label='Lagrange Interpolation')
plt.scatter(X, Y, color='red', edgecolor='black', s=100, label='Data Points')
plt.scatter(Xp, float(int_val), color='green', edgecolor='black', s=100, label='Interpolation Point')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation Polynomial')
plt.legend()
plt.grid()
plt.show()