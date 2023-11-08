# Klasa produktu - reprezentuje produkt końcowy, który ma być zbudowany.
class Computer:
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def display(self):
        print("Komputer składa się z:")
        for component in self.components:
            print("-", component)


# Klasa Builder - abstrakcyjny interfejs do tworzenia produktów.
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def build(self):
        raise NotImplementedError


# Konkretne klasy Builder - implementują konkretne kroki budowy produktu.
class GamingComputerBuilder(ComputerBuilder):
    def build(self):
        self.computer.add("Procesor i9")
        self.computer.add("32GB RAM")
        self.computer.add("GeForce RTX 3090")
        return self.computer


class OfficeComputerBuilder(ComputerBuilder):
    def build(self):
        self.computer.add("Procesor i5")
        self.computer.add("16GB RAM")
        self.computer.add("Intel HD Graphics")
        return self.computer


# Klasa Director - kieruje procesem budowy, używając odpowiedniego obiektu Builder.
class ComputerShop:
    def construct_computer(self, builder):
        return builder.build()


# Użycie wzorca Builder:
shop = ComputerShop()

gaming_builder = GamingComputerBuilder()
gaming_computer = shop.construct_computer(gaming_builder)
gaming_computer.display()

office_builder = OfficeComputerBuilder()
office_computer = shop.construct_computer(office_builder)
office_computer.display()
