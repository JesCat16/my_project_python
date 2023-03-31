from tkinter import *
from tkinter import messagebox
# tem q importar messagebox de forma explícita
#cria janela
janela = Tk()

janela.geometry('400x400')
janela.title('Algoritimos')

#escrever na janela
label = Label(janela, text="Primeira aplicação gráfica", font=('Arial Bold',16))
#localizer a letra. Usar as siglas dos pontos cardeais. x e y absoluto. relx e rely posição relativa
label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# caixa de entrada, width quantidade dos caracteres
entrada = Entry(janela, width=14, font=("Arial Bold",16))
entrada.place(relx = 0.5, rely = 0.3, anchor = 'center')

#muda texto
def funcao():
    #pega texto da caixa de entrada
    ent = entrada.get()
    label['text'] = ent

def show():
    resposta = messagebox.askyesno("Aviso!", "Python é legal?")
    print(resposta)

#botão #funcao sem parenteses
botao = Button(janela , text = 'clique aqui!',font=("Arial Bold",16), command = funcao)
botao.place(relx = 0.3, rely = 0.7, anchor = 'center')

botao2 = Button(janela , text = 'Mensagem!',font=("Arial Bold",16), command = show)
botao2.place(relx = 0.7, rely = 0.7, anchor = 'center')









janela.mainloop()