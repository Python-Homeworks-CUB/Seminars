## Try-else-finally

Write `read_file` function that performs the following:

* Tries to open and read a file.
* If successful, counts the number of words in the file.
* Always ensures the file is closed using a `finally` block.
* If the file does not exist, raise and handle an appropriate exception.

### Example

```python
>>> read_file("test.txt")
The file contains 120 words.
>>> read_file("nonexistent.txt")
Error: File does not exist.
```

### Solution
```py
def read_file(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("Error: File does not exist.")
    else:
        content = file.read()
        words = content.split()
        print(f"The file contains {len(words)} words.")
    finally:
        try:
            file.close()
        except UnboundLocalError:
            # finally is always executed, even if file is not opened
            pass
```

---

## Custom Exception

Create a custom exception named `NegativeValueError` that is raised when a negative number is passed to a function. Write a function that calculates the square root of a number but raises this custom exception for negative inputs.

### Example

```python
>>> sqrt(25)
5.0
>>> sqrt(-4)
NegativeValueError: Cannot take the square root of a negative number.
```

### Solution
```py
class NegativeValueError(Exception):
    pass

def sqrt(value):
    if value < 0:
        raise NegativeValueError("Cannot take the square root of a negative number.")
    return value ** 0.5

# Example usage
try:
    print(sqrt(25))
    print(sqrt(-4))
except NegativeValueError as e:
    print(e)
```

---

## Chained Exception Handling
`raise from`

Write a function that performs division between two numbers, handling division by zero with a custom exception called `InvalidDivisionError`. If a `ZeroDivisionError` occurs, it should raise `InvalidDivisionError`, using `raise from` to chain the exceptions.

### Example

```python
>>> divide(10, 2)
5.0
>>> divide(10, 0)
InvalidDivisionError: Cannot divide by zero (caused by ZeroDivisionError).
```

### Solution
```py
class InvalidDivisionError(Exception):
    pass

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        raise InvalidDivisionError("Cannot divide by zero") from e
    return result

# Example usage
try:
    print(divide(10, 2))
    print(divide(10, 0))
except InvalidDivisionError as e:
    print(f"{e} (caused by {e.__cause__.__class__.__name__}).")
```

---

## Custom Exception Logging
`sys.exc_info` `traceback.format_exception_only` `exc.with_traceback`

Create a function that performs a division of two numbers. If a `ZeroDivisionError` occurs, log the exception details using `sys.exc_info` and `traceback.format_exception_only`. Then, raise a new custom exception called `InvalidDivisionError` and attach the original traceback using `exc.with_traceback`.

* Log the original exception without stopping the program.
* When re-raising the custom exception, ensure that the original traceback is preserved.

### Example

```python
>>> divide_and_log(10, 2)
Result: 5.0
>>> divide_and_log(10, 0)
Logging error: Cannot divide by zero (ZeroDivisionError)
Traceback (most recent call last):
  ...
InvalidDivisionError: Division failed, invalid operation
```

### Solution
```py
import sys
import traceback

class InvalidDivisionError(Exception):
    pass

def divide_and_log(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        error_message = "".join(traceback.format_exception_only(exc_type, exc_value))
        print(f"Logging error: {error_message.strip()} ({exc_type.__name__})")

        # Raising custom exception with original traceback
        raise InvalidDivisionError("Division failed, invalid operation").with_traceback(exc_tb)
    else:
        print(f"Result: {result}")

# Example usage
try:
    divide_and_log(10, 2)
    divide_and_log(10, 0)
except InvalidDivisionError as e:
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb)  # Prints full traceback from the original ZeroDivisionError
    print(e)
```

---

## Persistent File Reader

Create a context manager named `FileHandler` that reads the content of a file and keeps the content available after the `with` block ends.

* The file should be opened inside the context manager and automatically closed at the end.
* After the `with` block, the file content should be stored in the `FileHandler` object, accessible via the `content` attribute.

### Example

```python
>>> handler = FileHandler("example.txt")
>>> with handler as f:
...     content = f.read()
File is now open.
File is now closed.

>>> print(handler.content)
This is a sample file content.
```

### Solution
```py
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.content = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        print("File is now open.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.content = self.file.read()  # Store content for later use
            self.file.close()
        print("File is now closed.")
```

---

## Custom Exception Handler

Create a context manager class named `CustomExceptionHandler`. It should:

* Accept two arguments:
  * `exceptions`: A list of exception types to handle (e.g., `ValueError`, `TypeError`).
  * `suppress_mode`: A boolean flag (`True` by default) that determines whether to suppress the exception or rethrow it.
* During the context:
  * If an exception occurs and is in the list of `exceptions`, print the exception name.
  * Suppress or rethrow based on the value of `suppress_mode`.
  * If an exception not in the list occurs, do nothing.

### Example

```python
>>> with CustomExceptionHandler([ValueError], suppress_mode=True):
...     x = int("not_a_number")
Caught ValueError: invalid literal for int() with base 10: 'not_a_number'

>>> with CustomExceptionHandler([ZeroDivisionError], suppress_mode=False):
...     1 / 0
Caught ZeroDivisionError: division by zero
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
```

### Solution
```py
class CustomExceptionHandler:
    def __init__(self, exceptions, suppress_mode=True):
        self.exceptions = exceptions
        self.suppress_mode = suppress_mode

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.exceptions:
            print(f"Caught {exc_type.__name__}: {exc_value}")
            return self.suppress_mode  # Suppress if `suppress_mode` is True, otherwise rethrow
        return False  # Do nothing for other exceptions
```
