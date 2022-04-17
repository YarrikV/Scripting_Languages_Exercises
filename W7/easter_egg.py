from string import ascii_uppercase as alphabet
from itertools import product


class EasterEgg:
    """
    >>> puzzel = EasterEgg(7, 7, 'D4', 'eieren.txt')
    >>> puzzel.haas()
    'D4'
    >>> puzzel.eieren()
    {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3', 'D5', 'D6', 'E2', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    >>> print(puzzel)
    #OOO#OO
    OO#####
    #O#O##O
    OOOXOO#
    #O#O##O
    OO#####
    #OOO#OO
    >>> puzzel.isleeg()
    False
    >>> puzzel.mogelijke_zetten()
    {'B3', 'B5', 'C2', 'C6', 'D5', 'D6', 'D7', 'E2', 'E6', 'F3', 'F5'}
    >>> print(puzzel.zet('E2'))
    #OOO#OO
    OO#####
    #O#O##O
    OOO#OO#
    #X#O##O
    OO#####
    #OOO#OO
    >>> puzzel.haas()
    'E2'
    >>> puzzel.loc_to_tuple()
    (5, 2)
    >>> puzzel.eieren()
    {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3', 'D5', 'D6', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    >>> puzzel.isleeg()
    False
    >>> puzzel.mogelijke_zetten()
    {'C1', 'C3', 'D4', 'E3', 'E4', 'E5', 'E6', 'E7', 'F4', 'G1', 'G3'}
    >>> puzzel.zet('B3')
    Traceback (most recent call last):
    AssertionError: ongeldige zet
    >>> puzzel.zet('B2')
    Traceback (most recent call last):
    AssertionError: ongeldige zet
    >>> print(puzzel.zet('G3').zet('F1').zet('E3').zet('G2').zet('G4'))
    #OOO#OO
    OO#####
    #O#O##O
    OOO#OO#
    ###O##O
    #O#####
    ###X#OO
    >>> puzzel.mogelijke_zetten()
    {'E3', 'E5', 'F2', 'F6', 'G5', 'G6', 'G7'}
    >>> print(puzzel.zet('F2').zet('E4').zet('D2').zet('B1').zet('A3'))
    #OXO#OO
    #O#####
    #O#O##O
    O#O#OO#
    ######O
    #######
    #####OO
    >>> print(puzzel.zet('C2').zet('C4').zet('B2').zet('D1').zet('D3'))
    #O#O#OO
    #######
    ######O
    ##X#OO#
    ######O
    #######
    #####OO
    >>> print(puzzel.zet('B4').zet('A2').zet('A4').zet('A6').zet('A7'))
    ######X
    #######
    ######O
    ####OO#
    ######O
    #######
    #####OO
    >>> print(puzzel.zet('C6').zet('C7').zet('D5').zet('E7').zet('G6'))
    #######
    #######
    #######
    #####O#
    #######
    #######
    #####XO
    >>> print(puzzel.zet('G7').zet('F5').zet('D6').zet('D7'))
    #######
    #######
    #######
    ######X
    #######
    #######
    #######
    >>> puzzel.isleeg()
    True
    """

    def __init__(self, m, n, init_pos, file_location) -> None:
        self.height = m
        self.width = n
        self.bunny_pos = init_pos
        self.egg_locations = set()

        self.readfile(file_location)

    def readfile(self, file_location):
        with open(file_location, "r") as f:
            for egg in f:
                self.egg_locations.add(egg.strip())

    def __str__(self) -> str:
        repr_str = ""
        for x in range(1, 1+self.height):
            for y in range(1, 1+self.width):
                loc_str = self.tuple_to_loc((x, y))
                # if egg
                if loc_str in self.egg_locations:
                    repr_str += "O"
                elif loc_str == self.bunny_pos:
                    repr_str += "X"
                else:
                    repr_str += "#"

            repr_str += "\n"

        return repr_str.strip()

    def haas(self) -> str:
        """De methode moet de positie (str) van de paashaas in het rooster teruggeven."""
        return self.bunny_pos

    def eieren(self) -> set:
        """De methode moet een verzameling (set) teruggeven met
        de posities (str) van alle paaseieren die nog in het rooster liggen."""
        return self.egg_locations

    def loc_to_tuple(self, pos=None) -> tuple:
        """from str "A2" to tuple (1,2) with each number starting from A=1 (not A=0).
        B=2, C=3, etc."""
        if pos is None:
            return (alphabet.index(self.bunny_pos[0]) + 1, int(self.bunny_pos[1]))
        else:
            return (alphabet.index(pos[0]) + 1, int(pos[1]))

    def tuple_to_loc(self, pos) -> str:
        """inverse of loc_to_tuple, pos is required"""
        return alphabet[pos[0] - 1] + str(pos[1])

    def mogelijke_zetten(self) -> set:
        """
        De methode moet een verzameling teruggeven met de posities van alle velden in het rooster waarnaar de paashaas vanaf zijn huidige positie kan springen.
        """
        mogelijke_zetten = set()
        row, column = self.loc_to_tuple()

        # rechts van haas
        if column < self.width:
            for mogelijke_column in range(column + 1, self.width + 1):
                mogelijke_zetten.add(
                    self.tuple_to_loc((row, mogelijke_column))
                )

        # paardenzetten zoals in schaken
        for drow, dcol in [(-1, 2), (1, -2), (-1, -2), (1, 2), (2, -1), (2, 1), (-2, 1), (-2, -1)]:
            mogelijke_pos = (row + drow, column + dcol)
            if self.is_in_bounds(mogelijke_pos):
                mogelijke_zetten.add(self.tuple_to_loc(mogelijke_pos))
            else:
                print("not in bounds: ", self.tuple_to_loc(mogelijke_pos))
        return mogelijke_zetten

    def is_in_bounds(self, pos) -> bool:
        """Returns if pos is in bounds of veld."""
        if isinstance(pos, str):
            x, y = self.loc_to_tuple(pos)
        else:
            x, y = pos
        return (
            1 <= x <= self.height and
            1 <= y <= self.width
        )

    def zet(self, p: str):
        """
        Als de paashaas niet vanaf zijn huidige positie naar positie kan springen,
        dan moet de paashaas blijven staan en moet de methode een AssertionError
        opwerpen met de boodschap ongeldige zet. Anders moet de paashaas naar
        positie springen en er het paasei oprapen als er daar één ligt
        (waardoor het paasei van het rooster verdwijnt), en moet de methode een
        verwijzing teruggeven naar het object waarop de methode werd aangeroepen.
        """
        mogelijke_zetten = self.mogelijke_zetten()
        assert p in mogelijke_zetten, "ongeldige zet"

        self.bunny_pos = p

        if p in self.egg_locations:
            self.egg_locations.remove(p)
        return self

    def isleeg(self) -> bool:
        """
        De methode moet een Booleaanse waarde (bool) teruggeven
        die aangeeft of er geen paaseieren meer op het rooster liggen.

        Lege set -> isleeg True
        """
        return not bool(self.egg_locations)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
