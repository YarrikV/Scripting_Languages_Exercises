from pydoc import plain


ORDE = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Rooster:
    """
    >>> rooster = Rooster('Anakin Skywalker')
    >>> print(rooster)
    ANKI SYWL
    ERBCDFGHJ
    MOPQTUVXZ
    >>> rooster.positie('A')
    (0, 0)
    >>> rooster.positie('H')
    (1, 7)
    >>> rooster.positie('z')
    (2, 8)
    >>> rooster.karakter(0, 0)
    'A'
    >>> rooster.karakter(1, 7)
    'H'
    >>> rooster.karakter(2, 8)
    'Z'

    >>> rooster = Rooster('Padme Amidala')
    >>> print(rooster)
    PADME ILB
    CFGHJKNOQ
    RSTUVWXYZ
    >>> rooster.positie('P')
    (0, 0)
    >>> rooster.positie('H')
    (1, 3)
    >>> rooster.positie('z')
    (2, 8)
    >>> rooster.karakter(0, 0)
    'P'
    >>> rooster.karakter(1, 3)
    'H'
    >>> rooster.karakter(2, 8)
    'Z'
    """

    def add(self, char):
        idx = self.waarden.index(None) if None in self.waarden else -1

        # empty space required
        if idx > -1:
            # cannot already be present
            if char not in self.waarden:
                self.waarden[idx] = char

    def __init__(self, sleutel) -> None:
        self.waarden = [None for _ in range(27)]

        for krkt in sleutel.upper():
            self.add(krkt)

        for krkt in ORDE:
            self.add(krkt)

    def __str__(self) -> str:
        return (
            "".join(self.waarden[:9])
            + "\n"
            + "".join(self.waarden[9:18])
            + "\n"
            + "".join(self.waarden[18:])
        )

    def positie(self, kkt):
        idx = self.waarden.index(kkt.upper())
        return (idx // 9, idx % 9)

    def karakter(self, r, k):
        return self.waarden[r * 9 + k]


class Digrafid:
    """
    >>> digrafid = Digrafid('Anakin Skywalker', 'Padme Amidala')
    >>> digrafid.triplet('So')
    (5, 1, 7)
    >>> digrafid.triplet('me')
    (0, 6, 4)
    >>> digrafid.triplet('da')
    (4, 3, 1)
    >>> digrafid.digraaf(5, 1, 7)
    'SO'
    >>> digrafid.digraaf(0, 6, 4)
    'ME'
    >>> digrafid.digraaf(4, 3, 1)
    'DA'
    >>> digrafid.digraaf(5, 0, 4)
    'SE'
    >>> digrafid.digraaf(1, 6, 3)
    'OM'
    >>> digrafid.digraaf(7, 4, 1)
    'HF'
    >>> digrafid.codeer('Someday I will be the most powerful Jedi ever')
    'SEOMHFGLAPFXJCAMXW PHLCYFFKBK EZFRE JJCPTEYOGZTI'
    >>> digrafid.decodeer('SEOMHFGLAPFXJCAMXW PHLCYFFKBK EZFRE JJCPTEYOGZTI')
    'SOMEDAY I WILL BE THE MOST POWERFUL JEDI EVERXXX'

    >>> digrafid = Digrafid('Darth Vader', 'Admiral Motti')
    >>> digrafid.codeer('I find your lack of faith disturbing')
    'TNIILD MQPM VLIBOKAFIIVTHID LTUZVRJR'
    >>> digrafid.decodeer('TNIILD MQPM VLIBOKAFIIVTHID LTUZVRJR')
    'I FIND YOUR LACK OF FAITH DISTURBING'
    """

    def __init__(self, s_a, s_b) -> None:
        self.rooster_a = Rooster(s_a)
        self.rooster_b = Rooster(s_b)

    def triplet(self, digraaf):
        """returns triplet of given digraaf, inverse of "digraaf"."""
        r_a, k_a = self.rooster_a.positie(digraaf[0])
        r_b, k_b = self.rooster_b.positie(digraaf[1])

        return (k_a, 3 * r_a + r_b, k_b)

    def digraaf(self, k_a, r_ab, k_b) -> str:
        """returns digraaf of given triplet, inverse of "triplet"."""
        return self.rooster_a.karakter(r_ab // 3, k_a) + self.rooster_b.karakter(
            r_ab % 3, k_b
        )

    def codeer_block(self, text_block) -> str:
        """Returns ciphertext of text_block, with text_block containing 3 digrafen."""
        matrix = [self.triplet(text_block[i * 2 : (i + 1) * 2]) for i in range(3)]
        return "".join(
            self.digraaf(matrix[0][i], matrix[1][i], matrix[2][i]) for i in range(3)
        )

    def codeer(self, plain_text) -> str:
        """Returns ciphertext (capital letters) after coding using keys s_a and s_b."""
        plain_text = plain_text.upper()

        # add X's if needed
        amount_residu = (((len(plain_text) // 6) + 1) * 6 - len(plain_text)) % 6
        plain_text += amount_residu * "X"

        print(f"len:{len(plain_text)}, amount_res:{amount_residu}\ntext:{plain_text}")

        # split plaintext in blocks of 3 digraafs
        return "".join(
            self.codeer_block(plain_text[i * 6 : (i + 1) * 6])
            for i in range(len(plain_text) // 6)
        )

    def decodeer(self, ciphertext) -> str:
        """Inverse of "codeer".
        Fortunately, digraf-id is symmetrical."""
        return self.codeer(ciphertext)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
