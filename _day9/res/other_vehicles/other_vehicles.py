from vehicles import Vehicle
class Bicycle(Vehicle):

    def __init__(self, long:float = 0):
        super(self, Bicycle).__init__('manualny', wheels=2, seats=1,\
                engine=None, long=long)
class Train(Vehicle):

    def __init__(self, long:float = 100):
        super(self, Train).__init__('szyowny', wheels=200, seats=100,\
 engine=None, long=long)
        
class Car(Vehicle):

    def __init__(self, long:float = 2):
        super(self, Car).__init__('wolnobiezny', wheels=4, seats=2,\
 engine=None, long=long)

class Scooter(Vehicle):

    def __init__(self, long:float = 1.5):
        super(self, Scooter).__init__('wolnobiezny', wheels=2, seats=2,\
 engine=None, long=long)

class Board(Vehicle):

    def __init__(self, long:float = 1.5):
        super(self, Board).__init__('wolnobiezny', wheels=2, seats=2,\
 engine=None, long=long)

class SurfBoard(Board):

    def __init__(self, long:float = 1.5):
        super(self, Board).__init__('wolnobiezny', wheels=2, seats=2,\
                engine=None,long=long)
