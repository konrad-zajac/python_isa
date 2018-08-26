def distinct_list(common_list):
    """
    Description: Creates a new list with distinct elements.

    Input: '[1,2,3]',  '[1,2,1]', '[1,2,1,2]' ,[1,2,1,2,1,2]

    Output: (temp:str)

    Examples:
    >>> distinct_list([1,2,3])
    [1, 2, 3]
    >>> distinct_list([1,2,1])
    [2]
    >>> distinct_list([1,2,1,2])
    []
    >>> distinct_list([1,2,1,2,1,2])
    [1, 2]

    """
    try:
        return list(set(common_list))

    except Exception as e:
        raise ValueError()

