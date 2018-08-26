class Person:
    def __init__(self, imie: str, nazwisko: str, ulica: str, numer: int):
        self.__name = imie
        self.__second_name = nazwisko
        self.ulica = ulica
        self.numer = numer

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, second_name):
        self.__second_name = second_name


wiktor = Person('wiktor', 'rutka', 'costam', 12)

persons = [
    ('Wiktor', 'Rutka', 'Podgórna', 14),
    ('Antoni', 'Wagner', 'Maciejkowa', 1),
    ('Bożydar', 'Brzęczyk', 'Organowa', 1412),
    ('Bożysław', 'Rowerek', 'Łebska', 10),
    ('Karolina', 'Karaś', 'Fioletowa', 29),
]

ludzie_ktorych_kocham = [
    ('Wiktor', 'Rutka', 'Podgórna', 14),
    ('Antoni', 'Wagner', 'Maciejkowa', 1),
]


def generate_persons(persons_arg):
    new_persons = []

    for ele in persons_arg:
        new_person = {
            'imie': ele[0],
            'nazwisko': ele[1],
            'ulica': ele[2],
            'nr': ele[3]
        }
        new_persons.append(new_person)
    return new_persons


# new_persons = generate_persons(persons)

new_persons = generate_persons(ludzie_ktorych_kocham)

print(new_persons)