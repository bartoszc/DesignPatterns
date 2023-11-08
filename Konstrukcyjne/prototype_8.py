import copy


# W tym przykładzie mamy klasę Sheep, która reprezentuje owcę. Chcemy stworzyć kopię tej owcy, ale z możliwością
# modyfikacji niektórych jej atrybutów (np. zmiana imienia).
class Sheep:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Metoda clone w klasie Sheep używa funkcji deepcopy z modułu copy do stworzenia dokładnej kopii obiektu.
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Sheep [name='{self.name}', breed='{self.breed}']"


# Użycie wzorca Prototype:
original_sheep = Sheep("Jolly", "Merino")
print(original_sheep)

# Klonujemy owcę
cloned_sheep = original_sheep.clone()
cloned_sheep.name = "Dolly"
print(cloned_sheep)

# Sprawdzamy, czy obiekty są różne
print(original_sheep is cloned_sheep)  # Powinno wyświetlić False

# W sekcji "Użycie wzorca Prototype" tworzymy oryginalną owcę o imieniu "Jolly". Następnie klonujemy tę owcę i zmieniamy
# jej imię na "Dolly". Na końcu sprawdzamy, czy oryginalna owca i jej klon to dwa różne obiekty (co jest prawdą).
