
import pyodbc
server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'

cnxn = pyodbc.connect(strConnectionString)
cnxn.autocommit = False
cursor = cnxn.cursor()
cursor.execute("select * from Employees")
row = cursor.fetchone() # Returns the next row in the query, or None when no more data is available.
while row:
    print (str(row.EmployeeID) + " " + str(row.FirstName) + " " + str(row.LastName))
    row = cursor.fetchone()

data_source_name = cnxn.getinfo(pyodbc.SQL_DATA_SOURCE_NAME)
print(data_source_name)
