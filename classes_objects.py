# Defining a class named 'Car'
class Car:
    # Constructor method (__init__) to initialize object attributes
    def __init__(self, make, model, year):
        self.make = make  # Brand of the car
        self.model = model  # Model of the car
        self.year = year  # Manufacturing year of the car
    
    # Method to display car details
    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is now running!")

    # Method to stop the car engine
    def stop_engine(self):
        print(f"The engine of the {self.make} {self.model} has been turned off.")


# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)  # Creating an object of 'Car' class with values for make, model, and year
car2 = Car("Honda", "Civic", 2022)  # Another car object

# Calling methods on objects
car1.display_info()  # Displays details of car1
car1.start_engine()  # Starts the engine of car1
car1.stop_engine()  # Stops the engine of car1

car2.display_info()  # Displays details of car2
car2.start_engine()  # Starts the engine of car2
car2.stop_engine()  # Stops the engine of car2
