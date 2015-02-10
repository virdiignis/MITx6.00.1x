def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    wynik=False
    if n == 20 or n == 9 or n == 6:
        return True
    if n <  6:
        return False
    if n > 20:
        wynik = McNuggets(n-20)
    if n > 9 and wynik == False:
        wynik = McNuggets(n-9)
    if n > 6 and wynik == False:
        wynik = McNuggets(n-6)
    return wynik