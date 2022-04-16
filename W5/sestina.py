from math import floor


def valid_word(word):
    """Word consists of [a-Z-]
    First and last char are alpha chars.

    >>> valid_word("test-")
    False
    >>> valid_word("alp-oma")
    False
    >>> valid_word("a#bc")
    False
    """
    return all(c.isalpha() for c in word)
    # allAlpha = [c.isalpha() for c in word]
    # extraChars = [False] + [c in ["-"] for c in word[1:-1]] + [False]
    # return all(allAlpha[i] or extraChars[i] for i in range(len(allAlpha)))


def endword(line):
    """
    >>> endword("Lo ferm voler qu'el cor m'intra")
    'intra'
    >>> endword("no'm pot ges becs escoissendre ni ongla")
    'ongla'
    >>> endword("de lauzengier qui pert per mal dir s'arma;")
    'arma'
    """
    tl = [c.isalpha() for c in line]
    tl.reverse()
    end = tl.index(True)

    word = line[::-1][end:][::-1]
    while not valid_word(word):
        word = word[1:]
        if len(word) == 1:
            return word
    return word


def stanzas(filename):
    """
    >>> stanzas('sestina0.txt')
    [['intra', 'ongla', 'arma', 'verja', 'oncle', 'cambra'], ['cambra', 'intra', 'oncle', 'ongla', 'verja', 'arma'], ['arma', 'cambra', 'verja', 'intra', 'ongla', 'oncle'], ['oncle', 'arma', 'ongla', 'cambra', 'intra', 'verja'], ['verja', 'oncle', 'intra', 'arma', 'cambra', 'ongla'], ['ongla', 'verja', 'cambra', 'oncle', 'arma', 'intra'], ['oncle', 'arma', 'intra']]
    >>> stanzas('sestina1.txt')
    [['enters', 'nail', 'soul', 'rod', 'uncle', 'room'], ['room', 'enters', 'uncle', 'nail', 'rod', 'soul'], ['soul', 'room', 'rod', 'enters', 'nail', 'uncle'], ['uncle', 'soul', 'nail', 'room', 'enters', 'rod'], ['rod', 'uncle', 'enters', 'soul', 'room', 'nail'], ['nail', 'rod', 'room', 'uncle', 'soul', 'enters'], ['nail', 'soul', 'enters']]
    >>> stanzas('sestina2.txt')
    [['woe', 'sound', 'cryes', 'part', 'sleepe', 'augment'], ['augment', 'woe', 'sound', 'cryes', 'part', 'sleepe'], ['sleepe', 'augment', 'woe', 'sound', 'cryes', 'part'], ['part', 'sleepe', 'augment', 'woe', 'sound', 'cryes'], ['cryes', 'part', 'sleepe', 'augment', 'woe', 'sound'], ['sound', 'cryes', 'part', 'sleepe', 'augment', 'woe'], ['sound', 'part', 'augment']]
    """
    ll = [[]]
    with open(filename, "r") as f:
        for line in f:
            if len(line.strip()) == 0:
                if ll[-1]:
                    ll.append([])
            else:
                ll[-1].append(endword(line).lower())
    return ll


def permutation(wordlist, pattern=None):
    """
    >>> permutation(['a', 'b', 'c', 'd', 'e', 'f'])
    ['f', 'a', 'e', 'b', 'd', 'c']
    >>> permutation(['a', 'b', 'c', 'd', 'e'])
    ['e', 'a', 'd', 'b', 'c']
    >>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'])
    ['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
    >>> permutation(['woe', 'rose', 'rhyme', 'love', 'sang', 'heart'])
    ['heart', 'woe', 'sang', 'rose', 'love', 'rhyme']
    >>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme'])
    ['rhyme', 'rose', 'sang', 'love', 'heart']
    >>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 2, 4, 3])
    ['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
    >>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 5, 4, 3, 2, 1])
    ['woe', 'rhyme', 'sang', 'heart', 'love', 'rose']
    >>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 3, 4, 3])
    Traceback (most recent call last):
    AssertionError: invalid permutation
    """
    amount = len(wordlist)
    if pattern:
        # pattern has right amount of unique elements
        assert amount == len(set(pattern)), "invalid permutation"

        assert all(
            list(set(pattern))[i] == i + 1 for i in range(amount)
        ), "invalid permutation"

    else:
        # canonical permutation
        pattern = [i + 1 for i in range(amount)]

        half = floor(amount / 2)

        p1, p2 = pattern[:half], pattern[half:]
        pattern = [None] * (len(p1) + len(p2))
        pattern[::2] = p2[::-1]
        pattern[1::2] = p1

    return [wordlist[idx - 1] for idx in pattern]


def sestina(filename, pattern=None):
    """
    >>> sestina('sestina0.txt')
    True
    >>> sestina('sestina0.txt', [6, 1, 5, 2, 4, 3])
    True
    >>> sestina('sestina1.txt')
    True
    >>> sestina('sestina2.txt')
    False
    >>> sestina('sestina2.txt', [6, 1, 2, 3, 4, 5])
    True
    """
    sz = stanzas(filename)
    
    words = sz[0]

    n = len(words)

    # check if all stanzas have words contained in set
    for stanza in sz[1:]:
        if any(word not in words for word in stanza):
            # print("Unrecognized word.")
            return False

    # check if right amount of stanzas
    if len(sz) == n:
        envoi = False
    elif len(sz) == n + 1:
        envoi = True
    else:
        # print("Number of stanzas is wrong.")
        return False

    # check length of envoi
    if envoi and len(sz[-1]) != floor(n / 2):
        # print("Envoi has wrong length.")
        return False

    # check if permutations are correct
    perm = sz[0]
    for i in range(1, n):
        new_perm = permutation(perm, pattern)
        perm = sz[i]

        if any(new_perm[j].lower() != perm[j].lower() for j in range(len(perm))):
            # print(f"Invalid permutation of stanzas on alinea {i+1}.")
            return False

    # otherwise valid sestina
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
