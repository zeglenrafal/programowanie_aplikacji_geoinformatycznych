class Kino:

    def __init__(self):
        self.sala = {"1": [False], "2": [False], "3": [False], "4": [False], "5": [False], "6": [False], "7": [False], "8": [False], "9": [False],
                     "10": [False], "11": [False], "12": [False], "13": [False], "14": [False], "15": [False], "16": [False], "17": [False], "18": [False],
                     "19": [False], "20": [False], "21": [False], "22": [False], "23": [False], "24": [False], "25": [False], "26": [False], "27": [False], "28": [False], "29": [False], "30": [False], "31": [False], "32": [False],
                     "33": [False], "34": [False], "35": [False], "36": [False], "37": [False], "38": [False], "39": [False],
                     "40": [False], "41": [False], "42": [False], "43": [False], "44": [False], "45": [False], "46": [False],
                     "47": [False], "48": [False], "49": [False], "50": [False]}
        
    def zarezerwuj(self, miejsce, imie, nazwisko):
        self.sala[miejsce][0] = True
        self.sala[miejsce].append(imie)
        self.sala[miejsce].append(nazwisko)

    def odwolajRezerwacje(self, miejsce):
        self.sala[miejsce][0] = False
        self.sala[miejsce].pop(1)
        self.sala[miejsce].pop(1)

    def SprawdzSale(self):
        pelne = True
        for miejsce in self.sala.values():
            if miejsce[0] == False:
                pelne = False
                break
        if pelne:
            raise ValueError("Kino jest pełne")

    def SprawdzRezerwacje(self,lista,miejsce,imie,nazwisko):
        if self.sala[miejsce][0] == False:
            if not (imie, nazwisko) in lista:
                self.zarezerwuj(miejsce, imie, nazwisko)
            else:
                raise ValueError("Juz zarezerwowales miejsce")
        else:
            raise ValueError("Miejsce" + f": {miejsce}"+ "jest juz zajete")

        lista.append((imie, nazwisko))
        
    def SprawdzOdwolanie(self,miejsce,imie,nazwisko):
        if self.sala[miejsce][0] == True and self.sala[miejsce][1] == imie and self.sala[miejsce][2] == nazwisko:
            self.odwolajRezerwacje(miejsce)
            print('Rezerwacja zostala odwolana.')
        else:
            raise ValueError("Nie mozna odwolac rezerwacji, miejsce nie zostalo przez Ciebie zarezerwowane.")
        


kino = Kino()
lista = []

miejsce1 = "1"
imie1 = "Marzena"
nazwisko1 = "Musztarda"

miejsce2 = "4"
imie2 = "Janusz"
nazwisko2 = "Opryskiwacz"

kino.SprawdzRezerwacje(lista,miejsce1,imie1,nazwisko1)
kino.SprawdzRezerwacje(lista,miejsce2,imie2,nazwisko2)
print(kino.sala)

kino.SprawdzOdwolanie(miejsce1,imie1,nazwisko1)

kino.SprawdzOdwolanie(miejsce2,imie1,nazwisko1)




