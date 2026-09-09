import główne_okno


def przeliteruj():
    print("PRZELITERUJ SŁOWO!\n")
    while True:
        print("-" * 10)
        print("Dostępne komendy:")
        print("1) \"Pwrt\", żeby wrócić do głównego okna.")
        print("2) \"Wsc\", żeby zakończyć działanie programu.")
        print("-" * 10)
        rozkład = input("Podaj słowo, które chcesz przeliterować: ")


        if rozkład.lower() == "pwrt":
            print("\nNo to wracamy!")
            return główne_okno.główne_okno()
        
        
        elif rozkład.lower() == "wsc":
            print("\nDo zobaczenia!")
            exit()


        elif rozkład.isalpha():
            for x in rozkład:
                print(x)


        

        
        else:
            print("Spróbuj jeszcze raz.")
        