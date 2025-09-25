import pytest

from coffee import Coffee
from customer import Customer
from order import Order


@pytest.fixture(autouse=True)
def clean_state():
    # Reset in-memory registries before and after each test to keep tests isolated
    Coffee._all.clear()
    Customer._all.clear()
    Order._all.clear()
    yield
    Coffee._all.clear()
    Customer._all.clear()
    Order._all.clear()


def test_name_validation():
    # name must be a string
    with pytest.raises(ValueError, match="name must be a string"):
        Coffee(123)  # type: ignore[arg-type]

    # name must be at least 3 characters
    with pytest.raises(ValueError, match="at least 3"):
        Coffee("ab")

    # valid name is stored
    c = Coffee("Latte")
    assert c.name == "Latte"


def test_name_read_only_property():
    c = Coffee("Mocha")
    with pytest.raises(AttributeError):
        c.name = "NewName"  # read-only property; no setter defined


def test_orders_for_this_coffee_only():
    c1 = Coffee("Latte")
    c2 = Coffee("Espresso")
    alice = Customer("Alice")
    bob = Customer("Bob")

    o1 = Order(alice, c1, 3.5)
    o2 = Order(bob, c1, 4.0)
    o3 = Order(alice, c2, 2.0)

    assert c1.orders() == [o1, o2]
    assert c2.orders() == [o3]


def test_customers_unique_first_seen_order():
    c = Coffee("Cappuccino")
    alice = Customer("Alice")
    bob = Customer("Bob")

    # same customer ordering multiple times shouldn't duplicate in customers()
    Order(alice, c, 3.0)
    Order(alice, c, 3.5)
    Order(bob, c, 4.0)

    assert c.customers() == [alice, bob]


def test_average_price_and_num_orders():
    c = Coffee("Americano")

    # when there are no orders
    assert c.num_orders() == 0
    assert c.average_price() == 0.0

    # with some orders present
    alice = Customer("Alice")
    bob = Customer("Bob")
    Order(alice, c, 3.0)
    Order(bob, c, 5.0)

    assert c.num_orders() == 2
    assert c.average_price() == 4.0
