# dane
<<<<<<< HEAD
monety = [5, 2, 1, 0.5, 0.2, 0.1]
=======
monety =        [5, 2, 1, 0.5, 0.2, 0.1]
>>>>>>> dfebec1287f51467043e5b0cef579c57bc26b8ef
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup

# indeks do trzymania pozycji listy
indeks_mon_reszta = 0

for moneta in monety:
    import pudb; pudb.set_trace()
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta = reszta - wartosc

        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

<<<<<<< HEAD
print("Reszta do wydania:")
=======
print("Reszta do wydania:")
>>>>>>> dfebec1287f51467043e5b0cef579c57bc26b8ef
