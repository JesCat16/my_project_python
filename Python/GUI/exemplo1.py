from tkinter import *

janela = Tk()
janela.geometry('500x300')
janela.title("Soma dois números")

label1 = Label(janela, text= "Digite o 1° número: ", font=('Arial Bold',14))
label2 = Label(janela, text= "Digite o 2° número: ", font=('Arial Bold',14))
label3 = Label(janela, text= "Resposta: ", font=('Arial Bold',14))

label1.place(relx = 0.2,rely = 0.2)
label2.place(relx = 0.2,rely = 0.4)
label3.place(relx = 0.2,rely = 0.6)

entrada1 = Entry(janela, width = 8, font=("Times New Roman", 14))
entrada2 = Entry(janela, width = 8, font=("Times New Roman", 14))
entrada3 = Entry(janela, width = 8, font=("Times New Roman", 14))

entrada1.place(relx = 0.6,rely = 0.2)
entrada2.place(relx = 0.6,rely = 0.4)
entrada3.place(relx = 0.6,rely = 0.6)

def soma():
    valor1 = int(entrada1.get())
    valor2 = int(entrada2.get())
    resultado = valor1+valor2
    entrada3.insert(0,resultado)


botao=Button(janela, text= "Somar", font=('Arial Bold',14), command = soma)
botao.place(relx = 0.5,rely = 0.8, anchor='center')

janela.mainloop()