from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract base class for pizzas."""

    def __init__(self):
        self.description = "Unknown Pizza"

    @abstractmethod
    def cost(self):
        """Calculate the cost of the pizza."""
        pass

    def get_description(self):
        """Return the description of the pizza."""
        return self.description


class Margherita(Pizza):
    """Margherita pizza implementation."""

    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"

    def cost(self):
        return 8.0  # Base cost for Margherita


class Pepperoni(Pizza):
    """Pepperoni pizza implementation."""

    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza"

    def cost(self):
        return 10.0  # Base cost for Pepperoni


class PizzaFactory:
    """Factory to create pizza objects."""

    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type.lower() == 'margherita':
            return Margherita()
        elif pizza_type.lower() == 'pepperoni':
            return Pepperoni()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


class ToppingDecorator(Pizza):
    """Decorator for adding toppings to a pizza."""

    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def cost(self):
        return self.pizza.cost()


class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def cost(self):
        return self.pizza.cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Olives"

    def cost(self):
        return self.pizza.cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Mushrooms"

    def cost(self):
        return self.pizza.cost() + 0.7
