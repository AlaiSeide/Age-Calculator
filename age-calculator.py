from tkinter import *
from datetime import date

# Função para calcular a idade
def calcular_idade():
    today = date.today()
    birth_date = date(int(ano_entry.get()), int(mes_entry.get()), int(dia_entry.get()))
    idade = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    Label(text=f"{nome_entry.get()}, você tem {idade} anos.").grid(row=6, column=1)

root = Tk()
root.title("Calculadora de Idade")

Label(text="Nome").grid(row=1, column=0)
Label(text="Ano").grid(row=2, column=0)
Label(text="Mês").grid(row=3, column=0)
Label(text="Dia").grid(row=4, column=0)

nome_entry = Entry()
ano_entry = Entry()
mes_entry = Entry()
dia_entry = Entry()

nome_entry.grid(row=1, column=1)
ano_entry.grid(row=2, column=1)
mes_entry.grid(row=3, column=1)
dia_entry.grid(row=4, column=1)

Button(text="Calcular Idade", command=calcular_idade).grid(row=5, column=1)

root.mainloop()
