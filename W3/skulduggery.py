def split(t, m):
    """
    >>> split('ABCDEFGHIJKL', 6)
    ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
    >>> split('ABCDEFGHIJKL', 4)
    ['ABC', 'DEF', 'GHI', 'JKL']
    >>> split('ABCDEFGHIJKL', 3)
    ['ABCD', 'EFGH', 'IJKL']
    """
    l = len(t) // m
    return [t[i * l : (i + 1) * l] for i in range(m)]


def merge(seq):
    """
    >>> merge(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'])
    'ABCDEFGHIJKL'
    >>> merge(['ABC', 'DEF', 'GHI', 'JKL'])
    'ABCDEFGHIJKL'
    >>> merge(['ABCD', 'EFGH', 'IJKL'])
    'ABCDEFGHIJKL'
    """
    return "".join(seq)


def halve(seq):
    """
    >>> halve(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'])
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    >>> halve(['ABCD', 'EFGH', 'IJKL'])
    ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
    """
    l = len(seq[0]) // 2
    return [element for row in [[t[:l], t[l:]] for t in seq] for element in row]


def double(seq):
    """
    >>> double(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
    >>> double(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'])
    ['ABCD', 'EFGH', 'IJKL']
    """
    l = len(seq) // 2
    return ["".join(seq[i * 2 : (i + 1) * 2]) for i in range(l)]


def swap(seq):
    """
    >>> swap(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'])
    ['ACEGIK', 'BDFHJL']
    >>> swap(['ABC', 'DEF', 'GHI', 'JKL'])
    ['ADGJ', 'BEHK', 'CFIL']
    >>> swap(['ABCD', 'EFGH', 'IJKL'])
    ['AEI', 'BFJ', 'CGK', 'DHL']
    """
    l = len(seq[0])
    return ["".join(s[i] for s in seq) for i in range(l)]


def interweave(seq, s):
    """
    >>> interweave(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'], 2)
    ['AB', 'EF', 'IJ', 'CD', 'GH', 'KL']
    >>> interweave(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'], 3)
    ['AB', 'GH', 'CD', 'IJ', 'EF', 'KL']
    >>> interweave(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'], 4)
    ['AB', 'IJ', 'CD', 'KL', 'EF', 'GH']
    """
    woven = []

    for i in range(s):
        partial = []

        j = i
        while j < len(seq):
            partial.append(seq[j])
            j += s

        woven.extend(partial)
    return woven


def decode(t, m):
    """
    >>> decode("Ie fradnoCh' a ac guaamoffiiy  pvtenham fatoa  eciSoruwitJ ksprrn!", 3)
    "I'm afraid you have the misfortune of facing Captain Jack Sparrow!"
    >>> decode("Iofc Ch'friyaam anopv figuteaad  a itciat!nhksruZ e frnZJ SooeZamprw Z", 5)
    "I'm afraid you have the misfortune of facing Captain Jack Sparrow!ZZZZ"
    >>> decode("Ifrnot' aguamfi  i adChnac aa fiypvJeamatX ciruXtksrnXh foeXeSow X pr!oX", 6)
    "I'm afraid you have the misfortune of facing Captain Jack Sparrow!XXXXXX"
    """
    return merge(interweave(swap(double(interweave(halve(split(t, m)), m))), 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()