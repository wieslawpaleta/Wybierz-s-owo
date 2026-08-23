#To jest plik odpowiedzialny za losowanie słów w różnych językach, które użytkownik może wybrać do nauki.


import random
from slowniki import baza_jezykowa
import Główne_okno
import Lista
import Zgadywanka


def poczatek_losowania():
    while True:
        print("Wylosuj słowo!")
        print("Albo wpisz 'powrót', aby wrócić do głównego menu.")
        while True:    
            język = input("Wybierz język: ").strip().lower()  
            if język == "en":
                print("Wybrałeś język angielski.")
                return losowanie_slowa(język)
            elif język == "ru":
                print("Wybrałeś język rosyjski.")
                return losowanie_slowa(język)
            elif język == "es":
                print("Wybrałeś język hiszpański.")
                return losowanie_slowa(język)
            elif język == "fr":
                print("Wybrałeś język francuski.")
                return losowanie_slowa(język)
            elif język == "de":
                print("Wybrałeś język niemiecki.")
                return losowanie_slowa(język)
            elif język == "ar":
                print("Wybrałeś język arabski.")
                return losowanie_slowa(język)
            elif język == "ch":
                print("Wybrałeś język chiński.")
                return losowanie_slowa(język)
            elif język == "kr":
                print("Wybrałeś język koreański.")
                return losowanie_slowa(język)
            elif język == "jp":
                print("Wybrałeś język japoński.")
                return losowanie_slowa(język)
            elif język == "tj":
                print("Wybrałeś język tajski.")
                return losowanie_slowa(język)
            elif język == "powrót":
                return Główne_okno.Główne_okno()
            else:
                print("Wybrany język jest nieobsługiwany.")
                
                
def losowanie_slowa(język):
        while True:
            gamba = input("Czy chcesz wylosować słowo? (tak/nie): ").strip().lower()
            if gamba == "tak":
                maszyna = random.randint(1, 100)
                if 1 <= maszyna <= 100:
                    slowo_obce = baza_jezykowa[język][maszyna - 1]
                    slowo_polskie = baza_jezykowa["pl"][maszyna - 1]
                    print("Wylosowane słowo to: \n" + slowo_obce + "-" + slowo_polskie)
            elif gamba == "nie":
                print("Wpisz 'Wybór słowa', aby przejść do trybu wyboru słowa.")
                print("Wpisz 'Zgadywanka', aby przejść do trybu zgadywania.")
                print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                print("Wpisz 'Wyjście', aby zakończyć program.")
                print("Wpisz 'Nowe losowanie', aby zrobić nowe losowanie.")
                lufa_pytanie = input("Co chcesz teraz zrobić?: ").strip().lower()
                if lufa_pytanie == "wybór słowa":
                    return Lista.wybierz_slowo()
                elif lufa_pytanie == "zgadywanka":
                    return Zgadywanka.zgadnij()
                elif lufa_pytanie == "powrót":
                    return Główne_okno.Główne_okno()
                elif lufa_pytanie == "wyjście":
                    print("Zamykanie programu. Do zobaczenia!")
                    exit()
                elif lufa_pytanie == "nowe losowanie":
                    return poczatek_losowania()
                else:
                    print("Niepoprawna opcja. Spróbuj ponownie.")
            else:
                print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.")
        