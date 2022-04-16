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

    return Rechthoek(x_min, y_min, 1 + x_max - x_min, 1 + y_max - y_min)


class Rechthoek:
    """
    >>> groen = Rechthoek(0, 5, 5, 1)
    >>> groen
    Rechthoek(0, 5, 5, 1)
    >>> groen.oppervlakte()
    5
    >>> groen.cellen()
    {(1, 5), (4, 5), (0, 5), (2, 5), (3, 5)}
    >>> blauw = Rechthoek(3, 0, 2)
    >>> blauw
    Rechthoek(3, 0, 2, 2)
    >>> blauw.oppervlakte()
    4
    >>> blauw.cellen()
    {(3, 1), (4, 0), (4, 1), (3, 0)}
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
        self.r = r
        self.k = k

    def __repr__(self) -> str:
        return (
            "Rechthoek("
            + str(self.r)
            + ", "
            + str(self.k)
            + ", "
            + str(self.hoogte)
            + ", "
            + str(self.breedte)
            + ")"
        )

    def oppervlakte(self) -> int:
        return self.breedte * self.hoogte

    def cellen(self, ordered=False):
        verz_cellen = set(
            (self.r + i, self.k + j)
            for j in range(self.breedte)
            for i in range(self.hoogte)
        )
        if ordered:
            return set(
                sorted(list(verz_cellen), key=lambda element: (element[0], element[1]))
            )

        return verz_cellen

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
        communal_cells = filter(lambda cell: cell in other.cellen(), self.cellen())
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
    >>> groen = Rechthoek(0, 5, 5, 1)
    >>> blauw = Rechthoek(3, 0, 2)
    >>> shikaku = Shikaku('shikaku.txt')
    >>> shikaku.cellen(blauw)
    [(4, 0)]
    >>> shikaku.getallen(blauw)
    [4]
    >>> shikaku.cellen(Rechthoek(1, 1, 3, 5))
    [(3, 2), (1, 5)]
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
        self.rechthoeken = []

        with open(filename, "r") as f:
            self.hoogte, self.breedte = (int(s) for s in f.readline().split())
            self.nummers = set()

            for line in f.readlines():
                nummer = tuple([int(s) for s in line.split()])
                self.nummers.add(nummer)

    def getallen(self, R):
        nummers_in_R = []

        for x, y, nummer in self.nummers:
            if (x, y) in R.cellen(ordered=True):
                nummers_in_R.append(nummer)

        return nummers_in_R

    def cellen(self, R: Rechthoek):
        """
        Een methode cellen waaraan een rechthoek (Rechthoek) moet doorgegeven worden.
        De methode moet een lijst (list) teruggeven met de posities van alle
        genummerde cellen van het rooster die door bedekt worden.

        De posities moeten opgelijst worden in de volgorde waarin je de cellen tegenkomt
        als je het rooster van links naar rechts en van boven naar onder doorloopt.
        """
        cellen_in_R = []

        for r, k, _ in self.nummers:
            if (r, k) in R.cellen(ordered=True):
                cellen_in_R.append((r, k))

        return cellen_in_R

    def verwijderen(self, positie):
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
        err_msg = "ongeldige positie"
        assert positie in self.cellen(
            Rechthoek(0, 0, self.hoogte, self.breedte)
        ), err_msg

        done = False
        for r_idx, r in enumerate(self.rechthoeken):
            if positie in r.cellen():
                self.rechthoeken.pop(r_idx)
                done = True
        if not done:
            raise AssertionError(err_msg)

    def onbedekt(self):
        """
        Een methode onbedekt waaraan geen argumenten moeten doorgegeven worden.

        De methode moet een verzameling (set) teruggeven met de
        posities van alle genummerde cellen van het rooster die
        nog niet door een rechthoek bedekt zijn.
        """
        onbedekte_nummers = set(self.cellen(Rechthoek(0, 0, self.hoogte, self.breedte)))

        for rechthoek in self.rechthoeken:
            for positie in self.cellen(rechthoek):
                onbedekte_nummers.discard(positie)
        # print("nummers onbedekt: ", len(onbedekte_nummers), "/", len(self.nummers))
        return onbedekte_nummers

    def in_bounds(self, R: Rechthoek):
        return (
            0 <= R.r  # r_min
            and R.r + R.hoogte <= self.hoogte  # r_min
            and 0 <= R.k  # k_min
            and R.k + R.breedte <= self.breedte  # k_max
        )

    def bedekken(self, R: Rechthoek):
        err_msg = "ongeldige rechthoek"

        # in bounds
        assert self.in_bounds(R), err_msg

        # no overlap with other rechthoek
        cellen_R = set(R.cellen())
        for other_r in self.rechthoeken:
            for other_cell in other_r.cellen():
                assert other_cell not in cellen_R, err_msg

        # only 1 numbered cell
        numb_cellen = self.getallen(R)

        assert len(numb_cellen) == 1, err_msg
        assert numb_cellen[0] == R.oppervlakte(), err_msg

        self.rechthoeken.append(R)

    def isopgelost(self):
        return len(self.onbedekt()) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
