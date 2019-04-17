# https://github.com/mkleehammer/pyodbc/wiki/Using-an-Output-Converter-function

import struct
import pyodbc

server = 'DESKTOP-E021K2T\SQLEXPRESS'
database ='Northwind'
driver= '{ODBC Driver 17 for SQL Server}'
strConnectionString = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES;'
cnxn = pyodbc.connect(strConnectionString)


def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked)


crsr = cnxn.cursor()
# create test data
crsr.execute("CREATE TABLE #dto_test (id INT PRIMARY KEY, dto_col DATETIMEOFFSET)")
crsr.execute("INSERT INTO #dto_test (id, dto_col) VALUES (1, '2017-03-16 10:35:18 -06:00')")

cnxn.add_output_converter(-155, handle_datetimeoffset)
value = crsr.execute("SELECT dto_col FROM #dto_test WHERE id=1").fetchval()
print(value)

crsr.close()
cnxn.close()