import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
eqn = input('Enter the equation in x using Python syntax ')
def f(x):
    return eval(eqn, {"x": x, "np": np})
a = float(input('Enter the first guess a: '))
b = float(input('Enter the second guess b: '))
tolerance = float(input('Enter the tolerance: '))
max_iter = int(input('Enter the maximum number of iterations: '))
if abs(b - a) < 1e-12:
    print("Initial guesses a and b are too close.")
    exit()
iteration = []
points = []
itr = 0
while itr < max_iter:
    f_a = f(a)
    f_b = f(b)
    if f_a == f_b:
        print(f"Division by zero encountered in iteration {itr + 1}")
        break
    c = b - f_b * (b - a) / (f_b - f_a)
    err = abs((c - b) / c) if c != 0 else 0
    f_c = f(c)
    iteration.append([itr + 1, a, f_a, b, f_b, c, f_c, err])
    points.append((c, itr))
    if err < tolerance:
        print(f"\nThe approximate root is {c} found in {itr + 1} iterations.")
        break
    a, b = b, c
    itr += 1
if itr >= max_iter:
    print(f"\nMethod did not converge within {max_iter} iterations.")
df = pd.DataFrame(iteration, columns=['Iteration', 'a', 'f(a)', 'b', 'f(b)', 'c', 'f(c)', 'Error'])
print("\nIteration details:")
print(df.to_string(index=False))

x_vals = np.linspace(a - 2, b + 2, 500)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='red', linestyle='--')  # x-axis
for c, i in points:
    plt.plot(c, f(c), 'ro')  # red point
    plt.text(c, f(c) + 0.1, f'{i+1}', ha='center')  
plt.title("Secant Method Approximations")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
