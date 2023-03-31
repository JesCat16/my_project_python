from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton

janela = Tk()
janela.geometry('350x200')
janela.title('Teste')

#Variável inteira
selecionado = IntVar()

rad1=Radiobutton(janela, text='Primeira opção', value = 1, variable = selecionado)
rad2=Radiobutton(janela, text='Segunda opção', value = 2, variable = selecionado)
rad3=Radiobutton(janela, text='Terceira opção', value = 3, variable = selecionado)

rad1.place(relx='0.5', rely='0.2', anchor='center')
rad2.place(relx='0.5', rely='0.4', anchor='center')
rad3.place(relx='0.5', rely='0.6', anchor='center')


#variavel booleana(True/False) no tkinter
c1_estado = BooleanVar()
#Não está selecionado
c1_estado.set(False)

c2_estado = BooleanVar()
#Está selecionado
c2_estado.set(True)

c3_estado = BooleanVar()
c3_estado.set(False)


#check1 = Checkbutton(janela, text='Texto 1', var = c1_estado)
#check2 = Checkbutton(janela, text='Texto 2', var = c2_estado)
#check3 = Checkbutton(janela, text='Texto 3', var = c3_estado)

#check1.place(relx='0.5', rely='0.2', anchor='center')
#check2.place(relx='0.5', rely='0.4', anchor='center')
#check3.place(relx='0.5', rely='0.6', anchor='center')

def show():
    messagebox.showinfo("Botão selecionado", selecionado.get())

botao = Button(janela, text='Clique aqui!', command = show)
botao.place(relx='0.5', rely='0.8', anchor='center')
janela.mainloop()