def pswd_foo(pswd:str):


    """
    Description: Validates a password.

    Input: 'abc', 'abcd','abcdef' - String

    Output: [
    Bardzo słabe haslo|
    Słabe haslo
    ]

    Examples:
    >>> pswd_foo(11)
    : 11
    'Bardzo słabe haslo'
    >>> pswd_foo(12345)
    : 12345
    'Słabe haslo'
    >>> pswd_foo(123454)
    : 123454
    'podałeś super hasło'

    """

    str_pswd = str(pswd)
    print(': ' + str_pswd)

    try:
        while len(str_pswd) < 6:
            if len(str_pswd) < 4:
                return 'Bardzo słabe haslo'
                str_pswd = int(input('Podaj hasło: '))
            elif len(str_pswd) >=4 :
                return 'Słabe haslo'
            str_pswd = int(input('Podaj hasło: '))

        return "podałeś super hasło"

    except Exception as e:
        raise ValueError()

