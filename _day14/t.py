
persons = [
    ('Wiktor', 'Rutka', 'Podgórna', 14),
    ('Antoni', 'Wagner', 'Maciejkowa', 1),
    ('Bożydar', 'Brzęczyk', 'Organowa', 1412),
    ('Bożysław', 'Rowerek', 'Łebska', 10),
    ('Karolina', 'Karaś', 'Fioletowa', 29),
]
def generate_persons(persons_arg):
    new_persons = []
    keys = ['imie', 'nazwisko', 'ulica', 'nr']
    new_person = {key: val for (key, val) in zip(keys, ele)}
    new_persons.append(new_person)
    return new_persons


new_persons = generate_persons(persons)
print(new_persons)
