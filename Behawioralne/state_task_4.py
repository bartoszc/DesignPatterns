# Klasy stanów
class OnState:
    def switch(self, light):
        print("Light is OFF!")
        light.state = OffState()

class OffState:
    def switch(self, light):
        print("Light is ON!")
        light.state = OnState()

# Klasa Light
class Light:
    def __init__(self):
        self.state = OffState()

    def toggle(self):
        self.state.switch(self)

# Test
lamp = Light()
lamp.toggle()  # Powinno wyświetlić "Light is ON!"
lamp.toggle()  # Powinno wyświetlić "Light is OFF!"
lamp.toggle()  # Powinno wyświetlić "Light is ON!"