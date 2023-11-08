# Zrozumiałe nazwy zmiennych i funkcji:
# Niech nazwy mówią czytelnikowi, co dana zmienna czy funkcja robi.
def p(d):
    return d * 3.14


def obwod_kola(diameter):
    return diameter * 3.14



#Funkcje powinny robić jedną rzecz:
#Upewnij się, że twoje funkcje są małe i skupiają się na jednym konkretnym zadaniu.
def analiza_danych(data):
    pass #obliczenia statyczne
    pass #inne obliczenia

def obliczenia_statystyczne(data):
    pass

def rysuj_wykres(data):
    pass


# Unikaj dużych ilości argumentów w funkcji:
# Im mniej argumentów, tym lepiej.
def stworz_uzytkownika(imie, nazwisko, email, haslo, adres, telefon, data_urodzenia):
    pass


class Uzytkownik:
    def __init__(self, imie, nazwisko, email, haslo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.haslo = haslo

    def dodaj_adres(self, adres):
        self.adres = adres

    def dodaj_telefon(self, telefon):
        self.telefon = telefon

    def dodaj_date_urodzenia(self, data_urodzenia):
        self.data_urodzenia = data_urodzenia
