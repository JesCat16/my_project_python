from tkinter import *
janela = Tk()
janela.geometry('500x300')
janela.title('Contador')

label = Label(janela, text='0', font=("Arial Black", 36))
label.place(relx= 0, rely = 0, anchor = 'center')

count = 1

def loop():
    global count
    #janela.geometry(str(count) + 'x' + str(count))
    label['text'] = count
    label.place(x=count, y= count)
    count+=1
    janela.after(100, loop)

loop()

janela.mainloop()
