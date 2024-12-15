from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """Abstract strategy for payment methods."""

    @abstractmethod
    def pay(self, amount):
        """Pay the specified amount."""
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")
