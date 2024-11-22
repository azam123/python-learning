# python-learning

### **Data Types:**
- **Integer**: Whole numbers.
# Integer: Whole numbers.
integer_val = 42

- **Float**: Numbers with decimals.
# Float: Numbers with decimals.
float_val = 3.14

- **Complex**: Numbers with a real and imaginary part.
# Complex: Numbers with a real and imaginary part.
complex_val = 2 + 3j

- **String**: Sequence of characters.
# String: Sequence of characters.
string_val = "Hello, World!"

- **Boolean**: Logical values (True or False).
# Boolean: Logical values (True or False).
boolean_val = True

- **List**: Ordered and mutable collection.
# List: Ordered and mutable collection.
list_val = [1, 2, 3, 4]

- **Tuple**: Ordered but immutable collection.
# Tuple: Ordered but immutable collection.
tuple_val = (1, 2, 3, 4)

- **Set**: Unordered collection of unique elements.
# Set: Unordered collection of unique elements.
set_val = {1, 2, 3, 4}

- **Dictionary**: Key-value pairs.
# Dictionary: Key-value pairs.
dict_val = {"key1": "value1", "key2": "value2"}

- **None**: Represents the absence of a value.
# None: Represents the absence of a value.
none_val = None

- **Bytes**: Immutable sequence of bytes.
# Bytes: Immutable sequence of bytes.
bytes_val = b"Hello"

- **Bytearray**: Mutable sequence of bytes.
# Bytearray: Mutable sequence of bytes.
bytearray_val = bytearray(b"Hello")

- **Range**: Represents a sequence of numbers.
# Range: Represents a sequence of numbers.
range_val = range(1, 10)

- **Frozenset**: Immutable version of a set.
# Frozenset: Immutable version of a set.
frozenset_val = frozenset([1, 2, 3, 4])

 
**Examples here :** https://github.com/azam123/python-learning/blob/main/data_types.py
---

### **Conditional Statements:**

- **if**: Executes a block of code if the condition is True.
- **if-else**: Executes one block if the condition is True and another if it’s False.
- **if-elif-else**: Handles multiple conditions.
- **Nested if**: Checks conditions within another condition.
- **Logical operators (and, or)**: Combine multiple conditions.
- **Shorthand if**: Allows concise conditional expressions.
- **pass**: Placeholder when no action is required.
- 
**Examples here :** https://github.com/azam123/python-learning/blob/main/conditional_statements.py

---

### **Loops:**

- **For Loop (List Iteration)**: Iterates over each item in the list and performs an action.
- **For Loop (Range)**: Uses `range(1, 6)` to generate numbers from 1 to 5, iterating through each to perform an action.
- **While Loop**: Executes as long as the condition (e.g., `counter <= 5`) is True.
- **Nested Loops**: An outer loop that runs multiple times, and for each iteration, an inner loop runs, like printing a multiplication table.
- **Break Statement**: Exits the loop when a condition is met (e.g., `i == 6`).
- **Continue Statement**: Skips the current iteration and moves to the next when a condition is met (e.g., `i == 3`).

**Examples here :**https://github.com/azam123/python-learning/blob/main/loops.py
---

### **Functions in Python:**

- **Simple Function (No Arguments, No Return Value)**: 
  ```python
  def greet():
      print("Hello!")
  ```

- **Function with Arguments (No Return Value)**: 
  ```python
  def greet_person(name):
      print(f"Hello, {name}!")
  ```

- **Function with Return Value (No Arguments)**: 
  ```python
  def get_favorite_number():
      return 7
  ```

- **Function with Arguments and Return Value**: 
  ```python
  def add_numbers(a, b):
      return a + b
  ```

- **Function with Default Arguments**: 
  ```python
  def greet_person_with_default(name="Guest"):
      print(f"Hello, {name}!")
  ```

- **Function with Variable Number of Arguments (Using *args)**: 
  ```python
  def print_numbers(*args):
      print(args)
  ```

- **Function with Keyword Arguments (Using **kwargs)**: 
  ```python
  def print_info(**kwargs):
      print(kwargs)
  ```

- **Lambda Function (Anonymous Function)**: 
  ```python
  multiply = lambda x, y: x * y
  ```
  
**Examples here :**https://github.com/azam123/python-learning/blob/main/functions.py
---

### **Classes and Objects:**

- **Class Definition**: 
  ```python
  class Car:
      def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year

      def display_info(self):
          print(f"{self.year} {self.make} {self.model}")

      def start_engine(self):
          print("Engine started")

      def stop_engine(self):
          print("Engine stopped")
  ```

- **Creating Objects**:
  ```python
  car1 = Car("Toyota", "Corolla", 2020)
  car2 = Car("Honda", "Civic", 2022)
  ```

- **Accessing Methods and Attributes**:
  ```python
  car1.display_info()  # Outputs: 2020 Toyota Corolla
  car1.start_engine()  # Outputs: Engine started
  ```
  **Examples here : **https://github.com/azam123/python-learning/blob/main/classes_objects.py


  # Understanding Modules in Python

In Python, a **module** is simply a file that contains Python definitions and statements. It allows us to organize code logically, group related functions, classes, and variables, and make our code more modular and reusable. Using modules, you can break down complex programs into smaller, manageable parts. Python has a rich ecosystem of built-in modules, and you can also create your own.

### **Why Use Modules?**

- **Code Organization**: Instead of writing all the code in a single file, you can separate it into different modules. This makes the code more readable and manageable.
- **Reusability**: Once a module is created, you can reuse it in multiple programs.
- **Namespace Management**: Modules help avoid naming conflicts by keeping the variables and functions in separate namespaces.

### **How to Create and Use a Module in Python?**

To create a module, simply create a Python file (`.py`) containing functions, variables, and classes. Then, use the `import` statement to use the module in other Python files.

### **Creating a Simple Module**

Let's create a simple Python module called `math_operations.py`. This module will contain a few basic mathematical functions.

1. **Create a new Python file `math_operations.py`**:

```python
# math_operations.py

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
```

### **Using the Module in Another Program**

Once you have created the `math_operations.py` module, you can import and use it in another Python script.

2. **Create a new Python file `main.py`** where you'll use the `math_operations` module.

```python
# main.py

# Importing the entire module
import math_operations

# Using functions from the module
print("Addition: ", math_operations.add(10, 5))  # Output: Addition: 15
print("Subtraction: ", math_operations.subtract(10, 5))  # Output: Subtraction: 5
print("Multiplication: ", math_operations.multiply(10, 5))  # Output: Multiplication: 50
print("Division: ", math_operations.divide(10, 5))  # Output: Division: 2.0
```

### **Importing Specific Functions from a Module**

Instead of importing the entire module, you can import specific functions. This can make your code more concise.

3. **Modify `main.py` to import specific functions**:

```python
# main.py

# Importing specific functions from the module
from math_operations import add, subtract

# Using the imported functions
print("Addition: ", add(10, 5))  # Output: Addition: 15
print("Subtraction: ", subtract(10, 5))  # Output: Subtraction: 5
```

### **Renaming a Module on Import**

You can also rename a module when importing it to avoid conflicts or simply for convenience.

4. **Modify `main.py` to import the module with a different name**:

```python
# main.py

# Importing the module with an alias
import math_operations as mo

# Using the module with the alias
print("Addition: ", mo.add(10, 5))  # Output: Addition: 15
print("Multiplication: ", mo.multiply(10, 5))  # Output: Multiplication: 50
```

### **The `__name__` Special Variable**

In Python, each module has a special built-in variable called `__name__`. This variable is set to `"__main__"` when the module is run directly, but if it is imported into another module, it is set to the name of the module.

This can be useful to write code that only runs when the module is executed directly and not when it is imported.

5. **Example of `__name__`** in the `math_operations.py`:

```python
# math_operations.py

def add(a, b):
    return a + b

# Check if this module is being run directly or imported
if __name__ == "__main__":
    print("This module is being run directly!")
else:
    print("This module has been imported!")
```

When you run `math_operations.py` directly, it will print `"This module is being run directly!"`. However, if you import it in another file, it will print `"This module has been imported!"`.

### **Built-in Modules in Python**

Python comes with many built-in modules that provide functionality for handling files, date/time, mathematics, and more. For example, the `math` module provides mathematical functions, and the `datetime` module helps with date and time operations.

Example of using the `math` module:

```python
# Using the math module
import math

print("Square root of 16: ", math.sqrt(16))  # Output: Square root of 16: 4.0
print("Value of pi: ", math.pi)  # Output: Value of pi: 3.141592653589793
```

