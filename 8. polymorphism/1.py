class Animal:
    def speak(self):
        print("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Duck(Animal):
    def speak(self):
        print("Quack! Quack!")

# Create instances of different animal types
my_dog = Dog()
my_cat = Cat()
my_duck = Duck()

# Call the speak from different animal objects
my_dog.speak() # Woof! Woof!
my_cat.speak() # Meow!
my_duck.speak() # Quack! Quack!

# Another way to demonstrate polymorphism with a list
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())