# Classes/instances and methods/attributes

Classes are like blueprints for objects. They define the structure (attributes) and behavior (methods) that objects created from them will have. Objects are instances of classes, meaning each one has its own unique data, but they all follow the same blueprint.

- **Class**: A blueprint that defines attributes (data) and methods (functions).
- **Instance**: A unique object created from a class.
- **Attributes**: Data stored in an instance or class.
- **Methods**: Functions defined inside a class that operate on instances.

```py
# Define a class "Car" (blueprint for car objects)
class Car:
    # Constructor method, initializes attributes (data)
    def __init__(self, brand, color):
        self.brand = brand  # instance attribute
        self.color = color  # instance attribute

    # Method that describes the car
    def describe(self):
        return f"This car is a {self.color} {self.brand}."

# Create an instance (object) of Car
my_car = Car(brand="Toyota", color="red")

# Accessing attributes and methods of the instance
print(my_car.describe())  # Calls the method 'describe' for 'my_car'
print(my_car.brand)       # Access the attribute 'brand' of 'my_car'
```

```
This car is a red Toyota.
Toyota
```

```py
# Create another instance of Car
another_car = Car(brand="Honda", color="blue")

# Each instance has its own data
print(another_car.describe())  # "This car is a blue Honda."
```

```
This car is a blue Honda.
```

# Class Attributes

Classes can also have **class attributes**. These belong to the class itself and are _shared among all instances_ of that class.

- **Instance attributes**: Unique to each object (defined in `__init__`).
- **Class attributes**: Shared by all instances (defined directly inside the class, outside `__init__`).

```py
# Define a class "Car" with a class attribute
class Car:
    # Class attribute (shared by all instances)
    wheels = 4

    # Constructor method (instance attributes)
    def __init__(self, brand, color):
        self.brand = brand   # instance attribute
        self.color = color   # instance attribute

    # Method to describe the car
    def describe(self):
        return f"A {self.color} {self.brand} with {Car.wheels} wheels."

# Create two instances of Car
car1 = Car(brand="Toyota", color="red")
car2 = Car(brand="Honda", color="blue")

# Accessing class attribute and instance methods
print(car1.describe())  # "A red Toyota with 4 wheels."
print(car2.describe())  # "A blue Honda with 4 wheels."

# Class attributes are shared by all instances
print(car1.wheels)  # 4
print(car2.wheels)  # 4
```

```
A red Toyota with 4 wheels.
A blue Honda with 4 wheels.
4
4
```

```py
# Change the class attribute 'wheels' for all instances
Car.wheels = 6

# Both instances now reflect the change
print(car1.wheels)  # "A red Toyota with 6 wheels."
print(car2.wheels)  # "A blue Honda with 6 wheels."

# Modifying only an instance's attribute does not affect others
car1.wheels = 8  # This only changes for 'car1'
print(car1.wheels)  # 8
print(car2.wheels)  # 6 (unchanged for car2)
```

```
6
6
8
6
```

# Properties (Getters and Setters)

In Python, properties provide a way to control access to an attribute. With properties, you can define methods to get or set values (called **getters** and **setters**) while keeping the syntax of simple attribute access.

- **Getter**: A method that gets the value of an attribute.
- **Setter**: A method that sets the value of an attribute.

This allows for validation or custom behavior when accessing or updating an attribute, without changing how it's accessed.

```py
# Define a class with a private attribute and property methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected attribute (conventionally starts with _)

    # Getter method to access the age attribute
    @property
    def age(self):
        return self._age

    # Setter method to set the age attribute with validation
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Create an instance of Person
person = Person(name="Alice", age=30)

# Accessing the 'age' attribute using the getter
print(person.age)  # 30

# Modifying the 'age' attribute using the setter
person.age = 35
print(person.age)  # 35
```

```
30
35
```

```py
# Trying to set an invalid value using the setter
try:
    person.age = -5  # This will raise a ValueError
except ValueError as e:
    print(e)  # "Age cannot be negative"
```

```
Age cannot be negative
```

### Why use properties?

- You can keep the same syntax for accessing attributes (like `person.age`).
- Add validation or logic to attribute access without changing how it is used.
- Helps maintain control over how values are stored or changed.

# Inheritance

Inheritance allows one class to inherit attributes and methods from another class. This helps reuse code and makes it easier to create specialized versions of a class.

- **Parent class** (or base class): The class that is inherited from.
- **Child class** (or derived class): The class that inherits from the parent class. It can extend or override the behavior of the parent class.

Inheritance creates an "is-a" relationship. For example, if a `Dog` class inherits from an `Animal` class, a dog _is a_ type of animal.

### Motivation for Inheritance

- **Reuse code**: Avoid duplicating code by inheriting from a base class.
- **Organize code**: Group related classes under a common parent, making it easier to manage and extend.
- **Extend functionality**: Child classes can add or override methods from the parent class, making it easy to create specialized versions.
- **Maintainability**: Changes in the parent class are automatically reflected in the child classes, making code easier to maintain.

```py
# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another child class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Create instances of Dog and Cat
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

# Using inherited methods
print(dog.speak())  # "Buddy barks"
print(cat.speak())  # "Whiskers meows"
```

```
Buddy barks.
Whiskers meows.
```

### Inheritance from Python Built-ins

You can also inherit from Python's built-in classes, like `list`, `dict`, or `object`, to create custom versions of them, while keeping their original functionality.

For example, you can extend the functionality of a list by creating a new class that inherits from `list`.

```py
# Inheriting from Python's built-in list
class CustomList(list):
    # Method to sum all elements in the list
    def sum(self):
        return sum(self)

# Create an instance of CustomList
my_list = CustomList([1, 2, 3, 4])

# Use methods from the built-in list class
my_list.append(5)
print(my_list)  # [1, 2, 3, 4, 5]

# Use the new 'sum' method
print(my_list.sum())  # 15
```

```
[1, 2, 3, 4, 5]
15
```

# Magic Methods (Dunder Methods)

Magic methods (also called **dunder** methods because they start and end with double underscores, `__`) allow you to define how objects of a class behave with Python's built-in operations (like addition, string representation, comparisons, etc.).

- `__init__`: Initializes an object (called when an instance is created).
- `__str__`: Defines how the object is represented as a string.
- **Operation methods**: Like `__add__` (for `+`), `__sub__` (for `-`), `__mul__` (for `*`), and `__truediv__` (for `/`).
- **Comparison methods**: Like `__eq__` (for `==`), `__lt__` (for `<`), and `__gt__` (for `>`).
- `__float__` (bonus): Converts an object to a float.

You can read more online (e.g. at [RealPython](https://realpython.com/python-magic-methods/))

```py
# Example class using magic methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic method for string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Magic method for addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Magic method for equality comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Float: distance from origin
    def __float__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Create two points
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using magic methods
print(p1)             # Calls __str__: "Point(1, 2)"
print(p1 + p2)        # Calls __add__: "Point(4, 6)"
print(p1 == p2)       # Calls __eq__: False
print("Distance from (0, 0):", float(p1))  # Calls __float__: 2.236
```

```
Point(1, 2)
Point(4, 6)
False
Distance from (0, 0): 2.23606797749979
```

# Dataclasses

`dataclass` is a "special" class that simplifies class creation for storing data. It automatically generates methods like `__init__`, `__repr__`, and comparison methods, making your code cleaner and less repetitive.

- **Default values**: You can set default values for attributes.
- **Order**: By using `order=True`, you can automatically generate comparison methods (`<`, `>`, etc.).
- **post_init**: A special method (`__post_init__`) that is run after the `__init__` method, useful for additional initialization logic.

```py
from dataclasses import dataclass, field

# Using dataclass with default values and ordering
@dataclass(order=True)
class Person:
    name: str
    age: int = 0   # Default value for age
    height: float = field(default=1.75)  # Using 'field' for default value
    subjects: list = field(default_factory=list) # Use a factory function since list is mutable

    # post-init method for additional logic
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# Create instances of Person
p1 = Person(name="Alice", age=30, height=1.7, subjects=["Math", "Science"])
p2 = Person(name="Bob", age=25, height=1.8, subjects=["History"])

# Using generated methods
print(p1)            # "Person(name='Alice', age=30, height=1.75)"
print(p1 > p2)       # Calls __lt__: False (because "Alice" < "Bob")
```

```
Person(name='Alice', age=30, height=1.7, subjects=['Math', 'Science'])
False
```

### Comparison Methods

```py
from dataclasses import dataclass, field

# Example 1: Using dataclass with 'order=True' to compare by 'x' and 'y' (ignoring 'name')
@dataclass(order=True)
class Point:
    # The fields used for comparison will be considered in the order they are declared
    name: str = field(compare=False)  # 'name' is not used for comparison
    x: int
    y: int
    price: float = field(default=0.0, compare=False)


# Create two points
p1 = Point(name="A", x=1, y=5)
p2 = Point(name="B", x=2, y=3)

# Comparing points
print(p1 < p2)  # True, compares (1, 5) with (2, 3)
print(p1 > p2)  # False
```

```
True
False
```

```py
# Example 2: Manually implementing __lt__ for custom comparison logic
@dataclass
class PointManual:
    name: str
    x: int
    y: int
    price: float = 0.0

    # Custom __lt__ method for comparison (ignoring 'name')
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


# Create two points
p1 = PointManual(name="A", x=1, y=5)
p2 = PointManual(name="B", x=2, y=3)

# Comparing points using custom __lt__
print(p1 < p2)  # True, compares (1, 5) with (2, 3)
print(p1 > p2)  # False
```

```
True
False
```
