

# for i in range(3):
#     print(i)

tajemnicze_słowo = "czapka"

zakreskowane_slowo = ["_"] * len(tajemnicze_słowo)

pierwsza_próba = input("Podaj literę: ")

for i in range(len(tajemnicze_słowo)):
                    
    if pierwsza_próba == tajemnicze_słowo[i]:
        zakreskowane_slowo[i] = pierwsza_próba
       

wynik_wyswietlany = " ".join(zakreskowane_slowo)

print("Aktualny stan słowa:", wynik_wyswietlany)







# import random
# from slowa_wordle import slowa

# def jeden():
    
#     print("Wital w grze Wordle!")
#     print("Zgadnij sześcioliterowe słowo w sześciu próbach.")

#     słowo = random.choice(slowa).lower()
#     print(słowo)
#     tajemnicze_słowo = słowo

#     zakreskowane_slowo = ["_"] * len(tajemnicze_słowo)

#     proby = 0
#     max_prob = 6

#     while proby < max_prob:

#         pierwsza_próba = input(f"\nPróba {proby + 1}/{max_prob} Podaj swoje słowo: ").lower()

#         if len(pierwsza_próba) != len(tajemnicze_słowo):
#                     print("Słowo ma składa się z sześciu liter!")
#                     continue
        

#         for i in range(len(tajemnicze_słowo)):
#             if pierwsza_próba[i] == tajemnicze_słowo[i]:
#                 zakreskowane_slowo[i] = pierwsza_próba[i]        
            

#             wynik_wyswietlany = " ".join(zakreskowane_slowo)
#             print("Aktualny stan słowa:", wynik_wyswietlany)
            
        
#         if "_" not in zakreskowane_slowo:
#             print("\nGratulacje! Odgadłeś słowo!")
#             return

#         proby += 1

#     print(f"\nPrzegrałeś! Tajemniczym słowem było: {tajemnicze_słowo}")


# if __name__ == "__main__":
#     jeden() 
     





