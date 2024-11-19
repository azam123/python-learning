# python-learning
**Data Types:**
**Integer:** Whole numbers.
**Float:** Numbers with decimals.
**Complex:** Numbers with a real and imaginary part.
**String:** Sequence of characters.
**Boolean:** Logical values (True or False).
**List:** Ordered and mutable collection.
**Tuple:** Ordered but immutable collection.
**Set:** Unordered collection of unique elements.
**Dictionary:** Key-value pairs.
**None:** Represents the absence of a value.
**Bytes:** Immutable sequence of bytes.
**Bytearray:** Mutable sequence of bytes.
**Range:** Represents a sequence of numbers.
**Frozenset:** Immutable version of a set.


**Conditional Statements:**
**if:** Executes a block of code if the condition is True.
**if-else:** Executes one block if the condition is True and another if it’s False.
**if-elif-else:** Handles multiple conditions.
**Nested if:** Checks conditions within another condition.
**Logical operators (and, or):** Combine multiple conditions.
**Shorthand if:** Allows concise conditional expressions.
**pass:** Placeholder when no action is required.


**Loops:**
**For Loop (List Iteration):** The for loop iterates over each item in the list fruits and prints them.
**For Loop (Range):** The range(1, 6) generates numbers from 1 to 5, and the loop iterates through each number to print it.
**While Loop:** This loop continues as long as the condition (counter <= 5) is True, printing numbers from 1 to 5.
**Nested Loops:** The outer for loop runs from 1 to 3, and for each iteration, the inner for loop runs from 1 to 3, printing a multiplication table.
**Break Statement:** The break statement exits the loop when i equals 6.
**Continue Statement:** The continue statement skips the current iteration when i equals 3 and moves to the next iteration.



**Functions in python:**
**Simple Function (No Arguments, No Return Value):**
greet() is a function that prints a simple greeting message without accepting any arguments or returning a value.

**Function with Arguments (No Return Value):**
greet_person(name) accepts a name argument and prints a personalized greeting message without returning a value.

**Function with Return Value (No Arguments):**
get_favorite_number() doesn't take any arguments but returns a value (7 in this case).

**Function with Arguments and Return Value:**
add_numbers(a, b) takes two arguments, adds them, and returns the sum.

**Function with Default Arguments:**
greet_person_with_default(name="Guest") has a default value for the name argument. If no argument is passed, it defaults to "Guest".

**Function with Variable Number of Arguments (Using *args):**
print_numbers(*args) accepts any number of positional arguments and prints them as a tuple.

**Function with Keyword Arguments (Using kwargs):**
print_info(**kwargs) accepts any number of keyword arguments and prints them in a key-value pair format.

**Lambda Function (Anonymous Function):**
multiply = lambda x, y: x * y creates a simple anonymous function that multiplies two numbers.
