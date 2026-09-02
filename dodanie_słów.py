#Tu znajdują się potrzebne importy.

import główne_okno
import json
import os
from słownik_zgadywanka import zbiór_słów


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCIEZKA_JSON = os.path.join(BASE_DIR, "lista_palabras.json")


#Tutaj jest zapisany kod, który dodaje słowo do zbioru słów.
def edytor_zbioru():


    while True:

        cochceszzrobić = input("\nPokaż listę słów albo dodaj lub usuń słowo ze zbioru słów. Wpisz \"Pokaż\" albo \"Dodaj\" albo \"Usuń\" albo \"Powrót\":")

        if cochceszzrobić.lower() == "pokaż":
            print("\nLista słów:")
            print(zbiór_słów)

        elif cochceszzrobić.lower() == "dodaj":

            początek = input("\nCzy chcesz dodać nowe słowo do zgadywanki? (tak/nie): ")


            if początek.lower() == "tak":
                dodatek = input("\nWprowadź słowe, które chcesz dodać: ")
                zbiór_słów.append(dodatek)
                print("\nSłowo zostało dodane")


                with open(SCIEZKA_JSON, "w", encoding="utf-8") as archivo:
                    json.dump(zbiór_słów, archivo, ensure_ascii=False, indent=4)


                print("\nLista actualizada y guardada en lista_palabras.json")



            elif początek.lower() == "nie":
                print("\nNo to wracamy do głównego menu!\n")
                return główne_okno.główne_okno()
                


            else:
                print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.\n")


        elif cochceszzrobić.lower() == "usuń":
            usuwanie = input("\nWprowadź słowo, które chcesz usunąć: ")
            if usuwanie in zbiór_słów:
                zbiór_słów.remove(usuwanie)
                print("\nSłowo zostało usunięte")


                with open(SCIEZKA_JSON, "w", encoding="utf-8") as archivo:
                    json.dump(zbiór_słów, archivo, ensure_ascii=False, indent=4)


                print("\nLista actualizada y guardada en lista_palabras.json")



            else:
                print("\nNie znaleziono słowa w zbiorze.\n")

        else:  
            return główne_okno.główne_okno()



