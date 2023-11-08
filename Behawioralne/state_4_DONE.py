# (1) Interfejs Stanu
class State:
    def handle(self, context):
        pass


# (2) Konkretyne stany
class RedLight(State):
    def handle(self, context):
        print("Red light is on. Wait!")
        context.state = GreenLight()


class GreenLight(State):
    def handle(self, context):
        print("Green light is on. Go!")
        context.state = YellowLight()


class YellowLight(State):
    def handle(self, context):
        print("Yellow light is on. Prepare to stop!")
        context.state = RedLight()


# (3) Kontekst - Semafor
class TrafficLight:
    def __init__(self):
        self.state = RedLight()

    def change(self):
        self.state.handle(self)


# Klient
if __name__ == "__main__":
    light = TrafficLight()

    light.change()  # Wypisuje: Red light is on. Wait!
    light.change()  # Wypisuje: Green light is on. Go!
    light.change()  # Wypisuje: Yellow light is on. Prepare to stop!
