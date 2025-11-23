class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        return f"The {self.brand}'s engine started."

    def stop_engine(self):
        self.is_running = False
        return f"The {self.brand}'s engine stopped."

    def display_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

# --- Child Classes ---

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        # Call the parent class's constructor to set brand and year
        super().__init__(brand, year) 
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self.num_doors}"

class Bicycle(Vehicle):
    def pedal(self):
        return f"The {self.brand} is moving by pedals."
    
    # Optional: Override the inherited engine methods to provide custom behavior
    def start_engine(self):
        return f"The {self.brand} doesn't have an engine to start!"


# --- Usage Example ---

my_car = Car(brand="Toyota", year=2022, num_doors=4)
my_bike = Bicycle(brand="Giant", year=2024)

print(my_car.display_info())   # Uses the overridden method
print(my_car.start_engine())   # Uses the inherited method
print(my_car.honk())           # Uses the car's specific method

print("-" * 20)

print(my_bike.display_info())  # Uses the inherited method
print(my_bike.pedal())         # Uses the bicycle's specific method
print(my_bike.start_engine())  # Uses the bicycle's overridden start method
