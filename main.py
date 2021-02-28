import tkinter as tk
from tkinter import filedialog as fd

class App(tk.Tk):
    def __init__(self):
        org, org_rooms, events, event_type, groups, participation, room, slot_template, slots = '','','','','','','','',''
        super().__init__()
        self.btn = tk.Button(self, text="Нажми!",
                             command=self.takeCSVPath(org))
        self.btn.pack(padx=120, pady=30)

    def takeCSVPath(table):
        table = fd.askopenfilename(filetype=(('CSV file', '*.csv')))
        return table


if __name__ == "__main__":
    app = App()
    app.title("Мое приложение Tkinter")
    app.mainloop()

print(App.org)

import pandas
import pyodbc
import getpass

data = pandas.read_csv(f'C:\\Users\\{getpass.getuser()}}\\Documents\\InClass\\table.csv', sep=';', encoding='utf-8')
df = pandas.DataFrame(data, columns=['group_id','group_description','group_size'])

connection_string = ('')

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO InClassServer.dbo.groups (group_id, group_description, group_size)
                VALUES (?,?,?)
                ''',
                row.group_id,
                row.group_description,
                row.group_size
                )
conn.commit()
