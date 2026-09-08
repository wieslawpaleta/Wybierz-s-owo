import główne_okno




def przeliteruj():
    print("PRZELITERUJ SŁOWO!\n")
    while True:
        print("-" * 10)
        print("Dostępne komendy:")
        print("1) \"Powrót\"")
        print("2) \"Wyjście\"")
        print("-" * 10)
        rozkład = input("Podaj słowo, które chcesz przeliterować: ")

        if rozkład.isalpha():
            for x in rozkład:
                print(x)
        else:
            print("Spróbuj jeszcze raz.")
        


if __name__ == "__main__":
    przeliteruj() 