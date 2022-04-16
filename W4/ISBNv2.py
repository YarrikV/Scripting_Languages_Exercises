def isISBN(code, isbn13=True):
    """
    >>> isISBN('9789027439642', False)
    False
    >>> isISBN('9789027439642', True)
    True
    >>> isISBN('9789027439642')
    True
    >>> isISBN('080442957X')
    False
    >>> isISBN('080442957X', False)
    True
    """
    getNumber = lambda s: int(s) if s != "X" else 10

    if type(code) != str or not all([str(s) in "0123456789X" for s in code]):
        return False

    l = len(code)
    if isbn13 is None:
        if l == 13:
            isbn13 = True
        elif l == 10:
            isbn13 = False
        else:
            return False

    if (isbn13 and l != 13) or (not isbn13 and l != 10):
        return False

    code = list(code)
    if isbn13:
        y = 0

        for i in range(1, 13):
            n = getNumber(code.pop(0))
            y += n if i % 2 == 1 else 3 * n

        return (10 - (y % 10)) % 10 == getNumber(code.pop(0))

    else:
        y = 0
        for i in range(1, 10):
            n = getNumber(code.pop(0))
            y += i * n
        return y % 11 == getNumber(code.pop(0))


def areISBN(codes, isbn13=None):
    """
    >>> codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']
    >>> areISBN(codes)
    [False, True, True, True, False, False, False, True, False]
    >>> areISBN(codes, True)
    [False, False, False, False, False, False, False, True, False]
    >>> areISBN(codes, False)
    [False, True, True, True, False, False, False, False, False]
    """
    """
    lengths = [len(code) for code in codes]
    isbnDict = {10: False, 13: True}
    l = []
    for code, length in zip(codes, lengths):
        if length not in isbnDict.keys():
            l.append(False)
        else:
            l.append(isISBN(code, isbnDict[length]))
    """
    return [isISBN(code, isbn13) for code in codes]


if __name__ == "__main__":
    import doctest

    doctest.testmod()