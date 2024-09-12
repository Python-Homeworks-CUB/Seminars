# Not an obstacle

John wants to calculate the average time he needs to run $x$ km. If he is tired, he runs 2 times slower than usual. The average speed of John is 5 km/h. The distance is $x$ km. Help John to calculate the average time he needs to run $x$ km.

Write a function `average_time(x, is_tired)` that returns the average time in hours.

```py
>>> average_time(10, is_tired=False)
2.0
>>> average_time(10, is_tired=True)
4.0
```

<details>
    <summary><b>Solution</b></summary>

```py
def average_time(x: int, is_tired: int) -> float:
    speed = 5
    if is_tired:
        speed /= 2
    return x / speed


print(average_time(10, is_tired=False))  # 2.0
print(average_time(10, is_tired=True))  # 4.0
```
</details>


# Leap year

Write a function `is_leap(year)` that returns `True` if the year is a leap year and `False` otherwise.

```py
>>> is_leap(2020)
True
>>> is_leap(2021)
False
```

<details>
    <summary><b>Solution</b></summary>

```py
def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap(2020))  # True
print(is_leap(2021))  # False
```
</details>


# Cake for everyone

At the Bioinformatics Institute, a competition is being organized between computer scientists and biologists. The winners of the competition will receive a large and delicious pie. In the biologists' team, there are $a$ people, and in the computer scientists' team, there are $b$ people.

The pie needs to be pre-cut in such a way that it can be distributed to either team, depending on which one wins the competition, with each team member receiving an equal number of pie pieces. Since we don't want to cut the pie into too many tiny pieces, we need to find the minimum suitable number of pieces.

Write a function `cake(a, b)` that returns the minimum number of pieces needed to pre-cut the pie.

***Hint:*** use the while loop

```py
>>> cake(5, 5)
5
>>> cake(5, 3)
15
>>> cake(12, 8)
24
```

<details>
    <summary><b>Solution</b></summary>

```py
def cake(a: int, b: int) -> int:
    pieces = a
    while pieces % b != 0:
        pieces += a
    return pieces


print(cake(5, 5))  # 5
print(cake(5, 3))  # 15
print(cake(12, 8))  # 24
```
</details>

<details>
    <summary><b>Solution (using the <code>math</code> module)</b></summary>

```py
from math import lcm


def cake(a: int, b: int) -> int:
    return lcm(a, b)


print(cake(5, 5))  # 5
print(cake(5, 3))  # 15
print(cake(12, 8))  # 24
```
</details>


# Eval

Write a function `calc(expr)` that returns the result of the expression `expr`.

***Hint:*** use the built-in `eval` function

```py
>>> calc('2 + 2')
4
>>> calc('2 * 2')
4
>>> calc('2 ** 3')
8
```

<details>
    <summary><b>Solution</b></summary>

```py
def calc(expr: str) -> int:
    return eval(expr)


print(calc('2 + 2'))  # 4
print(calc('2 * 2'))  # 4
print(calc('2 ** 3'))  # 8
```
</details>
