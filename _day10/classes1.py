class Math:

    @staticmethod
    def min(first, last):
        if first > last:
            return last
        return first

    @staticmethod
    def max(first, last):
        if first > last:
            return first
        return last


class Employee:

    annual_raise = 1000

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return 'Imie: {}, nazwisko: {}, roczna podwyzka: {}'.format(self.imie, self.nazwisko, self.annual_raise)

    def __add__(self, other):
        emp = Employee(self.imie + other.imie, self.nazwisko+other.nazwisko)
        return emp

    @classmethod
    def change_annual_raise(cls, new_raise):
        cls.annual_raise = new_raise

    @staticmethod
    def nakrzycz():
        print('Jestes guuupi!!!!!!!')


    @classmethod
    def initialise_with_raise(cls, imie, nazwisko, new_raise):
        # alternatywny konstruktor
        employee = cls(imie, nazwisko)
        employee.annual_raise = new_raise
        return employee



print(max(12, 10))


# Employee.nazwisko = 'Rutka'

wiktor = Employee('wiktor', 'rutka')
print(wiktor)

#alternatywny konstruktor
konrad = Employee.initialise_with_raise('konrad', 'zajac', 4000)
print(konrad)
anna = Employee.initialise_with_raise('anna', 'hawryluk', 12000)
print(anna)

klaudia = Employee('klaudia', 'schiffer')
print(klaudia)
Employee.nakrzycz()
