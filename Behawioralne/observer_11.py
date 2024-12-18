# (1) Interfejs Observer
class Observer:
    def update(self, message):
        pass


# (2) Interfejs Subject
class Subject:
    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass


# (3) Konkretny Subject - Newsletter
class Newsletter(Subject):
    def __init__(self):
        self._observers = []
        self._latest_message = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._latest_message)

    def add_message(self, message):
        self._latest_message = message
        self.notify_observers()


# (4) Konkretny Observer - Subscriber
class Subscriber(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


# Klient
if __name__ == "__main__":
    newsletter = Newsletter()

    bob = Subscriber("Bob")
    alice = Subscriber("Alice")

    newsletter.add_observer(bob)
    newsletter.add_observer(alice)

    newsletter.add_message("This is the first message!")  # Wypisuje:
    # Bob received message: This is the first message!
    # Alice received message: This is the first message!
