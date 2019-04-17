# https://github.com/mkleehammer/pyodbc/wiki/Getting-started

import textwrap
import pyodbc

server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'
cnxn = pyodbc.connect(strConnectionString)
cursor = cnxn.cursor()

sql = textwrap.dedent("""
    select p.firstname,
           p.lastname,
           p.title
    from employees as p
    where p.employeeid = ?
""")
rows = cursor.execute(sql, 2).fetchall()
for row in rows:
    print(row.firstname)