def seasons(month:int,day:int):

    """
    Doctype: def seasons()

    Description: function returns the season from the given date.

    Input: (month:int,day:int)

    Output: Season is [summoer|autumn|winter|spring]

    Examples:

    >>> seasons(1,1)
    'Season is winter'
    >>> seasons(5,1)
    'Season is spring'
    >>> seasons(8,1)
    'Season is summer'
    >>> seasons(11,1)
    'Season is autumn'
    """
    month = int(month)
    day = int(day)
    try:
        if month in (0,1,2):
            season = 'winter'
        elif month in (3,4,5):
            season = 'spring'
        elif month in (6,7,8):
            season = 'summer'
        else:
            season = 'autumn'

        if (month == 3) and (day > 19):
            season = 'spring'
        elif (month == 5) and (day > 20):
            season = 'summer'
        elif (month == 8) and (day > 21):
            season = 'autumn'
        elif (month == 11) and (day > 20):
            season = 'winter'

        return "Season is " + season
    except:
        raise ValueError('A very specific bad thing happened.')
