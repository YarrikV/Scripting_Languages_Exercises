def getNumber(s):
    if s == "X":
        return 10
    elif s in "0123456789":
        return int(s)
    else:
        return 1000


def isISBN(code, isbn13=None):
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
    if isbn13 == None:
        l = len(code)
        if l == 10:
            isbn13 = False
        elif l == 13:
            isbn13 = True
        else:
            return False

    if isbn13:
        # ISBN 13
        o, e = 0, 0

        for i in range(1, 13):
            n = getNumber(input())
            if n == 1000:
                return False

            if i % 2 == 0:
                e += n
            else:
                o += n
        n = getNumber(input())
        if n == 1000:
            return False
        return (10 - (o + 3 * e) % 10) % 10 == n

    else:
        # ISBN 10
        y = 0
        for i in range(1, 10):
            n = getNumber(input())
            if n == 1000:
                return False
            y += i * n

        n = getNumber(input())
        if n == 1000:
            return False
        return y % 11 == getNumber(input())


def areISBN(list, isbn13):
    """
    >>> codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']
    >>> areISBN(codes)
    [False, True, True, True, False, False, False, True, False]
    >>> areISBN(codes, True)
    [False, False, False, False, False, False, False, True, False]
    >>> areISBN(codes, False)
    [False, True, True, True, False, False, False, False, False]
    """
    return [isISBN(c, isbn13) for c in list]


if __name__ == "__main__":
    import doctest

    doctest.testmod()