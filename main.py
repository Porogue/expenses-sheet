import psycopg2 as psy
from dbconfig import dbconf

connection = psy.connect(**dbconf)

cursor = connection.cursor()

print(connection)

class ExpensesSheet:
    def __init__(self):
        self.connection = psy.connect(**dbconf)
        self.cursor = connection.cursor()
        print("You have connected to the database")
    
    def __close__(self):
        self.cursor.close()
        print("Connection to the database has been closed")
    
    def selectAll(self):
        self
