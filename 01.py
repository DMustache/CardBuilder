from tkinter.constants import E
import pyodbc
import tkinter
from tkinter import messagebox as meb

class LoginFrame(tkinter.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.label_driver = tkinter.Label(self, text="Драйвер:")
        self.label_driver.grid(row=0, sticky=E)
        self.entry_driver = tkinter.Entry(self)
        self.entry_driver.grid(row=0, column=1)

        self.label_server = tkinter.Label(self, text="Сервер:")
        self.label_server.grid(row=1, sticky=E)
        self.entry_server = tkinter.Entry(self)
        self.entry_server.grid(row=1, column=1)

        self.label_database = tkinter.Label(self, text="База Данных:")
        self.label_database.grid(row=2, sticky=E)
        self.entry_database = tkinter.Entry(self)
        self.entry_database.grid(row=2, column=1)

        self.logbtn = tkinter.Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=3)


    def _login_btn_clicked(self):
        self.grab_set()
        self.wait_window()
        self.logbtn['state'] = 'disabled'
        driver = self.entry_driver.get()
        server = self.entry_server.get()
        database = self.entry_database.get()
        try:
            cs = f'DRIVER={driver};SERVER={server};database={database};Trusted_Connection=True;'
            conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};database={database};Trusted_Connection=True;')
            self.accept = meb.showinfo(title='Connected!', message=f'Вы подключены к серверу {server}')
        except pyodbc.Error as err:
            self.error = meb.showerror(title='Error!', message='Сервер не найден')
            self.logbtn['state'] = 'active'
        self.logbtn['state'] = 'active'



class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        entry = LoginFrame(self)
        entry.resizable(width=False, height=False)
        entry.grab_set()

        self.labelOrgRooms = tkinter.Label(self, text='Комнаты предприятия')
        self.labelOrgRooms.grid(row=0, column=0)

        orgRooms = tkinter.StringVar()
        self.entryOrgRooms = tkinter.Entry(self, textvariable=orgRooms)
        self.entryOrgRooms.grid(row=0, column=1)

        self.buttonOrgRooms = tkinter.Entry(self, text='Выбрать', command=lambda: orgRooms.set(tkinter.filedialog.askopenfilename()))
        self.buttonOrgRooms.grid(row=0, column=2)
    
    def _select_CSV_file():
        tkinter.filedialog.askopenfilename(filetypes=(('CSV file', '*.csv')))

if __name__ == '__main__':
    app = App()
    app.mainloop()