from typing import List


class Order:
	_all: List["Order"] = []

	def __init__(self, customer, coffee, price):
		# import here to avoid circular import issues.
		from customer import Customer
		from coffee import Coffee

		# check that customer is really a Customer object.
		if not isinstance(customer, Customer):
			raise ValueError("customer must be a Customer instance")
		# check that coffee is really a Coffee object.
		if not isinstance(coffee, Coffee):
			raise ValueError("coffee must be a Coffee instance")

		# Allow an int like 5 but turn it into 5.0
		if isinstance(price, int):
			price = float(price)
		# Now be sure it is a float.
		if not isinstance(price, float):
			raise ValueError("price must be a float")
		#check range
		if not (1.0 <= price <= 10.0):
			raise ValueError("price must be between 1.0 and 10.0")

		# Store the values in private variables (read-only via properties).
		self._customer = customer
		self._coffee = coffee
		self._price = price

		# Add this new Order to the list of all orders.
		Order._all.append(self)

	# RO properties
	@property
	def customer(self):
		return self._customer

	@property
	def coffee(self):
		return self._coffee

	@property
	def price(self):
		return self._price

	# class helper
	@classmethod
	def all(cls) -> List["Order"]:
		return cls._all

	def __repr__(self):
		return f"Order(customer={self._customer.name!r}, coffee={self._coffee.name!r}, price={self._price})"
