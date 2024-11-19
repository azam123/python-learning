# 1. For Loop - Iterating through a list
fruits = ["Apple", "Banana", "Cherry", "Date"]
print("Using for loop to iterate through a list:")
for fruit in fruits:
    print(fruit)

# 2. For Loop - Using range() to iterate through a sequence of numbers
print("\nUsing for loop with range to iterate through a sequence:")
for i in range(1, 6):  # range(1, 6) will generate numbers 1 to 5
    print(f"Number: {i}")

# 3. While Loop - Print numbers from 1 to 5
print("\nUsing while loop to print numbers from 1 to 5:")
counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # Increment the counter to avoid an infinite loop

# 4. Nested Loop - Nested for loops to print a multiplication table (1-3)
print("\nUsing nested for loops to print a multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print()  # Print an empty line for better readability

# 5. Breaking out of a loop - Demonstrating break statement
print("\nUsing break to exit a loop early:")
for i in range(1, 10):
    if i == 6:
        print("Breaking the loop at i = 6")
        break
    print(i)

# 6. Skipping an iteration - Demonstrating continue statement
print("\nUsing continue to skip an iteration:")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
