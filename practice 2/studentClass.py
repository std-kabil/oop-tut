class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def is_honors(self):
        return self.gpa >= 3.5


# Create objects
s1 = Student("Kabil", "AI", 3.9)
s2 = Student("Sarah", "CS", 3.1)

print(s1.is_honors())  # True
print(s2.is_honors())  # False
