class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a product with a name, price, and stock quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Displays the details of the product."""
        print(f"Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.quantity}")

    def update_quantity(self, amount: int):
        """Updates the stock quantity (can accept positive or negative integers)."""
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0  # Prevents negative stock
        print(f"Updated '{self.name}' quantity. New stock: {self.quantity}")

    def get_total_value(self) -> float:
        """Calculates the total monetary value of this specific product's stock."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        """Initializes an empty store inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """Adds a new product to the inventory management system."""
        self.products[product.name] = product
        print(f"Added {product.name} to inventory.")

    def show_all_products(self):
        """Displays details for every product currently in stock."""
        if not self.products:
            print("The inventory is completely empty.")
            return
        print("\n--- Current Inventory Status ---")
        for product in self.products.values():
            product.display_info()
        print("---------------------------------")

    def calculate_inventory_value(self) -> float:
        """Calculates and returns the grand total value of all stock combined."""
        total_value = sum(product.get_total_value() for product in self.products.values())
        return total_value


# --- Demonstration of the System ---
if __name__ == "__main__":
    # 1. Initialize the inventory system
    my_store = Inventory()

    # 2. Create sample product instances
    prod1 = Product(name="Laptop", price=999.99, quantity=10)
    prod2 = Product(name="Wireless Mouse", price=25.50, quantity=50)
    prod3 = Product(name="Headphones", price=79.99, quantity=25)

    # 3. Add products to the system
    print("--- Registering Products ---")
    my_store.add_product(prod1)
    my_store.add_product(prod2)
    my_store.add_product(prod3)

    # 4. Display baseline inventory information
    my_store.show_all_products()

    # 5. Update stock levels for a product
    print("\n--- Modifying Quantities ---")
    prod2.update_quantity(-5)  # Sold 5 units
    prod3.update_quantity(10)  # Restocked 10 units

    # 6. Display total portfolio valuation
    grand_total = my_store.calculate_inventory_value()
    print(f"\nGrand Total Value of Inventory: ${grand_total:,.2f}")