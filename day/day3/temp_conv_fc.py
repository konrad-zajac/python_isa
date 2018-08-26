def temp_conv_fc(temp:str):
    """
    Doctype: temp_conv_fc(temp:str)

    Description: Converts temperature in C to F and the opposite.

    Input: '32F', '0C' - NUmber then uppercase [F|C].

    Output: (temp:str)

    Examples:
    >>> temp_conv_fc('32F')
    '0C'
    >>> temp_conv_fc('0C')
    '32F'
    >>> temp_conv_fc('a')
    Invalid argument, must be a str.
    """
    #import re
    def conv_C_F(x):

        wyn = str((int(x.rstrip('C')) * (9//5) + 32)) + 'F'
        return wyn

    def conv_F_C(x):
        wyn = str((int(x.rstrip('F')) - 32) * 5//9) + 'C'
        return wyn
    try:
      # x = re.match(r'^[0-9]*[C|F]$', temp, re.M|re.I)
        if temp:
            return(conv_C_F(temp) if temp.find('F') == -1 else conv_F_C(temp))

    except:
        raise ValueError('Invalid argument, must be a str')
