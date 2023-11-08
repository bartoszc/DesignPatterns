# (1) Klasa bazowa z metodą szablonową
class Beverage:
    def prepare(self):
        self.boil_water()
        self.brew_or_steep()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    # Metody do przedefiniowania w podklasach
    def brew_or_steep(self):
        pass

    def add_condiments(self):
        pass

# (2) Konkretne klasy napojów
class Tea(Beverage):
    def brew_or_steep(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(Beverage):
    def brew_or_steep(self):
        print("Brewing the coffee grounds")

    def add_condiments(self):
        print("Adding sugar and milk")

# Klient
if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("Preparing tea:")
    tea.prepare()
    # Wypisuje:
    # Boiling water
    # Steeping the tea
    # Pouring into cup
    # Adding lemon

    print("\nPreparing coffee:")
    coffee.prepare()
    # Wypisuje:
    # Boiling water
    # Brewing the coffee grounds
    # Pouring into cup
    # Adding sugar and milk
