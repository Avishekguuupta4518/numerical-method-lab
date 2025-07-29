import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input('Enter the equation in x using Python syntax')
def f(x):
    return eval(eqn, {"x": x, "np": np})
def g(f, x, h=1e-10):
    return (f(x + h) - f(x)) / h
a = float(input('Enter the first guess a: '))
tolerance = float(input('Enter the tolerance: '))
max_iter = int(input('Enter the maximum number of iterations: '))
iteration = []
points = []
itr = 0
while itr < max_iter:
    f_a = f(a)
    deriv = g(f, a)
    if deriv == 0:
        print("Division by 0 encountered in iteration", itr + 1)
        break
    b = a - f_a / deriv
    err = abs(b - a)
    iteration.append([itr + 1, a, f_a, err])
    points.append((b, itr))
    if err < tolerance:
        print(f"\nThe approximate root is {b} found in {itr + 1} iterations.")
        break
    a = b
    itr += 1
if itr >= max_iter:
    print(f"\nMethod did not converge within {max_iter} iterations.")
df = pd.DataFrame(iteration, columns=['Iteration', 'a', 'f(a)', 'Error'])
print("\nIteration details:")
print(df)
all_x = [row[1] for row in iteration]
x_min, x_max = min(all_x) - 1, max(all_x) + 1
x_vals = np.linspace(x_min, x_max, 500)
y_vals = [f(x) for x in x_vals]
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=f'f(x) = {eqn}', color='blue')
plt.axhline(0, color='red', linestyle='--')
for pt, i in points:
    plt.plot(pt, f(pt), 'ro')
    plt.annotate(f'{i + 1}', (pt, f(pt)), textcoords='offset points', xytext=(0, 10), ha='center')
plt.title("Function Plot with Newton-Raphson Method Points")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
