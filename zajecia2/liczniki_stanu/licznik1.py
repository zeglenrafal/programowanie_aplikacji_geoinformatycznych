def licznik_1():
    x = 0
    def wewnetrzna():
        nonlocal x
        x += 1
        return x

    return wewnetrzna