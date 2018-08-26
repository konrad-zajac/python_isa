class Home:
    def __init__(self, doors: int = 1, windows: int = 0, area: int = 1, color: str = 'white',
                 materials: str = 'wood', owner: str = 'Wiktor'):

        self.__owner = owner
        self.__is_finished = False
        self.doors = doors
        self.windows = windows
        self.area = area
        self.color = color
        self.__materials = materials

    @property
    def materials(self):
        return self.__materials

    @materials.setter
    def materials(self, materials):
        if not self.__is_finished:
            self.__materials = materials
            return
        raise Exception('home is finished')

    def finish_building(self, person_who_is_closing):
        if self.__owner == person_who_is_closing:
            self.__is_finished = True
            return
        raise Exception('you are not an owner of this building')

    def __str__(self):
        return f'Home with {self.doors} doors, {self.windows} windows and {self.area}m area.'\
               f'Is {self.color} and is made of {self.materials}'

if __name__ == '__main__':
    my_home = Home(doors=1, windows=7, area=86, color='pink', materials='brick')

    my_home.materials = 'wood'
    # my_home.finish_building('Wiktor')
    my_home.materials = 'steel'


    print(my_home)

