def isISBN13(code):
    if not (isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False

    checkdigit = (
        10 - sum((3 if i % 2 else 1) * int(code[i]) for i in range(12)) % 10
    ) % 10
    return checkdigit == int(code[-1])


def overview(codes):
    """
    PREFIX: 978 or 979
    fourth digit: which country
    0,1: EN
    2: FR
    3: DE
    4: JAP
    5: RU
    7: CH
    6,8,9: OTHER
    """
    countries = [
        "English speaking countries",
        "French speaking countries",
        "German speaking countries",
        "Japan",
        "Russian speaking countries",
        "China",
        "Other countries",
        "Errors",
    ]
    amounts = {country: 0 for country in countries}

    ids = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 5, 8: 6, 9: 6}
    for code in codes:
        # errors
        if not (code[:3] in ["978", "979"] and isISBN13(code)):
            amounts[countries[7]] += 1
        else:
            amounts[countries[ids[int(code[3])]]] += 1

    [print(f"{country}: {amounts[country]}") for country in countries]
