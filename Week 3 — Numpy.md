## 1) Basic Array Creation 🍏

Create a 1D NumPy array containing the integers from 10 to 50, inclusive

<details><summary>Useful functions</summary>

```py
numpy.arange(start, stop, step)  # Returns an array of evenly spaced values within a given interval.
```
</details>

<details><summary><b>Solution</b></summary>

```py
import numpy as np

arr = np.arange(10, 51)
print(arr)
```
</details>


## 2) Array Arithmetic 🔢

Create two NumPy arrays of shape `(3, 3)`, filled with random integers between 1 and 20

Perform element-wise addition, subtraction, multiplication, and division

<details><summary>Useful functions</summary>

```py
numpy.random.randint(low, high, size)  # Returns an array of random integers from low (inclusive) to high (exclusive)
```
</details>

<details><summary><b>Solution</b></summary>

```py
arr1 = np.random.randint(1, 21, size=(3, 3))
arr2 = np.random.randint(1, 21, size=(3, 3))

addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Division:\n", division)
```
</details>


## 3) Summing the Diagonals 🎲

Create a 5x5 matrix of random integers between 10 and 100

Calculate the sum of both the main diagonal and the anti-diagonal

<details><summary>Useful functions</summary>

```py
numpy.diag(array)    # Extracts the diagonal elements of an array
numpy.fliplr(array)  # Flips the array in the left/right direction
numpy.sum(array)     # Returns the sum of all elements in the array
```
</details>

<details><summary><b>Solution</b></summary>

```py
matrix = np.random.randint(10, 101, size=(5, 5))

main_diag_sum = np.sum(np.diag(matrix))
anti_diag_sum = np.sum(np.diag(np.fliplr(matrix)))

print("Main diagonal sum:", main_diag_sum)
print("Anti-diagonal sum:", anti_diag_sum)
```
</details>


## 4) Fancy Indexing with Conditions 🔍

Generate a NumPy array of 100 random integers between 1 and 100

Find all elements that are divisible by 3 but not by 5 using array indexing

<details><summary><b>Solution</b></summary>

```py
arr = np.random.randint(1, 101, size=100)

filtered = arr[(arr % 3 == 0) & (arr % 5 != 0)]

print(filtered)
```
</details>


## 5) Flatten, Sort, and Find 📏

Create a 6x6 matrix of random integers

Flatten it into a 1D array, sort the array, and find the 3 largest elements

<details><summary>Useful functions</summary>

```py
numpy.ndarray.ravel(array)  # Returns a flattened array
numpy.sort(array)           # Returns a sorted copy of the array
```
</details>

<details><summary><b>Solution</b></summary>

```py
matrix = np.random.randint(1, 101, size=(6, 6))

flattened = matrix.ravel()
sorted_array = np.sort(flattened)
largest_3 = sorted_array[-3:]

print("3 largest elements:", largest_3)
```
</details>


## 6) Normalize the Data 📈

Create a NumPy array with 20 random floating-point numbers between 0 and 1

Normalize this data so that the new values range between 0 and 100

> *Hint:* The formula for normalization is: $X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}} \times (\text{new-max} - \text{new-min}) + \text{new-min}$

<details><summary>Useful functions</summary>

```py
numpy.random.rand(size)  # Returns an array of random floats in the half-open interval [0.0, 1.0)
```
</details>

<details><summary><b>Solution</b></summary>

```py
arr = np.random.rand(20)

normalized = (arr - arr.min()) / (arr.max() - arr.min()) * (100 - 0) + 0

print("Normalized array:", normalized)
```
</details>


## 7) Broadcasting and Scaling 📊

Create a 4x5 matrix of random integers between 10 and 100

Subtract the column-wise mean from each element in the matrix

<details><summary>Useful functions</summary>

```py
numpy.ndarray.mean(array, axis)  # Returns the mean of the array along the specified axis
```
</details>

<details><summary><b>Solution</b></summary>

```py
matrix = np.random.randint(10, 101, size=(4, 5))

column_means = matrix.mean(axis=0)
standardized = matrix - column_means

print("Column-wise mean subtracted:\n", standardized)
```
</details>


## 8) Matrix Multiplication Challenge 🤯

Create two matrices of size 4x3 and 3x5 with random integers

Perform matrix multiplication on them

<details><summary>Useful functions</summary>

```py
numpy.ndarray.dot(array1, array2)  # Returns the dot product of two arrays
```
</details>

<details><summary><b>Solution</b></summary>

```py
matrix1 = np.random.randint(1, 10, size=(4, 3))
matrix2 = np.random.randint(1, 10, size=(3, 5))

result = np.dot(matrix1, matrix2)

print("Matrix multiplication result:\n", result)
```
</details>


## 9) Find the Peaks 📉

Generate a 1D NumPy array with 20 random integers between 0 and 50

Identify the "peaks" (local maxima) in the array (local maxima)

> *Hint:* compare each element to its neighbors

<details><summary><b>Solution</b></summary>

```py
arr = np.random.randint(0, 51, size=20)

peaks = arr[1:-1][(arr[1:-1] > arr[:-2]) & (arr[1:-1] > arr[2:])]

print("Peaks:", peaks)
```
</details>


## 10) Simulate a Dice Roll 🎲🎲

Simulate rolling two six-sided dice 10,000 times

Count how many times the sum of the two dice equals 7

<details><summary><b>Solution</b></summary>

```py
rolls = np.random.randint(1, 7, size=(10000, 2))

sums = rolls.sum(axis=1)
sevens = np.sum(sums == 7)

print("Number of times the sum is 7:", sevens)
```
</details>
