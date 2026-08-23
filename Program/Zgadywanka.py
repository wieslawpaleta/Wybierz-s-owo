import random
from slowa_zgadywanka import slowa
import Główne_okno
import Lista
import Losowanie

def zgadnij():
    
    print("Witaj w zgadywance!")
    print("Zgadnij słowo w dziesięciu próbach.")

    słowo = random.choice(slowa).lower()
    print(słowo)
    tajemnicze_słowo = słowo

    zakreskowane_slowo = ["_"] * len(tajemnicze_słowo)

    proby = 0
    max_prob = 10

    while proby < max_prob:

        pierwsza_próba = input(f"\nPróba {proby + 1}/{max_prob} Podaj literę albo zgadnij słowo albo wpisz \"Wyjście\", aby wyjść z programu albo \"Powrót\", aby powróć do głównego okna: ").lower()

        if pierwsza_próba.lower() == "wyjście":
            print("Do zobaczenia!")
            exit()
            
        if pierwsza_próba.lower() == "powrót":
            return Główne_okno.Główne_okno()
            

        if pierwsza_próba == tajemnicze_słowo:
            print("Brawo! Odgadłeś słowo!")
            break

        if len(pierwsza_próba) != 1 or not pierwsza_próba.isalpha():
            print("Podaj jedną literę (bez cyfr i symboli)!")
            continue

        

        for i in range(len(tajemnicze_słowo)):
            if pierwsza_próba == tajemnicze_słowo[i]:
                zakreskowane_slowo[i] = pierwsza_próba        
            

        wynik_wyswietlany = " ".join(zakreskowane_slowo)
        print("Aktualny stan słowa:", wynik_wyswietlany)
            
        
        if "_" not in zakreskowane_slowo:
            print("\nGratulacje! Odgadłeś słowo!")
            break

        proby += 1
    else:
        print(f"\nPrzegrałeś! Słowem było: {tajemnicze_słowo} \n")


    while True:   
        print("Wpisz 'Zgadywanka', aby raz jeszcze zgadnąć słowo.")
        print("Wpisz 'Losowanie', aby przejść do trybu losowania słowa.")
        print("Wpisz 'Lista', aby przejść do trybu listy.")
        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
        print("Wpisz 'Wyjście', aby zakończyć program.")      
        сozrobic = input("Co chcesz teraz zrobić?: ").strip().lower()        
        if сozrobic == "lista":
            return Lista.wybierz_slowo()
        elif сozrobic == "losowanie":
            return Losowanie.poczatek_losowania()
        elif сozrobic == "zgadywanka":
            return zgadnij()
        elif сozrobic == "powrót":
            print("No to wracamy!")
            return Główne_okno.Główne_okno()
        elif сozrobic == "wyjście":
            print("Do zobaczenia!")
            exit()
        else:
            print("Spróbuj jeszcze raz.")

     





