# (1) Interfejs Observer
class Observer:
    def update(self, product_name):
        pass


# (2) Interfejs Store (analogiczny do Subject)
class Store:
    def add_customer(self, customer):
        pass

    def remove_customer(self, customer):
        pass

    def notify_customers(self):
        pass


# (3) Konkretny Store - OnlineStore
class OnlineStore(Store):
    def __init__(self):
        self._customers = []
        self._latest_product = None

    def add_customer(self, customer):
        self._customers.append(customer)

    def remove_customer(self, customer):
        self._customers.remove(customer)

    def notify_customers(self):
        for customer in self._customers:
            customer.update(self._latest_product)

    def add_product(self, product_name):
        self._latest_product = product_name
        self.notify_customers()


# (4) Konkretny Observer - Customer
class Customer(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, product_name):
        print(f"{self._name} has been notified about a new product: {product_name}")


# Klient
if __name__ == "__main__":
    store = OnlineStore()

    bob = Customer("Bob")
    alice = Customer("Alice")

    store.add_customer(bob)
    store.add_customer(alice)

    store.add_product("New Shoes")  # Wypisuje:
    # Bob has been notified about a new product: New Shoes
    # Alice has been notified about a new product: New Shoes
