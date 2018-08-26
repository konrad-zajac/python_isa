def is_div_357(inp:int):
    """
    Doctype: is_div_357()

    Description:This function determines
    if input is devideble by 3,5 and 7.

    Input: Integer

    Output: [True|False]

    Examples:
    >>> is_div_357(105)
    >>> True

    >>> is_div_357(22)
    >>> False

    >>> is_div_357('w')
    >>> ValueError
    """
    if inp:
        if (int(inp) % 3 or int(inp) % 5 or int(inp) % 7):
            return False
        else:
            return True
    else:
        raise ValueError('Invalid arg')
