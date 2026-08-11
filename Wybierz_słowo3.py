#wersja 4.0

import Główne_okno
from slowniki import baza_jezykowa


def wybierz_slowo():
    while True:
        print("Wybierz język oraz trzy liczby całkowite z określonych zakresów, aby wygenerować listę słów")
        print("Wpisz 'powrót', aby wrócić do głównego menu.")
        
        while True:    
            język = input("Wybierz język: ").strip().lower()


            if język == "en":
                print("Wybrałeś język angielski.")
                break
            elif język == "ru":
                print("Wybrałeś język rosyjski.")
                break
            elif język == "es":
                print("Wybrałeś język hiszpański.")
                break
            elif język == "fr":
                print("Wybrałeś język francuski.")
                break
            elif język == "de":
                print("Wybrałeś język niemiecki.")
                break
            elif język == "ar":
                print("Wybrałeś język arabski.")
                break
            elif język == "ch":
                print("Wybrałeś język chiński.")
                break
            elif język == "kr":
                print("Wybrałeś język koreański.")
                break
            elif język == "jp":
                print("Wybrałeś język japoński.")
                break
            elif język == "tj":
                print("Wybrałeś język tajski.")
                break
            elif język == "powrót":
                return Główne_okno.Główne_okno()   
            else:
                print("Wybrany język jest nieobsługiwany.")
                
            

    while True:
        try:
            print("Wybierz pierwszą liczbę od 1 do 100: ")
            a = int(input())
            print("Wybierz drugą liczbę od 1 do 100(musi być większa niż pierwsza): ")
            b = int(input()) 
            print("Wybierz trzecią liczbę od 1 do 3: ")
            c = int(input())    

            if 1 <= a <= 100 and 1 <= b <= 100 and a < b and 1 <= c <= 3:
                print("Twoja lista słów to: ")
                for i in range(a - 1, b, c):
                    slowo_obce = baza_jezykowa[język][i]
                    slowo_pl = baza_jezykowa["pl"][i]
            
                    print(slowo_obce, "-", slowo_pl)

                break
            else:
                print("Wprowadzone liczby są nie spełniają warunków.")

        except ValueError:
            print("Błąd! Musisz wpisać liczby całkowite, a nie litery. Spróbuj ponownie.\n")