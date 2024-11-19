# Function for switch-case-like behavior using dictionary
def switch_case_example(option):
    switch_dict = {
        1: "You selected option 1: Display Hello",
        2: "You selected option 2: Display Goodbye",
        3: "You selected option 3: Display Greetings",
        4: "You selected option 4: Exit"
    }
    
    # Using get method to handle missing cases
    return switch_dict.get(option, "Invalid option selected")

# Input from user
print("Select an option:")
print("1: Display Hello")
print("2: Display Goodbye")
print("3: Display Greetings")
print("4: Exit")

# User input
user_input = int(input("Enter your option (1-4): "))

# Call the function to simulate the switch-case
result = switch_case_example(user_input)
print(result)

