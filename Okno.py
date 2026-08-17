import tkinter as tk
from tkinter import ttk
import Losowanie
import Lista

def accion_boton():
    etiqueta.config(text="")

ventana = tk.Tk()
ventana.title("")
ventana.geometry("1920x1080")


etiqueta = tk.Label(ventana, text="Pora na przygodę!")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Losowanie", command=accion_boton)
boton.pack(pady=10)


ventana.mainloop()


# # To jest główne okno programu, w którym użytkownik wybiera tryb działania programu.


# def Główne_okno():
#     print("Cześć! wybierz tryb, aby przejść dalej do programu.")
#     tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
#     while True:
#         try:
#             if tryb.lower() == "losowanie":
#                 return Losowanie.poczatek_losowania()   
#             elif tryb.lower() == "wybierz słowo":
#                 return Lista.wybierz_slowo()
#             elif tryb.lower() == "wyjście":
#                 print("Do zobaczenia!")
#                 exit()
#             else:
#                 print("Masz ostatnie ostrzeżenie w tej chwili, \nmasz ostatnie ostrzeżenie!")
#                 tryb = input("Wybierz tryb \"Losowanie\" albo \"Wybierz słowo\" albo \"Wyjście\": ")
#         except ValueError:
#             print("Posłuchaj dzieciaku!")


# if __name__ == "__main__":
#     Główne_okno() 
     


import tkinter as tk

