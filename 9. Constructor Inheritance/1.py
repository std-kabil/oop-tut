class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor called for {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent's constructor
        self.age = age
        print(f"Child constructor called for {self.name} (age: {self.age})")

# Creating an object of the Child class
child_obj = Child("Alice", 10)