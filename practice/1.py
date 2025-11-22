# Define a class called Person to represent a person with a name, country, and date of birth
class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, year_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth
    
    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        this_year = 2025
        age = this_year - self.year_of_birth
        return age

# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", 1962)
person2 = Person("Shweta Maddox", "Canada", 1982)
person3 = Person("Elizaveta Tilman", "USA", 2005)

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.year_of_birth)
print("Age:", person1.calculate_age())

person1.calculate_age() # 63
person2.calculate_age() # 43
person3.calculate_age() # 20

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.year_of_birth)
print("Age:", person2.calculate_age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.year_of_birth)
print("Age:", person3.calculate_age())
