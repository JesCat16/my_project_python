from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

janela = Tk()
janela.geometry('500x300')
janela.title('Cronômetro de Pomodoro')

def tarefas():
    nova_janela = Tk()
    nova_janela.geometry('500x300')
    nova_janela.title('Tarefas')
    item = (entrada1.get())
    txt = scrolledtext.ScrolledText(nova_janela, width = 50, height = 10 )
    txt.place(relx=0.5, rely = 0.5, anchor = 'center')
    nova_janela.mainloop()

cont = 25 


def show():
    global cont
    if cont > 0:
        numero['text'] = cont
        cont-=1
        janela.after(1000, show)
    elif cont == 0:
        messagebox.showinfo("Tempo","Tempo acabou")
        
def pausa():
    pass


label = Label(janela, text="Tarefa", font=("Arial Black" , 20))
label.place(relx=0.5, rely=0.2, anchor = 'center')

entrada1 = Entry(janela, width = 30, font=("Arial Black", 10))
entrada1.place(relx = 0.5,rely = 0.3, anchor = 'center')

botaoI = Button(janela, text='Inicio',font=("Arial Black", 15), command = show)
botaoI.place(relx= 0.5, rely= 0.45, anchor='center')

botaoP = Button(janela, text='Pausa',font=("Arial Black", 15), command = pausa)
botaoP.place(relx= 0.5, rely= 0.75, anchor='center')

numero = Label(janela, text="25", font=("Arial Black" , 15), fg = 'blue')
numero.place(relx=0.5, rely=0.6, anchor = 'center')


meu_menu = Menu (janela)
novo_item = Menu(meu_menu, tearoff=0)
meu_menu.add_command(label = "Tarefas Realizadas", command = tarefas)


janela.config(menu = meu_menu)
janela.mainloop()