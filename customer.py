from typing import List


class Customer:
    # class list that remembers every Customer created.
    _all: List["Customer"] = []

    def __init__(self, name: str):
        # use the property below so the validation runs.
        self.name = name
        # store this new object in the shared list.
        Customer._all.append(self)

    @property
    def name(self) -> str:
        # Give back the stored name value.
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # Make sure the name is a string.
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        # Make sure length is between 1 and 15 (inclusive).
        if not (1 <= len(value) <= 15):
            raise ValueError("name must be 1 to 15 characters long")
        self._name = value

    # ------------- relationship helpers -------------
    def orders(self) -> List["Order"]:
        # Return a list of this customer's Order objects
        from order import Order  # Import here to avoid circular import problems.
        return [o for o in Order.all() if o.customer is self]

    def coffees(self) -> List["Coffee"]:
        """Return each Coffee this customer has ordered (no duplicates)."""
        seen = []  # keeps order of first time each coffee appears
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee: "Coffee", price: float) -> "Order":
        """Make a new Order for this customer. Price validation is handled by the Order class."""
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def all(cls) -> List["Customer"]:
        """Return every Customer created so far."""
        return cls._all

    def __repr__(self):  # Helpful text when you print the object.
        return f"Customer(name={self._name!r})"