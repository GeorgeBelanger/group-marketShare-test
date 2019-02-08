import sqlite3

db = sqlite3.connect('brokers.db')

result = db.execute('SELECT COUNT(*), * FROM brokers GROUP BY FORM_ID, ROW_ORDER, INS_BROKER_NAME, INS_BROKER_US_ADDRESS1, INS_BROKER_US_ADDRESS2, INS_BROKER_US_CITY, INS_BROKER_US_STATE, INS_BROKER_US_ZIP ORDER BY COUNT(*) DESC')

for row in result:
  print (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[16], row[17], row[18], row[19])
  
# Not sure what file you would want but this groups the records based on name, address, FORM_ID and ROW_ORDER.
# Row 0 is count.
    
