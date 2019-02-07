import csv, sqlite3

con = sqlite3.connect('example2.db')
cur = con.cursor()
cur.execute("CREATE TABLE brokers (ACK_ID VARCHAR(30), FORM_ID NUMERIC, ROW_ORDER NUMERIC, INS_BROKER_NAME VARCHAR(35), INS_BROKER_US_ADDRESS1 VARCHAR(35), INS_BROKER_US_ADDRESS2 VARCHAR(35), INS_BROKER_US_CITY VARCHAR(22), INS_BROKER_US_STATE VARCHAR(2), INS_BROKER_US_ZIP VARCHAR(12), INS_BROKER_FOREIGN_ADDRESS1 VARCHAR(35), INS_BROKER_FOREIGN_ADDRESS2 VARCHAR(35), INS_BROKER_FOREIGN_CITY VARCHAR(22), INS_BROKER_FOREIGN_PROV_STATE VARCHAR(22), INS_BROKER_FOREIGN_CNTRY VARCHAR(2), INS_BROKER_FOREIGN_POSTAL_CD VARCHAR(22), INS_BROKER_COMM_PD_AMT NUMERIC, INS_BROKER_FEES_PD_AMT NUMERIC, INS_BROKER_FEES_PD_TEXT VARCHAR(105), INS_BROKER_CODE VARCHAR(1));") # use your column names here

with open('C:\my_developments\groupMarketShareTest\F_SCH_A_PART1_2016_Latest\F_SCH_A_PART1_2016_latest.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ACK_ID'], i['FORM_ID'], i['ROW_ORDER'], i['INS_BROKER_NAME'], i['INS_BROKER_US_ADDRESS1'], i['INS_BROKER_US_ADDRESS2'], i['INS_BROKER_US_CITY'], i['INS_BROKER_US_STATE'], i['INS_BROKER_US_ZIP'], i['INS_BROKER_FOREIGN_ADDRESS1'], i['INS_BROKER_FOREIGN_ADDRESS2'], i['INS_BROKER_FOREIGN_CITY'], i['INS_BROKER_FOREIGN_PROV_STATE'], i['INS_BROKER_FOREIGN_CNTRY'], i['INS_BROKER_FOREIGN_POSTAL_CD'], i['INS_BROKER_COMM_PD_AMT'], i['INS_BROKER_FEES_PD_AMT'], i['INS_BROKER_FEES_PD_TEXT'], i['INS_BROKER_CODE'] ) for i in dr]

cur.executemany("INSERT INTO brokers (ACK_ID, FORM_ID, ROW_ORDER, INS_BROKER_NAME, INS_BROKER_US_ADDRESS1, INS_BROKER_US_ADDRESS2, INS_BROKER_US_CITY, INS_BROKER_US_STATE, INS_BROKER_US_ZIP, INS_BROKER_FOREIGN_ADDRESS1, INS_BROKER_FOREIGN_ADDRESS2, INS_BROKER_FOREIGN_CITY, INS_BROKER_FOREIGN_PROV_STATE, INS_BROKER_FOREIGN_CNTRY, INS_BROKER_FOREIGN_POSTAL_CD, INS_BROKER_COMM_PD_AMT, INS_BROKER_FEES_PD_AMT, INS_BROKER_FEES_PD_TEXT, INS_BROKER_CODE ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close