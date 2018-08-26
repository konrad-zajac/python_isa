def fibonacci(n):
    '''input: from distinct_list import distinct_list
         out: fibonaccis sequence'''
    try:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
    except exception as e:
       raise ValueError()
