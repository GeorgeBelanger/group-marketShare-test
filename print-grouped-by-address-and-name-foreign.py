import sqlite3

db = sqlite3.connect('brokers.db')

result = db.execute('SELECT COUNT(*), * FROM brokers GROUP BY FORM_ID, ROW_ORDER, INS_BROKER_NAME, INS_BROKER_FOREIGN_ADDRESS1, INS_BROKER_FOREIGN_ADDRESS2, INS_BROKER_FOREIGN_CITY, INS_BROKER_FOREIGN_PROV_STATE, INS_BROKER_FOREIGN_CNTRY, INS_BROKER_FOREIGN_POSTAL_CD ORDER BY COUNT(*) DESC')

for row in result:
  print (row[0], row[1], row[2], row[3], row[4], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19] )
  
# Not sure what file you would want but this groups the records based on name, address, FORM_ID and ROW_ORDER.
# Row0 is count. 
