
import pyodbc
server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'

cnxn = pyodbc.connect(strConnectionString)
cnxn.autocommit = False
cursor = cnxn.cursor()
cursor.execute("select * from Employees")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()

# fast_executemany
# Under the hood, there is one important difference when fast_executemany=True.
# In that case, on the client side, pyodbc converts the Python parameter values to their ODBC "C" equivalents,
#  based on the target column types in the database.
# Executes the same SQL statement twice with parameters

params = [ ('Snow','John'), ('Targaryen','Aegon') ]
cursor.fast_executemany = True
cursor.executemany("insert into Employees(Lastname,FirstName) values (?, ?)", params)
cnxn.commit()

cursor.execute("SELECT * FROM Employees")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()
