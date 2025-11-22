class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty, price):
        item = (item_name, qty, price)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        return total

# Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("apple", 2, 5)
cart.add_item("Bread", 3, 1)
cart.add_item("Stake", 2, 15)

total_price = cart.calculate_total_price()
print("Total Price:", total_price)

# Remove items to the shopping cart
cart.remove_item("apple")

total_price = cart.calculate_total_price()
print("Total Price:", total_price)

