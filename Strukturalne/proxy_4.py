# Podstawowa klasa abstrakcyjna Image, która definiuje interfejs obrazu.
class Image:
    def display(self):
        pass

# Klasa RealImage reprezentuje prawdziwy obiekt, który chcemy "chronić" za proxy.
# Za każdym razem, gdy jest tworzony, obraz jest ładowany z dysku.
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading image {self.filename}")

    def display(self):
        print(f"Displaying image {self.filename}")

# Klasa ProxyImage działa jako zastępca dla prawdziwego obrazu.
# Jej głównym celem jest opóźnienie ładowania obrazu z dysku, dopóki nie jest to konieczne.
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        # Jeśli prawdziwy obraz nie został jeszcze załadowany, ładowane jest to teraz.
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        # Wywołanie metody display() prawdziwego obrazu.
        self.real_image.display()

# Tworzymy obiekt proxy z nazwą pliku obrazu.
image = ProxyImage("example_photo.jpg")

# Za pierwszym razem obraz jest ładowany z dysku, ponieważ prawdziwy obraz jeszcze nie został załadowany.
image.display()

# Teraz obraz jest już załadowany, więc proxy tylko wyświetla go bez ponownego ładowania.
image.display()


# Wzorzec Proxy działa jako "zastępca" lub "pośrednik" dla innego obiektu. W tym przypadku ProxyImage służy jako
# zastępca dla RealImage. Główną zaletą tego podejścia jest możliwość opóźnienia pewnych kosztownych operacji
# (takich jak ładowanie obrazu z dysku) do momentu, kiedy są one naprawdę potrzebne. W tym przypadku obraz jest
# ładowany tylko przy pierwszym wywołaniu metody display(), a kolejne wywołania tej metody korzystają z już załadowanego
# obrazu.
