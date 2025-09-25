# Coffee / Customer / Order

In‑memory Python implementation of a many‑to‑many relationship using an explicit join class.

Relationship: `Customer  --<  Order  >--  Coffee`

## 1. Scope
Demonstrates:
* Plain Python object relationships (no database / ORM)
* Input validation and controlled mutability
* Simple aggregate queries over in‑memory collections

## 2. Setup

```bash
git clone <your-fork-or-repo-url> coffee-oop
cd coffee-oop
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # (pytest only)
python -q
```

Python REPL example:

```python
from customer import Customer
from coffee import Coffee

alice = Customer("Alice")
latte = Coffee("Latte")
alice.create_order(latte, 5.5)

print(latte.num_orders())        # 1
print(latte.average_price())     # 5.5
print(latte.customers())         # [Customer(name='Alice')]
```

## 3. Structure
```
coffee.py    # Coffee class (read‑only name, order aggregates)
customer.py  # Customer class (mutable validated name, helpers)
order.py     # Order join class (validates links & price range)
tests/       # Pytest suite exercising validation & aggregates
```

## 4. Model

### Coffee
| Aspect | Details |
|--------|---------|
| Identity | `name` (string, >= 3 chars, immutable after creation) |
| Relationships | `orders()` → list of `Order`; `customers()` → unique `Customer`s |
| Aggregates | `num_orders()`, `average_price()` (0.0 if none) |

### Customer
| Aspect | Details |
|--------|---------|
| Identity | `name` (1–15 chars, mutable with validation) |
| Relationships | `orders()`, `coffees()` (unique) |
| Factory | `create_order(coffee, price)` convenience wrapper |

### Order (Join Object)
| Aspect | Details |
|--------|---------|
| Links | One `Customer`, one `Coffee` |
| Price | float in range 1.0–10.0 (int auto‑cast to float) |
| Immutability | `customer`, `coffee`, `price` exposed as read‑only properties |

## 5. Validation
* Coffee.name: string, length ≥ 3, set once (no setter)
* Customer.name: string, 1–15 inclusive, can be reassigned
* Order.customer: must be a `Customer` instance
* Order.coffee: must be a `Coffee` instance
* Order.price: float (int converted) and 1.0 ≤ price ≤ 10.0

## 6. Examples

### Aggregates
```python
from customer import Customer
from coffee import Coffee

alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")

alice.create_order(latte, 4.5)
bob.create_order(latte, 5.0)

print(latte.num_orders())      # 2
print(latte.average_price())   # 4.75
print(latte.customers())       # [Customer(name='Alice'), Customer(name='Bob')]
```

### Invalid Data Rejection
```python
from coffee import Coffee
from order import Order
from customer import Customer

try:
	Coffee("ab")  # too short
except ValueError as e:
	print(e)

try:
	Order(Customer("A"), Coffee("Mocha"), 20.0)  # price out of range
except ValueError as e:
	print(e)
```

## 7. Tests
Pytest suite covers validation, relationship navigation, and aggregates.

```bash
pytest -q
```

## 8. Design Notes
* Data stored only in class-level `_all` lists.
* Local imports inside methods avoid circular references.
* Read‑only vs mutable properties are explicit.
* Code favors clarity over abstraction.

## 9. Possible Extensions
* Timestamp orders
* Deletion / archival facilities
* Additional query helpers
* Persistence layer (JSON / SQLite)

## 10. Contributing
Submit pull requests with clear rationale and accompanying tests for behavior changes.

## 11. License
Refer to `LICENSE` (MIT if not otherwise specified).


