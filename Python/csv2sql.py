#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
from mySQLConnect import *

# # Put data in db tables
def putData():
    db = dbConnect("your-database")
    cursor = db.cursor()
    df2 = pd.read_csv("read-a-csv-file") # OR
    df2 = pd.DataFrame({'A':['k1','k2','k3','k4'], 'B':[1,2,3,4]})
    for index, row in df2.iterrows():
      sql = "INSERT INTO your_table VALUES('" + str(row['A']) + "', " + str(row['B']) + ")"
      print sql
      InsertOrUpdateorDelete(cursor, sql, db)
    db.close()
putData()
