from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry('500x300')
janela.title("Vogal ou Consoante")

label1 = Label(janela, text= "Digite a letra: ")

label1.place(relx = 0.5,rely = 0.5, anchor='center')

entrada1 = Entry(janela, width = 14)

entrada1.place(relx = 0.7,rely = 0.5, anchor='center' )

def conferidor():
    letra = entrada1.get()
    if letra == "a" or letra == "e":
        messagebox.showinfo("Vogal", "É uma vogal!")
    elif letra == "i" or letra == "o":
        messagebox.showinfo("Vogal", "É uma vogal!")
    elif letra == "u":
        messagebox.showinfo("Vogal", "É uma vogal!")
    elif letra == "y":
        messagebox.showinfo("Depende", "Em certas regiões é vogal, em ortras é consoante")
    elif len(letra) > 1:
        messagebox.showerror("Erro", "Mais de uma letra")
        entrada1.delete(0,END)
    else:
       messagebox.showinfo("Consoante", "É uma Consoante!")

botao=Button(janela, text= "Conferir", command = conferidor)
botao.place(relx = 0.5,rely = 0.7, anchor='center')

janela.mainloop()

