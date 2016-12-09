#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# pip install MySQL-python
import MySQLdb
import time
from generateLogs import *

def dbConnect(database):
  # Open database connection
  db = MySQLdb.connect("host-name","user-name","password",database)
  return(db)

# db = dbConnect("myDatabase")

# prepare a cursor object using cursor() method
# cursor = db.cursor()

# Prepare SQL query to INSERT/UPDATE/DELETE a record in the database.
# sql = "YOUR-INSERT-OR-UPDATE-OR-DELETE-STATEMENT"

def InsertOrUpdateorDelete(cursor, sql, db):
  try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    generateLogs("mySQL_logs", str(time.strftime('%Y-%m-%d %H:%M:%S'))+" - CHANGED\n")
    generateLogs("mySQL_logs", "==========================================================\n")
  except:
    # Rollback in case there is any error
    db.rollback()
    generateLogs("mySQL_logs", str(time.strftime('%Y-%m-%d %H:%M:%S'))+" - Failed\n")
    generateLogs("mySQL_logs", "==========================================================\n")
  # disconnect from server
  db.close()


# Prepare SQL query to SELECT few records from the database.
# sql = "YOUR-SELECT-STATEMENT"

def selectData(cursor, sql):
  # Prepare SQL query to INSERT a record into the database.
  try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    if len(results) == 0:
      generateLogs("mySQL_logs", str(time.strftime('%Y-%m-%d %H:%M:%S'))+" - Select Successful\n")
      generateLogs("mySQL_logs", "==========================================================\n")
      for row in results:
        col_1 = row[0]
        col_2 = row[0]
        # and so on ..
        print col_1 + "," + col_2 # + "," + so on
    else:
      print "No rows returned"
      sys.exit()
  except:
    # disconnect from server
    generateLogs("mySQL_logs", str(time.strftime('%Y-%m-%d %H:%M:%S'))+" - Failed to Select\n")
    generateLogs("mySQL_logs", "==========================================================\n")
    db.close()

