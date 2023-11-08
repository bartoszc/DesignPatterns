# Importujemy niezbędne klasy do tworzenia klas abstrakcyjnych i metod abstrakcyjnych.
from abc import ABC, abstractmethod

# "Employee" jest klasą bazową dla wszystkich pracowników. Działa jako interfejs,
# który muszą zaimplementować wszystkie jego podklasy.
class Employee(ABC):

    # Definiujemy abstrakcyjną metodę, co oznacza, że każda podklasa tej klasy
    # musi dostarczyć własną implementację tej metody.
    @abstractmethod
    def show_details(self):
        pass

# "Developer" to konkretna klasa reprezentująca pojedynczego pracownika-programistę.
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Dostarczamy implementację metody "show_details" dla klasy Developer.
    def show_details(self):
        print(f"{self.name} - {self.position}")

# "Manager" to inna klasa pracownika, która może mieć pod sobą innych pracowników.
class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        # Lista podwładnych pracowników.
        self.subordinates = []

    # Metoda umożliwiająca dodanie pracownika do listy podwładnych.
    def add(self, employee):
        self.subordinates.append(employee)

    # Metoda umożliwiająca usunięcie pracownika z listy podwładnych.
    def remove(self, employee):
        self.subordinates.remove(employee)

    # Dostarczamy implementację metody "show_details" dla klasy Manager.
    # Pokazuje ona nie tylko szczegóły menedżera, ale również wszystkich jego podwładnych.
    def show_details(self):
        print(f"{self.name} - {self.position}")
        for subordinate in self.subordinates:
            subordinate.show_details()

# Tworzymy obiekty pracowników i menedżera.
developer1 = Developer("Jan Kowalski", "Developer")
developer2 = Developer("Anna Nowak", "Developer")

manager = Manager("Robert Wiśniewski", "Manager IT")
manager.add(developer1)
manager.add(developer2)

# Wywołujemy metodę show_details, aby zobaczyć szczegóły menedżera i jego podwładnych.
manager.show_details()


# Ten kod ilustruje wzorzec projektowy "Kompozyt" (Composite), który pozwala na tworzenie hierarchicznych struktur
# obiektów, w których pojedyncze obiekty oraz ich kompozycje są traktowane jednolicie.