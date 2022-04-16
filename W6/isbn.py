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


class ISBN13:
    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isvalid()
    True
    >>> code.asISBN10()
    '0-13611067-3'
    """

    def __init__(self, code, country_spec_len=1) -> None:
        assert 1 <= country_spec_len <= 5, "invalid ISBN code"
        self.code = str(code)
        self.country_spec_len = country_spec_len

    def __str__(self) -> str:
        return (
            self.code[:3]
            + "-"
            + self.code[3 : 3 + self.country_spec_len]
            + "-"
            + self.code[3 + self.country_spec_len : -1]
            + "-"
            + self.code[-1]
        )

    def __repr__(self) -> str:
        return "ISBN13(" + self.code + ", " + str(self.country_spec_len) + ")"

    def isvalid(self) -> bool:
        return isISBN13(self.code)

    def asISBN10(self) -> str:
        if isISBN13(self.code) and self.code.startswith("978"):
            isbn10 = self.code[3:-1]
            checkdigit = sum((i + 1) * int(isbn10[i]) for i in range(9)) % 11
            isbn10 += str(checkdigit) if checkdigit != 10 else "X"
            return (
                isbn10[: self.country_spec_len]
                + "-"
                + isbn10[self.country_spec_len : -1]
                + "-"
                + isbn10[-1]
            )
            # self.country_spec_len = 1
        else:
            return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
