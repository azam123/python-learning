# 1. Simple Function (No Arguments, No Return Value)
def greet():
    print("Hello! Welcome to Python Functions.")

# 2. Function with Arguments (No Return Value)
def greet_person(name):
    print(f"Hello, {name}! How are you?")

# 3. Function with Return Value (No Arguments)
def get_favorite_number():
    return 7  # Returns a fixed value

# 4. Function with Arguments and Return Value
def add_numbers(a, b):
    return a + b  # Adds two numbers and returns the result

# 5. Function with Default Arguments
def greet_person_with_default(name="Guest"):
    print(f"Hello, {name}!")

# 6. Function with Variable Number of Arguments (Using *args)
def print_numbers(*args):
    print("The numbers are:", args)

# 7. Function with Keyword Arguments (Using **kwargs)
def print_info(**kwargs):
    print("Person's Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 8. Lambda Function (Anonymous Function)
multiply = lambda x, y: x * y  # Lambda function to multiply two numbers

# Calling the functions
greet()

greet_person("Alice")

favorite_number = get_favorite_number()
print(f"My favorite number is: {favorite_number}")

sum_result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {sum_result}")

greet_person_with_default()
greet_person_with_default("John")

print_numbers(1, 2, 3, 4, 5)

print_info(name="Alice", age=30, city="New York")

product_result = multiply(4, 5)
print(f"The product of 4 and 5 is: {product_result}")
