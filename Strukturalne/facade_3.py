# Podsystem: Skomplikowane elementy, które chcemy uprościć.

# Klasa reprezentująca telewizor z podstawowymi funkcjami.
class Television:
    def turn_on(self):
        print("Television turned on")

    def turn_off(self):
        print("Television turned off")

# Klasa reprezentująca odtwarzacz DVD z podstawowymi funkcjami.
class DVDPlayer:
    def play(self):
        print("Movie is playing")

    def stop(self):
        print("Movie stopped")

# Klasa reprezentująca oświetlenie z podstawowymi funkcjami.
class Lights:
    def dim(self):
        print("Lights dimmed")


# Uproszczony interfejs do powyższego podsystemu.
# Fasada (Facade) służy do uproszczenia interfejsu zestawu klas w podsystemie.
class HomeTheaterFacade:
    # Konstruktor przyjmuje referencje do obiektów kluczowych elementów podsystemu.
    def __init__(self, television, dvd, lights):
        self.television = television
        self.dvd = dvd
        self.lights = lights

    # Metoda start_movie() wywołuje odpowiednie metody z klas podsystemu w odpowiedniej kolejności.
    def start_movie(self):
        self.television.turn_on()
        self.lights.dim()
        self.dvd.play()

    # Podobnie, end_movie() kończy oglądanie filmu, wywołując odpowiednie metody.
    def end_movie(self):
        self.dvd.stop()
        self.television.turn_off()

# Tworzymy obiekty dla każdej z klasy podsystemu.
television = Television()
dvd = DVDPlayer()
lights = Lights()

# Tworzymy obiekt fasady, dostarczając jej potrzebne obiekty z podsystemu.
home_theater = HomeTheaterFacade(television, dvd, lights)

# Teraz, zamiast wywoływać poszczególne metody z każdej klasy, możemy użyć uproszczonego interfejsu fasady.
home_theater.start_movie()
home_theater.end_movie()


# Wzorzec projektowy "Facade" (Fasada) pozwala ukryć skomplikowaną logikę wewnętrznego systemu za prostym interfejsem.
# Ułatwia to korzystanie z systemu przez klienta, ponieważ klient nie musi znać szczegółów wewnętrznych działania
# systemu. W tym przypadku zamiast wywoływać metody różnych urządzeń, klient może po prostu wywołać dwie metody:
# start_movie() i end_movie(), aby uzyskać oczekiwane działanie.