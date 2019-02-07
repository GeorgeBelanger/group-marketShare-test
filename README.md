# Group MarketShare Test
  Here is the original text from the email:

>    Thank you for your time today.  As a next step can you please take a stab at the following coding test?  
>
>    Thanks,
>    Jason
>
>    Broker Consolidation Programming Test
>
>    Please develop a working computer programming in Python, which matches broker records as best you can using the name and address from the dataset below.  Do not spend more than 4 hours coding your solution and please write up a description of how you would improve your solution with more time.
> 
>    Send a link to your matched dataset including some sort of identifier indicating your grouping of brokers.  Please also send along the code for your solution.
>
>    File Layout:
>    http://askebsa.dol.gov/FOIA%20Files/2016/Latest/F_SCH_A_PART1_2016_Latest_layout.txt
>
>    Data Set:
>    http://askebsa.dol.gov/FOIA%20Files/2016/Latest/F_SCH_A_PART1_2016_Latest.zip

  - Based on the description, I think they just want me to group the brokers using python. I've had limited python experience but should have something working in 2 hours. 
    - The first thing I thought about was putting the data into an SQL database and using the GROUP BY and ORDER BY operators to group the brokers. 
      - I would start this by plugging the data into DB Broswer for SQLite on desktop to manipulate the data there and see what SQL queries I would need.
      - Then I would find out how to execute raw SQL in python and then create a group function and an order function that take an argument (that may get validated by regex) and then return the result of the query on the database. 
      -- I get an error that says "Please enter the key used to encrypt the database" when I try to upload the CSV to DB Browser
      - Googled turning a CSV into an sqlite database in python and got this thread on Stack Overflow: [https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python](https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python)
      - I made a new file named csv-into-sqlite3.py and pasted the first answer and changed table name from 't' to 'brokers', changed the file name to reflect the csv and changed the column names to reflect the columns. 
      - Now I have to run the file. To call python It has to be in my path. Right now I have to run `C:\Python34\python --version` to use the command. I added `C:\Python34` to my path.
      - I got EOL for a syntax error, file not found for a path error, and now '_csv.Error: iterator should return strings, not bytes (did you open the file in text mode?)'
      - I see this is because I used 'rb' in my script. I thought it meant ruby at first but now I see I should use rt for text instead of bytes. 
      - I get error 'sqlite3.OperationalError: 2 values for 19 columns' And am adding more ? marks. I know this is used to protect against sql injection. 
        - Glad to know that csv.py is in the default library. 
        - I checked and sqlite3 is a folder in the default library as well.
      - I run the script and get no output which I know is a good thing. I am not sure where my file is though. 
        - Realizing that this is because the connection I am using is `:memory:` and should be a file. I am using 'example.db'
        - This creates a file, but the file is in binary. VS Code is recommending an extension to open it with and I downloaded the SQLite extension. 
          - I am trying to use the open DB in broswer command using SQLite extension but nothing is coming up.
      - I am able to open example.db in DB Browser. 
      -- I now realize that all my fields are TEXT fields. I have to figure out how to change the type of field in my file. 
      - I see this in the documentation: `con.execute("create table person (id integer primary key, firstname varchar unique)")` but this doesn't tell me how to set the text size. 
      - I see varchar(20) and will try that with TEXT(20) and NUMERIC. Putting them into example2.db
      - I see that you cannot choose the size of TEXT but you can with VARCHAR. 
      - I run `python C:\my_developments\groupMarketShareTest\csv-into-sqlite3.py`
    - Now when I open the file in DB Browser, I see the data in browse data. The command that the application outputs is 
    ```
    SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `brokers` ORDER BY `_rowid_` ASC);
    SELECT `_rowid_`,* FROM `brokers` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
    ```
    - I see now that there are 416869 entries in the CSV. 
      - I see a few ways to group the brokers:
        1. Group by Form ID
        2. Group by Row Order
        3. Group by broker code
        4. Group by Country
        5. Group by State(US)
        6. Group by Zip
        7. Group by Broker Fees Paid Text
        8. Group by Neither Broker Fees Paid or Commission Paid. 
      - It wasn't clear to me what the sort of grouping I should do with this data. 
      - Do they want me to find duplicates?? 
      - I'm going to try and find duplicates. 
      - Looking at the data, I see that there are records that have the same name and address, but not the same ROW_ORDER, FORM_ID, FEES PAID or COMM PAID. 
      - Now I think they are asking me to group the records by name and address... exactally what was said but they didn't include what the purpose was so I was unsure of what a match meant. 
      - as 
      ```      
      "20170512110912P040023397799001"	"1"	"1"	"1ST GLOBAL CAPITAL"	"12750 MERIT DRIVE"	"SUITE 1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"4511"	"0"	"BROKER COMMISSIONS"	"7"
      "20170217135540P040024637537001"	"1"	"2"	"1ST GLOBAL CAPITAL CORP"	"PO BOX 743248"	""	"DALLAS"	"TX"	"75374"	""	""	""	""	""	""	"892"	""	""	"7"
      "20170420111106P040107871281001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	""	""	""	""	""	""	""	""	""	""	""	"7660"	"0"	"BROKER COMISSION"	"3"
      "20170512111834P030019658253001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"12750 MERIT DR"	"STE 1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"2921"	""	""	"7"
      "20170503194049P040014694721001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"PO BOX 743248"	""	"DALLAS"	"TX"	"75374"	""	""	""	""	""	""	"5007"	""	""	"7"
      "20170710144715P030033690957001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	""	""	""	""	""	""	""	""	""	""	""	"5243"	"0"	"BROKER COMMISSION"	"1"
      "20170628101430P030024043879001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"12750 MERIT DR"	"#1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"5799"	""	""	"7"
      "20170707110832P040033655943001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"1733 MANHATTAN DRIVE"	"SUITE D"	"WAUKESHA"	"WI"	"531862671"	""	""	""	""	""	""	"10753"	""	""	"7"
      "20170707145757P030033888215001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"8150 N CENTRAL EXPRESSWAY"	"SUITE 500"	"DALLAS"	"TX"	"75206"	""	""	""	""	""	""	""	"10340"	"BROKER COMMISSION"	"3"
      "20170530094411P030037332557001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"12750 MERIT DRIVE"	"SUITE 1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"887"	"0"	"COMMISSIONS"	"7"
      ```
      - Based on the above, I see that a record can match in name, address, address 2, broker code and still differ in commission paid and fees paid, as denoted by the text" BROKWER COMMISSION" and "COMMISSION"
      - Also notice that the top and bottom match on all addresses but differ in name. 
      ```
      "20170503194049P040014694721001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"PO BOX 743248"	""	"DALLAS"	"TX"	"75374"	""	""	""	""	""	""	"5007"	""	""	"7"
      "20170217135540P040024637537001"	"1"	"2"	"1ST GLOBAL CAPITAL CORP"	"PO BOX 743248"	""	"DALLAS"	"TX"	"75374"	""	""	""	""	""	""	"892"	""	""	"7"
      ```
      - Notice that the above only differ in row order. 
      - Not sure what records I'm supposed to match: 
        1. Records with the same name, address 1, address 2, zip, & broker code but differ in row order 
        2. Records with only the same name and address but different address 2
        3. Records with only the same name but different address 1 and 2
        4. Records with only the same address but different name 
      - For times sake I'm going to do the first. 
      - Acutally it's really important for me to get this correct. 
      - I think that grouping by address and zip is more important than by name because we see a typo in name below
      ```
      "20170512110912P040023397799001"	"1"	"1"	"1ST GLOBAL CAPITAL"	"12750 MERIT DRIVE"	"SUITE 1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"4511"	"0"	"BROKER COMMISSIONS"	"7"
      "20170530094411P030037332557001"	"1"	"1"	"1ST GLOBAL CAPITAL CORP"	"12750 MERIT DRIVE"	"SUITE 1200"	"DALLAS"	"TX"	"75251"	""	""	""	""	""	""	"887"	"0"	"COMMISSIONS"	"7"
      ```
      - But I also notice that the differences between SUITE 1200, STE 1200 and #1200 but no difference in ROW_ORDER. 
      - I think the issue arrises when it is obviously the same broker but ROW_ORDER and FORM_ID is 1 on each of them. 
      
__Going to look for records where the name and address are slighly different but it is obviously the same place (SUITE 1200 vs STE 1200) but the FORM_ID and ROW_ORDER is the same on both.__ 
