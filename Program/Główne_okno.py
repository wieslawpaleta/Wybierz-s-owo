
import Losowanie
import Lista

def Główne_okno():
    print("Cześć! wybierz tryb, aby przejść dalej do programu.")
    tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
    while True:
        try:
            if tryb.lower() == "losowanie":
                return Losowanie.poczatek_losowania()
                
            elif tryb.lower() == "wybierz słowo":
                return Lista.wybierz_slowo()
            
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
     


