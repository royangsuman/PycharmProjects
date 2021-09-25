from typing import List
import pyodbc
import threading

class sqlServ:
    def conn(self):
        conn = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-9GF6S2KV;Database=CodeFirstDemo;Trusted_Connection=yes;')
        return conn
    def getAllTableList(self):
        listTables =[]
        cursor = self.conn().cursor()
        cursor.execute("SELECT name FROM SYSOBJECTS WHERE xtype = 'U'")
        for row in cursor:
            listTables.append(str(row).replace(",","").replace('(','').replace(')',''))
        return listTables
    def processList(self):
        listTables =[]
        listTables = self.getAllTableList()
        self.thread_function(self,listTables)
        self.threads_function(self, listTables)
    def thread_function(self,name):
        print('1')       
    def threads_function(self,name):
        print('2')

sql = sqlServ()
sql.processList()   