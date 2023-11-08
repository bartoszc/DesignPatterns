perimeterfrom abc import ABC, abstractmethod
from math import pi

# (1) Definicja interfejsów
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# (2) Konkretne klasy kształtów
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)

# (3) Konkretny gość
class AreaVisitor(Visitor):
    def visit_circle(self, circle):
        return pi * circle.radius * circle.radius

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

class PerimeterVisitor(Visitor):
    def visit_circle(self, circle):
        return 2 * pi * circle.radius

    def visit_rectangle(self, rectangle):
        return 2 * (rectangle.width + rectangle.height)

# Klient
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    area_visitor = AreaVisitor()
    perimeter_visitor = PerimeterVisitor()

    print(f"Circle area: {circle.accept(area_visitor)}")        # Wypisuje: Circle area: 78.53981633974483
    print(f"Circle perimeter: {circle.accept(perimeter_visitor)}") # Wypisuje: Circle perimeter: 31.41592653589793
    print(f"Rectangle area: {rectangle.accept(area_visitor)}")     # Wypisuje: Rectangle area: 24
    print(f"Rectangle perimeter: {rectangle.accept(perimeter_visitor)}") # Wypisuje: Rectangle perimeter: 20
