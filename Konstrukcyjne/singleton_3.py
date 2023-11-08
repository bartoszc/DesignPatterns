def Singleton(class_):
    # słownik, który przechowuje instancje klas.
    __instances = {}

    # funkcja wewnętrzna, która sprawdza, czy instancja klasy już istnieje. Jeśli nie, tworzy ją i zapisuje w słowniku
    # __instances. Następnie zwraca tę instancję.
    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    # zwraca funkcję get_instance, która zastępuje konstruktor klasy.
    return get_instance


# Klasy FirstClass i SecondClass są dekorowane przez Singleton. Oznacza to, że próba utworzenia instancji tych klas
# faktycznie wywołuje funkcję get_instance.
@Singleton
class FirstClass:
    def __init__(self):
        self.val = 0


@Singleton
class SecondClass:
    def __init__(self):
        self.val = 0


# Tworzy instancję klasy FirstClass. Ponieważ jest to pierwsza instancja, zostaje ona zapisana w słowniku __instances.
a = FirstClass()
# Wyświetla wartość 0, ponieważ jest to domyślna wartość val dla klasy FirstClass.
print(a.val)
a.val = 10
# Próbuje utworzyć kolejną instancję klasy FirstClass, ale zamiast tego zwraca już istniejącą instancję (czyli a).
b = FirstClass()
print(b.val)

c = SecondClass()
print(c.val)
c.val = 20
d = SecondClass()
print(d.val)

# Dzięki temu wzorcowi Singleton, mimo wielokrotnego "tworzenia" instancji klasy, faktycznie otrzymujemy za każdym razem
# tę samą instancję.
