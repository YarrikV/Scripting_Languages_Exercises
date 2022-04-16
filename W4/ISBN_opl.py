def isISBN10(code):
    if not (isinstance(code, str) and len(code) == 10 and code[:9].isdigit()):
        return False

    checkdigit = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    x10 = code[9]

    return (checkdigit == 10 and x10 == "X") or str(checkdigit) == x10


def isISBN13(code):
    if not (isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False

    checkdigit = (
        10 - sum((3 if i % 2 else 1) * int(code[i]) for i in range(12)) % 10
    ) % 10
    return checkdigit == int(code[-1])


def isISBN(code, isbn13=True):
    if not isinstance(code, str):
        return False

    l = len(code)
    if isbn13 is None:
        if l == 13:
            isbn13 = True
        elif l == 10:
            isbn13 = False
        else:
            return False
    return isISBN13(code) if isbn13 else isISBN10(code)


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
    return [isISBN(code, isbn13) for code in codes]


if __name__ == "__main__":
    import doctest

    doctest.testmod()