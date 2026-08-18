import tkinter as tk
from tkinter import ttk
import Losowanie
import Lista
import sys
import threading


class Przekierowanie:
    def __init__(self, widget_tekstowy):
        self.widget_tekstowy = widget_tekstowy

    def write(self, tekst):
        self.widget_tekstowy.insert(tk.END, tekst)
        self.widget_tekstowy.see(tk.END)

    def flush(self):
        pass

# def accion_boton():
#     etiqueta.config(text="No to losujemy słowo!")
#     Losowanie.poczatek_losowania()
def accion_boton():
    watek = threading.Thread(target=Losowanie.poczatek_losowania())
    # daemon=True sprawia, że wątek zamknie się automatycznie, gdy zamkniesz okno GUI
    watek.daemon = True 
    # Uruchamiamy wątek w tle
    watek.start()


ventana = tk.Tk()
ventana.title("")
ventana.geometry("1920x1080")


etiqueta = tk.Label(ventana, text="Pora na przygodę!")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Losowanie", command=accion_boton)
boton.pack(pady=10)

pole_tekstowe = tk.Text(ventana, wrap="word", height=20, width=80)
pole_tekstowe.pack(pady=20, padx=20, fill="both", expand=True)

sys.stdout = Przekierowanie(pole_tekstowe)


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
     



