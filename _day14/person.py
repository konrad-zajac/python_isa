class Persons:

    def __init__(self, imie: str, nazwisko: str, ulica: str, numer: int):

        self.__imie = imie
        self.__nazwisko = nazwisko
        self.ulica = ulica
        self.numer = numer


    @property
    def imie(self):
            return self.__imie


    @imie.setter
    def imie(self, new_imie: str):
        if new_imie.isalpha():
            self.__imie = new_imie


    @property
    def nazwisko(self):
        if self.__nazwisko:
            return self.__nazwisko


    @nazwisko.setter
    def nazwisko(self, new_nazwisko: str):
        if new_nazwisko.isalpha():
            self.__nazwisko = new_nazwisko


