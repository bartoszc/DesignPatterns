# Klasa bazowa
class Dish:
    def prepare_dish(self):
        self.preheat_oven()
        self.prepare_ingredients()
        self.cook()
        self.serve()

    def preheat_oven(self):
        print("Podgrzewanie piekarnika...")

    def serve(self):
        print(f"Podawanie {self.__class__.__name__} na talerzu!")

    def prepare_ingredients(self):
        print("Przygotowywanie składników...")

    def cook(self):
        print("Gotowanie...")


# Konkretne klasy potraw
class Pizza(Dish):
    def prepare_ingredients(self):
        print("Przygotowywanie ciasta, sosu i dodatków dla pizzy...")

    def cook(self):
        print("Pieczenie pizzy przez 20 minut...")


class Pasta(Dish):
    def prepare_ingredients(self):
        print("Przygotowywanie makaronu, sosu i przypraw...")

    def cook(self):
        print("Gotowanie makaronu i sosu...")


# Klient
if __name__ == "__main__":
    pizza = Pizza()
    pasta = Pasta()

    print("Przygotowywanie pizzy:")
    pizza.prepare_dish()

    print("\nPrzygotowywanie makaronu:")
    pasta.prepare_dish()
