import json
import pyodbc
import pandas as pd
from datetime import datetime

# Connection string
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=//DESKTOP-N0ELQRQ/timbang/DatabaseWb.mdb;')

# Create cursor
cursor = conn.cursor()

query = """
  SELECT 
    TOP 10 *
  FROM 
    TbTransCustomer tc 
  ORDER BY 
    DATEIN DESC
"""

# df = pd.read_sql(
#     query,
#     cnxn,
# )
# data = df.to_json(orient="records")
# data = json.loads(data)
# for i in range(len(data)):
#     date_added = data[i]["Date_Added"]
#     date_added = datetime.fromtimestamp(date_added / 1000).strftime(
#         "%Y-%m-%d %H:%M:%S"
#     )
#     data[i]["Date_Added"] = date_added

# Execute SQL query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Iterate through the rows
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()