import tkinter
from tkinter.constants import BOTTOM, CENTER, LEFT

class EntryField:
    def __init__(self, master, whatFind, message, posRow, posCollumn):
        self.label = tkinter.Label(master, text=whatFind).grid(row=posRow, column=posCollumn)
        self.entry = tkinter.Entry(master, textvariable=message).grid(row=posRow, column=posCollumn + 1)

root = tkinter.Tk()
root.geometry('500x350')
root.resizable(width=False, height=False)

server = tkinter.StringVar()
serverName = EntryField(root, 'Имя Сервера:', message=server, posRow=0, posCollumn=0)

database = tkinter.StringVar()
serverDataBase = EntryField(root, 'Имя Базы Данных:', message=database, posRow=1, posCollumn=0)

applyButton = tkinter.Button(root, text='Принять', command=lambda:(print(server.get(), database.get()))).grid(row=3, column=0)



root.mainloop()