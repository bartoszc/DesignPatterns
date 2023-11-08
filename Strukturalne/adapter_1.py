# est to nasza "stara" klasa drukarki
class OldPrinter:
    def show(self, msg):
        print(f"Printed: {msg}")


# Jest to nasza "nowa" klasa drukarki z inną metodą o nazwie display
class NewPrinter:
    def display(self, msg):
        print(f"Displayed: {msg}")


# est to nasz adapter, który dziedziczy po OldPrinter. Zamiast jednak wykorzystywać oryginalną implementację metody
# show z klasy OldPrinter, przedefiniowuje ją, aby wykorzystywała metodę display z klasy NewPrinter. Dzięki temu, kiedy
# wywołujemy metodę show na obiekcie PrinterAdapter, faktycznie korzysta on z metody display z klasy NewPrinter.
class PrinterAdapter(OldPrinter):
    def __init__(self):
        self.new_printer = NewPrinter()

    def show(self, msg):
        self.new_printer.display(msg)


# Tworzymy instancję klasy PrinterAdapter i wywołujemy na niej metodę show. Dzięki naszemu adapterowi, mimo że
# wywołujemy show, faktyczne działanie odbywa się w metodzie display klasy NewPrinter. Dlatego też na ekranie pojawia
# się komunikat "Displayed: Hello, World!" zamiast "Printed: Hello, World!".
printer = PrinterAdapter()
printer.show("Hello, World!")
