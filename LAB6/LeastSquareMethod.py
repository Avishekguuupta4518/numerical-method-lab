# To fit a second degree curve y = a+bx+cx^2 for Given Data Points Using Least Squares Method

import numpy as np
import scipy.linalg as slg 
import matplotlib.pyplot as plt 

n = int(input('No. of data points: '))

x = np.array(list(map(float, input('Enter all x-data separated by space: ').split())))
y = np.array(list(map(float, input('Enter all y-data separated by space: ').split())))

print('Data points are:')
for i in range(n):
    print(f'{x[i]}, {y[i]}')

A = [
    [n, np.sum(x), np.sum(x**2)],
    [np.sum(x), np.sum(x**2), np.sum(x**3)],
    [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
]    

B = [
    [np.sum(y)],
    [np.sum(x*y)],
    [np.sum(x**2*y)]
]

coeff = slg.solve(A, B).flatten() 

print(f'The curve of best fit is: y = {coeff[0]} + {coeff[1]}x + {coeff[2]}x²')

x_fit = np.linspace(min(x) - 2, max(x) + 2, 100)
y_fit = coeff[0] + coeff[1]*x_fit + coeff[2]*x_fit**2

plt.scatter(x, y, color='red', label='Data points')
plt.plot(x_fit, y_fit, color='blue', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Quadratic Fit')
plt.legend()
plt.grid(True)
plt.show()
