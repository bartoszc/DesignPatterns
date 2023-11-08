class CentralProcessingUnit:
    def start(self):
        print("CPU started")

    def execute(self):
        print("CPU is executing commands")

    def stop(self):
        print("CPU stopped")


class RandomAccessMemory:
    def load(self, position, data):
        print(f"Loading data '{data}' onto position {position} in RAM")

    def free(self, position):
        print(f"Freeing position {position} in RAM")


class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from LBA {lba}")
        return "system_data"

    def write(self, lba, data):
        print(f"Writing data to LBA {lba}")


class ComputerFacade:
    def __init__(self, cpu, ram, hd):
        self.cpu = cpu
        self.ram = ram
        self.hd = hd

    def start_computer(self):
        # Proces startowy komputera
        data = self.hd.read(0, 1024)
        self.ram.load(0, data)
        self.cpu.start()
        self.cpu.execute()

    def shut_down_computer(self):
        # Proces wyłączania komputera
        self.cpu.stop()
        self.ram.free(0)
        print("Computer shut down")


cpu = CentralProcessingUnit()
ram = RandomAccessMemory()
hd = HardDrive()

computer = ComputerFacade(cpu, ram, hd)
computer.start_computer()
print("---")
computer.shut_down_computer()
