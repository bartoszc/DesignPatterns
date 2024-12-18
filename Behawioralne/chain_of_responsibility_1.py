# Abstrakcyjna klasa Handler definiuje interfejs dla obsługi żądań.
# Posiada również opcjonalne pole, które wskazuje na następny obiekt w łańcuchu.
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

# Klasa ConcreteHandlerA obsługuje żądanie tylko jeśli jest to liczba parzysta.
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request % 2 == 0:
            print(f"ConcreteHandlerA obsługuje żądanie dla {request}")
        elif self.successor:
            self.successor.handle_request(request)

# Klasa ConcreteHandlerB obsługuje żądanie tylko jeśli jest to liczba nieparzysta.
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request % 2 != 0:
            print(f"ConcreteHandlerB obsługuje żądanie dla {request}")
        elif self.successor:
            self.successor.handle_request(request)

if __name__ == "__main__":
    # Tworzymy łańcuch odpowiedzialności: ConcreteHandlerA -> ConcreteHandlerB
    handler_chain = ConcreteHandlerA(ConcreteHandlerB())

    # Przesyłamy różne żądania do łańcucha odpowiedzialności.
    requests = [1, 2, 3, 4, 5]

    for req in requests:
        handler_chain.handle_request(req)
