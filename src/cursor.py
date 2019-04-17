#https://github.com/mkleehammer/pyodbc/wiki/Cursor

import pyodbc
server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'

cnxn = pyodbc.connect(strConnectionString)
cnxn.autocommit = False
cursor = cnxn.cursor()

# fast_executemany

# Under the hood, there is one important difference when fast_executemany=True.
# In that case, on the client side, pyodbc converts the Python parameter values to their ODBC "C" equivalents,
#  based on the target column types in the database.
# Executes the same SQL statement twice with parameters

params = [ ('Snow','John'), ('Targaryen','Aegon') ]
# cursor.fast_executemany = True
# cursor.executemany("insert into Employees(Lastname,FirstName) values (?, ?)", params)
# cnxn.commit()

# show all table's name
for row in cursor.tables():
    print(row.table_name)
# show all column's name
for row in cursor.columns():
    print(row.column_name)

