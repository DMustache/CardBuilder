import pandas
from tkinter import Entry, Label, PhotoImage, StringVar, Tk, Toplevel, Button
from tkinter.constants import E, END
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename
from os.path import abspath
import pyodbc

class ConnectionWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.resizable(width=False, height=False)
        self.title('Подключение к базе')

        self.label_driver = Label(self, text="Драйвер:")
        self.label_driver.grid(row=0, sticky=E)
        self.entry_driver = Entry(self)
        self.entry_driver.grid(row=0, column=1)

        self.label_server = Label(self, text="Сервер:")
        self.label_server.grid(row=1, sticky=E)
        self.entry_server = Entry(self)
        self.entry_server.grid(row=1, column=1)

        self.label_database = Label(self, text="База Данных:")
        self.label_database.grid(row=2, sticky=E)
        self.entry_database = Entry(self)
        self.entry_database.grid(row=2, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=3)

    def _login_btn_clicked(self):
        driver = self.entry_driver.get()
        server = self.entry_server.get()
        database = self.entry_database.get()
        try:
            cs = f'DRIVER={driver};SERVER={server};database={database};Trusted_Connection=True;'
            conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};database={database};Trusted_Connection=True;')
            self.accept = showinfo(title='Connected!', message=f'Вы подключены к серверу {server}')

            self.destroy
        except pyodbc.Error as err:
            self.error = showerror(title='Error!', message='Сервер не найден')

class App(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title('InClass')
        #self.iconphoto(True, PhotoImage(file='path')) #TODO set icon path

        self.buttonConnect = Button(self, text='Подключиться', command=self._activate_connection_win)
        self.buttonConnect.grid(row=0, sticky=E)


        #!org
        self.labelORG = Label(self, text='Предприятие')
        self.labelORG.grid(row=1, sticky=E)

        self.stringORG = StringVar()
        self.entryORG = Entry(self, textvariable=self.stringORG)
        self.entryORG.grid(row=1, column=1, columnspan=2)

        self.buttonORG = Button(self, text='Выбрать', command=lambda:self.stringORG.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonORG.grid(row=1, column=3)

        #!org_rooms
        self.labelORG_ROOMS = Label(self, text='Предприятие')
        self.labelORG_ROOMS.grid(row=1, sticky=E)

        self.stringORG_ROOMS = StringVar()
        self.entryORG_ROOMS = Entry(self, textvariable=self.stringORG_ROOMS)
        self.entryORG_ROOMS.grid(row=1, column=1, columnspan=2)

        self.buttonORG_ROOMS = Button(self, text='Выбрать', command=lambda:self.stringORG_ROOMS.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonORG_ROOMS.grid(row=1, column=3)

        #!room
        self.labelROOM = Label(self, text='Комнаты')
        self.labelROOM.grid(row=3, sticky=E)

        self.stringROOM = StringVar()
        self.entryROOM = Entry(self, textvariable=self.stringROOM)
        self.entryROOM.grid(row=3, column=1, columnspan=2)

        self.buttonROOM = Button(self, text='Выбрать', command=lambda:self.stringROOM.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonROOM.grid(row=3, column=3)

        #!event_types
        self.labelEVENT_TYPES = Label(self, text='Типы Занятий')
        self.labelEVENT_TYPES.grid(row=4, sticky=E)

        self.stringEVENT_TYPES = StringVar()
        self.entryEVENT_TYPES = Entry(self, textvariable=self.stringEVENT_TYPES)
        self.entryEVENT_TYPES.grid(row=4, column=1, columnspan=2)

        self.buttonEVENT_TYPES = Button(self, text='Выбрать', command=lambda:self.stringEVENT_TYPES.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonEVENT_TYPES.grid(row=4, column=3)

        #!groups
        self.labelGROUPS = Label(self, text='Группы')
        self.labelGROUPS.grid(row=5, sticky=E)

        self.stringGROUPS = StringVar()
        self.entryGROUPS = Entry(self, textvariable=self.stringGROUPS)
        self.entryGROUPS.grid(row=5, column=1, columnspan=2)

        self.buttonGROUPS = Button(self, text='Выбрать', command=lambda:self.stringGROUPS.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonGROUPS.grid(row=5, column=3)

        #!events
        self.labelEVENTS = Label(self, text='Занятия')
        self.labelEVENTS.grid(row=6, sticky=E)

        self.stringEVENTS = StringVar()
        self.entryEVENTS = Entry(self, textvariable=self.stringEVENTS)
        self.entryEVENTS.grid(row=6, column=1, columnspan=2)

        self.buttonEVENTS = Button(self, text='Выбрать', command=lambda:self.stringEVENTS.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonEVENTS.grid(row=6, column=3)

        #!slots
        self.labelSLOTS = Label(self, text='Слоты')
        self.labelSLOTS.grid(row=7, sticky=E)

        self.stringSLOTS = StringVar()
        self.entrySLOTS = Entry(self, textvariable=self.stringSLOTS)
        self.entrySLOTS.grid(row=7, column=1, columnspan=2)

        self.buttonSLOTS = Button(self, text='Выбрать', command=lambda:self.stringSLOTS.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonSLOTS.grid(row=7, column=3)

        #!slot_template
        self.labelSLOT_TEMPLATE = Label(self, text='Временный слоты')
        self.labelSLOT_TEMPLATE.grid(row=8, sticky=E)

        self.stringSLOT_TEMPLATE = StringVar()
        self.entrySLOT_TEMPLATE = Entry(self, textvariable=self.stringSLOT_TEMPLATE)
        self.entrySLOT_TEMPLATE.grid(row=8, column=1, columnspan=2)

        self.buttonSLOT_TEMPLATE = Button(self, text='Выбрать', command=lambda:self.stringSLOT_TEMPLATE.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonSLOT_TEMPLATE.grid(row=8, column=3)

        #!participation
        self.labelPARTICIPATION = Label(self, text='Рассписание')
        self.labelPARTICIPATION.grid(row=9, sticky=E)

        self.stringPARTICIPATION = StringVar()
        self.entryPARTICIPATION = Entry(self, textvariable=self.stringPARTICIPATION)
        self.entryPARTICIPATION.grid(row=9, column=1, columnspan=2)

        self.buttonPARTICIPATION = Button(self, text='Выбрать', command=lambda:self.stringPARTICIPATION.set(askopenfilename(filetypes=(('CSV file', '*.csv')))))
        self.buttonPARTICIPATION.grid(row=9, column=3)

        self.buttonSend = Button(self, text='Отправить файлы', command=self.sendFiles)
        self.buttonSend.grid(row=10, sticky=E)

    def _activate_connection_win(self):
        connection = ConnectionWindow(self)
        connection.grab_set()

    def _select_CSV_table(CSV_path, entry_el):
        CSV_path = askopenfilename(filetype=(('CSV file', '*.csv'), ('Any', '*')))
        entry_el.delete(0, END)
        entry_el.insert(0, CSV_path)
        print(CSV_path)

    #!org
    def _send_org(org_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(org_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['org_id', 'org_description', 'parent_org'])
        org_cursor = conn.cursor()

        for row in df.itertuples():
            org_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.org ('org_id', 'org_description', 'parent_org')
            VALUES (?,?,?)
            ''',
            row.org_id,
            row.org_description,
            row.parent_org
            )
        conn.commit()

    #!org_rooms
    def _send_org_rooms(org_rooms_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(org_rooms_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['rooms_id', 'org', 'room'])
        org_rooms_cursor = conn.cursor()

        for row in df.itertuples():
            org_rooms_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('room_id', 'org', 'room')
            VALUES (?,?,?)
            ''',
            row.room_id,
            row.org,
            row.room
            )
        conn.commit()

    #!room
    def _send_room(room_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(room_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['room_id', 'room_description', 'room_size'])
        room_cursor = conn.cursor()

        for row in df.itertuples():
            room_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('room_id', 'room_description', 'room_size')
            VALUES (?,?,?)
            ''',
            row.room_id,
            row.room_description,
            row.room_size
            )
        conn.commit()

    #!event_types
    def _send_event_types(event_types_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(event_types_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['event_type_id', 'event_type', 'event_media'])
        event_types_cursor = conn.cursor()

        for row in df.itertuples():
            event_types_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('event_type_id', 'event_type', 'event_media')
            VALUES (?,?,?)
            ''',
            row.event_type_id,
            row.event_type,
            row.event_media
            )
        conn.commit()

    #!groups
    def _send_groups(groups_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(groups_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['group_id', 'groups_description', 'group_size'])
        groups_cursor = conn.cursor()

        for row in df.itertuples():
            groups_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('group_id', 'groups_description', 'group_size')
            VALUES (?,?,?)
            ''',
            row.group_id,
            row.groups_description,
            row.group_size
            )
        conn.commit()

    #!events
    def _send_events(events_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(events_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['event_id', 'event_type', 'datetime'])
        events_cursor = conn.cursor()

        for row in df.itertuples():
            events_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('event_id', 'event_type', 'datetime')
            VALUES (?,?,?)
            ''',
            row.event_id,
            row.event_type,
            row.datetime
            )
        conn.commit()

    #!slots
    def _send_slots(slots_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(slots_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['slot_id', 'room', 'datetime'])
        slots_cursor = conn.cursor()

        for row in df.itertuples():
            slots_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('slot_id', 'room', 'datetime')
            VALUES (?,?,?)
            ''',
            row.slot_id,
            row.room,
            row.datetime
            )
        conn.commit()

    #!slot_template
    def _send_org(slot_template_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(slot_template_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['slot_template_id', 'slot_template_start', 'time', 'period'])
        slot_template_cursor = conn.cursor()

        for row in df.itertuples():
            slot_template_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('slot_template_id', 'slot_template_start', 'time', 'period')
            VALUES (?,?,?)
            ''',
            row.slot_template_id,
            row.slot_template_start,
            row.time,
            row.period
            )
        conn.commit()

    #!participation
    def _send_org(participation_CSV_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(participation_CSV_path, sep=';', encoding='utf-8')
        df = pandas.DataFrame(data, columns=['participation_id', 'event', 'group'])
        participation_cursor = conn.cursor()

        for row in df.itertuples():
            participation_cursor.execute(
            '''
            INSERT INT InClassServer.dbo.room ('participation_id', 'event', 'group')
            VALUES (?,?,?)
            ''',
            row.participation_id,
            row.event,
            row.group
            )
        conn.commit()

    def sendFiles(self):
        try:
            self._send_org(self.stringORG.get())
            self._send_org_rooms(self.stringORG_ROOMS.get())
            self._send_room(self.stringROOM.get())
            self._send_event_types(self.stringEVENT_TYPES.get())
            self._send_groups(self.stringGROUPS.get())
            self._send_events(self.stringEVENTS.get())
            self._send_slots(self.stringSLOTS.get())

        except Exception:
            self.connException = showerror('Обишка', 'Введите правильные данные')
            #logsPath = abspath(r'logs.log')
            #f = open('logs.log', 'a', encoding='utf-8')
            #f.write(Exception)
            #f.close()


if __name__ == '__main__':
    app = App()
    app.mainloop()