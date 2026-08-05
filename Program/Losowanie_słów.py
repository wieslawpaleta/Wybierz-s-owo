import random
from slowniki import baza_jezykowa

while True:
    print("Wylosuj słowo!")
    print("Albo wpisz 'powrót', aby wrócić do głównego menu.")
    
    while True:    
        język = input("Wybierz język: ").strip().lower()

        if język == "powrót":
            import Główne_okno
            break   

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
        else:
            print("Wybrany język jest nieobsługiwany.")
            
            

    while True:
        
        gumbu = input("Czy chcesz wylosować słowo? (tak/nie): ").strip().lower()
        if gumbu == "tak":
            gamba = random.randint(1, 100)
            if 1 <= gamba <= 100:
                slowo_obce = baza_jezykowa[język][gamba - 1]
                slowo_polskie = baza_jezykowa["pl"][gamba - 1]
                print("Wylosowane słowo to: \n" + slowo_obce + "-" + slowo_polskie)
        
        elif gumbu == "nie":
            zmianawyjscie = input("Wpisz 'powrót' aby wrócić do menu głównego lub 'wyjście' aby zamknąć program: ").strip().lower()
            if zmianawyjscie == "powrót":
                import Główne_okno
                break
            elif zmianawyjscie == "wyjście":
                print("Zamykanie programu. Do zobaczenia!")
                exit()
            else:
                print("Niepoprawna opcja. Spróbuj ponownie.")
        else:
            print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.")
    