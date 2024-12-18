# (1) Interfejs Strategii
class DeliveryStrategy:
    def calculate_fee(self, amount):
        pass


# (2) Konkretne strategie
class USADeliveryStrategy(DeliveryStrategy):
    def calculate_fee(self, amount):
        return 10  # stała opłata 10 dolarów


class PolandDeliveryStrategy(DeliveryStrategy):
    def calculate_fee(self, amount):
        return 0 if amount > 200 else 15  # Dostawa gratis powyżej 200 zł, inaczej 15 zł


class GermanyDeliveryStrategy(DeliveryStrategy):
    def calculate_fee(self, amount):
        return 8  # stała opłata 8 euro


# (3) Kontekst
class Purchase:
    def __init__(self, amount, strategy: DeliveryStrategy):
        self._amount = amount
        self._strategy = strategy

    def calculate_total_with_fee(self):
        return self._amount + self._strategy.calculate_fee(self._amount)


# Klient
if __name__ == "__main__":
    purchase_usa = Purchase(150, USADeliveryStrategy())
    print(purchase_usa.calculate_total_with_fee())  # Wypisuje: 160.0

    purchase_pl = Purchase(150, PolandDeliveryStrategy())
    print(purchase_pl.calculate_total_with_fee())  # Wypisuje: 165.0

    purchase_de = Purchase(150, GermanyDeliveryStrategy())
    print(purchase_de.calculate_total_with_fee())  # Wypisuje: 158.0
