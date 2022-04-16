def salt(pile):
    """
    >>> salt('gj1h##hg3ur#zt#zhg#e#2h##jgs#kjl')
    9
    >>> salt('gj2h##hg7ur#zt#zhg#e#5h##jgs#kjl')
    9
    """
    return pile.count("#")


def gold(pile):
    """
    >>> gold('gj1h##hg3ur#zt#zhg#e#2h##jgs#kjl')
    6
    >>> gold('gj2h##hg7ur#zt#zhg#e#5h##jgs#kjl')
    14
    """
    c = 0
    for i in range(10):
        c += pile.count(str(i)) * i
    return c


def remove_salt(pile):
    """
    >>> remove_salt('gj1h##hg3ur#zt#zhg#e#2h##jgs#kjl')
    'gj1hhg3urztzhge2hjgskjl'
    >>> remove_salt('gj2h##hg7ur#zt#zhg#e#5h##jgs#kjl')
    'gj2hhg7urztzhge5hjgskjl'
    """
    while (t := pile.find("#")) >= 0:
        pile = pile[:t] + pile[t + 1 :]
    return pile


def remove_gold(pile):
    """
    >>> remove_gold('gj1h##hg3ur#zt#zhg#e#2h##jgs#kjl')
    'gjh##hgur#zt#zhg#e#h##jgs#kjl'
    >>> remove_gold('gj2h##hg7ur#zt#zhg#e#5h##jgs#kjl')
    'gjh##hgur#zt#zhg#e#h##jgs#kjl'
    """
    for i in range(10):
        while (t := pile.find(str(i))) >= 0:
            pile = pile[:t] + pile[t + 1 :]
    return pile


def trade(pile):
    """
    >>> trade('gj1h##hg3ur#zt#zhg#e#2h##jgs#kjl')
    'gj1hhg3urztzhge2hjgskjl'
    >>> trade('gj2h##hg7ur#zt#zhg#e#5h##jgs#kjl')
    'gjh##hgur#zt#zhg#e#h##jgs#kjl'
    """
    s = salt(pile)
    g = gold(pile)
    if s > g:
        return remove_salt(pile)
    else:
        return remove_gold(pile)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
