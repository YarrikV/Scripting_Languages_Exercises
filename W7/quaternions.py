from math import sqrt


def sign(n):
    return "+" if n >= 0 else "-"


class Quaternion:
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

    def __init__(self, a=0, b=0, c=0, d=0) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return (
            str(self.a)
            + " "
            + sign(self.b)
            + " "
            + str(abs(self.b))
            + "i "
            + sign(self.c)
            + " "
            + str(abs(self.c))
            + "j "
            + sign(self.d)
            + " "
            + str(abs(self.d))
            + "k"
        )

    def __repr__(self) -> str:
        return (
            "Quaternion("
            + str(self.a)
            + ", "
            + str(self.b)
            + ", "
            + str(self.c)
            + ", "
            + str(self.d)
            + ")"
        )

    def norm(self):
        """
        De methode moet de norm (float) teruggeven.
        """
        return sqrt(
            self.a * self.a + self.b * self.b + self.c * self.c + self.d * self.d
        )

    def __add__(self, other):
        if isinstance(other, int):
            other = Quaternion(other)
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        return Quaternion(a, b, c, d)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int):
            other = Quaternion(other)
        a = self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d
        b = self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c
        c = self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b
        d = self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
        return Quaternion(a, b, c, d)

    def __rmul__(self, other):
        return self * other


if __name__ == "__main__":
    import doctest

    doctest.testmod()
