
class Animal:

    legs = None
    head = None
    eyes = 2
    _max_speed = 12

    def __init__(self, legs: list = None):
        print('init invoked')
        self.legs = []
        if legs:
            self.legs = legs
        self.speed = 0
        self.eyes = 3

    def run(self):
        self.speed = 10

    def faster(self, increment: int = 1):
        if not self.speed >= self._max_speed:
            self.speed += increment
            return
        self.speed = self._max_speed


    def slower(self):
        self.speed -= 1

    def stop(self):
        self.speed = 0


print(Animal.eyes)
dog = Animal()
dog.legs.append('left')
dog.legs.append('right')
dog.run()
dog.faster(increment=2)
# dog.faster()
# dog.speed = 17
# dog.faster()
dog.legs.append('tylna lewa')
print(dog.speed)
cat = Animal(legs = ['przednia prawa', 'przednia lewa', 'tylna prawa'])
print(cat.legs)

Animal.legs
