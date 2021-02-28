import pandas
import pyodbc
import getpass

data = pandas.read_csv(f'C:\\Users\\{getpass.getuser()}}\\Documents\\InClass\\table.csv', sep=';', encoding='utf-8')
df = pandas.DataFrame(data, columns=['group_id','group_description','group_size'])

connection_string = (
    'Driver={SQL Server};'
    'Server=DMUSTACHE;'
    'Database=InClassServer;'
    'Trusted_Connection = yes;'
)

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

