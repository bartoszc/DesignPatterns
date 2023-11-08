# Jest to klasa bazowa (lub interfejs) dla wszystkich gier. Zawiera metody, które powinny zostać zaimplementowane przez
# konkretne klasy gier.
class Game:
    def get_name(self):
        pass

    def get_type(self):
        pass

    def get_min_number_of_players(self):
        pass

    def get_max_number_of_players(self):
        pass

    def can_be_played_remotely(self):
        pass


# BoardGame reprezentuje gry planszowe, takie jak Monopoly. Zakłada, że minimalna liczba graczy wynosi 2, a gry
# planszowe nie mogą być grane zdalnie.
class BoardGame(Game):
    def __init__(self, name, type, max_player_num):
        self._name = name
        self._type = type
        self._max_player_num = max_player_num

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return 2

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False

    def __str__(self):
        return f"{__name__} [name='{self._name}', type='{self._type}', max_player_num={self._max_player_num}]"


# PCGame reprezentuje gry komputerowe, takie jak Valorant. Może mieć różną liczbę graczy i opcję gry online.
class PCGame(Game):
    def __init__(self, name, type, min_player_num, max_player_num, is_online):
        self._name = name
        self._type = type
        self._min_player_num = min_player_num
        self._max_player_num = max_player_num
        self._is_online = is_online

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return self._min_player_num

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False

    def __str__(self):
        return (f"{__name__} [name='{self._name}', type='{self._type}', min_player_num={self._min_player_num}"
                f", max_player_num={self._max_player_num}, is_online={self._is_online}]")


# Jest to klasa bazowa (lub interfejs) dla wszystkich fabryk gier. Zawiera metodę create, która powinna zostać
# zaimplementowana przez konkretne klasy fabryk.
class GameFactory:
    def create(self):
        pass


# Są to konkretne klasy fabryk, które dziedziczą po klasie GameFactory i implementują jej metodę create.
# MonopolyGameCreator tworzy obiekt klasy BoardGame reprezentujący grę Monopoly.
class MonopolyGameCreator(GameFactory):
    def create(self):
        return BoardGame("Monopoly", "Family Game", 4)


# ValorantGameCreator tworzy obiekt klasy PCGame reprezentujący grę Valorant.
class ValorantGameCreator(GameFactory):
    def create(self):
        return PCGame("Valorant", "FPS", 4, 10, True)


# Prosi użytkownika o wprowadzenie typu gry (PC lub Board).
# Na podstawie wprowadzonego typu gry tworzy odpowiednią fabrykę gier.
# Używa fabryki do stworzenia konkretnej gry i wyświetla informacje o niej.
def main():
    game_type = input('Podaj typ gry [PC, Board]: ')
    game_factory = None
    if game_type == 'PC':
        game_factory = ValorantGameCreator()
    elif game_type == 'Board':
        game_factory = MonopolyGameCreator()

    if game_factory:
        game = game_factory.create()
        print(game)


# Jest to standardowy sposób w Pythonie na uruchomienie funkcji main, jeśli skrypt jest uruchamiany jako główny program,
# a nie importowany jako moduł.
if __name__ == '__main__':
    main()