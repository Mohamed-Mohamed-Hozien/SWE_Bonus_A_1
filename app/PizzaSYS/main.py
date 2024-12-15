from pizza import PizzaFactory, Cheese, Olives
from payment import PayPalPayment

# Step 1: Create a Margherita Pizza
pizza = PizzaFactory.create_pizza("Margherita")

# Step 2: Add Toppings
pizza = Cheese(pizza)
pizza = Olives(pizza)

# Step 3: Calculate cost and display order
print(f"Order: {pizza.get_description()}")
print(f"Total Cost: ${pizza.cost()}")

# Step 4: Process payment
payment_method = PayPalPayment()
payment_method.pay(pizza.cost())
