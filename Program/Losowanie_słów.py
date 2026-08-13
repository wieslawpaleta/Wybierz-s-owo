import random
from slowniki import baza_jezykowa
import Główne_okno
import Wybierz_słowo3

def losuj_slowo():
    while True:
        print("Wylosuj słowo!")
        print("Albo wpisz 'powrót', aby wrócić do głównego menu.")
        
        while True:    
            język = input("Wybierz język: ").strip().lower()  


            if język == "en":
                print("Wybrałeś język angielski.")
                return grzyb(język)
            elif język == "ru":
                print("Wybrałeś język rosyjski.")
                return grzyb(język)
            elif język == "es":
                print("Wybrałeś język hiszpański.")
                return grzyb(język)
            elif język == "fr":
                print("Wybrałeś język francuski.")
                return grzyb(język)
            elif język == "de":
                print("Wybrałeś język niemiecki.")
                return grzyb(język)
            elif język == "ar":
                print("Wybrałeś język arabski.")
                return grzyb(język)
            elif język == "ch":
                print("Wybrałeś język chiński.")
                return grzyb(język)
            elif język == "kr":
                print("Wybrałeś język koreański.")
                return grzyb(język)
            elif język == "jp":
                print("Wybrałeś język japoński.")
                return grzyb(język)
            elif język == "tj":
                print("Wybrałeś język tajski.")
                return grzyb(język)
            elif język == "powrót":
                return Główne_okno.Główne_okno()
            else:
                print("Wybrany język jest nieobsługiwany.")
                
                
def grzyb(język):
        while True:
            
            gumbu = input("Czy chcesz wylosować słowo? (tak/nie): ").strip().lower()
            if gumbu == "tak":
                gamba = random.randint(1, 100)
                if 1 <= gamba <= 100:
                    slowo_obce = baza_jezykowa[język][gamba - 1]
                    slowo_polskie = baza_jezykowa["pl"][gamba - 1]
                    print("Wylosowane słowo to: \n" + slowo_obce + "-" + slowo_polskie)
            
            elif gumbu == "nie":
                
                print("Wpisz 'Wybór słowa', aby przejść do trybu wyboru słowa.")
                print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                print("Wpisz 'Wyjście', aby zakończyć program.")
                print("Wpisz 'Nowe losowanie', aby zrobić nowe losowanie.")
                kielbasa = input("Co chcesz teraz zrobić?: ").strip().lower()
                if kielbasa == "wybór słowa":
                    return Wybierz_słowo3.wybierz_slowo()
                elif kielbasa == "powrót":
                    return Główne_okno.Główne_okno()
                elif kielbasa == "wyjście":
                    print("Zamykanie programu. Do zobaczenia!")
                    exit()
                elif kielbasa == "nowe losowanie":
                    return losuj_slowo()
                else:
                    print("Niepoprawna opcja. Spróbuj ponownie.")
            else:
                print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.")
        