# Strings
# Palindrome

Write a function `is_palindrome` that checks if the word is palindrome (i.e. reads the same from left to right and right to left). Ignore the letter case.

**Bonus:** \
Rewrite the function using only 1 line

### Solution:
```py
# Option 1:
def is_palindrome_1(word: str) -> bool:
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            return False
    return True

# Option 2 (better, but slower):
def is_palindrome_2(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]

# Option 3 (even better, although even more slower):
def is_palindrome_3(word: str) -> bool:
    return word.lower() == word.lower()[::-1]

# Tests
for func in (is_palindrome_1, is_palindrome_2, is_palindrome_3):
    print(func("Eevee"), func("Charizard"))
```
---

# Simple calculator

Little Johnny has been asked by his teacher to create a simple calculator that processes mathematical equations and prints the results. Unfortunately, Johnny is so lazy that he doesn’t want to read the entire problem statement! Can you help him by writing a program that accepts and processes all input text?

The input text may include:
- Signed numbers
- Spaces anywhere
- Irrelevant text (might appear within the equation)

The calculator should be able to handle the following operations:
- Addition (`+`)
- Subtraction (`-`)

Example input 1:
```txt
Johnny has 10 apples, then he eats 3, plus 5 more come from the store, and finally, he gives -2 to his friend. How many apples does he have now?
```

Example input 2:
```txt
- Two to the power of ten is 1024.
  Two to the power of eleven is 2024.
- Two weeks equals 14 days.
  1000 is a very round number.
  What year was the first "The Legend of Zelda" game released?
```

**Bonus:** \
To get an excellent grade, Johnny must present his answer in a neatly formatted manner. For example:

Output: `-9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1 = -45`

#### Template:
```py
def calc(statement: str) -> str:
    # Write your code here
    pass


print(calc(
    """
    Johnny has 10 apples, then he eats 3, plus 5 more come from the store, and finally, he gives -2 to his friend. How many apples does he have now?
    """
))  # 10 + 3 + 5 - 2 = 16

print(calc(
    """
    - Two to the power of ten is 1024.
      Two to the power of eleven is 2024.
    - Two weeks equals 14 days.
      1000 is a very round number.
      What year was the first "The Legend of Zelda" game released?
    """
))  # -1024 - 2024 + 14 - 1000 = 1986
```

### Solution:
```py
def calc(statement: str) -> str:
    result = []

    current_operation = ''
    current_number = ''

    statement += '#'  # Trick to process the last number in the statement

    for letter in statement:
        # 1) We encounter space -> skip it
        if letter.isspace():
            continue

        # 2) We encounter a digit -> add it to the current number
        if letter.isnumeric():
            current_number += letter

        # 3) We encounter a sign symbol (minus) -> store it for later
        elif letter == '-':
            current_operation = '-'

        # 4) We encounter non-space and non-number symbol, which means that the number sequence has ended
        else:
            if current_number:
                result.append(int(f'{current_operation}{current_number}'))

                current_operation = '+'
                current_number = ''

    return f'{" ".join(map(str, (
        f"{'-' if item < 0 else '+'} {abs(item)}" if index else item
        for index, item in enumerate(result)
    )))} = {sum(result)}'

print(calc(
    """
    Johnny has 10 apples, then he eats 3, plus 5 more come from the store, and finally, he gives -2 to his friend. How many apples does he have now?
    """
))  # 10 + 3 + 5 - 2 = 16

print(calc(
    """
    - Two to the power of ten is 1024.
      Two to the power of eleven is 2024.
    - Two weeks equals 14 days.
      1000 is a very round number.
      What year was the first "The Legend of Zelda" game released?
    """
))  # -1024 - 2024 + 14 - 1000 = 1986
```
---

# No numbers

Get two **digits** from the standard input: left and right bounds.
Print all **digits** in the given range without using `int()` or `float()`

### Solution:
```py
# left, right = input("Enter two digits").split()
left, right = '3', '8'

for i in range(ord(left), ord(right) + 1):
    print(chr(i), end=' ')
```

#### Follow up:

Write a function `my_int()` that converts a string to an integer without using an `int()` or `float()` function (a.k.a. a simple implementation of `int()` function)

### Solution:
```py
def my_int(string: str) -> int:
    result = 0
    for letter in string:
        result *= 10
        result += ord(letter) - ord('0')
    return result

print(my_int('136'))  # 136
```

#### Follow up 2:

The same as before, but the base of the number system can be any number from 2 to 10

##### Tests:

```python
print(my_int('136'))  # 136
print(my_int('136', base=8))    # 94 = 6 + 3 * 8 + 1 * 8^2 = 6 + 24 + 64
print(my_int("01010", base=2))  # 10 = 1 * 2 + 1 * 2^3     = 2 + 8
# print(my_int('136', base=2))  # ValueError
```

### Solution:
```py
def my_int(string: str, base: int = 10) -> int:
    result = 0
    for letter in string:
        result *= base
        if ord(letter) >= ord('0') + base:
            raise ValueError(f"Invalid digit for base {base}: {letter}")
        result += ord(letter) - ord('0')
    return result

print(my_int('136'))  # 136
print(my_int('136', base=8))    # 94 = 6 + 3 * 8 + 1 * 8^2 = 6 + 24 + 64
print(my_int('01010', base=2))  # 10 = 1 * 2 + 1 * 2^3     = 2 + 8
# print(my_int('136', base=2))  # ValueError
```
---

# Math problem?

When solving mathematical problems, unnecessary text is sometimes not crossed out, but enclosed in brackets. This means that it does not need to be read. However, we don't want to accidentally skip reading variables and small expressions, so we'll assume that anything with length <= 5 is easy to read anyway and should not be skipped.

Write a function `clean_solution` that will remove everything inside the brackets that has length > 5 and the brackets themselves, returning the cleaned text (brackets can be nested)

<!-- This problem can be solved using either simple loops and string manipulation, or **regular expressions** (can't be easily) -->

Example input:
```txt
To calculate the total work done (W) by a variable force (F), use the integral formula W=∫_a^b F(x) dx.
(
Here, F(x) is the force as a function of position x.
The integral is computed from x=a to x=b (In this case, a and b are the initial and final positions, respectively)
)
```

### Template:
```py
def clean_solution(text: str) -> str:
    # Write your code here
    pass

print(clean_solution(
    '''
    To calculate the total work done (W) by a variable force (F), use the integral formula W=∫_a^b F(x) dx.
    (
    Here, F(x) is the force as a function of position x.
    The integral is computed from x=a to x=b (In this case, a and b are the initial and final positions, respectively)
    )
    '''
.strip()))  # To calculate the total work done (W) by a variable force (F), use the integral formula W=∫_a^b F(x) dx.
```

### Solution:
```py
def clean_solution(text: str) -> str:
    opened_pos = 0
    depth = 0
    for current_pos, char in enumerate(text):
        if char == '(':
            if depth == 0:
                opened_pos = current_pos
            depth += 1
        elif char == ')':
            depth -= 1
            if depth == 0 and current_pos - opened_pos > 5:
                text = text[:opened_pos] + text[current_pos + 1:]
    return text

print(clean_solution(
    '''
    To calculate the total work done (W) by a variable force (F), use the integral formula W=∫_a^b F(x) dx.
    (
    Here, F(x) is the force as a function of position x.
    The integral is computed from x=a to x=b (In this case, a and b are the initial and final positions, respectively)
    )
    '''
.strip()))  # To calculate the total work done (W) by a variable force (F), use the integral formula W=∫_a^b F(x) dx.
```
---

# Automating emails

You are developing an automated system that will monitor incoming emails and read them out loud.

Using regular expressions, extract the following information:

- Sender name
- Sender email
- Sender domain
- Recipient name
- Email subject (without the "Re:")
- Email body

Example input:
```txt
From: Elon Musk `elon@tesla.com`
To: Constructor University
Subject: re: re: re: ready for More Rockets? 🚀🚀🚀
Body:
    Just letting you know, the House Party Protocol is now in the final stages of preparation 🥳
```

### Template:
```py
import re

email = '''
From: Elon Musk `elon@tesla.com`
To: Constructor University
Subject: re: re: re: ready for More Rockets? 🚀🚀🚀
Body:
    Just letting you know, the House Party Protocol is now in the final stages of preparation 🥳
'''

# Regular expressions for extracting the information
sender_pattern = ???
recipient_name_pattern = ???
subject_pattern = ???
body_pattern = ???

# Extracting information
sender_name, sender_email, sender_domain = ???
recipient_name = ???
subject = ???
body = ???

# Output the extracted information
print("Sender Name:", sender_name)
print("Sender Email:", sender_email)
print("Sender Domain:", sender_domain)
print("Recipient Name:", recipient_name)
print("Email Subject:", subject)
print("Email Body:", body)
```

### Solution:
```py
import re

email = '''
From: Elon Musk `elon@tesla.com`
To: Constructor University
Subject: re: re: re: ready for More Rockets? 🚀🚀🚀
Body:
    Just letting you know, the House Party Protocol is now in the final stages of preparation 🥳
'''

# Regular expressions for extracting the information
sender_pattern = r'From:\s*(.*)\s*`([^`@]+@([^`]+))`'
recipient_name_pattern = r'To:\s*(.*)'
subject_pattern = r'Subject:\s*(?:[Rr]e:\s*)*(.*)'
body_pattern = r'Body:\s*(.*)'

# Extracting information
sender_name, sender_email, sender_domain = re.search(sender_pattern, email).groups()
recipient_name = re.search(recipient_name_pattern, email).group(1)
subject = re.search(subject_pattern, email).group(1)
body = re.search(body_pattern, email).group(1).strip()

# Output the extracted information
print("Sender Name:", sender_name)
print("Sender Email:", sender_email)
print("Sender Domain:", sender_domain)
print("Recipient Name:", recipient_name)
print("Email Subject:", subject)
print("Email Body:", body)
```
