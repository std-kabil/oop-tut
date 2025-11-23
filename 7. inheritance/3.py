
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.isAcive = True
    
    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}"

class AdminUser(User):
    def delete_user(self, user):
        user.isAcive = False
    
    def add_credits_to_user(self, user, amount):
        if user.isAcive:
            user.credits += amount
        else:
            print(f"Cannot add credits. User {user.name} is inactive.")

class Member(User):
    def __init__(self, name, email, credits):
        super().__init__(name, email)
        self.credits = credits

    def spend_credits(self, amount):
        if self.isAcive:
            self.credits -= amount
        else:
            print(f"Cannot spend credits. User {self.name} is inactive.")



admin = AdminUser("Alice", "admin@gmail.com")
member1 = Member("Bob", "Bob@gmail.com", 100)
member2 = Member("John", "John@gmail.com", 100)