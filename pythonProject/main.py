import pyodbc
from SQLServer import sqls

def print_hi(name):
    print(f'Execution Start, {name}')  
    conn = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-9GF6S2KV;Database=CodeFirstDemo;Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Posts')
    for row in cursor:
        print(row)
    sqlss = sqls.sqlServ

if __name__ == '__main__':
    print_hi('PyCharm')
