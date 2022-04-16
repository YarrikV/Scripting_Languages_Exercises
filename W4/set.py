from random import choice
import itertools 

amount = ["one", "two", "three"]
shading = ["solid", "striped", "open"]
color = ["red", "green", "purple"]
shape = ["diamond", "squiggle", "oval"]


def random_card():
    return (choice(amount), choice(shading), choice(color), choice(shape))


def random_cards(n):
    s = set()
    while len(s) < n:
        s.add(random_card())
    return s


def features(ca, cb, cc):
    """
    >>> features(('one', 'open', 'green', 'diamond'), ('two', 'open', 'red', 'diamond'), ('three', 'open', 'purple', 'diamond'))
    ({'one', 'two', 'three'}, {'open'}, {'red', 'green', 'purple'}, {'diamond'})
    >>> features(('one', 'striped', 'green', 'oval'), ('two', 'striped', 'green', 'squiggle'), ('three', 'striped', 'purple', 'diamond'))
    ({'one', 'two', 'three'}, {'striped'}, {'green', 'purple'}, {'oval', 'diamond', 'squiggle'})
    >>> features(('two', 'striped', 'red', 'diamond'), ('one', 'solid', 'red', 'diamond'), ('two', 'solid', 'purple', 'oval'))
    ({'one', 'two'}, {'striped', 'solid'}, {'red', 'purple'}, {'oval', 'diamond'})
    """
    cs = [ca, cb, cc]
    get_set = lambda i: set(c[i] for c in cs)
    return tuple(get_set(i) for i in range(4))


def isset(ca, cb, cc):
    """
    >>> isset(('one', 'open', 'green', 'diamond'), ('two', 'open', 'red', 'diamond'), ('three', 'open', 'purple', 'diamond'))
    True
    >>> isset(('one', 'striped', 'green', 'oval'), ('two', 'striped', 'green', 'squiggle'), ('three', 'striped', 'purple', 'diamond'))
    False
    >>> isset(('two', 'striped', 'red', 'diamond'), ('one', 'solid', 'red', 'diamond'), ('two', 'solid', 'purple', 'oval'))
    False
    """
    ftrs = features(ca, cb, cc)
    return all((len(ftr) == 1 or len(ftr) == 3) for ftr in ftrs)


def sets(cards):
    """
    >>> sets([('three', 'solid', 'purple', 'oval'), ('one', 'open', 'green', 'diamond'), ('two', 'solid', 'purple', 'diamond'), ('one', 'solid', 'red', 'squiggle'), ('two', 'open', 'red', 'squiggle'), ('one', 'solid', 'purple', 'diamond'), ('three', 'solid', 'green', 'diamond'), ('one', 'striped', 'purple', 'squiggle'), ('three', 'solid', 'green', 'squiggle'), ('three', 'solid', 'green', 'oval'), ('two', 'open', 'red', 'diamond'), ('three', 'open', 'purple', 'diamond')])
    5
    >>> sets((('three', 'open', 'red', 'diamond'), ('three', 'open', 'green', 'squiggle'), ('one', 'striped', 'green', 'oval'), ('three', 'open', 'green', 'diamond'), ('one', 'open', 'purple', 'oval'), ('three', 'striped', 'purple', 'oval'), ('two', 'striped', 'red', 'squiggle'), ('three', 'solid', 'red', 'diamond'), ('two', 'solid', 'purple', 'oval'), ('one', 'striped', 'green', 'squiggle'), ('three', 'striped', 'green', 'diamond'), ('three', 'open', 'red', 'oval')))
    4
    >>> sets({('one', 'solid', 'green', 'oval'), ('two', 'solid', 'red', 'oval'), ('three', 'open', 'purple', 'diamond'), ('two', 'solid', 'red', 'diamond'), ('three', 'striped', 'purple', 'oval'), ('two', 'solid', 'red', 'squiggle'), ('two', 'striped', 'purple', 'oval'), ('one', 'open', 'purple', 'diamond'), ('two', 'open', 'green', 'diamond'), ('three', 'solid', 'purple', 'squiggle'), ('one', 'solid', 'green', 'diamond'), ('two', 'solid', 'green', 'diamond')})
    6
    >>> sets([('three', 'open', 'purple', 'diamond'), ('two', 'open', 'green', 'diamond'), ('three', 'striped', 'red', 'squiggle'), ('three', 'solid', 'purple', 'diamond'), ('three', 'solid', 'red', 'squiggle'), ('one', 'striped', 'green', 'oval'), ('two', 'solid', 'red', 'diamond'), ('three', 'open', 'purple', 'oval'), ('three', 'solid', 'purple', 'oval'), ('one', 'solid', 'green', 'oval'), ('one', 'open', 'purple', 'oval'), ('two', 'striped', 'red', 'diamond')])
    0
    """
    count = 0
    for ca, cb, cc in itertools.combinations(cards, 3):
        if isset(ca, cb, cc):
            count += 1
    
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()