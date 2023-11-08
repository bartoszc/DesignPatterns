from abc import ABC, abstractmethod


# "Square" to abstrakcyjna klasa bazowa (interfejs) dla obiektów typu Flyweight.
class Square(ABC):

    # Każda klasa dziedzicząca po "Square" musi dostarczyć implementację metody "draw".
    @abstractmethod
    def draw(self, x, y):
        pass


# "ColoredSquare" to konkretna implementacja klasy "Square". Reprezentuje kwadrat o określonym kolorze i rozmiarze.
class ColoredSquare(Square):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def draw(self, x, y):
        print(f"Drawing square of color {self.color} and size {self.size} at position ({x}, {y})")


# "SquareFactory" to fabryka, która zarządza tworzeniem i współdzieleniem obiektów "ColoredSquare".
class SquareFactory:
    # Prywatny słownik, w którym przechowujemy już utworzone obiekty "ColoredSquare" według koloru i rozmiaru.
    _squares = {}

    @classmethod
    def get_square(cls, color, size):
        # Klucz do słownika to krotka (color, size)
        key = (color, size)

        # Sprawdzamy, czy kwadrat o danym kolorze i rozmiarze już istnieje.
        if key not in cls._squares:
            # Jeśli nie, tworzymy nowy kwadrat o tym kolorze i rozmiarze i dodajemy go do słownika.
            cls._squares[key] = ColoredSquare(color, size)
            print(f"Creating square of color {color} and size {size}")

        # Zwracamy istniejący lub nowo utworzony obiekt "ColoredSquare".
        return cls._squares[key]


# Tworzenie i rysowanie kwadratów przy użyciu fabryki:
square1 = SquareFactory.get_square("Green", 5)  # Tworzy nowy kwadrat o kolorze zielonym i rozmiarze 5.
square1.draw(10, 10)

square2 = SquareFactory.get_square("Yellow", 8)  # Tworzy nowy kwadrat o kolorze żółtym i rozmiarze 8.
square2.draw(20, 20)

square3 = SquareFactory.get_square("Green",
                                   5)  # Używa istniejącego kwadratu o kolorze zielonym i rozmiarze 5 (nie tworzy nowego).
square3.draw(30, 30)
