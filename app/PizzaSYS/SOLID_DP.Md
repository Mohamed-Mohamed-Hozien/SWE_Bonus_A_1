# Design Patterns and Their Relation to SOLID Principles

## 1. Factory Pattern

**SOLID Principles Addressed:**

- **Open/Closed Principle (OCP)**: New pizzas can be added without modifying the main creation logic.
- **Single Responsibility Principle (SRP)**: The factory's sole responsibility is to handle object creation.

---

## 2. Decorator Pattern

**SOLID Principles Addressed:**

- **Open/Closed Principle (OCP)**: New toppings can be added as separate classes, without modifying existing logic.
- **Single Responsibility Principle (SRP)**: Each topping has a single responsibility (to add flavor to the pizza).

---

## 3. Singleton Pattern

**SOLID Principles Addressed:**

- **Single Responsibility Principle (SRP)**: Ensures that the InventoryManager handles a single responsibility — managing inventory.
- **Dependency Inversion Principle (DIP)**: Classes that rely on inventory depend on an abstraction, not a concrete implementation.

---

## 4. Strategy Pattern

**SOLID Principles Addressed:**

- **Open/Closed Principle (OCP)**: New payment methods can be added without modifying existing code.
- **Dependency Inversion Principle (DIP)**: Classes depend on an abstraction (PaymentStrategy), not a specific implementation.

---

## **Summary**

- **OCP (Open/Closed)**: Factory and Decorator allow easy extension of pizzas and toppings.
- **SRP (Single Responsibility)**: Each pattern isolates a clear responsibility (Pizza creation, Payment, etc.).
- **DIP (Dependency Inversion)**: Payment methods and inventory rely on abstractions instead of concrete implementations.
