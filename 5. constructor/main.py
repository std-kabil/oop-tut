class Student:
    def __init__(slef, name, age):
        # This function will be executed once a new instance is created
        slef.name = name
        slef.age = age
        
    
    def sayHey(slef):
        print("hey from the __init__ method")


s = Student("John", 20)