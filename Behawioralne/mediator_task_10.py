# (1) Interfejs Mediatora
class NotificationMediator:
    def notify(self, sender, event):
        pass


# (2) Konkretny Mediator
class StoreNotificationSystem(NotificationMediator):
    def notify(self, sender, event):
        if event == "NEW_PRODUCT":
            print(f"Notification to Sellers and Admins: {sender.name} added a new product!")
        elif event == "SALE":
            print(f"Notification to Customers: Sale is now live!")
        elif event == "ISSUE":
            print(f"Notification to Admins: {sender.name} reported an issue!")


# (3) Klasa bazowa dla "Użytkowników"
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_notification(self, event):
        self.mediator.notify(self, event)


# (4) Konkretne klasy użytkowników
class Customer(User):
    def send_notification(self, event):
        if event == "NEW_PRODUCT":
            print(f"{self.name} cannot add a product!")
        else:
            super().send_notification(event)


class Seller(User):
    pass


class Admin(User):
    pass


# Klient
if __name__ == "__main__":
    store_system = StoreNotificationSystem()

    alice = Customer("Alice", store_system)
    bob = Seller("Bob", store_system)
    charlie = Admin("Charlie", store_system)

    alice.send_notification("NEW_PRODUCT")  # Wypisuje: Alice cannot add a product!
    bob.send_notification("NEW_PRODUCT")    # Wypisuje: Notification to Sellers and Admins: Bob added a new product!
    charlie.send_notification("ISSUE")      # Wypisuje: Notification to Admins: Charlie reported an issue!
