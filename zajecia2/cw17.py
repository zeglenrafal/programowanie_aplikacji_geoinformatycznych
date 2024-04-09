def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    return f'Zamówiono {nazwa_produktu} w ilości {ilosc} sztuk. Łączna cena: {cena * ilosc}'

#c
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc_zamowienia = cena * ilosc
    return f'Zamówiono {nazwa_produktu} w ilości {ilosc} sztuk. Łączna cena: {wartosc_zamowienia}', wartosc_zamowienia
