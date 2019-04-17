# https://github.com/mkleehammer/pyodbc/wiki/Calling-Stored-Procedures
import pyodbc
server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'

cnxn = pyodbc.connect(strConnectionString)
cnxn.autocommit = False
cursor = cnxn.cursor()

sql = """\
DECLARE @rv int;
DECLARE @OrderID int
EXEC @rv = [dbo].[CustOrdersDetail] @OrderID = 10248;
SELECT @rv AS return_value;
"""
cursor.execute(sql)
return_value = cursor.fetchval()
print(return_value)