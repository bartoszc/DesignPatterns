# Jest to klasa bazowa (lub interfejs) dla wszystkich samochodów. Zawiera metody, które powinny zostać zaimplementowane
# przez konkretne klasy samochodów.
class Car:
    def get_type(self):
        pass

    def get_model_name(self):
        pass

    def get_cylinders_num(self):
        pass

    def get_producer(self):
        pass

    def get_engine_volume(self):
        pass

    def get_trunk_size(self):
        pass


# Jest to abstrakcyjna klasa samochodu, która dziedziczy po klasie Car i implementuje metodę __str__, która pozwala na
# ładne wyświetlanie informacji o samochodzie.
class AbstractCar(Car):
    def __str__(self):
        return (f"Car: {self.get_producer()} {self.get_model_name()} {self.get_type()} has {self.get_cylinders_num()} "
                f"cylinders and engine {self.get_engine_volume()} and trunk size {self.get_trunk_size()} litres")


class ToyotaCorolla(AbstractCar):
    def get_model_name(self):
        return "Corolla"

    def get_producer(self):
        return "Toyota"


# są konkretnymi implementacjami różnych modeli i typów samochodów. Każda z tych klas implementuje odpowiednie metody
# z klasy bazowej Car.
class ToyotaCorollaCombi(ToyotaCorolla):
    def get_type(self):
        return "Combi"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.6

    def get_trunk_size(self):
        return 540


class ToyotaCorollaHatchback(ToyotaCorolla):
    def get_type(self):
        return "Hatchback"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 2.0

    def get_trunk_size(self):
        return 350


class ToyotaCorollaSedan(ToyotaCorolla):
    def get_type(self):
        return "Sedan"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.8

    def get_trunk_size(self):
        return 420


class AudiA4(AbstractCar):
    def get_model_name(self):
        return "A4"

    def get_producer(self):
        return "Audi"


class AudiA4Combi(AudiA4):
    def get_type(self):
        return "Combi"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.8

    def get_trunk_size(self):
        return 520


class AudiA4Hatchback(AudiA4):
    def get_type(self):
        return "Hatchback"

    def get_cylinders_num(self):
        return 6

    def get_engine_volume(self):
        return 2.4

    def get_trunk_size(self):
        return 300


class AudiA4Sedan(AudiA4):
    def get_type(self):
        return "Sedan"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 2.0

    def get_trunk_size(self):
        return 450


# Jest to klasa bazowa (lub interfejs) dla wszystkich fabryk samochodów. Zawiera metody, które powinny zostać
# zaimplementowane przez konkretne klasy fabryk.
class CarFactory:
    def create_combi(self):
        pass

    def create_hatchback(self):
        pass

    def create_sedan(self):
        pass


class ToyotaCorollaFactory(CarFactory):
    def create_combi(self):
        return ToyotaCorollaCombi()

    def create_hatchback(self):
        return ToyotaCorollaHatchback()

    def create_sedan(self):
        return ToyotaCorollaSedan()


# są konkretnymi fabrykami, które dziedziczą po klasie CarFactory i implementują jej metody. Te fabryki tworzą konkretne
# modele i typy samochodów.
class AudiA4Factory(CarFactory):
    def create_combi(self):
        return AudiA4Combi()

    def create_hatchback(self):
        return AudiA4Hatchback()

    def create_sedan(self):
        return AudiA4Sedan()


# Jest to klasa pomocnicza, która dostarcza odpowiednią fabrykę na podstawie podanego typu fabryki. Używa metody
# statycznej create_factory do zwracania odpowiedniej fabryki.
class FactoryProvider:
    @staticmethod
    def create_factory(factory_type):
        if factory_type == 'T':
            return ToyotaCorollaFactory()
        elif factory_type == 'A':
            return AudiA4Factory()
        else:
            return None


# Prosi użytkownika o wprowadzenie typu fabryki (A dla Audi lub T dla Toyoty).
# Na podstawie wprowadzonego typu fabryki tworzy odpowiednią fabrykę.
# Używa fabryki do stworzenia konkretnego modelu samochodu (w tym przypadku hatchback) i wyświetla informacje o nim.
def main():
    factory_type = input('Jakie auto chcesz produkować - wybierz A lub T: ')
    factory = FactoryProvider.create_factory(factory_type)

    if factory:
        hatchback = factory.create_hatchback()
        print(hatchback)


if __name__ == '__main__':
    main()