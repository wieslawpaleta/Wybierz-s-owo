
import Losowanie_słów
import Wybierz_słowo3

def Główne_okno():
    print("Cześć! wybierz tryb, aby przejść dalej do programu.")
    tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
    while True:
        try:
            if tryb.lower() == "losowanie":
                return Losowanie_słów.losuj_slowo()
                
            elif tryb.lower() == "wybierz słowo":
                return Wybierz_słowo3.wybierz_slowo()
            
            elif tryb.lower() == "wyjście":
                print("Do zobaczenia!")
                exit()
            else:
                print("Masz ostatnie ostrzeżenie w tej chwili, \nmasz ostatnie ostrzeżenie!")
                tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
        except ValueError:
            print("Posłuchaj dzieciaku!")

if __name__ == "__main__":
    Główne_okno() 
     


