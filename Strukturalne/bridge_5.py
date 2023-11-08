# "RemoteControl" jest klasą "abstrakcji". Reprezentuje pewne działanie
# (w tym przypadku włączanie/wyłączanie urządzenia) niezależnie od
# konkretnego urządzenia, które będzie nim kierowane.
class RemoteControl:
    def __init__(self, device):
        # Tutaj przechowujemy odniesienie do konkretnego urządzenia (TV, Radio itp.)
        self.device = device

    def toggle_power(self):
        # Niezależnie od tego, jakie urządzenie kontrolujemy,
        # używamy tej samej metody w abstrakcji (włącz/wyłącz).
        # Samo urządzenie zadecyduje, co dokładnie się stanie.
        self.device.turn_on_off()


# Implementacja: Tutaj mamy konkretne klasy urządzeń. Każde urządzenie
# ma swoją własną implementację metody "turn_on_off".
class TV:
    def turn_on_off(self):
        print("TV is toggled")

class Radio:
    def turn_on_off(self):
        print("Radio is toggled")

# Utworzenie konkretnej instancji TV.
tv = TV()
# Tworzenie pilota do sterowania TV.
# Przekazujemy instancję TV do klasy "RemoteControl".
remote_for_tv = RemoteControl(tv)
# Użycie pilota do włączenia/wyłączenia TV.
# W rzeczywistości wywołuje to metodę "turn_on_off" klasy TV.
remote_for_tv.toggle_power()

# Podobnie jak powyżej, ale dla radia.
radio = Radio()
remote_for_radio = RemoteControl(radio)
remote_for_radio.toggle_power()


# W skrócie, kod prezentuje podstawowy wzorzec "most" (bridge) w programowaniu. Ideą jest oddzielenie abstrakcji
# (takiej jak działanie pilota) od implementacji (tj. rzeczywistych urządzeń, takich jak TV czy radio). Dzięki temu
# można łatwo dodawać nowe urządzenia lub zmieniać ich zachowanie, nie wpływając na działanie pilota (abstrakcji).
