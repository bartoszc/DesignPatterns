# Klasa Momento przechowuje stan obiektu Originator.
# W tym przykładzie jest to tylko jedno pole, ale może być dowolnie skomplikowane.
class Momento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Klasa Originator posiada pewien wewnętrzny stan, który chcemy zapisywać i przywracać.
class Originator:
    def __init__(self, state):
        self._state = state

    # Tworzenie momentu przechowującego aktualny stan.
    def create_momento(self):
        return Momento(self._state)

    # Przywracanie stanu obiektu Originator do stanu zapisanego w momencie.
    def restore(self, momento):
        self._state = momento.get_state()

    # Prosta metoda do zmiany stanu obiektu Originator (dla demonstracji).
    def change_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Klasa opiekuna (Caretaker) przechowuje historię stanów.
class Caretaker:
    def __init__(self, originator):
        self._momentos = []
        self._originator = originator

    def backup(self):
        self._momentos.append(self._originator.create_momento())

    def undo(self):
        if not self._momentos:
            return
        last_momento = self._momentos.pop()
        self._originator.restore(last_momento)



originator = Originator("Stan początkowy")
caretaker = Caretaker(originator)

caretaker.backup()  # Zapisujemy początkowy stan.
originator.change_state("Stan 1")
caretaker.backup()  # Zapisujemy stan po pierwszej zmianie.

originator.change_state("Stan 2")
print(originator.get_state())  # Powinno wyświetlić "Stan 2"

caretaker.undo()  # Przywracamy ostatni zapisany stan.
print(originator.get_state())  # Powinno wyświetlić "Stan 1"

caretaker.undo()  # Przywracamy początkowy stan.
print(originator.get_state())  # Powinno wyświetlić "Stan początkowy"
