#wersja 4.0
import Losowanie_słów
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
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "ru":
                print("Wybrałeś język rosyjski.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "es":
                print("Wybrałeś język hiszpański.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "fr":
                print("Wybrałeś język francuski.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "de":
                print("Wybrałeś język niemiecki.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "ar":
                print("Wybrałeś język arabski.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "ch":
                print("Wybrałeś język chiński.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "kr":
                print("Wybrałeś język koreański.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "jp":
                print("Wybrałeś język japoński.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "tj":
                print("Wybrałeś język tajski.")
                return generuj_liste_slow(język, a=None, b=None, c=None)
            elif język == "powrót":
                return Główne_okno.Główne_okno()   
            else:
                print("Wybrany język jest nieobsługiwany.")
                
            
def generuj_liste_slow(język, a, b, c):
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
                    while True:     
                        print("Wpisz 'Nowa lista', aby stworzyć nową listę.")
                        print("Wpisz 'Losowanie', aby przejść do trybu losowania słowa.")
                        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                        print("Wpisz 'Wyjście', aby zakończyć program.")                      
                        gothic = input("Co chcesz teraz zrobić?: ").strip().lower()                        

                        if gothic == "nowa lista":
                            return wybierz_slowo()
                        elif gothic == "losowanie":
                            return Losowanie_słów.losuj_slowo()
                        elif gothic == "powrót":
                            print("No to wracamy!")
                            return Główne_okno.Główne_okno()
                        elif gothic == "wyjście":
                            print("Do zobaczenia!")
                            exit()
                        else:
                            print("Spróbuj jeszcze raz.")
                else:
                    print("Wprowadzone liczby są nie spełniają warunków.")

            except ValueError:
                print("Błąd! Musisz wpisać liczby całkowite, a nie litery. Spróbuj ponownie.\n")