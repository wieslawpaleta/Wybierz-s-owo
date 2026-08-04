



print("Cześć! wybierz tryb, aby przejść dalej do programu.")
tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")

if tryb.lower() == "losowanie":
    import Losowanie_słów
elif tryb.lower() == "wybierz słowo":
    import Wybierz_słowo2
elif tryb.lower() == "wyjście":
    print("Do zobaczenia!")
    exit()
else:
    print("Niepoprawny tryb. Wybierz \"Losowanie\" albo \"Wybierz słowo\".")