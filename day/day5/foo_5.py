"""Module for day 5"""


def max_arr():
    """input: none
         out: maximum value"""
    arr = list()
    num = input("Enter how many elements you want:")
    print("Enter numbers in array:")
    for i in range(int(num)):
        arr.append(input("number :"))
        
    print("max: " + str(max(arr)))


def mul_arr():
    """input: none
         out: result of multipling every element"""
    wynik = 1
    num_array = list()
    num = input("Enter how many elements you want:")
    print("Enter numbers in array: ")
    for i in range(int(num)):
        n = input("num :")
        wynik *= int(n)
    print(wynik)

        
def foo_sorted_s():
    """input: none
         out: sorted list of surnames"""
    arr = list()
    num = input("Enter how many elements you want:")
    print("Enter surnames in array:")
    for i in range(int(num)):
        arr.append(input("surname :"))
    arr.sort()
    print(arr)


def foo_is_palindrome():
    """input: none
        out: True if sentence is palindrome, otherwise False """
    x = input("enter string")
    print(x.replace(" ", "") == x.replace(" ", "")[::-1])
