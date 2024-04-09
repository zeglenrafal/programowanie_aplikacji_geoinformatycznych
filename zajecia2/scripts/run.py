from cw15 import *
from cw16 import *
from cw17 import *
from cw18 import *
from cw19 import *
from cw21 import *
from cw23 import *

# lista = [1, (1,2),"sdc", 123,"asc"]
# a, *b, c =lista
# print(a,b,c)
# a=123
# a+=123
# print(a)

#6
dane = (2024, 'Python', 3.8)
rok,jezyk,wersja = dane
print(rok,jezyk,wersja)

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek,ostatnia = oceny
print(pierwsza,srodek,ostatnia)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie,nazwisko,_,_,zawod=info
print(imie,nazwisko,zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok,[jezyk, wersja, opis]=dane
print(rok,jezyk,wersja,opis)

#10
a = b = [1,2,3]
b[0]='zmieniono'

print(a,b)

#11
c=a[:]
c[0]='nowa wartosc'
print(a,b,c)

#12
x=y=10
y=y+1
print(x,y)

#13
K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

#14
imiona = ['Anna', 'Jan', 'Ewa'] 
oceny = [5, 4, 3]
for i in zip(imiona,oceny):
    print(i)

#15
liczby = [1, 2, 3, 4, 5]


nowa=map(kwadrat,liczby)
for i in nowa:
    print(i)

#16


print(zmien_wartosc(2))
print(zmien_wartosc([1,2,3]))

#17




zamowienia = []
zamowienia.append(zamowienie_produktu('Jabłka', cena=2.5, ilosc=3))
zamowienia.append(zamowienie_produktu('Banany', cena=3.2, ilosc=2))
zamowienia.append(zamowienie_produktu('Pomarańcze', cena=4.1, ilosc=4))

for zamowienie in zamowienia:
    print(zamowienie)

#c

wartosci_zamowien = []
for zamowienie in zamowienia:
    tekst_zamowienia, wartosc_zamowienia = zamowienie_produktu(*zamowienie)  # rozpakowanie słownika
    wartosci_zamowien.append(wartosc_zamowienia)
    print(tekst_zamowienia)

# d
print(f'Sumaryczna wartość zamówień: {sum(wartosci_zamowien)}')

#18

#
# stworz_raport(101, 102, 101_nazwa="Kubek termiczny", 101_cena="45.99 zł",102_nazwa="Długopis", 102_cena="4.99 zł")

#19

potega_2=stworz_funkcje_potegujaca(2)
print(potega_2(4))

#20

#21


#22
ksiazki = [
    {'tytul': 'Harry Potter and the Philosopher’s Stone ', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Harry Potter and the Chamber of Secrets', 'autor': 'J.K. Rowling', 'rok_wydania': 1998},
    {'tytul': 'Harry Potter and the Prisoner of Azkaban', 'autor': 'J.K. Rowling', 'rok_wydania': 1999},
    {'tytul': 'Harry Potter and the Half-Blood Prince', 'autor': 'J.K. Rowling', 'rok_wydania': 2005},
]

# a. Sortowanie książek według roku wydania
ksiazki_posortowane = sorted(ksiazki, key=lambda k: k['rok_wydania'])

# b. Filtracja książek wydanych po 2000 roku
ksiazki_po_2000 = list(filter(lambda k: k['rok_wydania'] > 2000, ksiazki))

# c. Transformacja listy do listy tytułów
tytuly_ksiazek = list(map(lambda k: k['tytul'], ksiazki))
print(ksiazki_posortowane)
print(ksiazki_po_2000)

#23


generator_dni_tygodnia = dni_tygodnia()

# Wyświetlanie każdego
for dzien in generator_dni_tygodnia:
    print(dzien)

#Pobieranie pierwszych trzech
pierwsze_trzy_dni = [next(generator_dni_tygodnia) for _ in range(3)]
print(pierwsze_trzy_dni)
