#Tu znajdują się potrzebne importy.

import główne_okno
import json
from słownik_zgadywanka import zbiór_słów


#Tutaj jest zapisany kod, który dodaje słowo do zbioru słów.
def rozszerzenie_zbioru():


    while True:


        początek = input("\nCzy chcesz dodać nowe słowo do zgadywanki? (tak/nie): ")


        if początek.lower() == "tak":
            dodatek = input("\nWprowadź słowe, które chcesz dodać: ")
            zbiór_słów.append(dodatek)
            print("\nSłowo zostało dodane")


            with open("lista_palabras.json", "w", encoding="utf-8") as archivo:
                json.dump(zbiór_słów, archivo, ensure_ascii=False, indent=4)


            print("\nLista actualizada y guardada en lista_palabras.json")



        elif początek.lower() == "nie":
            print("\nNo to wracamy do głównego menu!\n")
            return główne_okno.główne_okno()
            


        else:
            print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.\n")



