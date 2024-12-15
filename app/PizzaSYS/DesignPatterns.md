
# Design Patterns in Pizza Restaurant Ordering System

## 1. Factory Pattern

### **Description and Application**

The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In our Pizza Restaurant system, the Factory Pattern is used to create different types of pizzas (like Margherita and Pepperoni) dynamically at runtime without hardcoding object creation logic.

### **Before Applying the Pattern**

Previously, creating a new pizza required multiple conditional statements (`if-else` or `switch-case`) to identify the type of pizza and instantiate it directly. For example:

```python
if pizza_type == "Margherita":
    pizza = Margherita()
elif pizza_type == "Pepperoni":
    pizza = Pepperoni()
else:
    raise ValueError("Unknown pizza type")
```

### **After Applying the Pattern**

Using the Factory Pattern, the pizza creation logic was moved into a single `PizzaFactory` class. New pizza types can be added by simply modifying the factory logic, which improves maintainability and avoids repetitive conditional logic.

```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type.lower() == 'margherita':
            return Margherita()
        elif pizza_type.lower() == 'pepperoni':
            return Pepperoni()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
```

### **How it Improves the System**

- **Maintainability**: Adding a new pizza type only requires changes in the Factory logic, not the main application logic.
- **Extensibility**: New pizza classes can be added easily without modifying the existing codebase.

---

## 2. Decorator Pattern

### **Description and Application**

The Decorator Pattern allows for the dynamic addition of responsibilities to objects at runtime. It’s an alternative to subclassing for extending functionality. In our Pizza Restaurant system, this pattern is used to add dynamic toppings (like Cheese, Olives, and Mushrooms) to pizzas.

### **Before Applying the Pattern**

Adding new toppings to a pizza required creating separate classes for every possible combination of toppings (e.g., `MargheritaWithCheese`, `MargheritaWithOlives`, etc.), leading to a combinatorial explosion of classes.

### **After Applying the Pattern**

Using the Decorator Pattern, each topping is a "decorator" that wraps an existing pizza object and extends its functionality (like `get_description` and `cost`). Here’s how it was done:

```python
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def cost(self):
        return self.pizza.cost()
```

Toppings like Cheese, Olives, and Mushrooms extend this base decorator:

```python
class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def cost(self):
        return self.pizza.cost() + 1.0
```

### **How it Improves the System**

- **Maintainability**: New toppings can be added as individual classes without modifying existing classes.
- **Extensibility**: Combinations of toppings are created at runtime, avoiding the need for a separate subclass for each combination.

---

## 3. Singleton Pattern

### **Description and Application**

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. In the Pizza Restaurant system, this pattern is applied to the `InventoryManager`, which tracks the availability of ingredients.

### **Before Applying the Pattern**

Each time an ingredient was needed, a new instance of `InventoryManager` was created. This led to inconsistencies in the tracking of inventory, as each instance had a separate state.

### **After Applying the Pattern**

By using the Singleton Pattern, only one `InventoryManager` instance is created, and it is shared across the entire system.

```python
class InventoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.inventory = {"Cheese": 10, "Olives": 20, "Mushrooms": 15}
        return cls._instance
```

### **How it Improves the System**

- **Maintainability**: Inventory tracking is centralized in one place, ensuring consistent tracking of resources.
- **Extensibility**: New inventory items can be added without affecting existing logic.

---

## 4. Strategy Pattern

### **Description and Application**

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows a class's behavior to be selected at runtime. In our Pizza system, we applied the Strategy Pattern for the payment methods (Credit Card and PayPal).

### **Before Applying the Pattern**

Payment logic was hardcoded into the main system logic, and changes required direct modifications to the payment logic.

### **After Applying the Pattern**

Using the Strategy Pattern, different payment methods (like PayPal and Credit Card) are implemented as separate classes following a shared interface.

```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

Concrete payment strategies:

```python
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")
```

### **How it Improves the System**

- **Maintainability**: New payment methods can be added as new classes without changing existing payment logic.
- **Extensibility**: Users can choose payment methods at runtime.

---

## Overengineering Example

### **Concept**

Overengineering happens when systems become unnecessarily complex. For instance, if we create a **Factory** for every single **Topping** (like a `CheeseFactory`, `OlivesFactory`), it would introduce unnecessary complexity.

### **Example of Overengineering**

```python
class CheeseFactory:
    def create_cheese(self):
        return "Cheese"

class OlivesFactory:
    def create_olives(self):
        return "Olives"
```

This is overengineered because toppings are simple objects, and using a **Decorator** to attach them to pizzas at runtime is a cleaner approach.

---
