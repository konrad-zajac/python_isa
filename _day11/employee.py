# Stwórz klasę Employee i ustaw w niej następujące pola (wszystkie jako prywatne)
# * name
# * second_name
# * position (default: None)
#
# napisz metodę 'print_name' która wypisze na ekranie imie pracownika
# napisz gettery i setter do pola position. Stanowisko możemy zwrócić tylko i wyłącznie jeżeli nie jest Nonem
# stanowisko możemy ustawić jeżeli ustawiana nazwa zawiera tylko i wyłącznie znaki alfanumeryczne


class Employee(object):
    """ Employee class """ 
    def __init__(self, name, second_name, position = None):
        self.__name = name
        self.__second_name = second_name
        self.__position = position 

    def print_name(self):
        print(self.__name)
    @property
    def position(self):
        if self.__position:
            return self.__position
    @position.setter
    def position(self, x):
        if x.isalpha():
            self.__position = x

e = Employee('Jan','Dzban','xyz')
e.print_name()
print(e.position)
e.position = 'zzz'
print(e.position)
