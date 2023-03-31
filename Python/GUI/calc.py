from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry('400x500')
janela.title("Vogal ou Consoante")

entrada1 = Entry(janela, width = 14)
entrada1.place(relx = 0.5,rely = 0.2, anchor='center' )
def display(num):
    entrada1.insert(END,num)
#para fazer uma função com parametro usa-se o lambda
b1=Button(janela, text= "1", command = lambda : display("1"))
b1.place(relx = 0.2,rely = 0.8, anchor='center')
b2=Button(janela, text= "2", command = lambda : display("1"))
b2.place(relx = 0.25,rely = 0.8, anchor='center')
b3=Button(janela, text= "3", command = lambda : display("1"))
b3.place(relx = 0.3,rely = 0.8, anchor='center')
b4=Button(janela, text= "4", command = lambda : display("1"))
b4.place(relx = 0.2,rely = 0.7, anchor='center')
b5=Button(janela, text= "5", command = lambda : display("1"))
b5.place(relx = 0.25,rely = 0.7, anchor='center')
b6=Button(janela, text= "6", command = lambda : display("1"))
b6.place(relx = 0.3,rely = 0.7, anchor='center')



janela.mainloop()