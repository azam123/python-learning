# python-learning

### **Data Types:**

- **Integer**: Whole numbers.
- **Float**: Numbers with decimals.
- **Complex**: Numbers with a real and imaginary part.
- **String**: Sequence of characters.
- **Boolean**: Logical values (True or False).
- **List**: Ordered and mutable collection.
- **Tuple**: Ordered but immutable collection.
- **Set**: Unordered collection of unique elements.
- **Dictionary**: Key-value pairs.
- **None**: Represents the absence of a value.
- **Bytes**: Immutable sequence of bytes.
- **Bytearray**: Mutable sequence of bytes.
- **Range**: Represents a sequence of numbers.
- **Frozenset**: Immutable version of a set.

---

### **Conditional Statements:**

- **if**: Executes a block of code if the condition is True.
- **if-else**: Executes one block if the condition is True and another if it’s False.
- **if-elif-else**: Handles multiple conditions.
- **Nested if**: Checks conditions within another condition.
- **Logical operators (and, or)**: Combine multiple conditions.
- **Shorthand if**: Allows concise conditional expressions.
- **pass**: Placeholder when no action is required.

---

### **Loops:**

- **For Loop (List Iteration)**: Iterates over each item in the list and performs an action.
- **For Loop (Range)**: Uses `range(1, 6)` to generate numbers from 1 to 5, iterating through each to perform an action.
- **While Loop**: Executes as long as the condition (e.g., `counter <= 5`) is True.
- **Nested Loops**: An outer loop that runs multiple times, and for each iteration, an inner loop runs, like printing a multiplication table.
- **Break Statement**: Exits the loop when a condition is met (e.g., `i == 6`).
- **Continue Statement**: Skips the current iteration and moves to the next when a condition is met (e.g., `i == 3`).

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
