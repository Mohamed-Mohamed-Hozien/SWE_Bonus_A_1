class InventoryManager:
    """Singleton class to manage ingredient inventory."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(
                cls, *args, **kwargs)
            cls._instance.inventory = {
                "Cheese": 10,
                "Olives": 20,
                "Mushrooms": 15
            }
        return cls._instance

    def check_ingredient(self, ingredient):
        """Check if the ingredient is available."""
        return self.inventory.get(ingredient, 0) > 0

    def use_ingredient(self, ingredient):
        """Use an ingredient from inventory."""
        if self.check_ingredient(ingredient):
            self.inventory[ingredient] -= 1
