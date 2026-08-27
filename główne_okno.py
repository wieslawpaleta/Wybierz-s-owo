#To jest główne okno, w którym użytkownik wybiera tryb działania programu.
#Tutaj znajdują się potrzebne importy.
import losowanie
import lista
import zgadywanka


#Główne okno wyboru.
def główne_okno():


    print("Cześć!")
    tryb = input("Wybierz i wpisz nazwę jednego z trybów: \"Losowanie\", \"Lista\", \"Zgadywanka\", \"Wyjście\": ")


    while True:


        try:
            if tryb.lower() == "losowanie":
                return losowanie.początek_losowania()  

             
            elif tryb.lower() == "lista":
                return lista.wybierz_słowo()

            
            elif tryb.lower() == "zgadywanka":
                return zgadywanka.zgadnij()

            
            elif tryb.lower() == "wyjście":
                print("Do zobaczenia!")
                exit()

                
            else:
                print("Masz ostatnie ostrzeżenie w tej chwili,\nmasz ostatnie ostrzeżenie!")
                tryb = input("Wybierz i wpisz nazwę jednego z trybów: \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")


        except ValueError:
            print("Posłuchaj dzieciaku!")


#Dzięki temu można uruchomić program.
if __name__ == "__main__":
    główne_okno() 
     


