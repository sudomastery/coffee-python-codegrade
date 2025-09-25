#import module so I can annotate
from typing import List


class Coffee:
    _all: List["Coffee"] = []

    def __init__(self, name: str):
    # All data is stored in a private variable named _name.
        # Start with None just so the attribute exists.
        self._name = None
        # Validate and set the actual name (one-time only).
        self._set_name_first_time(name)
        # Keep track of every Coffee created.
        Coffee._all.append(self)

    # internal one‑time setter used only inside __init__
    def _set_name_first_time(self, value: str) -> None:
        """Check name rules and store it. Only used inside __init__."""
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        self._name = value

    # Public read-only property: coffee.name can be read but not set.
    @property
    def name(self) -> str:
        return self._name



   #lists order objects for coffee
    def orders(self) -> List["Order"]:
        """Return all Order objects that point at this coffee."""
        from order import Order
        return [o for o in Order.all() if o.coffee is self]
    
    #lists unique customers who ordered it
    def customers(self) -> List["Customer"]:
        """Return each Customer who bought this coffee (no duplicates)."""
        seen = []  # simple list to preserve first-seen order
        for o in self.orders():
            if o.customer not in seen:
                seen.append(o.customer)
        return seen

    #count orders
    def num_orders(self) -> int:
        """How many orders exist for this coffee?"""
        return len(self.orders())


    #check the avrage price
    def average_price(self) -> float:
        """Average price paid. If there are no orders, return 0.0."""
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)

   
    @classmethod
    def all(cls) -> List["Coffee"]:
        """Return every Coffee instance created so far."""
        return cls._all

    def __repr__(self):
        return f"Coffee(name={self._name!r})"