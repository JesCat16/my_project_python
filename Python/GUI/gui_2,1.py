from tkinter import *
from tkinter import Menu
from tkinter import messagebox
janela = Tk()
janela.geometry('500x300')
janela.title('Teste de menu')

def clique():
    messagebox.showinfo("Teste Novo", "Botão pressionado")



meu_menu = Menu (janela)
# retira trasejado
novo_item = Menu(meu_menu, tearoff=0)
novo_item2 = Menu(meu_menu)
#abre opções
meu_menu.add_cascade(label = "Arquivo", menu = novo_item)
#adiciona comando
novo_item.add_command(label="Novo",command = clique)
novo_item2.add_command(label="Preferências",command = clique)
meu_menu.add_cascade(label = "Ferramentas", menu = novo_item2)

janela.config(menu = meu_menu)
janela.mainloop()