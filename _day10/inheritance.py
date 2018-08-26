class Zwierze:
    """tylko kregowce"""
    def __init__(self):
        print('init zwierzecia')
        self.buzia = 1

    def speak(self):
        print('Zwierze mowi: nie wiem czy umiem sprechać')


class Kon(Zwierze):

    def __init__(self):
        super().__init__()
        print('jestem w Kon.__init__')
        self.imie = 'rafal'

    def speak(self):
        print('Kon mowi: ihhhahahahhhha')


class Osiol(Zwierze):

    def __init__(self):
        print('jestem w Osiol.__init__')
        self.imie = 'przyjaciel shreka'
        super().__init__()

    def speak(self):
        print('Osioł mowi: iha iha iha')


class Mul(Osiol, Kon):

    def __init__(self):
        print('jestem w Mul.__init__')
        self.imie = 'nie w szczepionke'
        super().__init__()

    def speak(self):
        print('nie wiedm co mam mowic. jestem mul')

        # this method should be invoked from class Osiol
        super().speak()


kon = Kon()
print('--- po koniu')
osiol = Osiol()
print('--- po osle')
mul = Mul()
print('--- po mule')

print('---------------')

kon.speak()
print('--- po koniu')
osiol.speak()
print('--- po osle')
mul.speak()
print('--- po mule')
