# SciPy

**`SciPy`** is a powerful library that builds upon NumPy, designed to perform advanced scientific and technical computations efficiently. It offers modules for optimization, integration, interpolation, algebraic equations, and more. Like `NumPy`, `SciPy` is written primarily in C, making it highly performant for large-scale computations.


## 1) Easy Roots 🌱

Find the root (zero) of the following equation using [`scipy.optimize.root`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html) (accepts a function and an initial guess; returns the root value), for example:

$$
f(x) = cos⁡(x) − x
$$

*Hint*: You can use `numpy.cos` for the cosine function

```py
from scipy.optimize import root
import numpy as np


def f(x):
    return ???  # Write some function here (maybe the audience can suggest one 😉)

solution = ???

print("SciPy's result:", solution)  # Preview the output of SciPy's optimization
print()
print("x =", solution.x)
```

<details><summary><b>Solution</b></summary>

```py
from scipy.optimize import root
import numpy as np


def f(x):
    return np.cos(x) - x

solution = root(f, 0)  # Initial guess: x = 0. In this example you can put basically any number here

print("SciPy's result:", solution)  # Preview the output of SciPy's optimization
print()
print("x =", solution.x)
```
</details>


## 2) Basic Optimization with minimize 🔍

You task is to optimize a function. For example:
$$
f(x) = x^2 + 5x + 4
$$

Find the value of $x$ that minimizes the function using [`scipy.optimize.minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) (accepts the function and the initial guess; returns the optimized value)

```py
from scipy.optimize import minimize


def f(x):
    return ???  # Write some function here (maybe the audience can suggest one 😉)

result = ???

print("SciPy's result:", result)  # Preview the output of SciPy's optimization
print()
print("x =", result.x)
```

<details><summary><b>Solution</b></summary>

```py
from scipy.optimize import minimize


def f(x):
    return x**2 + 5*x + 4

result = minimize(f, 0)  # Initial guess: x = 0. In this example you can put basically any number here

print("SciPy's result:", result)   # Preview the output of SciPy's optimization
print()
print("x =", result.x)
```
</details>


## 3) Determinant and Inverse of a Matrix 🔄

Given the following matrix:
$$
A = \begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
$$

- Calculate the determinant of the matrix $A$ using [`scipy.linalg.det`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.det.html) (accepts a matrix; returns the determinant)
- Compute the inverse of the matrix $A$ using [`scipy.linalg.inv`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html) (accepts a matrix; returns the inverse)
- Verify the result by multiplying the original matrix $A$ by its inverse and checking if the result is the identity matrix

```py
import numpy as np
from scipy.linalg import det, inv


A = np.array([[2, 3],
              [1, 4]])

determinant = ???

A_inv = ???

identity_check = np.round(???, decimals=5)

print("Matrix A:\n", A)
print("Determinant of A:", determinant)
print("Inverse of A:\n", A_inv)
print("Product of A and its inverse (should be identity):\n", identity_check)
```

<details><summary><b>Solution</b></summary>

```py
import numpy as np
from scipy.linalg import det, inv


A = np.array([[2, 3],
              [1, 4]])

determinant = det(A)

A_inv = inv(A)

identity_check = np.round(np.dot(A, A_inv), decimals=5)

print("Matrix A:\n", A)
print("Determinant of A:", determinant)
print("Inverse of A:\n", A_inv)
print("Product of A and its inverse (should be identity):\n", identity_check)
```
</details>


## 4) Solving a System of Linear Equations 🔗

We can solve a system of linear equations using SciPy's [`scipy.linalg.solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html) (accepts a matrix of coefficients and a vector of constants; returns the solution vector), for example:
$$
2x + y = 3
$$
$$
3x + 2y = 5
$$

**Additionally:** check yourself by substituting the values of the calculated $x$ and $y$ in the equations by hand

```py
from scipy.linalg import solve


A = ???  # Matrix of coefficients
b = ???  # Vector of constants

solution = ???

print("Solution:", solution)
```

<details><summary><b>Solution</b></summary>

```py
from scipy.linalg import solve


A = [[2, 1],
     [3, 2]]

b = [3, 5]

solution = solve(A, b)

print("Solution:", solution)  # [1, 1], which means x = 1 and y = 1
```
</details>


## 5) Numerical Integration 📐

Numerically integrate the following function over the interval $[0, 1]$ using [`scipy.integrate.quad`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html) (accepts the function, the left limit and the right limit; returns the integral value + the estimated absolute error), for example:

$$
f(x) = e^{−x ^ 2}
$$

*Hint*: You can use `numpy.exp` for the exponential function

> The function is called `quad`, because it is based on the **Fortran**'s `QUADPACK` library.\
> Also the term "*numerical quadrature*" (often abbreviated to "*quadrature*") is more or less a synonym for numerical integration, especially as applied to one-dimensional integrals

```py
from scipy.integrate import quad
import numpy as np


def f(x):
    return ???

result, error = ???

print("Integral result:", result, "with an estimate of the absolute error:", error)
```

<details><summary><b>Solution</b></summary>

```py
from scipy.integrate import quad
import numpy as np


def f(x):
    return np.exp(-x**2)

result, error = quad(f, 0, 1)

print("Integral result:", result, "with an estimate of the absolute error:", error)
```
</details>


## 6) Interpolation of Data 📈

You have the following data points:
$$
x = [0, 1, 2, 3, 4]
$$
$$
y = [1, 3, 2, 5, 7]
$$

Linearly interpolate the data using [`scipy.interpolate.interp1d`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html) (stands for "interpolation in 1 dimension"; accepts the data points and the interpolation method; returns a function that can be used to interpolate new values) and find the interpolated value at $x = 2.5$. The result should be the middle point between $2$ and $5$, which is $3.5$

```py
from scipy.interpolate import interp1d


x = [0, 1, 2, 3, 4]
y = [1, 3, 2, 5, 7]

function = ???

interpolated_value = ???

print("Interpolated value at x = 2.5:", interpolated_value)
```

<details><summary><b>Solution</b></summary>

```py
from scipy.interpolate import interp1d


x = [0, 1, 2, 3, 4]
y = [1, 3, 2, 5, 7]

function = interp1d(x, y)

interpolated_value = function(2.5)

print("Interpolated value at x = 2.5:", interpolated_value)
```
</details>


## 7) Finding Local Maxima/Minima 🌄

Use [`scipy.signal.find_peaks`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html) (accepts the data; returns the indices of the peaks and some properties of the peaks) to identify the local maxima in a given dataset.

- Create a randomized sample dataset using NumPy
- Find the indices of the peaks
- Convert the dataset to integer type for easier visualization.

```py
import numpy as np
from scipy.signal import find_peaks

np.set_printoptions(edgeitems=30, linewidth=180)  # Prettier printing


x = ???  # Create an array of values from 0 to 10 (hint: np.linspace)
y = np.sin(x) + 0.5 * np.random.normal(size=x.size)

peaks, _ = ???

print("Dataset:", y???)  # We can convert the dataset to integer type for easier visualization (hint: astype(dtype))
print("Indices of peaks:", peaks)
```

<details><summary><b>Solution</b></summary>

```py
import numpy as np
from scipy.signal import find_peaks

np.set_printoptions(edgeitems=30, linewidth=180)  # Prettier printing


x = np.linspace(0, 10, 20)
y = np.sin(x) + 0.5 * np.random.normal(size=x.size)

peaks, _ = find_peaks(y)

print("Dataset:", (y * 100).astype(int))  # We can convert the dataset to integer type for easier visualization
print("Indices of peaks:", peaks)
```
</details>


## 8) (Hard math) Solving Differential Equations 🧮

Solve the ordinary differential equation (ODE) using [`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) (stands for "Initial value problem").

This function numerically integrates a system of ODEs given an initial value:
```text
dy / dt = f(t, y)
y(t0) = y0
```

With the initial condition $y(0) = 1$, solve the following ODE over the interval $[0, 5]$:

$$
\frac{dy}{dx} = −2y
$$

The `solve_ivp` function accepts the ODE function ($f$), the interval ($[0, 5]$), and the initial condition ($[1]$); returns the value of $y$ that satisfies the ODE

*Hint*: You can use the `max_step` parameter to increase the number of points in the output, which would make the graph smoother

```py
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def dy_divided_by_dx(x, y):
    return ???

solution = ???

print("Solution (as points):")
amount_of_points = 10
for i in range(0, len(solution.t) // 3, len(solution.t) // 3 // amount_of_points):
    print(f"t = {solution.t[i]:.2f}, y = {solution.y[0, i]:.2f}")

plt.plot(solution.t, solution.y[0], label='y(t) = e^(-2t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of dy/dx = -2y')
plt.grid(True)
plt.legend()
plt.show()
```

<details><summary><b>Solution</b></summary>

```py
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def dydx(x, y):
    return -2 * y

solution = solve_ivp(dydx, [0, 5], [1], max_step=0.01)

print("Solution (as points):")
amount_of_points = 10
for i in range(0, len(solution.t) // 3, len(solution.t) // 3 // amount_of_points):
    print(f"t = {solution.t[i]:.2f}, y = {solution.y[0, i]:.2f}")

plt.plot(solution.t, solution.y[0], label='y(t) = e^(-2t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of dy/dx = -2y')
plt.grid(True)
plt.legend()
plt.show()
```
</details>
