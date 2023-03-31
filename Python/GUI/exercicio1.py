from tkinter import *

janela = Tk()
janela.geometry('500x300')
janela.title("Conversão numérica")

label1 = Label(janela, text= "Número decimal: ", font=('Arial Bold',14))
label2 = Label(janela, text= "Resposta: ", font=('Arial Bold',14))

label1.place(relx = 0.2,rely = 0.2)
label2.place(relx = 0.2,rely = 0.7)

entrada1 = Entry(janela, width = 14, font=("Arial Bold", 12))
entrada2 = Entry(janela, width = 14, font=("Arial Bold", 12))

entrada1.place(relx = 0.5,rely = 0.2)
entrada2.place(relx = 0.4,rely = 0.7)

def binario():
    entrada2.delete(0,END)
    valor = int(entrada1.get())
    convB=bin(valor)
    entrada2.insert(0,convB[2:])


def hexa():
    entrada2.delete(0,END)
    valor = int(entrada1.get())
    convH=hex(valor)
    entrada2.insert(0,convH)

def octal():
    entrada2.delete(0,END)
    valor = int(entrada1.get())
    convO=oct(valor)
    entrada2.insert(0,convO)

botao=Button(janela, text= "Binário", font=('Arial Bold',10), command = binario)
botao.place(relx = 0.2,rely = 0.5, anchor='center')

botao2=Button(janela, text= "Hexadecimal", font=('Arial Bold',10), command = hexa)
botao2.place(relx = 0.5,rely = 0.5, anchor='center')

botao3=Button(janela, text= "Octal", font=('Arial Bold',10), command = octal)
botao3.place(relx = 0.8,rely = 0.5, anchor='center')


janela.mainloop()