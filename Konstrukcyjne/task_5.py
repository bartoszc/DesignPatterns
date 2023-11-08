class Pizza:
    def __init__(self, name="Nieznana Pizza"):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print(f"Pizza {self.name} składa się z:")
        for ingredient in self.ingredients:
            print("-", ingredient)


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        raise NotImplementedError


class MargheritaBuilder(PizzaBuilder):
    def build(self):
        self.pizza.name = "Margherita"
        self.pizza.add_ingredient("Pomidory")
        self.pizza.add_ingredient("Ser")
        self.pizza.add_ingredient("Bazylia")
        return self.pizza


class HawaiianBuilder(PizzaBuilder):
    def build(self):
        self.pizza.name = "Hawajska"
        self.pizza.add_ingredient("Szynka")
        self.pizza.add_ingredient("Ananas")
        return self.pizza


class PepperoniBuilder(PizzaBuilder):
    def build(self):
        self.pizza.name = "Pepperoni"
        self.pizza.add_ingredient("Salami pepperoni")
        self.pizza.add_ingredient("Ser")
        return self.pizza


class Pizzeria:
    def order_pizza(self, builder):
        return builder.build()


pizzeria = Pizzeria()

margherita_builder = MargheritaBuilder()
margherita_pizza = pizzeria.order_pizza(margherita_builder)
margherita_pizza.display()

hawaiian_builder = HawaiianBuilder()
hawaiian_pizza = pizzeria.order_pizza(hawaiian_builder)
hawaiian_pizza.display()

pepperoni_builder = PepperoniBuilder()
pepperoni_pizza = pizzeria.order_pizza(pepperoni_builder)
pepperoni_pizza.display()

