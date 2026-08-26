#wersja 4.0
#Tutaj znajdują się potrzebne importy.
import losowanie
import główne_okno
from słowniki_lista_losowanie import słowniki
import zgadywanka


#Tutaj dokonuje się wybór języka.    
def wybierz_słowo():


    while True:


        print("Wybierz język oraz trzy liczby całkowite z określonych zakresów, aby wygenerować listę słów.")
        print("Wpisz 'Powrót', aby wrócić do głównego menu albo 'Wyjśćie', zakończyć działanie programu.")


        while True:    


            język = input("Wybierz język: ").strip().lower()


            if język == "en":
                print("Wybrałeś język angielski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ru":
                print("Wybrałeś język rosyjski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "es":
                print("Wybrałeś język hiszpański.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "fr":
                print("Wybrałeś język francuski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "de":
                print("Wybrałeś język niemiecki.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ar":
                print("Wybrałeś język arabski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "ch":
                print("Wybrałeś język chiński.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "kr":
                print("Wybrałeś język koreański.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "jp":
                print("Wybrałeś język japoński.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "tj":
                print("Wybrałeś język tajski.")
                return generuj_listę_słów(język, a=None, b=None, c=None)

            
            elif język == "powrót":
                return główne_okno.główne_okno()   


            elif język == "wyjście":
                print("Do zobaczenia!")
                exit()   

            
            else:
                print("Wybrany język jest nieobsługiwany.")
                

#Tutaj tworzy się lista.         
def generuj_listę_słów(język, a, b, c):

        
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
                        słowo_obce = słowniki[język][i]
                        słowo_pl = słowniki["pl"][i]
                        print(słowo_obce, "-", słowo_pl)


                    #Tutaj dokonuje się wybór o przyszłości.    
                    while True:     


                        print("Wpisz 'Lista', aby stworzyć nową listę.")
                        print("Wpisz 'Losowanie', aby przejść do trybu losowania.")
                        print("Wpisz 'Zgadywanka', aby przejść do trybu zgadywania.")
                        print("Wpisz 'Powrót', aby wrócić do głównego menu.")
                        print("Wpisz 'Wyjście', aby zakończyć działanie programu.")                      
                        сozrobić = input("Co chcesz teraz zrobić?: ").strip().lower()                        


                        if сozrobić == "lista":
                            return wybierz_słowo()

                        
                        elif сozrobić == "losowanie":
                            return losowanie.początek_losowania()

                        
                        elif сozrobić == "zgadywanka":
                            return zgadywanka.zgadnij()

                        
                        elif сozrobić == "powrót":
                            print("No to wracamy!")
                            return główne_okno.główne_okno()

                        
                        elif сozrobić == "wyjście":
                            print("Do zobaczenia!")
                            exit()


                        else:
                            print("Spróbuj jeszcze raz.")


                else:
                    print("Wprowadzone liczby są nie spełniają warunków.")


            except ValueError:
                print("Błąd! Musisz wpisać liczby całkowite. Spróbuj ponownie.\n")