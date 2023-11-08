# Klasa Coffee reprezentuje prostą kawę bez dodatków.
class Coffee:
    def __init__(self):
        # Podstawowy koszt kawy.
        self.cost = 5
        # Opis kawy.
        self.description = "Simple coffee"

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

# Klasa MilkDecorator jest "dekoratorem", który dodaje mleko do kawy.
class MilkDecorator:
    def __init__(self, coffee):
        # Przechowujemy oryginalny obiekt kawy, który chcemy "udekorować".
        self._coffee = coffee
        # Dodatkowy koszt mleka.
        self._cost = 2
        # Dodatkowy opis mleka.
        self._description = " + milk"

    def get_cost(self):
        # Zwracamy sumę kosztu oryginalnej kawy i mleka.
        return self._coffee.get_cost() + self._cost

    def get_description(self):
        # Dodajemy opis mleka do opisu oryginalnej kawy.
        return self._coffee.get_description() + self._description

# Klasa CaramelDecorator dodaje karmel do kawy.
class CaramelDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
        self._cost = 3
        self._description = " + caramel"

    def get_cost(self):
        return self._coffee.get_cost() + self._cost

    def get_description(self):
        return self._coffee.get_description() + self._description

# Klasa WhippedCreamDecorator dodaje bitą śmietanę do kawy.
class WhippedCreamDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
        self._cost = 1
        self._description = " + whipped cream"

    def get_cost(self):
        return self._coffee.get_cost() + self._cost

    def get_description(self):
        return self._coffee.get_description() + self._description

# Tworzymy prostą kawę.
my_coffee = Coffee()
print(f"Cost: {my_coffee.get_cost()}; Description: {my_coffee.get_description()}")

# Udekorujmy kawę mlekiem.
my_coffee = MilkDecorator(my_coffee)
print(f"Cost: {my_coffee.get_cost()}; Description: {my_coffee.get_description()}")

# Dodajmy karmel do naszej kawy z mlekiem.
my_coffee = CaramelDecorator(my_coffee)
print(f"Cost: {my_coffee.get_cost()}; Description: {my_coffee.get_description()}")

# Dodajmy bitą śmietanę do naszej kawy z mlekiem i karmelem.
my_coffee = WhippedCreamDecorator(my_coffee)
print(f"Cost: {my_coffee.get_cost()}; Description: {my_coffee.get_description()}")


# Dzięki wzorcowi Dekorator możemy dynamicznie dodawać funkcjonalności (w tym przypadku składniki) do naszej kawy bez
# konieczności tworzenia wielu różnych klas dla każdej kombinacji składników. Zamiast tego każdy składnik to osobny
# dekorator, który "opakowuje" oryginalny obiekt kawy i dodaje do niego swoje właściwości.