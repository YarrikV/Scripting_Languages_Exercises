import struct


class Netwerk:
    """
    >>> netwerk = Netwerk('www.txt')
    >>> len(netwerk)
    6
    >>> netwerk.score('A')
    0.16666666666666666
    >>> netwerk.volgende_score('A')
    0.09583333333333334
    >>> netwerk.volgende_score('E')
    0.16666666666666666
    >>> netwerk.scores_bijwerken()
    >>> netwerk.score('A')
    0.09583333333333334
    >>> netwerk.score('E')
    0.16666666666666666
    >>> netwerk.scores_bijwerken()
    >>> netwerk.score('A')
    0.08245370370370371
    >>> netwerk.scores_bijwerken(stappen=100)
    >>> netwerk.score('A')
    0.05170474575702128
    >>> netwerk.score('B')
    0.07367926270375533
    >>> netwerk.score('C')
    0.057412412496432724
    >>> netwerk.score('D')
    0.34870368521481654
    >>> netwerk.score('E')
    0.1999038119733183
    >>> netwerk.score('F')
    0.268596081854656
    >>> netwerk.scores_initialiseren()
    >>> netwerk.score('A')
    0.16666666666666666
    >>> netwerk.scores_bijwerken(stappen=100)
    >>> netwerk.score('A')
    0.05170474575702128
    >>> netwerk.rangschikking()
    [('D', 0.34870368521481654), ('F', 0.268596081854656), ('E', 0.1999038119733183), ('B', 0.07367926270375533), ('C', 0.057412412496432724), ('A', 0.05170474575702128)]
    >>> netwerk = Netwerk('www.txt', demping=0.9)
    >>> netwerk.scores_bijwerken(stappen=100)
    >>> netwerk.rangschikking()
    [('D', 0.3750808151098345), ('F', 0.2862458852154), ('E', 0.20599833187742753), ('B', 0.05395734936310289), ('C', 0.04150565335623299), ('A', 0.03721196507800199)]

    # >>> netwerk.uitgaand('A')
    # {'B', 'C'}
    # >>> netwerk.uitgaand('B')
    # {'A', 'B', 'C', 'D', 'E', 'F'}
    # >>> netwerk.uitgaand('C')
    # {'A', 'B', 'E'}
    # >>> netwerk.uitgaand('D')
    # {'E', 'F'}
    # >>> netwerk.uitgaand('E')
    # {'D', 'F'}
    # >>> netwerk.uitgaand('F')
    # {'D'}
    # >>> netwerk.inkomend('A')
    # {'B', 'C'}
    # >>> netwerk.inkomend('B')
    # {'A', 'B', 'C'}
    # >>> netwerk.inkomend('C')
    # {'A', 'B'}
    # >>> netwerk.inkomend('D')
    # {'B', 'E', 'F'}
    # >>> netwerk.inkomend('E')
    # {'B', 'C', 'D'}
    # >>> netwerk.inkomend('F')
    # {'B', 'D', 'E'}
    """

    def __init__(self, file_location: str, d: float = 0.85) -> None:
        self.d = d
        self.network_connections: dict = dict()
        self.scores: dict = dict()
        self.webpages: set = set()

        with open(file_location, "r") as f:
            solitary_webpages = set()
            for webpage_connections in f:
                webpage_connections = webpage_connections.strip().split("\t")
                webpage = webpage_connections[0]
                webpage_connections = webpage_connections[1:]

                # add page
                self.webpages.add(webpage)

                # add connections
                self.network_connections[webpage] = set()
                for connection in webpage_connections:
                    self.network_connections[webpage].add(connection)

                # if solitary
                if len(webpage_connections) == 0:
                    solitary_webpages.add(webpage)

            # process solitary webpages
            # add every other webpage to the connections of the solitary webpage
            for solitary_webpage in solitary_webpages:
                for other_webpage in self.network_connections.keys():
                    self.network_connections[solitary_webpage].add(other_webpage)

        # scores
        self.scores_initialiseren()

    def scores_initialiseren(self):
        """initialise scores to 1/N for network with N webpages"""
        for webpage in self.webpages:
            self.scores[webpage] = 1 / len(self)

    def __len__(self) -> int:
        """Returns amount of webpages."""
        return len(self.webpages)

    def __str__(self) -> str:
        print_str = ""
        for webpage, webpage_connections in self.network_connections.items():
            print_str += (
                f"{webpage} ({self.scores[webpage]}) -> {webpage_connections}\n"
            )

        return print_str.strip()

    def uitgaand(self, p):
        """De methode moet een verzameling (set) teruggeven met de labels van alle webpagina's waar p naar verwijst volgens PageRank."""
        assert p in self.network_connections.keys(), f"Ongeldige webpagina {p}."
        return self.network_connections[p]

    def inkomend(self, p):
        """De methode moet een verzameling (set) teruggeven met de labels van alle webpagina's die naar p verwijzen volgens PageRank."""
        assert p in self.network_connections.keys(), f"Ongeldige webpagina {p}."

        inkomend = set()
        for other_webpage, webpage_outgoing in self.network_connections.items():
            if p in webpage_outgoing:
                inkomend.add(other_webpage)
        return inkomend

    def score(self, p) -> float:
        """De methode moet de huidige score (float) van p teruggeven."""
        pass

    def volgende_score(self, p) -> float:
        """De methode moet de nieuwe score (float) teruggeven die p zou krijgen in de volgende stap
        van het PageRank-algoritme, berekend op basis van de huidige scores van de webpagina's."""
        pass

    def rangschikking(self):
        """
        De methode moet een lijst (list) teruggeven met voor elke webpagina in
        het netwerk een tuple (tuple) met het label en de score van de webpagina.
        De tuples moeten opgelijst worden volgens dalende score.
        Tuples met dezelfde score moeten alfabetisch volgens label opgelijst worden.
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()