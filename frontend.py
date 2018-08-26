
#!/usr/bin/python5
from day.day2.foo_2_1 import string_operations

from day.day3.is_div_357 import is_div_357
from day.day3.ttto import ttto
from day.day3.seasons import seasons
from day.day3.temp_conv_fc import temp_conv_fc

from day.day4.pswd_foo import pswd_foo 
from day.day4.tree_foo import tree_foo
from day.day4.matrix_list import matrix_list
from day.day4.distinct_list import distinct_list
from day.day4.fibonacci import fibonacci

from day.day5.foo_5 import max_arr
from day.day5.foo_5 import mul_arr
from day.day5.foo_5 import foo_sorted_s
from day.day5.foo_5 import foo_is_palindrome

from day.day6.foo_6 import read_lorem
from day.day6.foo_6 import with_foo
#foo_6_1,foo_6_2, foo_6_3, foo_6_4, foo_6_5
welcome_message = """
Info Share Academy Homework
-----------day-2-----------
Input_21: String operations
-----------day-3-----------
Input31 - Is deviseble by
        3,5 and 7
Input_32: tic tac toe
Input_33: Insert month
        and day and
        output the season
Input_34: Convert  C to F
        and F to C
-----------day-4-----------
Input_41: Password
Input_42: X-mas tree
Input_43: Print list like
        matrix
Input_44: Create a distinct
          list
Input_45: Write out numbers
         in fibonaccis
         sequence
-----------day-5-----------
Input_51: Write out numbers
         in fibonaccis
         sequence
Input_52: Max out of arr
Input_53: Multipy each
         element of a list
Input_54: Sort surnames
Input_55: If palindrome
         return true
-----------day-6-----------
Input_61:read_lorem
Input_62:with function
Input_63:
Input_64:
Input_65:
Input_66:

"""
options = {
'0': exit,
'21': string_operations,
'31': is_div_357,
'32': ttto,
'33': seasons,
'34': temp_conv_fc,
'41': pswd_foo,
'42': tree_foo,
'43': matrix_list,
'44': distinct_list,
'45': fibonacci,
'51': fibonacci,
'52': max_arr,
'53': mul_arr,
'54': foo_sorted_s,
'55': foo_is_palindrome,
'61': read_lorem,
'62': with_foo,
#'63':,
#'64':,
#'65':,
#'66':,
}

r = 0
response = "4"
while response != "0":
    if r == 0:
        response = input(welcome_message)


    if response not in options.keys():
        print('podaj prawidlowa opcje')
        continue
    inp=input('is there an input, [0] - yes [1] - no n')
    if inp == '1':
        options[response]()
    else:
        options[response](inp)


    r = int(input('Do you want to restart[0] or quit[1]?'))

    if r == 1:
        raise SystemExit
#while response != 0:
#    respose = input(welcome_message)
#    if response not in options.keys():
#        print('podaj prawidlowa opcje')
#        continue
#
#     options[response]

#if x.isdecimal() and y.isdecimal():
#    TASK, DAY = int(x), int(y)
#    # if DAY == 3 and TASK == 2:
#    # elif DAY == 3 and TASK == 2:
#    #     kik()
#    # napisz metodę która przyjmuje listę dowolnej wielkości lub string a zwraca jej odwróconą zawartość
#        #print(odwroc(input('ENTER STH')))
##-----------------------------------DAY @-----------------------------------
#    #elif DAY == @ and TASK == 1:
#        #ZADANIE @-1 -
#    #elif DAY == @ and TASK == 2:
#        # ZADANIE @-2 -
#    #elif DAY == @ and TASK == 3 :
#        # ZADANIE @-3 -
#    #elif DAY == @ and TASK == 4:
#        # ZAD` ANIE @-4 -
#    #elif DAY == @ and TASK == 5:
#        # ZADANIE @-5 -
##-----------------------------------DAY 2-----------------------------------
#    if DAY == 2 and TASK == 1:
#        #ZADANIE 2-1 - stringi
#        foo_2_1()
##-----------------------------------DAY 3-----------------------------------
#    elif DAY == 3 and TASK == 1:
#        #ZADANIE 3-1 - czy liczba jest podzielna przez 3,5 i 7
#        foo_3_1(int(input('ENTER NUMBER\n')))
#    elif DAY == 3 and TASK == 2:
#        # ZADANIE 3-2 - kólko i kryzyk
#        foo_3_2()
#    elif DAY == 3 and TASK == 3:
#        # ZADANIE 3-3 - pory roku
#        foo_3_3()
#    elif DAY == 3 and TASK == 4:
#        # ZADANIE 3-4 - C -> F, F -> C
#        foo_3_4()
##-----------------------------------DAY 4-----------------------------------
#    elif DAY == 4 and TASK == 1:
#        # dopoki haslo nie spelni warunkow haslo musi być co najmniej 6 znaków jeżeli hasło będzie miało mniej niż 4 znaki wypisz "Bardzo słabe hasło" jeżeli hasło będzie miało między 4 a 6 znaków wypisz "słabe hasło"
#        foo_4_1(input('ENTER PASS\n'))
#    elif DAY == 4 and TASK == 2:
#        # ZADANIE 4-2 Narysuj piramidę Mario - jako input - wysokość piramidy
#        foo_4_2(int(input('ENTER TREE SIZE:\n')))
#    elif TASK == 4 and DAY == 4:
#        # ZADANIE 4-3 - metoda ktora zwraca liste w ladnej macierzy
#        print(foo_4_4())
#    elif DAY == 4 and TASK == 3:
#        # ZADANIE 4-3 - metoda ktora zwraca niepowtarzajace sie elementy w liscie
#        foo_4_3()
#    elif DAY == 4 and TASK == 5:
#        #ZADANIE 4-5 - fibonacci w funkcji
#        foo_4_5_5_1(int(input('ENTER FIBONACCI RANGE\n')))
##-----------------------------------DAY 5-----------------------------------
#    elif DAY == 5 and TASK == 1:
#        #ZADANIE 5-1 - fibonacci w funkcji
#        foo_4_5_5_1(int(input('ENTER FIBONACCI RANGE\n')))
#    elif DAY == 5 and TASK == 2:
#        # ZADANIE 5-2 napisz metodę która będzie porównywała  zadane jej parametry
#       # print(max())
#        print(foo_5_2())
#    elif DAY == 5 and TASK == 3 :
#        # ZADANIE 5-3 - napisz metodę która przemnozy wszystkie elementy zadanej listy i ZWROCI wynik
#        print(foo_5_3())
#    elif DAY == 5 and TASK == 4:
#        # ZADANIE 5-4 - napisz metodę która przyjmuje listę nazwisk dowolnej wielkosci i zwroci jej posortowana zawartosc
#        print(foo_5_4())
#    elif DAY == 5 and TASK == 5:
#        # ZADANIE 5-5 - napisz funkcję która zwróci True jeżeli przekazany string jest palindromem
#        print(foo_5_5(input('ENTER PHRASE\n')))
##-----------------------------------DAY 6-----------------------------------
#    elif DAY == 6 and TASK == 1:
#    #ZADANIE 6-1 - wczytaj plik lorem.txt i wyświetl jego zawartość linijka po linijce z OPEN i CLOSE
#        foo_6_1()
#    elif DAY == 6 and TASK == 2:
#    # ZADANIE 6-2 -wczytaj plik lorem.txt i wyświetl jego zawartość linijka po linijce z WITH
#        foo_6_2()
#    elif DAY == 6 and TASK == 3:
#    # ZADANIE 6-3 - ile linii ma text
#        print(foo_6_3())
#    elif DAY == 6 and TASK == 4:
#    # ZADANIE 6-4 - wczytaj plik na raz osoby.csv i wypisz listę osób ze wszystkimi dostępnymi danymi format printa: "Imię: <imie z pliku>, nazwisko: <nazwisko z pliku>, wiek: <wiek z pliku> uzyj modułu csv
#        foo_6_4()
#    elif DAY == 6 and TASK == 5:
#    # ZADANIE 6-5 -
#        foo_6_5()
#else:
#    print('INVALID ARG')
#
#
