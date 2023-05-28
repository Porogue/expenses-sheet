import psycopg2 as psy
from dbconfig import dbconf

connection = psy.connect(**dbconf)

print(connection)

cursor = connection.cursor()