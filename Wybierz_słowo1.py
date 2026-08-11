#wersja 2.0


from slowniki import baza_jezykowa

print("Wybierz język oraz trzy liczby całkowite z określonych zakresów, aby wygenerować listę słów")
      
język = input("Wybierz język: ").strip().lower()

if język == "en":
    print("Wybrałeś język angielski.")
elif język == "ru":
    print("Wybrałeś język rosyjski.")
elif język == "es":
    print("Wybrałeś język hiszpański.")
elif język == "fr":
    print("Wybrałeś język francuski.")
elif język == "de":
    print("Wybrałeś język niemiecki.")
elif język == "ar":
    print("Wybrałeś język arabski.")
elif język == "ch":
    print("Wybrałeś język chiński.")
elif język == "kr":
    print("Wybrałeś język koreański.")
elif język == "jp":
    print("Wybrałeś język japoński.")
elif język == "tj":
    print("Wybrałeś język tajski.")
else:
    print("Wybrany język jest nieobsługiwany.")
    exit()

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
                slowo_obce = baza_jezykowa[język][i]
                slowo_pl = baza_jezykowa["pl"][i]
        
                print(slowo_obce, "-", slowo_pl)

            break
        else:
            print("Wprowadzone liczby są nie spełniają warunków.")

    except ValueError:
        print("Błąd! Musisz wpisać liczby całkowite, a nie litery. Spróbuj ponownie.\n")
        



# print("Wybierz pierwszą liczbę od 1 do 100: ")
# a = int(input())
# print("Wybierz drugą liczbę od 1 do 100(musi być większa niż pierwsza): ")
# b = int(input()) 
# print("Wybierz trzecią liczbę od 1 do 3: ")
# c = int(input())    

# if 1 <= a <= 100 and 1 <= b <= 100 and a < b and 1 <= c <= 3:
#     print("Twoja lista słów to: ")
#     for i in range(a - 1, b, c):
#         slowo_obce = baza_jezykowa[język][i]
#         slowo_pl = baza_jezykowa["pl"][i]
        
#         print(slowo_obce, "-", slowo_pl)
# else:
#     print("Wprowadzone liczby są nie spełniają warunków.")

