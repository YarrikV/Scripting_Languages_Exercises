def isISBN13(code):
    if not (isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False

    checkdigit = (
        10 - sum((3 if i % 2 else 1) * int(code[i]) for i in range(12)) % 10
    ) % 10
    return checkdigit == int(code[-1])


def remove_tags(s):
    s = s.strip()
    while s.find("<") >= 0:  # while still tag present
        start = s.find("<")
        stop = s.find(">")
        if stop == -1:
            stop = len(s)
        # only keep what is not contained in a tag
        s = s[:start] + s[stop + 1 :]
    # remove leading and trailing whitespace
    return s.strip()


def display_book_info(code):
    """
    if code is valid isbn-13 code,
    print
    Title: [Title]
    Authors: [AuthorsText]
    Publisher: [PublisherText]

    >>> display_book_info('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> display_book_info('9780136110678')
    Wrong ISBN-13 code
    """
    error = "Wrong ISBN-13 code"
    if isISBN13(code):
        import urllib.request

        url = "https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php"
        pms = "?isbn=" + code.strip()  # strip deletes blank characters at ends

        info = urllib.request.urlopen(url + pms)

        # extract data
        for line in info:
            line = line.decode("utf-8")

            if line.startswith("<Title>"):
                print(f"Title: {remove_tags(line)}")
            elif line.startswith("<AuthorsText>"):
                # remove trailing ", "
                print(f"Authors: {remove_tags(line).rstrip(', ')}")
            elif line.startswith("<PublisherText "):
                print(f"Publisher: {remove_tags(line)}")

        # close web page
        info.close()

    else:
        print(error)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
