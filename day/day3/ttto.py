def ttto(x):
    """
    Doctype:def ttto(x):

    Description: determines who won
    in a game of tic-tactoe

    Input:
        nine character string with a game containing
        only the characters
        x - sign of player one
        o - sign of player two
        n - fileld that is not used

    Output:
        [
        x wins - horizontally
        |
        x wins - vertically
        |
        x wins - diagonally
        |
        o wins - horizontally
        |
        o wins - vertically
        |
        o wins - diagonally
        |
        n wins - horizontally
        |
        n wins - vertically
        |
        n wins - diagonally
        |
        the house wins
        ]


    Examples:
        >>> ttto('xoooxooox')
        'x wins - diagonally'
        >>> ttto('oxxxoxxxo')
        'o wins - diagonally'
        >>> ttto('oxxxoxxxn')
        'the house wins'

    """
    try:
        gra = list(x)
        if gra:

            #2 diagonal
            if gra[0] == gra[4] == gra[8] or gra[2] == gra[4] == gra[6]:
                if gra[4] == 'x':
                    return gra[4]+' wins - diagonally'
                elif gra[4] == 'o':
                    return gra[4]+' wins - diagonally'
            #3 - horizontal
            elif gra[0] == gra[3] == gra[6]:
                if gra[0] == 'x':
                    return 'x wins - diagonally'
                elif gra[0] == 'o':
                    return 'o  wins - diagonally'
            #4 - horizontal
            elif gra[1] == gra[4] == gra[7]:
                if gra[1] == 'x':
                    return 'x wins - diagonally'
                elif gra[1] == 'o':
                    return 'o  wins - diagonally'
            #5 - horizontal
            elif gra[2] == gra[5] == gra[8]:
                if gra[2] == 'x':
                    return 'x wins - diagonally'
                elif gra[2] == 'o':
                    return 'o  wins - diagonally'
            #6 - horizaontal
            elif gra[0] == gra[1] == gra[2]:
                if gra[0] == 'x':
                    return 'x wins - diagonally'
                elif gra[0] == 'o':
                    return 'o  wins - diagonally'
            #7 - horizaontal
            elif gra[3] == gra[4] == gra[5]:
                if gra[3] == 'x':
                    return 'x wins - diagonally'
                elif gra[3] == 'o':
                    return 'o  wins - diagonally'
            #8 - horizaontal
            elif gra[6] == gra[7] == gra[8]:
                if gra[6] == 'x':
                    return 'x wins - diagonally'
                elif gra[6] == 'o':
                    return 'o  wins - diagonally'
            else:
                return 'the house wins'
    except:
        raise ValueError('Invalid arg')
