class Employee(object):
    """ Employee class """

    employee_counter = 0

    def __init__(self, name, second_name, position = None):
        self.__name = name
        self.__second_name = second_name
        self.__position = position
        Employee.employee_counter += 1

    def print_name(self):
        print(self.__name)

    @property
    def position(self):
        if self.__position:
            return self.__position

    @position.setter
    def position(self, new_position: str):
        if new_position.isalpha():
            self.__position = new_position

    def __del__(self):
        Employee.employee_counter -= 1
