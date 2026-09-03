#Tu znajdują się potrzebne importy.

import główne_okno
import json
import os
from słownik_zgadywanka import zbiór_słów


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCIEZKA_JSON = os.path.join(BASE_DIR, "lista_palabras.json")


#Tutaj jest zapisany kod, który dodaje, usuwa słowo, wyświetla zbiór słów, wraca do głównego okna oraz kończy działanie programu.
def edytor_zbioru():


    while True:

        cochceszzrobić = input("\nWpisz:\n1) \"Wyświetl\",aby wyświetlić zbiór,\n2) \"Dodaj\",aby dodać słowo,\n3) \"Usuń\",aby usunąć słowo,\n4) \"Powrót\",aby wrócić do głównego menu:")

        if cochceszzrobić.lower() == "wyświetl":
            print("\nLista słów:")

            słowa_lista = list(zbiór_słów)
            for i, słowo in enumerate(słowa_lista):

                print(słowo, end=" ")
                if (i + 1) % 5 == 0:
                    print()
            print()

        elif cochceszzrobić.lower() == "dodaj":


            dodatek = input("\nWprowadź słowe, które chcesz dodać: ")
            zbiór_słów.append(dodatek)
            print("\nSłowo zostało dodane")


            with open(SCIEZKA_JSON, "w", encoding="utf-8") as archivo:
                json.dump(zbiór_słów, archivo, ensure_ascii=False, indent=4)


            print("\nLista actualizada y guardada en lista_palabras.json")


        elif cochceszzrobić.lower() == "usuń":


            usuwanie = input("\nWprowadź słowo, które chcesz usunąć: ")
            if usuwanie in zbiór_słów:
                zbiór_słów.remove(usuwanie)
                print("\nSłowo zostało usunięte")


                with open(SCIEZKA_JSON, "w", encoding="utf-8") as archivo:
                    json.dump(zbiór_słów, archivo, ensure_ascii=False, indent=4)


                print("\nLista actualizada y guardada en lista_palabras.json")


            elif usuwanie not in zbiór_słów:
                print("\nNie znaleziono słowa w zbiorze.")
                


        elif cochceszzrobić.lower() == "powrót":
            print("\nNo to wracamy!\n")
            return główne_okno.główne_okno()
        

        else:  
            print("\nNiepoprawna opcja. Spróbuj ponownie.")



