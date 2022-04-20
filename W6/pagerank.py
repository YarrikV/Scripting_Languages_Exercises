from copy import deepcopy


class Netwerk:
    """
    >>> netwerk = Netwerk('www.txt')
    >>> len(netwerk)
    6
    >>> netwerk.scores_initialiseren()
    >>> netwerk.score('A')
    0.16666666666666666
    >>> netwerk.scores_bijwerken(stappen=100)
    >>> netwerk.score('A')
    0.05170474575702128
    >>> netwerk.rangschikking()
    [('D', 0.34870368521481654), ('F', 0.268596081854656), ('E', 0.1999038119733183), ('B', 0.07367926270375533), ('C', 0.057412412496432724), ('A', 0.05170474575702128)]
    """

    def __init__(self, file_location: str, demping: float = 0.85) -> None:
        self.d = demping
        self.network_connections: dict = {}
        self.scores: dict = {}
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
                for other_webpage in self.network_connections:
                    self.network_connections[solitary_webpage].add(other_webpage)

        # scores
        self.scores_initialiseren()

    def AssertValidPage(self, p):
        assert p in self.network_connections, f"Ongeldige webpagina {p}."

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
        self.AssertValidPage(p)
        return self.network_connections[p]

    def inkomend(self, p):
        """De methode moet een verzameling (set) teruggeven met de labels van alle webpagina's die naar p verwijzen volgens PageRank."""
        self.AssertValidPage(p)

        inkomend = set()
        for other_webpage, webpage_outgoing in self.network_connections.items():
            if p in webpage_outgoing:
                inkomend.add(other_webpage)
        return inkomend

    def score(self, p) -> float:
        """De methode moet de huidige score (float) van p teruggeven."""
        self.AssertValidPage(p)
        return self.scores[p]

    def volgende_score(self, p) -> float:
        """De methode moet de nieuwe score (float) teruggeven die p zou krijgen in de volgende stap
        van het PageRank-algoritme, berekend op basis van de huidige scores van de webpagina's."""
        self.AssertValidPage(p)

        new_score = (1 - self.d) / len(self)
        new_score += self.d * sum(
            self.score(webpage) / len(self.uitgaand(webpage))
            for webpage in self.inkomend(p)
        )
        return new_score

    def scores_bijwerken(self, stappen=1):
        """De methode moet ervoor zorgen dat elke webpagina in het netwerk een
        nieuwe score krijgt door stappen van het PageRank-algoritme uit te voeren.
        """
        for _ in range(stappen):
            # scores berekend uit data van vorige stap
            new_scores = deepcopy(self.scores)
            for webpage in self.webpages:
                new_scores[webpage] = self.volgende_score(webpage)
            self.scores = new_scores

    def rangschikking(self):
        """
        De methode moet een lijst (list) teruggeven met voor elke webpagina in
        het netwerk een tuple (tuple) met het label en de score van de webpagina.
        De tuples moeten opgelijst worden volgens dalende score.
        Tuples met dezelfde score moeten alfabetisch volgens label opgelijst worden.
        """
        rank = []

        for p in self.webpages:
            rank.append((p, self.scores[p]))
        rank.sort(key=lambda x: (-x[1], x[0]))
        return rank


if __name__ == "__main__":
    import doctest

    doctest.testmod()