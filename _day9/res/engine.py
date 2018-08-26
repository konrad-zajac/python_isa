
class Engine:
    def __init__(self, h_p, capacity):
        self.h_p = h_p
        self.capacity = capacity
        self.is_working = False
        self.is_moving = True


    def run(self):
        if self.is_working:
            print('no przecie jade')
            return
        print('ruszamy')
        self.is_working = True

    def stop(self):
        if not self.is_working:
            print('Silnik już dawno zgaszony ty gupku')
            return
        print('Koniec jazdy - wysiadaj')
        self.is_working = False
