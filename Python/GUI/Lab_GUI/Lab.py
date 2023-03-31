from itertools import count
from tkinter import *
from tkinter import scrolledtext

janela = Tk()
janela.title("Filtro de palavras")
janela.geometry("900x600")

palavra = Label(janela, text="Palavra Suspeita", font=("Arial", 14))
palavra.place(relx=0.05, rely=0.08)

quantidade = Label(janela, text="Frequência", font=("Arial", 14))
quantidade.place(relx= 0.05,rely=0.15)

palavraEntrada = Entry(janela, width = 15, font = ("Arial",14)) 
palavraEntrada.place(relx = 0.25, rely=0.08)

frequancia =  Entry(janela, width = 15, font = ("Arial",14)) 
frequancia.place(relx = 0.25, rely=0.15)

txt = scrolledtext.ScrolledText(janela, width = 100, height=23 )
txt.place(relx=0.05, rely = 0.35)

def buscapalavras():
    cont=0
    texto = open("chat.txt","r")
    textonovo = texto.readlines()
    tx=[]
    for l in textonovo:
        tx.append(l.lower())
    a = (palavraEntrada.get())
    for i in tx:
        if a in i:
            txt.insert(END, i)
            cont +=1
    frequancia.insert(0,cont)


pesquisar = Button(janela, text = "Pesquisar", command = buscapalavras)
pesquisar.place(relx=0.5, rely = 0.08)

ocorrencias = Label(janela, text="Ocorrencias", font = ("Arial",14))
ocorrencias.place(relx=0.05, rely = 0.3)



janela.mainloop()
