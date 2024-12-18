# Klasa odbiorcy
class Television:
    def __init__(self):
        self.is_on = False
        self.channel = 1

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Telewizor włączony.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Telewizor wyłączony.")

    def change_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print(f"Kanał zmieniony na: {self.channel}")


# Interfejs dla poleceń
class Command:
    def execute(self):
        pass


# Konkretne klasy poleceń
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()


class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()


class ChangeChannelCommand(Command):
    def __init__(self, device, channel):
        self.device = device
        self.channel = channel

    def execute(self):
        self.device.change_channel(self.channel)


# Klasa inicjatora
class RemoteControl:
    def press_button(self, command):
        command.execute()


# Test
tv = Television()
remote = RemoteControl()

# Włącz telewizor
on_command = TurnOnCommand(tv)
remote.press_button(on_command)

# Zmień kanał na 5
change_channel_command = ChangeChannelCommand(tv, 5)
remote.press_button(change_channel_command)

# Wyłącz telewizor
off_command = TurnOffCommand(tv)
remote.press_button(off_command)
