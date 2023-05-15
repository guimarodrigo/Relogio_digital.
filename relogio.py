import tkinter as tk
from tkinter import*
import os 
from time import strftime

name = os.getlogin()
root = tk.Tk()
root.title (f'Relógio de {name}')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#2F4F4F')

def get_saudacao():
    saudacao.config(text = 'Horário Atual')
    return

def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text=data_atual)
    return

def get_hora():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text = hora_atual)
    horas.after(1000,get_hora)
    return

tela_margem = tk.Canvas(root, width= 600, height=50, bg='#2F4F4F', highlightthickness=0)
tela_margem.pack()

saudacao = Label(root, bg='#2F4F4F', fg='#F5F5DC', font=('GILSANUB', 20))
saudacao.pack()

data = Label(root, bg='#2F4F4F', fg='#F5F5DC', font=('GILSANUB', 10))
data.pack(pady=2)

horas =Label(root, bg='#2F4F4F', fg='#F5F5DC', font=('GILSANUB', 60, 'bold'))
horas.pack(pady = 2)

get_saudacao()
get_data()
get_hora()

root.mainloop(
)




