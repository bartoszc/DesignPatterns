from abc import ABC, abstractmethod

# Flyweight to wzorzec projektowy, który pozwala na współdzielenie danych między wieloma obiektami
# w celu zmniejszenia zużycia pamięci i zwiększenia wydajności.

# "Shape" to abstrakcyjna klasa bazowa (interfejs) dla obiektów typu Flyweight.
class Shape(ABC):

    # Każda klasa dziedzicząca po "Shape" musi dostarczyć implementację metody "draw".
    @abstractmethod
    def draw(self, x, y):
        pass

# "Circle" to konkretna implementacja klasy "Shape". Reprezentuje okrąg o określonym kolorze.
class Circle(Shape):
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        print(f"Drawing circle of color {self.color} at position ({x}, {y})")

# "ShapeFactory" to fabryka, która zarządza tworzeniem i współdzieleniem obiektów "Circle".
class ShapeFactory:
    # Prywatny słownik, w którym przechowujemy już utworzone obiekty "Circle" według koloru.
    _circles = {}

    @classmethod
    def get_circle(cls, color):
        # Sprawdzamy, czy okrąg o danym kolorze już istnieje.
        if color not in cls._circles:
            # Jeśli nie, tworzymy nowy okrąg o tym kolorze i dodajemy go do słownika.
            cls._circles[color] = Circle(color)
            print(f"Creating circle of color {color}")
        # Zwracamy istniejący lub nowo utworzony obiekt "Circle".
        return cls._circles[color]

# Tworzenie i rysowanie okręgów przy użyciu fabryki:
circle1 = ShapeFactory.get_circle("Red")  # Tworzy nowy okrąg o kolorze czerwonym.
circle1.draw(10, 10)

circle2 = ShapeFactory.get_circle("Blue")  # Tworzy nowy okrąg o kolorze niebieskim.
circle2.draw(20, 20)

circle3 = ShapeFactory.get_circle("Red")  # Używa istniejącego okręgu o kolorze czerwonym (nie tworzy nowego).
circle3.draw(30, 30)
