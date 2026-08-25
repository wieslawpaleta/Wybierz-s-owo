#Tutaj znajdują się potrzebne importy.
import random
from słowniki_lista_losowanie import słowniki
import główne_okno
import lista
import zgadywanka


#Tutaj dokonuje się wybór języka.
def poczatek_losowania():


    while True:


        print("Wylosuj słowo!")
        print("Albo wpisz \"Powrót\", aby powrócić do głównego menu, albo \"Wyjście\", aby wyjść z programu.")


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
                return główne_okno.główne_okno()


            elif język == "wyjście":
                print("Zamykanie programu. Do zobaczenia!")
                exit()

            
            else:
                print("Wybrany język jest nieobsługiwany.")
                

#Tutaj dokonuje się losowanie słowa.                
def losowanie_slowa(język):

        
        while True:


            gamba = input("Czy chcesz wylosować słowo? (tak/nie): ").strip().lower()


            if gamba == "tak":
                maszyna = random.randint(1, 100)
                if 1 <= maszyna <= 100:
                    slowo_obce = słowniki[język][maszyna - 1]
                    slowo_polskie = słowniki["pl"][maszyna - 1]
                    print("Wylosowane słowo to: \n" + slowo_obce + "-" + slowo_polskie)


            #Tutaj można wybrać tryb, wrócić do głównego okna lub wyjść z programu.
            elif gamba == "nie":


                print("Wpisz 'Losowanie', aby rozpocząć nowe losowanie.")    
                print("Wpisz 'Lista', aby przejść do trybu listy.")
                print("Wpisz 'Zgadywanka', aby przejść do trybu zgadywania.")
                print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                print("Wpisz 'Wyjście', aby zakończyć działanie programu.")
                lufa_pytanie = input("Co chcesz teraz zrobić?: ").strip().lower()


                if lufa_pytanie == "losowanie":
                    return poczatek_losowania()
               

                elif lufa_pytanie == "wybór słowa":
                    return lista.wybierz_slowo()

                
                elif lufa_pytanie == "zgadywanka":
                    return zgadywanka.zgadnij()

                
                elif lufa_pytanie == "powrót":
                    return główne_okno.główne_okno()

                
                elif lufa_pytanie == "wyjście":
                    print("Do zobaczenia!")
                    exit()
            
                
                else:
                    print("Niepoprawna opcja. Spróbuj ponownie.")


            else:
                print("Niepoprawna odpowiedź. Wpisz 'tak' lub 'nie'.")
        