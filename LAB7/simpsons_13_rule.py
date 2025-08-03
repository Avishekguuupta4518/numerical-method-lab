import numpy as np
import matplotlib.pyplot as plt 

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: ')) 
n = int(input('Enter the number of partitions (must be even): '))

if n % 2 != 0:
    print('Enter a multiple of 2')
else:
    h = (b - a) / n
    func = input('Enter the function in terms of x : ')

    def F(x, func):
        return eval(func)

    def y(x):
        return F(x, func)

    x = np.linspace(a, b, n + 1)

    i = 0
    s1 = 0
    s2 = 0

    for i in range(1, n):
        if i % 2 == 0:
            s2 += y(x[i])
        else:
            s1 += y(x[i])

    i = (h / 3) * (y(x[0]) + 4 * s1 + 2 * s2 + y(x[n]))

    print(f"\nApproximate integral using Simpson's 1/3 Rule: {i:.6f}")

    plt.plot(x, [y(xi) for xi in x], color='red', label='f(x) ')
    xval = np.linspace(a+10, b-10, 1000)
    plt.plot(xval, [y(xi) for xi in xval], label='Smooth Curve')

    ypoints = [y(xi) for xi in x]

    for i in range(0, n, 2):
        xs = x[i:i+3]
        ys = ypoints[i:i+3]
        plt.fill_between(xs, ys, color='blue', edgecolor='green',alpha=0.3)

    plt.title('Simpson\'s 1/3 Approximation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()
