# Conditional Statements Examples in Python

# Example 1: if statement
number = 10
if number > 0:
    print(f"{number} is a positive number.")

# Example 2: if-else statement
number = -5
if number > 0:
    print(f"{number} is a positive number.")
else:
    print(f"{number} is a negative number.")

# Example 3: if-elif-else statement
number = 0
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

# Example 4: Nested if statement
age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can legally drink alcohol in some countries.")
else:
    print("You are a minor.")

# Example 5: Using multiple conditions with logical operators
grade = 85
if grade >= 90:
    print("You got an A.")
elif 80 <= grade < 90:
    print("You got a B.")
elif 70 <= grade < 80:
    print("You got a C.")
else:
    print("You need to improve.")

# Example 6: Using shorthand if statement
x, y = 5, 10
print("x is less than y.") if x < y else print("x is greater than or equal to y.")

# Example 7: Using pass statement in an if block
# Sometimes, you may want to create a placeholder for future code.
number = 15
if number > 0:
    pass  # Placeholder for future implementation
else:
    print("This will never be executed.")
