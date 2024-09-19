# A bit of school geometry

Write a class named `Circle` with attributes `center` and `radius`. The `center` should be an instance of `Point` and `radius` should be a number.

Also, write a method named `point_in_circle` that takes a `Point` as an argument and returns True if the `Point` lies in or on the boundary of the circle.

<details>
    <summary><b>Solution</b></summary>

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def point_in_circle(self, point):
        return (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 <= self.radius ** 2
```
</details>


# UserList

Create a class named `UserList` that functions similarly to a Python list.

The class should include the following features:

* The class should be initialized with a list of elements or, by default, an empty list.
* The class should have an attribute named `size` (with an alias `len`) that returns the length of the list.
* The class should have a read-write attribute named `first` that returns the first element of the list.

Hint: Use `property` to create the `first` attribute.

### Example

```python
>>> u = UserList([1, 2, 3, 4])
>>> u.first
1
>>> u.size
4
>>> u.len
4
>>> u.first = 5
>>> u.first
5
>>> u
[5, 2, 3, 4]
```

<details>
    <summary><b>Solution</b></summary>

```py
class UserList(list):
    def __init__(self, data=None):
        self.data = data if data is not None else []

    @property
    def size(self):
        return len(self.data)

    len = size

    @property
    def first(self):
        return self.data[0] if self.data else None

    @first.setter
    def first(self, value):
        if self.data:
            self.data[0] = value
        else:
            self.data.append(value)
```
</details>


# Dataclasses

Create a dataclass named `Student` with the following specifications:

* **Attributes**:
  * `name`: str
  * `age`: int
  * `grades`: List[float] (by default an empty list)
  * `average_grade`: float

* **Methods**:
  * `add_grade`: method that takes a grade, appends it to the grades list and updates the average_grade.
  * `__str__`: method that returns a string representation of the object in the following format: `Student(name='John', age=20, grades=[5.0, 4.0], average_grade=4.5)`.

* **Notes**:
  * The `average_grade` attribute should be computed as the average of the grades. If no grades are provided, the average should be 0.0.
  * The class should be ordered by the `average_grade` in descending order. If two students have the same average grade, they should be ordered by name in ascending order.

* **Hints**:
  * Use the `field` method and `default_factory` to set the default value of the `grades` attribute.
  * Use the `__post_init__` method to compute the average grade and `field(init=False)` to make the attribute initialization after the object creation.
  * Use the `order` parameter of the `dataclass` decorator and `compare` parameter of the `field` method.

<details>
    <summary><b>Solution</b></summary>

```py
from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class Student:
    name: str = field(compare=False)
    age: int = field(compare=False)
    grades: List[float] = field(default_factory=list, compare=False)
    average_grade: float = field(init=False, compare=True)

    def __post_init__(self):
        self.average_grade = sum(self.grades) / len(self.grades) if self.grades else 0.0

    def add_grade(self, grade):
        self.grades.append(grade)
        self.average_grade = sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}, grades={self.grades}, average_grade={self.average_grade})"
```
</details>


<details>
    <summary><b>Solution (custom order method: <code>__lt__()</code>)</b></summary>

```py
from dataclasses import dataclass, field
from typing import List

@dataclass(order=False)
class Student:
    name: str = field(compare=False)
    age: int = field(compare=False)
    grades: List[float] = field(default_factory=list, compare=False)
    average_grade: float = field(init=False, compare=True)

    def __post_init__(self):
        self.average_grade = sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __lt__(self, other):
        # compare students based on their average_grade, name
        return self.average_grade > other.average_grade or (self.average_grade == other.average_grade and self.name < other.name)

    def add_grade(self, grade):
        self.grades.append(grade)
        self.average_grade = sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}, grades={self.grades}, average_grade={self.average_grade})"


students = [
    Student("John", 20, [90, 80, 85]),
    Student("Jane", 19, [70, 75, 80]),
    Student("Dave", 22, [90, 95, 100]),
    Student("Diane", 21, [80, 85, 90]),
    Student("Mike", 19, [95, 100, 100]),
]
students.sort()
students
```
</details>


# A nasty bug

The following code is an implementation of a Kangaroo class. However, it contains a bug. Your task is to identify and fix the bug.

```python
class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)
```

Hint: Consider the mutability of lists.
```python
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
# print(roo)
```

<details>
    <summary><b>Solution</b></summary>

```py
# The bug in the code arises from the mutability of lists in Python.
# The `contents` parameter of the `__init__` method has a default value of an empty list.
# This list is shared among all instances of the class, leading to unexpected behavior.

# Here's the fixed version of the code:

class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents if contents is not None else []

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)

# Now, each instance of Kangaroo has its own list for `pouch_contents`,
# which prevents the side effects observed in the previous version.
```
</details>
