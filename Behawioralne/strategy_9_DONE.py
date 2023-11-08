# (1) Interfejs Strategii
class TaxStrategy:
    def calculate(self, amount):
        pass


# (2) Konkretne strategie
class USATaxStrategy(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.05  # 5% podatek


class PolandTaxStrategy(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.23  # 23% VAT


class GermanyTaxStrategy(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.19  # 19% VAT


# (3) Kontekst
class Order:
    def __init__(self, amount, strategy: TaxStrategy):
        self._amount = amount
        self._strategy = strategy

    def calculate_total_amount(self):
        return self._amount + self._strategy.calculate(self._amount)


# Klient
order_usa = Order(1000, USATaxStrategy())
print(order_usa.calculate_total_amount())  # Wypisuje: 1050.0

order_pl = Order(1000, PolandTaxStrategy())
print(order_pl.calculate_total_amount())  # Wypisuje: 1230.0

order_de = Order(1000, GermanyTaxStrategy())
print(order_de.calculate_total_amount())  # Wypisuje: 1190.0
