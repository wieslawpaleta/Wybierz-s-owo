



print("Cześć! wybierz tryb, aby przejść dalej do programu.")
tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
while True:
    try:
        if tryb.lower() == "losowanie":
            import Losowanie_słów
            break
        elif tryb.lower() == "wybierz słowo":
            import Wybierz_słowo2
            break
        elif tryb.lower() == "wyjście":
            print("Do zobaczenia!")
            exit()
            break
        else:
            print("Masz ostatnie ostrzeżenie w tej chwili, \nmasz ostatnie ostrzeżenie!")
            tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
    except ValueError:
        print("Posłuchaj dzieciaku!")



     


