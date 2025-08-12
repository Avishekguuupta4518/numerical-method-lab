import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

ode = input('Enter function dy/dx in terms of x and y: ') 

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input('Enter the initial x: '))
y = float(input('Enter the initial y: ')) 
h = float(input('Enter the step size: '))
n = int(input('Enter the number of steps: '))

t = []
xval = []
yval = []

t.append([x, y])
xval.append(x)
yval.append(y)

for i in range(n):
    y_pred = y + h * f(x, y)

    y = y + (h/2) * (f(x, y) + f(x + h, y_pred))
    
    x = x + h

    t.append([x, y])
    xval.append(x)
    yval.append(y)

t = pd.DataFrame(t, columns=['x', 'y'])
print('Solution (Heun’s Method):')
print(t)

plt.plot(xval, yval, marker='o', label="Heun's Method Solution", color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of ODE using Heun's Method")
plt.legend()
plt.grid(True)
plt.show()
