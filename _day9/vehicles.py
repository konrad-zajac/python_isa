# Zad1) stworz klase Vehicle która będzie posiadała atrybuty:
# - type (typ pojazdu: 'szynowy', 'wolnobiezny', 'manualny', 'hipsterski'
# - wheels (int liczba kół)
# - seats (int liczba siedzen)
# - engine (obiekt typu Engine)
# - long (float długość pojazdu w metrach)
#
# metody:
# - go
# - stop
# - turn_left
# - turn_right
# - reverse
# - lights_on
# - lights_off
#
# Zad2) zaimplementuj klasy ktore będą dziedziczyły po Vehicle lub innych klasach z tej rodziny: Bicycle, Train, Car,
# Scooter, Board, Surfboard
# np. Board może dziedziczyć po Vehicle ale Surfboard już po Board (są to podobne typy i możemy usunąć podwójną
# implementację.
#
# Zad3) Chcę żeby wpisująć
# >>> print(pojazd)
# zwróciło na ekran: "Vehicle type: {type} with engine {engine} have {seets} seets, {wheels} wheels and is {long}m long"
#
# Zad4) chcę mieć możliwość porównywania dwóch pojazdów. Pojazdy są równe, jeżeli ich pola są sobie równe, oraz
# wszystkie pola Enginse są sobie równe.
#
# Zad5) Chcę mieć możliwość dodawania dwóch pojazdów do siebie. Wynikiem jest pojazd który jest długości równej sum
# długości dwóch pojazdów. Pamiętaj, że możesz dodać tylko pojazdy które są sobie równe
#
# Zad6) zrób refactoring kodu. Przenieś definicje pojazdów do różnych plików. Od Ciebie zależy jak to będzie wyglądało
# warto zaznajomić się ze sposobem podziału kodu na moduły
from res.engine import Engine
from res.other_vehicles.other_vehicles import *




class Vehicle:

    _types = ['szynowy', 'wolnobiezny', 'manualny', 'hipsterski', ]
    _directions = ['stop', 'forward', 'left', 'right', 'backward', ]

    def __init__(self, type:str, wheels:int = 1, seats:int = 0,\
            engine:Engine = None, long:float = 0):
        if type not in self._types:
            raise Exception('Nie ma takiego typu pjazdu')

        self.type = type
        self.wheels = wheels
        self.seats = seats
        self.engine = engine
        self.long = long

        self._is_moving = False
        self._is_lights = False
        self._direction = 'stop'

    def go(self):
        print('pojazd ruszył')
        self._direction = 'forward'

    def stop(self):
        print('pojazd sie zatrzymał')
        self._direction = 'stop'

    def turn_left(self):
        print('skrecam w lewo')
        self._direction = 'left'

    def turn_right(self):
        print('skrecam w prawo')
        self._direction = 'rightf'

    def reverse(self):
        if self._direction != 'stop':
            print('nie mogę cofnąc jak jesteś w ruchu')
            return
        print('cofam')

    def lights_on(self):
        pass

    def lights_off(self):
        pass

    def __str__(self):
        obj = ''
        obj+=(f'type: {self.type}')
        obj+=(f'seats: {self.seats}')
        obj+=(f'wheels: {self.wheels}')
        obj+=(f'long: {self.long}')
        if self.engine:
            obj+=(f'engine: {self.engine.h_p} ')

        wyn = str(obj)
        print('return:'+ str(type(wyn)))
        return wyn

    def __eq__(self, other):
        line='------------------------------'
        print(line)
        print(f'type:   {self.type}   vs.  {other.type} ')
        print(f'engine:{self.engine.h_p}vs.{other.engine.h_p}')
        print(f'seats:     {self.seats} vs.  {other.seats} ')
        print(f'wheels:     {self.wheels} vs.  {other.wheels} ')
        print(f'long:     {self.long} vs.  {other.long} ')
        print(line)
#    To PRAWIE działa
#    for key,val in v.__dict__.items():
#        print(str(key) +'-'+ str(val))
        if self.engine.h_p == other.engine.h_p:
            if self.seats == other.seats:
                if self.wheels == other.wheels:
                    if self.long == other.long:
                        if self.type == other.type:
                            print('return:'+ str(type(True)))
                            return True
        else:
            print('return:'+ str(type(False)))
            return False

    def __add__(self, other):
        if self.long == other.long:
            new_obj = Vehicle('manualny', wheels=2,\
                    long=self.long + other.long, seats=1)
            print('return:'+ str(type(new_obj)))
            return new_obj.long
        else:
            return "objects not equal"

if __name__ == '__main__':
    eng1= Engine('300 kM', 'pojemność dwa czterysta')
    v = Vehicle('manualny', wheels=2, long=2, seats=1)
    x = Vehicle('manualny', wheels=4, long=4, seats=4)
    v.engine = eng1
    x.engine = eng1
    print('\n---print 1 obj ---\n')
    print(v)
    print('\n---print 2 obj ---\n')
    print(x)
    print('\n---eq 1 == 1 ---\n')
    print(x == x)
    print('\n---eq 2 == 1 ---\n')
    print(v == x)
    print('\n---add 1 + 1  ---\n')
    print(x+x)
    print('\n---add 2 + 1 ---\n')
    print(v+x)
