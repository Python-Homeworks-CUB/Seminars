## LEGB
**Scope** defines the region of code where a variable is accessible.

Example:

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Prints "local"
    inner()

print(x)  # Prints "global"
outer()
```
The **LEGB rule** determines the order Python looks for a variable: **Local**, then **Enclosing** (in nested functions), then **Global** (module-level), and finally **Built-in** (Python’s predefined names).

![image.png](attachment:image.png)
#### Example

Local scope:
```python
# local scope

def f():
    x = 1 # local
    print(x) # here python looks for x variable
f()
```

Enclosing scope:
```python
def f():
    x = 1
    def g():
        # x = 2 # if we uncomment this line, it will print 2
        print(x) # here python looks for x variable
    g()
f()
```

Global scope:
```python
# global scope
x = 1

def f():
    # x = 2 # enclosing scope
    def g():
        # x = 3 # local scope
        print(x)
    g()

f()
```

```py
# x = 4 # what if uncomment this line?

from week12_imports.some_file import x # global scope as well

# x = 5 # what if uncomment this line?
def f():
    # x = 2 # enclosing scope
    def g():
        # x = 3 # local scope
        print(x)
    g()

f()
```

Output:
```
1
```

```py
# built-in scope

print(print) # <built-in function print>
```

Output:
```
<built-in function print>
```


**Time for questions!**
```py
x = "global"

def outer():
    x = "enclosing"

    def inner1():
        print(x)  # What will this print?

    def inner2():
        global x
        x = "modified global"
        print(x)  # What will this print?

    def inner3():
        nonlocal x
        x = "modified enclosing"
        print(x)  # What will this print?

    inner1()
    inner2()
    inner3()

print(x)  # What will this print?
outer()
print(x)  # What will this print?
```

Output:
```
global
enclosing
modified global
modified enclosing
modified global
```

```py
f = 10

def f():
    print(f)

f()
```

Output:
```
<function f at 0x000001E8DC185DA0>
```

```py
import pprint

data = {
    'name': 'John',
    'age': 30,
    'children': [
        {'name': 'Jane', 'age': 10},
        {'name': 'Doe', 'age': 8}
    ]
}

print("pretty print: ")
pprint.pprint(data)
print("normal print: ")
print(data)
```

Output:
```
pretty print:
{'age': 30,
 'children': [{'age': 10, 'name': 'Jane'}, {'age': 8, 'name': 'Doe'}],
 'name': 'John'}
normal print:
{'name': 'John', 'age': 30, 'children': [{'name': 'Jane', 'age': 10}, {'name': 'Doe', 'age': 8}]}
```

```py
from pprint import pprint as print

print(data)  # which one is called?
```

Output:
```
{'age': 30,
 'children': [{'age': 10, 'name': 'Jane'}, {'age': 8, 'name': 'Doe'}],
 'name': 'John'}
```

## Importing modules
**Exercise 1**

```bash
imp_practice
├── main.py
└── utils
    ├── math.py
    └── science.py
```

You're task is to import the required functions in main.py so that it works as expected.
**How python resolves the path to the file?**

```bash
path_practice
├── data.txt
└── print_content.py
```

*Relative path:* Python looks for the file in the current directory. Current directory is the directory from where you run the script.

Example of relative paths:

```python
relative_path1 = "data.txt"
relative_path2 = "./data.txt"
relative_path3 = "../data.txt"
relative_path4 = "path_practice/data.txt"
```

*Absolute path:* Python looks for the file in the specified path.

Example of absolute paths:

```python
absolute_path = "/home/user/data.txt"
absolute_path_win = "C:/Users/user/data.txt"
```

**Bonus part:**

Relative imports: \
In python exists `relative` imports (they start with a dot). You should be careful about them. \
More on the topic: [this](https://stackoverflow.com/questions/55084977/attempted-relative-import-with-no-known-parent-package) and [this](https://stackoverflow.com/questions/16981921/relative-imports-in-python-3)

PYTHONPATH: \
`PYTHONPATH` - a list of directories from in which the Python interpreter should look for modules.

Launching a script as a module: \
`python -m module_name` \
In this case, the behavior of imports will be different. See more on the topic in `Relative imports` section.
## Virtual Environment

1. Basics
    - [ ] Create a virtual environment
    - [ ] Activate a virtual environment
    - [ ] Check `python` and `pip` location
    - [ ] Install a package in a virtual environment
    - [ ] Deactivate a virtual environment
    - [ ] Delete a virtual environment
2. Use cases
    - [ ] Create a virtual environment for a project (my internship reject story)
    - [ ] `requirements.txt` file
3. Virtual environment managers
    - [ ] `venv`
    - [ ] `virtualenv`
    - [ ] `poetry`

## How to write a package
### Python Package

Good [tutorial](https://www.youtube.com/watch?v=5KEObONUkik)

Instruction:
- [ ] Show a package source code
- [ ] Install a `wheel` package
- [ ] Create a `setup.py` file and fill it
- [ ] Install a package from source code (`pip install .`) and run an example
