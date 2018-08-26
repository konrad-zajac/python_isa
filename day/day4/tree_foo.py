def tree_foo(n:int):
    """
    Description: Creates a  tree with a given height

    Input: '3', '33' - Integer

    Output: (temp:str)

    Examples:
    >>> tree_foo(1)
    '+\n'
    >>> tree_foo(3)
    '  +  \n +++ \n+++++\n'
    >>> tree_foo(a)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'a' is not defined
    >>>
    """
    try:
        final_tree = ''
        z = n - 1
        x = 1
        for i in range(n):
            final_tree += (' ' * z + '+' * x + ' ' * z + '\n')
            x+=2
            z-=1

        return final_tree

    except Exception as e:
        raise ValueError()


