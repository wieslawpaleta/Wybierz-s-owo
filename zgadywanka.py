#Import potrzebnych elementów.
import random
from słownik_zgadywanka import zbiór_słów
import główne_okno
import lista
import losowanie


#Tu zaczyna się gra.
def zgadnij():

    
    print("\nZgadnij słowo!")


    słowo = random.choice(zbiór_słów).lower()


    #Na wypadek testów.
    #print(słowo)
    tajemnicze_słowo = słowo
    zakreskowane_słowo = ["_"] * len(tajemnicze_słowo)


    próby = 0
    max_prób = 10


    #Pętla zgadywania słowa z możliwością powrótu do głównego menu oraz zakończenia działania programu.
    while próby < max_prób:


        próba = input(f"\n(Próba {próby + 1}/{max_prób}) Podaj literę albo zgadnij słowo.\nWpisz \"Powrót\", żeby wrócić do głównego okna albo \"Wyjście\", żeby zakończyć działanie programu: ").lower()


        if próba.lower() == "wyjście":
            print("Do zobaczenia!")
            exit()

            
        if próba.lower() == "powrót":
            print("No to wracamy!\n")
            return główne_okno.główne_okno()
            

        if próba == tajemnicze_słowo:
            print("Brawo! Odgadłeś słowo!")
            break


        if len(próba) != 1 or not próba.isalpha():
            print("Podaj jedną literę albo słowo (bez cyfr i symboli)!")
            continue

        

        for i in range(len(tajemnicze_słowo)):
            if próba == tajemnicze_słowo[i]:
                zakreskowane_słowo[i] = próba        
            

        wynik_wyświetlany = " ".join(zakreskowane_słowo)
        print("Aktualny stan słowa:", wynik_wyświetlany)
            
        
        if "_" not in zakreskowane_słowo:
            print("\nGratulacje! Odgadłeś słowo!")
            break


        próby += 1


    else:
        print(f"\nPrzegrałeś, a tu słowo, którego szukałeś: {tajemnicze_słowo} \n")


    #Pętła wyboru trybów.
    while True:   


        print("Wpisz 'Zgadywanka', aby raz jeszcze zgadnąć słowo.")
        print("Wpisz 'Losowanie', aby przejść do trybu losowania.")
        print("Wpisz 'Lista', aby przejść do trybu listy.")
        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
        print("Wpisz 'Wyjście', aby zakończyć działanie programu.")               
        сozrobić = input("Co chcesz teraz zrobić?: ").strip().lower()  

              
        if сozrobić == "zgadywanka":
            return zgadnij()

        
        elif сozrobić == "lista":
            return lista.wybierz_słowo()

        
        elif сozrobić == "losowania":
            return losowanie.początek_losowania()

        
        elif сozrobić == "powrót":
            print("No to wracamy!\n")
            return główne_okno.główne_okno()

        
        elif сozrobić == "wyjście":
            print("Do zobaczenia!")
            exit()


        else:
            print("Spróbuj jeszcze raz.")

     



