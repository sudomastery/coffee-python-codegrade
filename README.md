<div align="center">

# Coffee / Customer / Order

Minimal Python OOP project demonstrating a classic many‑to‑many relationship modeled explicitly with a join class.

`Customer  --<  Order  >--  Coffee`

</div>

## 1. Purpose
This repository is a compact, readable reference for:
* Modeling relationships with plain Python classes (no ORM, no database)
* Applying simple validation & encapsulation (read‑only vs mutable fields)
* Deriving aggregate data (counts, averages, unique lists) from in‑memory objects

Great for beginners practicing reasoning about object graphs before introducing frameworks.

## 2. Quick Start

```bash
git clone <your-fork-or-repo-url> coffee-oop
cd coffee-oop
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # (pytest only)
python -q
```

Then in the Python REPL:

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

## 3. Project Structure
```
coffee.py    # Coffee class (read‑only name, order aggregates)
customer.py  # Customer class (mutable validated name, helpers)
order.py     # Order join class (validates links & price range)
tests/       # Pytest suite exercising validation & aggregates
```

## 4. Domain Model Overview

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

## 5. Validation Rules (Summary)
* Coffee.name: string, length ≥ 3, set once (no setter)
* Customer.name: string, 1–15 inclusive, can be reassigned
* Order.customer: must be a `Customer` instance
* Order.coffee: must be a `Coffee` instance
* Order.price: float (int converted) and 1.0 ≤ price ≤ 10.0

## 6. Usage Examples

### Multiple Orders & Aggregates
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

### Preventing Invalid Data
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

## 7. Running Tests
Pytest is included for fast feedback.

```bash
pytest -q
```

What is covered:
* Coffee name validation & immutability
* Orders filtered per Coffee
* Unique customers per Coffee
* Aggregate counts & averages (including empty case)

## 8. Design Notes
* No external persistence—everything lives in memory via class-level `_all` lists.
* Imports inside methods avoid circular dependency issues (`order` <-> `customer` / `coffee`).
* Read‑only vs mutable distinction teaches encapsulation patterns with properties.
* Simplicity favored over clever abstractions for educational clarity.

## 9. Extending the Model (Ideas)
* Add timestamps to `Order` and sort outputs.
* Introduce removal methods (`Customer.delete()` etc.).
* Add filtering (e.g., coffees ordered above an average threshold).
* Persist to JSON / SQLite for session durability.

## 10. Contributing
Fork, create a feature branch, keep style consistent, and add/adjust tests when changing behavior. Open a PR describing rationale and edge cases.

## 11. License
See `LICENSE` for details (MIT unless otherwise specified there).

---
Happy brewing & learning!
