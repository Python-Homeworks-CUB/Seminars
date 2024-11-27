### Plan

**Theory**
* functional vs OOP paradigm
* `args`, `kwargs`
* `map`, `filter`, `zip`, comprehension
* `all`, `any`


# Theory
### `args`, `kwargs`
```py
def foo(pos_arg, *args, keyword_arg, **kwargs):
    print(f"positional argument: {pos_arg}")
    print(f"keyword argument: {keyword_arg}")
    print(f"args: {args}")
    print(f"n args: {len(args)}")
    print(f"kwargs: {kwargs}")

foo(1, 2, 3, 4, keyword_arg=5, key1=6, key2=7)
```

### `map`
```py
def square_one(el):
    return el*el

def square(x):
    res = []
    for el in x:
        res.append(square_one(el))
    return res

x = [1, 2, 3, 4]
print(square(x))
print(list(map(square_one, x)))
print(list(map(lambda el: el*el, x)))
```

### `lambda`
```py
lam_const = lambda: 100
lam_const_ignore = lambda *args, **kwargs: 100
lam_square = lambda x: x*x
lam_sum = lambda *args: sum(args)
lam_with_default = lambda x, y=10: x+y
lam_kwargs_print = lambda **kwargs: print(', '.join(f"{k}={v}" for k, v in kwargs.items()))

print("lambda const", lam_const())
print("lambda const ignore", lam_const_ignore(1, 2, 3, y=4))
print("lambda square", lam_square(5))
print("lambda sum", lam_sum(1, 2, 3, 4))
print("lambda with default", lam_with_default(5))
print("lambda with default", lam_with_default(5, 5))
print("lambda kwargs print", lam_kwargs_print(a=1, b=2, c=3))
```

### `zip`, unpacking
```py
x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd', 'ignored_el', 'ignored_el2']

print("zip")
for el in zip(x, y, x):
    print(el)

for el_x, el_y in zip(x, y):
    print(el_x, el_y)



print("unpacking")
a, b, *rest = x

print(a, b, rest)
```

### `filter`
```py
def is_even(x):
    return x % 2 == 0

def get_even(x):
    res = []
    for el in x:
        if is_even(el):
            res.append(el)
    return res

x = [1, 2, 3, 4, 5, 6]
print(get_even(x))
print(list(filter(is_even, x)))
```

# Tasks
### Statement (Exploring Indices)

Given a string `s` and a start index `n`, write a function that returns a dictionary mapping indices (starting at `n`) to their corresponding characters in `s`.

```bash
>>> string_to_dict("hello", 5)
{5: 'h', 6: 'e', 7: 'l', 8: 'l', 9: 'o'}
```

```py
def string_to_dict_simple(s, n):
    result = {}
    for ch in s:
        result[n] = ch
        n += 1
    return result

def string_to_dict(s, n):
    return {i: ch for i, ch in enumerate(s, n)}


print(string_to_dict_simple('abc', 1))
print(string_to_dict('abc', 1))
```

### Statement (Custom Logical Functions - my_all)

Create a function that checks if all strings in a list are non-empty and contain at least one vowel.

```bash
>>> all_strings_have_vowels(["apple", "banana", ""])
False
>>> all_strings_have_vowels(["apple", "orange", "grape"])
True
```

```py
VOWELS = set('aeiou')

def all_strings_have_vowels_simple(lst):
    for s in lst:
        flag = False
        for ch in s.lower():
            if ch in VOWELS:
                flag = True
                break
        if not flag:
            return False
    return True

def all_strings_have_vowels(lst):
    return all(s and any(ch in VOWELS for ch in s.lower()) for s in lst)


print(all_strings_have_vowels_simple(["apple", "orange", "grape"]))
print(all_strings_have_vowels(["apple", "banana", ""]))
```

### Statement (When I'm bored...)

Implement a `add_one`, `add_three`, and `add_many` functions such that the following code works.

```bash
>>> add_many(1)(2)(3)()
6
>>> add_one(1)()
1
>>> add_many(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)()
55
```

```py
def add_one(a):
    return lambda: a

def add_three(a):
    return lambda b: lambda c: lambda: a + b + c


print(add_one(5)())
print(add_three(1)(2)(3)())
```

```py
from functools import partial

def add_many(*args, prev_sum=0):
    assert len(args) <= 1, 'Only one or zero arguments are allowed'
    if len(args) == 0:
        return prev_sum
    return partial(add_many, prev_sum=prev_sum + args[0])  # same as: lambda *args: add_many(*args, prev_sum=prev_sum + args[0])

print(add_many(3)())
print(add_many(3)(4)(5)())
print(add_many(3)(4)(5)(6)())
print(add_many(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)())
```

### Statement (Chained Functions - compose)

Write a function that takes a list of functions and an initial value, and applies the functions to the value in sequence.

```bash
>>> compose_functions([lambda x: x + 2, lambda x: x * 3], 5)
21
>>> compose_functions([lambda x: x - 1, lambda x: x ** 2], 4)
9
```

```py
def compose_functions_simple(funcs, value):
    result = value
    for f in funcs:
        result = f(result)
    return result

def compose_functions(funcs, value):
    from functools import reduce
    return reduce(lambda acc, f: f(acc), funcs, value)


print(compose_functions_simple([lambda x: x + 2, lambda x: x * 3], 5))
print(compose_functions([lambda x: x - 1, lambda x: x ** 2], 4))
```

### Statement (Add Argument Checker - add_arg_checker)

Write a function `add_arg_checker` that takes a function `foo` and an argument checker function `foo_checker`. It returns a new function `new_foo`. Before calling `foo`, `new_foo` will validate its arguments using `foo_checker`. If the arguments do not pass the check, an exception should be raised.

The argument checker function `foo_checker` takes the same arguments as `foo` and raises a `ValueError` if the arguments are invalid.

```bash
>>> def foo(a, b):
...     return a + b

>>> def foo_checker(a, b):
...     if not isinstance(a, int) or not isinstance(b, int):
...         raise ValueError("Both arguments must be integers.")

>>> new_foo = add_arg_checker(foo, foo_checker)
>>> new_foo(2, 3)
5

>>> new_foo(2, "3")
# Raises ValueError: Both arguments must be integers.
```

```py
def add_arg_checker(func, checker):
    def wrapper(*args, **kwargs):
        checker(*args, **kwargs)  # Validate the arguments
        return func(*args, **kwargs)  # Call the original function
    return wrapper

# Example usage
def foo(a, b):
    return a + b

def foo_checker(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

new_foo = add_arg_checker(foo, foo_checker)

# Valid call
print(new_foo(2, 3))  # Output: 5

# Invalid call
try:
    print(new_foo(2, "3"))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Both arguments must be integers.
```

```py
# note: the thing above is similar to decorators

def add_arg_checker(checker):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            checker(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return outer_wrapper

@add_arg_checker(foo_checker)
def foo(a, b):
    return a + b

# Valid call
print(foo(2, 3))  # Output: 5

# Invalid call
try:
    print(foo(2, "3"))  # Raises ValueError
except ValueError as e:
    print(e)
```
