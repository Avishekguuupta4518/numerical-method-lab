import numpy as np
import matplotlib.pyplot as plt 

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: ')) 
n = int(input('Enter the number of partitions: '))

h = (b - a) / n

func = input('Enter the function in terms of x : ')

def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n + 1)

i = 0
s = 0

for i in range(1, n):
    s += y(x[i])

i = (h / 2) * (y(x[0]) + 2 * s + y(x[n]))

print(f"\nApproximate integral using Trapezoidal Rule: {i:.6f}")

plt.plot(x, [y(x) for x in x], color='red', label='f(x)')

xval = np.linspace(a - 10, b + 10, 1000)
plt.plot(xval, [y(x) for x in xval], label='Smooth Curve')

ypoints = [y(xi) for xi in x]

for i in range(n):
    xs = [x[i], x[i+1], x[i+1], x[i]]
    ys = [0, 0, ypoints[i+1], ypoints[i]]
    plt.fill(xs, ys, color='blue', alpha=0.3)

plt.title('Trapezoidal Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
