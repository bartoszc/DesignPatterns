# Klasa Command (Polecenie) definiująca interfejs dla wykonania operacji
class Command:
    def execute(self):
        pass


# Konkretna klasa Command, która realizuje operację włączenia światła
class LightOnCommand(Command):
    def __init__(self, light):
        # Tutaj przekazujemy referencję do obiektu, który będzie odbiorcą polecenia
        self._light = light

    def execute(self):
        # Wywołanie metody obiektu odbiorcy
        self._light.turn_on()


# Konkretna klasa Command, która realizuje operację wyłączenia światła
class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()


# Odbiorca - klasa, która faktycznie wykonuje operację
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


# Klasa Invoker - używa polecenia do wykonania żądania
class RemoteControl:
    def __init__(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()


# Klient
if __name__ == "__main__":
    # Tworzenie obiektu odbiorcy
    light = Light()

    # Tworzenie konkretnych poleceń i przekazanie obiektu odbiorcy
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Użycie Invokera do wywołania poleceń
    remote = RemoteControl(light_on)
    remote.press_button()  # Light is ON

    remote = RemoteControl(light_off)
    remote.press_button()  # Light is OFF
