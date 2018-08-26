"""Module for day 5"""


def read_lorem():
    '''input: nothing  
    out: reads lorem.txt with  OPEN & CLOSE'''
    file = open('lorem.txt', 'r')
    for line in file:
        print(line, end='')
    file.close() 


def with_foo():
    '''input: nothing  
             out: reads lorem.txt with WITH'''
    with open('lorem.txt', 'r') as file:
        for line in file:
            print(line, end='')


def foo_6_3():
    '''input: nothing 
         out: how many lines does lorem.txt have'''
    with open('lorem.txt', 'r') as file:
     return(sum([1 for line in file]))


def foo_6_4():
    '''input: nothing
         out: the csv file from the task'''
    import csv
    with open('osoby.csv', 'r') as file:
        persons_reader = csv.reader(file)
        headers = next(persons_reader)

        for person in persons_reader:
            line = ''
            for index, header in enumerate(headers):
                line += '{}: {}, '.format(header.capitalize(), person[index].capitalize())
            print(line[:-2])


def foo_6_5():
    '''input: nothing
    out: the pickle from the task'''
    import csv
    import pickle
    with open('moj.csv', 'r') as file:
        persons_reader = csv.reader(file)
        headers = next(persons_reader)

        for person in persons_reader:
            for index, header in enumerate(headers):
                dict = {'first_name': person[0].capitalize(), 'last_name':person[1].capitalize(), 'Age':person[2] }

            pickle.dump( dict, open( "save.p", "wb" ))
