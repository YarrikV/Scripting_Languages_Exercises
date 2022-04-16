class Quaternion():
    """ 
    >>> q1 = Quaternion(2, 4, 7, 3)
    >>> q1.norm()
    8.831760866327848
    >>> print(q1)
    2 + 4i + 7j + 3k
    >>> q1
    Quaternion(2, 4, 7, 3)

    >>> q2 = Quaternion(a=-5, c=2, d=-4)
    >>> q2.norm()
    6.708203932499369
    >>> print(q2)
    -5 + 0i + 2j - 4k
    >>> q2
    Quaternion(-5, 0, 2, -4)

    >>> q1 + q2
    Quaternion(-3, 4, 9, -1)
    >>> q2 + q1
    Quaternion(-3, 4, 9, -1)
    >>> q1 + 3
    Quaternion(5, 4, 7, 3)
    >>> 3 + q1
    Quaternion(5, 4, 7, 3)
    >>> q1 * q2
    Quaternion(-12, -54, -15, -15)
    >>> q2 * q1
    Quaternion(-12, 14, -47, -31)
    >>> q1 * 3
    Quaternion(6, 12, 21, 9)
    >>> 3 * q1
    Quaternion(6, 12, 21, 9) 
    """

    def __init__(self, a, b, c, d) -> None:
        self.z = a
        self.i = b
        self.j = c
        self.k = d
