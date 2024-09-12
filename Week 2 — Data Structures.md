# Warm Up

Write the following functions:
* sum_with_step_k(nums, k)

Description: This function takes a list of integers (nums) and a positive integer (k). It returns the sum of all the integers in the list where the indices of these integers are divisible by k.

Example:
```python
>>> sum_with_step_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
22
```
Explanation: 22 = 1 + 4 + 7 + 10

* max_element(nums)

Description: This function takes a list of integers (nums) and returns the index of the maximum element in the list. \
Note: You can solve this problem using a one-liner with the built-in max function and enumerate function.

Example:
```python
>>> max_element([100, 2, 3, 4, 5, 6, 7, 8, 9, 10])
0
```

* k_multiples(a, b, k)

Description: This function takes two integers a and b and a positive integer k. It returns the list of multiples of k in the range from a to b.

Example:
```python
>>> k_multiples(1, 10, 3)
[3, 6, 9]
```

<details>
    <summary><b>Solution</b></summary>

```py
def sum_with_step_k(nums, k):
    return sum(nums[::k])


def max_element(nums):
    return max(enumerate(nums), key=lambda x: x[1])[0]


def k_multiples(a, b, k):
    return [i for i in range(a, b + 1) if i % k == 0]


print(sum_with_step_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # 22
print(max_element([100, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 0
print(k_multiples(1, 10, 3))  # [3, 6, 9]
```
</details>


# Has duplicates

Write a function named `has_duplicates` that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

Write the function in three different ways:
* using a list
* using a set
* using a dictionary

For example:
```python
>>> has_duplicates([1, 2, 3, 4, 4])
True
```

<details>
    <summary><b>Solution</b></summary>

```py
# Using a list
def has_duplicates_list(lst):
    for el in lst:
        if lst.count(el) > 1:
            return True
    return False


# Using a set
def has_duplicates_set(lst):
    return len(lst) != len(set(lst))


# Using a dictionary
def has_duplicates_dict(lst):
    d = {}
    for el in lst:
        if el in d:
            return True
        d[el] = 1
    return False


print(has_duplicates_list([1, 2, 3, 4, 4]))  # True
print(has_duplicates_set([1, 2, 3, 4, 4]))  # True
print(has_duplicates_dict([1, 2, 3, 4, 4]))  # True
```
</details>


# Cumulative Sum

Write a function called `cumsum` that takes a list of numbers and returns a new list where each element is the cumulative sum of the elements in the original list up to that point.

In other words, the ith element in the new list is the sum of the first i+1 elements from the original list.

Example:
```python
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
```
In this example, the first element is 1, the second element is 1 + 2 = 3, and the third element is 1 + 2 + 3 = 6.

<details>
    <summary><b>Solution</b></summary>

```py
def cumsum(t):
    return [sum(t[:i + 1]) for i in range(len(t))]


def cumsum_efficient(t):
    total = 0
    cumsum_list = []
    for num in t:
        total += num
        cumsum_list.append(total)
    return cumsum_list


t = [1, 2, 3]
print(cumsum(t))  # [1, 3, 6]
```
</details>


# Nested Dictionary

You have a list of transactions where each transaction is a tuple of the form `(customer_id, product, amount_spent)`. Write a function `total_by_client` that takes this list of transactions and returns a nested dictionary where each customer ID maps to another dictionary, which contains products as keys and total amount spent on each product as values.

Example input:
```python
transactions = [
    (1, 'apple', 5),
    (2, 'banana', 3),
    (1, 'banana', 2),
    (1, 'apple', 3),
    (2, 'apple', 4)
]
```

Expected output:
```python
{
    1: {'apple': 8, 'banana': 2},
    2: {'banana': 3, 'apple': 4}
}
```
Hint: You can use setdefault method to create a new dictionary for each customer ID.

<details>
    <summary><b>Solution</b></summary>

```py
def total_by_client(transactions: list) -> dict:
    result = {}
    for client_id, product, amount in transactions:
        result[client_id] = result.setdefault(client_id, {})
        result[client_id][product] = result[client_id].setdefault(product, 0) + amount
    return result


transactions = [
    (1, 'apple', 5),
    (2, 'banana', 3),
    (1, 'banana', 2),
    (1, 'apple', 3),
    (2, 'apple', 4)
]

print(total_by_client(transactions))  # {1: {'apple': 8, 'banana': 2}, 2: {'banana': 3, 'apple': 4}}
```
</details>

<details>
    <summary><b>Solution (using <code>defaultdict</code>)</b></summary>

```py
from collections import defaultdict


def total_by_client(transactions: list) -> dict:
    result = defaultdict(lambda: defaultdict(int))
    for client_id, product, amount in transactions:
        result[client_id][product] += amount
    return result


transactions = [
    (1, 'apple', 5),
    (2, 'banana', 3),
    (1, 'banana', 2),
    (1, 'apple', 3),
    (2, 'apple', 4)
]

print(total_by_client(transactions))  # {1: {'apple': 8, 'banana': 2}, 2: {'banana': 3, 'apple': 4}}
```
</details>


# Inclusion-Exclusion

You are managing a university course system, where students can enroll in multiple courses. You have the following data:
- A set of students enrolled in `Math`
- A set of students enrolled in `Science`
- A set of students enrolled in `Art`

Write a function `optimize_courses` that performs the following tasks using set operations:
1. Find the set of students enrolled in all three courses (Math, Science, and Art).
2. Find the set of students enrolled in exactly two out of the three courses.
3. Find the set of students enrolled in only one course.
4. Return a dictionary summarizing the results for the three tasks above.

Example input:
```python
math = {"Alice", "Bob", "Charlie", "David"}
science = {"Charlie", "David", "Edward", "Fiona"}
art = {"Alice", "David", "Fiona", "George"}
```

Expected output:
```python
{
    "all_three": {"David"},
    "exactly_two": {"Alice", "Charlie", "Fiona"},
    "only_one": {"Bob", "Edward", "George"}
}
```

Hint: Use set operations like union, intersection, and difference (`|`, `&`, `-`).

<details>
    <summary><b>Solution</b></summary>

```py
def optimize_courses(math: set, science: set, art: set) -> dict:
    # Students in all three courses
    all_three = math & science & art

    # Students in exactly two courses
    math_science = math & science
    math_art = math & art
    science_art = science & art
    exactly_two = (math_science | math_art | science_art) - all_three

    # Students in only one course
    only_one = (math | science | art) - (math & science) - (math & art) - (science & art)

    return {
        "all_three": all_three,
        "exactly_two": exactly_two,
        "only_one": only_one
    }


math = {"Alice", "Bob", "Charlie", "David"}
science = {"Charlie", "David", "Edward", "Fiona"}
art = {"Alice", "David", "Fiona", "George"}

print(optimize_courses(math, science, art))  # {'all_three': {'David'}, 'exactly_two': {'Alice', 'Charlie', 'Fiona'}, 'only_one': {'George', 'Edward', 'Bob'}}
```
</details>


# Chop-chop

Write a function called `chop` that takes a list, modifies it by removing the first and last elements. The function should return None.

For example:
```python
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
```

<details>
    <summary><b>Solution</b></summary>

```py
def chop(t):
    del t[0], t[-1]


t = [1, 2, 3, 4]
chop(t)
print(t)  # [2, 3]
```
</details>


# Anagrams

Two words are considered anagrams if you can rearrange the letters from one word to spell the other.

Write a function called `is_anagram` that takes two strings and returns `True` if they are anagrams and `False` otherwise.

For example:
```python
>>> is_anagram("listen", "silent")
True

>>> is_anagram("hello", "world")
False
```

<details>
    <summary><b>Solution</b></summary>

```py
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
```
</details>
