# \\TEST-PC\sharing

import pyodbc
import pandas as pd

cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\TEST-PC\sharing\testing.mdb;')

df = pd.read_sql("SELECT TOP 1 * FROM campaign_table ct ORDER BY ID DESC", cnxn) 
print(df.head())