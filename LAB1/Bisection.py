import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
def f(x):
  return x**2 - 4*x - 10

a = float(input('Enter first initial guess (a): '))
b = float(input('Enter second initial guess (b): '))

if f(a) * f(b) > 0:
    print(f'No root lies in the interval ({a}, {b})')
else:
    e = float(input('Enter tolerable error: '))
    n = int(input('Enter max number of iterations: '))
    itr = 0
    a_init, b_init = a, b
    iterations = []
    midpoints = []

    while itr < n:
        c = (a*f(b)-b*f(a))/ (f(b) - f(a))
        midpoints.append((c, itr)) 

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        er = abs(b - a) 

        iterations.append([itr, a, f(a), b, f(b), c, f(c), er])

        if er < e:
            print(f'The approximate root is {c} found in {itr} iterations')
            break

        itr += 1

    if itr == n:
        print(f'Method did not converge within {n} iterations')

    df = pd.DataFrame(iterations, columns=["Iteration", "a", "f(a)", "b", "f(b)", "c (mid)", "f(c)", "Error"])
    print("\nIteration Table:")
    print(df)

    x_vals = np.linspace(a_init - 1, b_init + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.axhline(y=0, color='black', linestyle='--') 

    for midpoint, index in midpoints:
        plt.scatter(midpoint, f(midpoint), color="red")
        plt.text(midpoint, f(midpoint), f"{index}", fontsize=9, verticalalignment='bottom', color="black")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method Visualization")
    plt.legend()
    plt.grid(True)
    plt.show()