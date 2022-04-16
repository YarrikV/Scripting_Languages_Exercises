def maak_Rechthoek(cells):
    """Returns Rechthoek if cells have any values
    Otherwise returns None.

    Assuming 'cells' is a valid iteration of cells."""
    if not cells:
        return None

    x_s = [cell[0] for cell in cells]
    y_s = [cell[1] for cell in cells]
    x_max, x_min = max(x_s), min(x_s)
    y_max, y_min = max(y_s), min(y_s)

    return Rechthoek(x_min, y_min, 1+x_max - x_min, 1 + y_max - y_min)


class Rechthoek:
    """
    >>> groen = Rechthoek(0, 5, 5, 1)
    >>> groen
    Rechthoek(0, 5, 5, 1)
    >>> groen.oppervlakte()
    5
    >>> groen.cellen()
    {(4, 5), (1, 5), (0, 5), (2, 5), (3, 5)}
    >>> blauw = Rechthoek(3, 0, 2)
    >>> blauw
    Rechthoek(3, 0, 2, 2)
    >>> blauw.oppervlakte()
    4
    >>> blauw.cellen()
    {(3, 0), (3, 1), (4, 1), (4, 0)}
    >>> groen & blauw
    >>> groen & Rechthoek(1, 1, 3, 5)
    Rechthoek(1, 5, 3, 1)
    >>> blauw & Rechthoek(1, 1, 3, 5)
    Rechthoek(3, 1, 1, 1)
    >>> Rechthoek(2, 3, 3, 2) <= Rechthoek(2, 2, 3)
    True
    >>> groen <= blauw
    False
    """

    def __init__(self, r, k, h, b=None) -> None:
        if b is None:
            self.breedte = h
        else:
            self.breedte = b
        self.hoogte = h
        self.x = r
        self.y = k

    def __repr__(self) -> str:
        return (
            "Rechthoek("
            + str(self.x)
            + ", "
            + str(self.y)
            + ", "
            + str(self.hoogte)
            + ", "
            + str(self.breedte)
            + ")"
        )

    def oppervlakte(self) -> int:
        return self.breedte * self.hoogte

    def cellen(self):
        return set(
            (self.x + i, self.y + j)
            for j in range(self.breedte)
            for i in range(self.hoogte)
        )

    def __eq__(self, other):
        """=="""
        print("==, Not implemented")
        return False

    def __gt__(self, other):
        """>"""
        print(">, Not implemented")
        return False

    def __lt__(self, other):
        """<"""
        print("<, Not implemented")
        return False

    def __and__(self, other):
        """&"""
        communal_cells = filter(
            lambda cell: cell in other.cellen(), self.cellen())
        return maak_Rechthoek(set(communal_cells))

        return communal_cells if communal_cells else None

    def __ge__(self, other):
        """>="""
        return other <= self

    def __le__(self, other):
        """<="""
        return all(cel in other.cellen() for cel in self.cellen())


class Shikaku:
    """
    >>> shikaku = Shikaku('shikaku.txt')
    >>> shikaku.cellen(blauw)
    [(4, 0)]
    >>> shikaku.getallen(blauw)
    [4]
    >>> shikaku.cellen(Rechthoek(1, 1, 3, 5))
    [(1, 5), (3, 2)]
    >>> shikaku.getallen(Rechthoek(1, 1, 3, 5))
    [5, 9]
    >>> shikaku.onbedekt()
    {(1, 5), (2, 0), (3, 2), (0, 3), (4, 0)}
    >>> shikaku.bedekken(blauw)
    >>> shikaku.onbedekt()
    {(1, 5), (3, 2), (2, 0), (0, 3)}
    >>> shikaku.isopgelost()
    False
    >>> shikaku.bedekken(groen)
    >>> shikaku.onbedekt()
    {(2, 0), (3, 2), (0, 3)}
    >>> shikaku.isopgelost()
    False
    >>> shikaku.bedekken(Rechthoek(1, 1, 3, 5))
    Traceback (most recent call last):
    AssertionError: ongeldig rechthoek
    >>> shikaku.verwijderen((3, 0))
    Traceback (most recent call last):
    AssertionError: ongeldige positie
    >>> shikaku.verwijderen((4, 0))
    >>> shikaku.onbedekt()
    {(2, 0), (3, 2), (4, 0), (0, 3)}
    >>> shikaku.bedekken(blauw)
    >>> shikaku.bedekken(Rechthoek(0, 0, 2, 5))  # paars
    >>> shikaku.bedekken(Rechthoek(2, 0, 1, 2))  # bruin
    >>> shikaku.bedekken(Rechthoek(2, 2, 3))     # roze
    >>> shikaku.onbedekt()
    set()
    >>> shikaku.isopgelost()
    True
    """

    def __init__(self, filename) -> None:
        self.rechthoeken = set()

        with open(filename, 'r') as f:
            self.hoogte, self.breedte = (int(s) for s in f.readline().split())
            self.nummers = set()

            for line in f.readlines():
                self.nummers.add((int(s) for s in line.split()))

    def getallen(self, R):
        pass

    def cellen(self, R):
        pass

    def verwijderen(self, r, k):
        """
        Een methode verwijderen waaraan de positie van 
        een genummerde cel moet doorgegeven worden. 
        Als de genummerde cel niet door een rechthoek 
        bedekt wordt, dan moet een AssertionError opgeworpen 
        worden met de boodschap ongeldige positie. Anders 
        moet de methode de rechthoek weghalen die de genummerde 
        cel bedekt, waardoor alle cellen die door deze 
        rechthoek bedekt werden niet langer bedekt zijn.
        """
        pass

    def onbedekt(self):
        pass

    def bedekken(self, R):
        pass

    def isopgelost(self):
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
