class Pizza():
    def __init__(self):
        self.ingridients = []
    def add(self, ingridient):
            self.ingridients.append(ingridient)
    def display(self):
        print("Pizza sklada sie z: ")
        for ingridient in self.ingridients:
                print("-", ingridient)
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    def build(self):
        raise NotImplementedError
class MargheritaBuilder(PizzaBuilder):
    def build(self):
        self.pizza.add("pomidory")
        self.pizza.add("ser")
        self.pizza.add("bazylia")
        return self.pizza
class HawaiianBuilder(PizzaBuilder):
    def build(self):
        self.pizza.add("szynka")
        self.pizza.add("ananas")
        return self.pizza
class PepperoniBuilder(PizzaBuilder):
    def build(self):
        self.pizza.add("salami pepperoni")
        self.pizza.add("ser")
        return self.pizza
class Director_Pizzeria():
    def order_pizza(self, builder):
        return builder.build()
pizzeria_director = Director_Pizzeria()
margherita_builder = MargheritaBuilder()
margherita_pizza = pizzeria_director.order_pizza(margherita_builder)
margherita_pizza.display()
hawaiian_builder = HawaiianBuilder()
hawaiian_pizza = pizzeria_director.order_pizza(hawaiian_builder)
hawaiian_pizza.display()