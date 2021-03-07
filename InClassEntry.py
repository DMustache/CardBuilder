import pandas
from tkinter import Entry, Label, StringVar, Tk, Toplevel, Button
from tkinter.constants import E, END
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename
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

        self.btn = Button(self, text='Подключиться', command=self._activate_connection_win)
        self.btn.grid(row=0, sticky=E)

        #!org
        self.labelORG = Button(self, text='Предприятие')
        self.labelORG.grid(row=1, sticky=E)

        self.stringORG = StringVar()
        self.entryORG = Entry(self, textvariable=self.stringORG)
        self.entryORG.grid(row=1, column=1, columnspan=2)

        self.buttonORG = Button(self, text='Выбрать:', command=self._select_CSV_table(self.stringORG, self.entryORG))
        self.buttonORG.grid(row=1, col=3)

        #!org_rooms
        #!room
        #!event_types
        #!groups
        #!events
        #!slots
        #!slot_template
        #!participation

    def _activate_connection_win(self):
        connection = ConnectionWindow(self)
        connection.grab_set()

    def _select_CSV_table(path, entry_el):
        path = askopenfilename(filetype=(('CSV file', '*.csv'), ('Any', '*')))
        entry_el.delete(0, END)
        entry_el.insert(0, path)
        print(path)

    #!org
    def _send_org(org_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(org_path, sep=';', encoding='utf-8')
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
    def _send_org_rooms(org_rooms_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(org_rooms_path, sep=';', encoding='utf-8')
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
    def _send_room(room_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(room_path, sep=';', encoding='utf-8')
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
    def _send_event_types(event_types_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(event_types_path, sep=';', encoding='utf-8')
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
    def _send_groups(groups_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(groups_path, sep=';', encoding='utf-8')
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
    def _send_events(events_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(events_path, sep=';', encoding='utf-8')
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
    def _send_slots(slots_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(slots_path, sep=';', encoding='utf-8')
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
    def _send_org(slot_template_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(slot_template_path, sep=';', encoding='utf-8')
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
    def _send_org(participation_path):
        conn = ConnectionWindow._login_btn_clicked.conn()

        data = pandas.read_csv(participation_path, sep=';', encoding='utf-8')
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

if __name__ == '__main__':
    app = App()
    app.mainloop()