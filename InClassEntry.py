import tkinter
from tkinter.constants import E

class ConnectWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.labelDriver = tkinter.Label(master, text='Драйвер:').grid(row=0, column=0)
        self.entryDriver = tkinter.Entry(master).grid(row=0, column=1)

        self.labelServerName = tkinter.Label(master, text='Имя Сервера').grid(row=1, column=0)
        self.entryServerName = tkinter.Entry(master).grid(row=1, column=1)

        self.labelDBName = tkinter.Label(master, text='Имя Базы Данных').grid(row=2, column=0)
        self.entryDBName = tkinter.Entry(master).grid(row=2, column=1)

        self.checkButton = tkinter.Button(master, text='Войти', command=self._login_to_server).grid(columnspan=2)

        self.pack()

    def _login_to_server(self):
        driver = self.entryDriver.get()
        server = self.entryServerName.get()
        database = self.entryDBName.get()
        connection_string=(f'DRIVER={driver};SERVER={server};database={database};Trusted_Connection=True;')
        print(connection_string)

root = tkinter.Tk()
connect = ConnectWindow(root)
root.mainloop()