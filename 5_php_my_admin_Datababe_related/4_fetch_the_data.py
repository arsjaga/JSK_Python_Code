import pymysql
  
dataBase = pymysql.connect(
  host ="localhost",
  user ="phpmyadmin",
  passwd ="root",
  database = "product_db"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()