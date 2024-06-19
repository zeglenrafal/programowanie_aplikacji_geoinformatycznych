from os import getcwd 
from imp import reload
import czas
import time


print("Hello World")
help(print)

current_path=getcwd()
print(current_path)

print(czas.aktualny_czas)
time.sleep(20)
print(czas.aktualny_czas)

reload(czas)
print(czas.aktualny_czas) 
#zmienna inicjowana jest przy ładowaniu pakietu(?)
