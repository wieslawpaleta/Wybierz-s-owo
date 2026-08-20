import random
from slowa_wordle import slowa

print("Wital w grze Wordle!")
print("Zgadnij słowo w 6 próbach.")

słowo = random.choice(slowa)

pierwsza_próba = input("Podaj swoje pierwsze słowo: ")

druga_próba = input("Podaj swoje drugie słowo: ")

trzecia_próba = input("Podaj swoje trzecie słowo: ")

czwarta_próba = input("Podaj swoje czwarte słowo: ")

piąta_próba = input("Podaj swoje piąte słowo: ")

szósta_próba = input("Podaj swoje szóste słowo: ")

if pierwsza_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w pierwszej próbie!")  
elif druga_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w drugiej próbie!")  
elif trzecia_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w trzeciej próbie!")
elif czwarta_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w czwartej próbie!")
elif piąta_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w piątej próbie!")
elif szósta_próba == słowo:
    print("Gratulacje! Zgadłeś słowo w szóstej próbie!")    
else:
    print(f"Niestety, nie udało Ci się zgadnąć słowa. Prawidłowe słowo to: {słowo}")













