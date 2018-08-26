from person import Persons
persons = [
    ('Wiktor', 'Rutka', 'Podgórna', 14),
    ('Antoni', 'Wagner', 'Maciejkowa', 1),
    ('Bożydar', 'Brzęczyk', 'Organowa', 1412),
    ('Bożysław', 'Rowerek', 'Łebska', 10),
    ('Karolina', 'Karaś', 'Fioletowa', 29),
]

# [
#     {'imie': 'wiktor', 'nazwisko': 'rutka'},
#     {'imie': 'Antorni', 'nazwisko': 'wagner'},
# ]
def p_foo (lis):
    new_people = []

    for ele in lis:
        new_person = (ele[1],
                ele[2],
                ele[3],
                ele[4])
        new_people.append(new_person)
    return new_people

print(p_foo(persons))



