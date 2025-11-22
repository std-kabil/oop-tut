class Car:
    # Class attribute
    wheels = 4

    def __init__(self, color, brand):
        # Instance attributes
        self.color = color
        self.brand = brand


# Create instances
car1 = Car("red", "Toyota")
car2 = Car("blue", "Honda")

print('================================')

# Accessing attributes
print(f"Car 1: Color={car1.color}, Brand={car1.brand}, Wheels={car1.wheels}")
print(f"Car 2: Color={car2.color}, Brand={car2.brand}, Wheels={car2.wheels}")
print(f"Class attribute 'wheels' directly: {Car.wheels}")

print('================================')

# Modifying instance attribute
car1.color = "green"
print(f"Car 1 color after modification: {car1.color}")
print(f"Car 2 color (unaffected): {car2.color}")

print('================================')

# Modifying class attribute (affects all instances)
Car.wheels = 5
print(f"Car 1 wheels after class attribute modification: {car1.wheels}")
print(f"Car 2 wheels after class attribute modification: {car2.wheels}")