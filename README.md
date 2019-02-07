# Group MarketShare Test
  Here is the original text from the email:

>  Thank you for your time today.  As a next step can you please take a stab at the following coding test?  
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

