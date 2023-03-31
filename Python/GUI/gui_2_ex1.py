from tkinter import *
from datetime import datetime
janela = Tk()
janela.geometry('300x300')
janela.title('Relógio Digital')

data = Label(janela, text='data', font=("Arial Black", 20), fg='blue')
data.place(relx= 0.5, rely = 0.4, anchor = 'center')

hora = Label(janela, text='hora', font=("Arial Black", 20), fg='blue')
hora.place(relx= 0.5, rely = 0.6, anchor = 'center')

def loop():
    agora = datetime.now()
    data['text'] = agora.strftime("%d/%m/%y")
    hora['text'] = agora.strftime("%H:%M:%S")
    janela.after(1000,loop)
loop()

janela.mainloop()