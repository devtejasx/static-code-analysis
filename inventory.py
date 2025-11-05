"""Inventory management system for basic stock operations."""

import json
from datetime import datetime

class Inventory:
    """Class to manage inventory operations."""

    def __init__(self):
        """Initialize empty inventory."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add an item and its quantity to the inventory.

        Args:
            item (str): Name of the item to add.
            qty (int): Quantity of the item to add.
            logs (list, optional): List to record operation logs. Defaults to None.
        """
        if logs is None:
            logs = []
        if not item or not isinstance(item, str):
            return
        if not isinstance(qty, int):
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove a given quantity of an item from the inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Item '{item}' not found in inventory")

    def get_qty(self, item):
        """Return the available quantity of a given item."""
        return self.stock_data[item]

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file."""
        with open(file, "r", encoding="utf-8") as f:
            self.stock_data = json.loads(f.read())

    def save_data(self, file="inventory.json"):
        """Save the current inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.stock_data))

    def print_data(self):
        """Print all inventory items and their current quantities."""
        print("Items Report")
        for i in self.stock_data:
            print(i, "->", self.stock_data[i])

    def check_low_items(self, threshold=5):
        """Return a list of items whose quantity is below a given threshold."""
        result = []
        for i in self.stock_data:
            if self.stock_data[i] < threshold:
                result.append(i)
        return result


def main():
    """Demonstrate inventory operations with sample data."""
    inventory = Inventory()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item(123, "ten")  # invalid types, no check
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()
    print("eval used")


if __name__ == "__main__":
    main()