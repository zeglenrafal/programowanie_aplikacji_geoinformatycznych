import math
import numpy as np
#dzialania matematyczne
a=100
dodawanie=a+123.15
potega=dodawanie**12
tekst = str(potega)
wartoscpi=math.pi
#print(tekst)

losowa=np.random.randint(4)+1
losowa1=np.random.choice([1 , 2 , 3 , 4 , 5])
print(losowa)
print(losowa1)
print("\n")
#łańcuchy znakow
tekst= f"Wartosc:{tekst}"
print("Dlugosc zmiennej tekst: "+ str(len(tekst)))
print(tekst[1:4])

print(dir(tekst))

print(tekst.upper())

#tekst[1]="p"
print(tekst.replace("A", "p"))

#print(tekst)
print("\n")
#dzialania na listach
lista=list(tekst)
print(lista)

lista=lista[0:8]
print(lista)

print(dir(lista))
lista.append(list([1,2,3,4,5]))
print(lista)

lista.remove(":")
print(lista)
print("\n")

#listy skladane
lista2=[1,2,3,"banan",100]
lista3=[i**2 for i in lista2 if i!="banan"]
lista4=list(range(2,16,2))

print("lista2: "+ str(lista2)+", lista3: "+ str(lista3)+", lista4: "+str(lista4))
print("\n")
#slowniki

ja={}
ja={
    "imie": "Rafal",
    "nazwisko":"Zeglen",
    "wiek":"21",
    "rodzice": [{"imie":"Anna",
                "wiek" : "49"},{"imie":"Marek",
                                "wiek":"50"}]
}
print(ja["rodzice"])
print(ja["rodzice"][0]["imie"])

for klucz,wartosc in ja.items():
    print(klucz)

print(ja.keys())
print(ja.__contains__("rodzenstwo"))
print("\n")

#krotki
krotka1=(1,2,"3",4,2,5)
print("dlugosc zmiennej: " + str(krotka1.__len__()) + ", pierwszy wyraz: " +str(krotka1[0]))
#print(dir(krotka1))
print("Wartosc 2 wystepuje: "+ str(krotka1.count(2)) +" razy")
#krotka1[0]=2 tak sie nie da, ale tak sie da:
temp=list(krotka1)
temp[0]=2
krotka1=tuple(temp)
print(krotka1)
print("\n")

#zbiory
X=set("kalarepa")
Y=set("lepy")
print(str(X&Y))
print("\n")

#instrukcje
#1
imiona=["Filip","Anita","Julka","Kornelia","Bartek","Milosz","Kinga","Oriana","Asia"]

for i in range(len(imiona)):
    print(i,imiona[i])
print("\n")
print(enumerate(imiona))
print("\n")
#2

liczba=int(input("Podaj liczbe: "))
if(liczba%2==0):
    print("parzysta")
else:
    print("nieparzysta")

if(liczba!=0):
    print("Liczba nie jest rowna 0")

owoce=["jablko","banan","kiwi"]
temp1=input()
if(temp1 in owoce):
    print("Owoc jest dostepny")

suma=0
while(suma<100):
    l=int(input("Podaj liczbe: "))
    suma=suma+l
print(str(suma))
print("\n")
#dziwactwa
# 1. Przypisanie tworzy referencje, a nie kopie
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

# 2. Powtórzenie dodaje jeden poziom zagłębienia
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")
