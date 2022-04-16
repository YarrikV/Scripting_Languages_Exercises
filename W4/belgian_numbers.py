def sequence(n, k=0, count=0):
    """
    >>> sequence(108)
    [0, 1, 1, 9, 10, 10, 18, 19, 19, 27, 28, 28, 36, 37, 37, 45, 46, 46, 54, 55, 55, 63, 64, 64, 72, 73, 73, 81, 82, 82, 90, 91, 91, 99, 100, 100, 108]
    >>> sequence(123, count=10)
    [0, 1, 3, 6, 7, 9, 12, 13, 15, 18]
    >>> sequence(n=81, k=1)
    [1, 9, 10, 18, 19, 27, 28, 36, 37, 45, 46, 54, 55, 63, 64, 72, 73, 81]
    >>> sequence(n=61, k=6)
    [6, 12, 13, 19, 20, 26, 27, 33, 34, 40, 41, 47, 48, 54, 55, 61]
    """
    if not (isinstance(n, int) or isinstance(k, int) or isinstance(count, int)):
        raise ValueError(
            f"Expected int type, but got something different.\nTypes of: n={type(n)}, k={type(k)}, count={type(count)}"
        )

    digits = [int(a) for a in str(n)]
    numDig = len(digits)
    seq = []
    i = 0
    seq.append(k)
    while k < n:
        k += digits[i]
        i = (i + 1) % numDig

        seq.append(k)

        # if count pm, return seq if length is count
        if count != 0 and len(seq) == count:
            return seq

    return seq


def isbelgian(n, k=0):
    """
    >>> isbelgian(81)
    True
    >>> isbelgian(108)
    True
    """
    return n in sequence(n, k)


def seeds(n):
    """
    >>> seeds(108)
    [0, 8, 9, 17, 18, 26, 27, 35, 36, 44, 45, 53, 54, 62, 63, 71, 72, 80, 81, 89, 90, 98, 99, 107, 108]
    >>> seeds(81)
    [0, 1, 9, 10, 18, 19, 27, 28, 36, 37, 45, 46, 54, 55, 63, 64, 72, 73, 81]
    """
    return [k for k in range(n + 1) if isbelgian(n, k=k)]


def isflemish(n):
    """
    >>> isflemish(108)
    False
    >>> isflemish(81)
    False
    >>> isflemish(61)
    True
    >>> isflemish(68)
    True
    """
    # flemish if n is belgian k-number, with k = first digit of n
    # 68 is belgian k=6-number
    return isbelgian(n, k=int(str(n)[0]))


def iswestflemish(n):
    """
    >>> iswestflemish(108)
    False
    >>> iswestflemish(81)
    False
    >>> iswestflemish(61)
    True
    >>> iswestflemish(68)
    False
    """
    if not isflemish(n):
        return False
    n_str = str(n)
    seq = sequence(n, k=int(n_str[0]), count=len(n_str))
    seq = "".join(str(number_n) for number_n in seq)
    return n_str == seq[: len(n_str)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()