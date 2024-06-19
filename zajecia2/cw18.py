def stworz_raport(*args, **kwargs):
    for id_produktu in args:
        nazwa_produktu = kwargs.get(f'{id_produktu}_nazwa')
        cena_produktu = kwargs.get(f'{id_produktu}_cena')

        if nazwa_produktu and cena_produktu:
            print(f'Produkt {id_produktu}:')
            print(f'  Nazwa: {nazwa_produktu}')
            print(f'  Cena: {cena_produktu}')
        else:
            print(f'Brak inf {id_produktu}')