#To jest główne okno, w którym użytkownik wybiera tryb działania programu.
#Tutaj znajdują się potrzebne importy.
import losowanie
import lista
import zgadywanka
import edytor_słowników

#Główne okno wyboru.
def główne_okno():


    print("Cześć!")
    tryb = input("Wybierz i wpisz nazwę jednego z trybów: \"Losowanie\", \"Lista\", \"Zgadywanka\", \"Wyjście\", \"Edytor słowników\": ")


    while True:


        try:
            if tryb.lower() == "losowanie":
                return losowanie.początek_losowania()  

             
            elif tryb.lower() == "lista":
                return lista.wybierz_słowo()

            
            elif tryb.lower() == "zgadywanka":
                return zgadywanka.zgadnij()


            elif tryb.lower() == "edytor słowników":
                return edytor_słowników.edytor_zbioru()

            
            elif tryb.lower() == "wyjście":
                print("\nDo zobaczenia!")
                exit()

                
            else:
                print("\nMasz ostatnie ostrzeżenie w tej chwili,\nmasz ostatnie ostrzeżenie!\n")
                tryb = input("Wybierz i wpisz nazwę jednego z trybów: \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")


        except ValueError:
            print("\nPosłuchaj dzieciaku!\n")


#Dzięki temu można uruchomić program.
if __name__ == "__main__":
    główne_okno() 
     


