
import pyodbc
server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'

driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Employees")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
