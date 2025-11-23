class ParentClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def parent_method(self):
        print("This is a method from the parent class.")

class ChildClass(ParentClass):  # ChildClass inherits from ParentClass
    def child_method(self):
        print("This is a method from the child class.")

# Create an instance of the child class
obj = ChildClass(1, 2, 3)
