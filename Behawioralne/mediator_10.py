# (1) Interfejs Mediatora
class Mediator:
    def notify(self, sender, event):
        pass


# (2) Konkretny Mediator - ChatRoom
class ChatRoom(Mediator):
    def notify(self, sender, event):
        if event == "MESSAGE":
            print(f"ChatRoom: {sender.name} sends a message")


# (3) Klasa bazowa dla "Kolegów"
class Colleague:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self):
        self.mediator.notify(self, "MESSAGE")


# (4) Konkretny "Kolega" - User
class User(Colleague):
    def message(self):
        print(f"{self.name}: Sending message...")
        self.send_message()


# Klient
if __name__ == "__main__":
    room = ChatRoom()

    john = User("John", room)
    anna = User("Anna", room)

    john.message()  # Wypisuje: John: Sending message...
    # ChatRoom: John sends a message
