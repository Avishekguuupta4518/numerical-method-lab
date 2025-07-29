import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
func_str = input("Enter the function f(x) : ")
def f(x):
    return eval(func_str)
a = float(input("Enter the first initial guess a: "))
b = float(input("Enter the second initial guess b: "))
if f(a) * f(b) > 0:
    print(f"No root lies in the interval [{a}, {b}]")
else:
    e = float(input("Enter the tolerable error: "))
    n = int(input("Enter the maximum number of iterations: "))
    iterations = []
    midpoints = []
    itr = 0
    while itr < n:
        c = (a + b) / 2
        midpoints.append((c, itr))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        err = abs((b - a) / a)
        iterations.append([itr, a, f(a), b, f(b), c, f(c), err])
        if err < e:
            print(f"The approximate root is {(a + b)/2} found in {itr+1} iterations.")
            break
        itr += 1
    if itr >= n:
        print(f"Method did not converge within {n} iterations.")
    df = pd.DataFrame(iterations, columns=['Iter', 'a', 'f(a)', 'b', 'f(b)', 'c', 'f(c)', 'Error'])
    print("\nIteration details:")
    print(df)
    x_vals = np.linspace(a - 2, b + 2, 400)
    y_vals = f(x_vals)  
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {func_str}')
    plt.axhline(0, color='gray', linestyle='--')
    for pt, i in midpoints:
        plt.plot(pt, f(pt), 'ro')
    plt.title("Bisection Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()