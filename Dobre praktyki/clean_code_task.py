class u:
    def __init__(self, i, n, e, h):
        self.i = i
        self.n = n
        self.e = e
        self.h = h

    def da(self, a):
        self.a = a

    def dt(self, t):
        self.t = t

    def dd(self, d):
        self.d = d


def ob(d):
    return d * 3.14


def d(data):
    # obliczenia i wykres
    pass


def r(data):
    pass


# Użycie:
j = u("Jan", "Kowalski", "email@email.com", "haslo123")
j.da("Kwiatowa 5, Warszawa")
j.dd("01.01.1990")

print(j.i, j.n, j.a)
