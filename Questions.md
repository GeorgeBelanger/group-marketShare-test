
Questions from from the last interview:
  - What is your main method of acquiring customers? 
    - How did you get business with Zurich for example? 
  - Who is the main competitor in this space and what percentage of the market do they have?
  - What growth are you projecting? Just using linear regression?
  - Did you ever do user case studies / systemic way of collecting feedback/testimonials? 
  - "Simple annual fee - no per user fees" Have you tried any other pricing models/packages? 
  - Did you take vacations this year?
  - What kind of people don't work out here?
  - Who do you guys follow on social media for industry insights?
  - Do you go to conferences?

New Questions for Becca and Michael
  - What is the main feature users ask you for? Could you list the top 3? Are they technical or ease-of-use or portability/sharability? 
  - It was not very hard technically to go from life to dental, and shouldn't be hard to get into other parts of the market outside of insurance
    - What other parts of the market do we have data for?
  - Could you give me a breakdown of percentage of GMS's sales for brokers, carriers and admins?   
  - Have you done any content marketing? 
  - Could I get an overview of the different database structures and endpoints you have for SGMS? 
  - Whats the process for interalizing the quarterly insurance data? 
  - What kind of checks do you require before you put a new database into production? 
  - What are we using for document DB?  
  - Any thoughts on GraphQL 
  - Have you heard of timeseries, ledger or graph databases? 
  - Do we write scala for spark? 

Things that got answered and established at the last interview:
  - Not just local customers 
  - Each new customer provides us with their data but get anonimity 
    - This was an easier sell in the past
  - Users are business users, either Actruary, Underwriter or Marketing
  - We deal with different kinds of businesses- Brokers, Carriers and Admins
  - DB is sometimes manually manipulated
  - Technologies used:
    - Use Echarts from Baidu
    - Jenkins is used for CI
    - GUnicorn is used for http logging
    - Cypress & selenium are used for end to end testing, which is the only front end testing done currently
    - Sentry is used for monitoring errors and crashes
    - Use AWS API Gateway
    - Use Flask
    - Use SQLAlchemy
    - SQL Server
    - GeoJSON is used
    -? It goes Backend- data api - frontend
    - RESTFUL Api using http
    - PySpark is used
    - 50/50 IE and chrome
  - Not sure what was meant by these notes: 
    - Light on individual to carrier...
    - Claims purchse... 
