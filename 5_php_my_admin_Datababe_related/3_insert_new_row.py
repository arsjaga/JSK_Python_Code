import pymysql
  
dataBase = pymysql.connect(
  host ="localhost",
  user ="phpmyadmin",
  passwd ="root",
  database = "product_db"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Ram", "CSE", "98", "A", "23")]
   
cursorObject.executemany(sql, val)
dataBase.commit()
   
# disconnecting from server
dataBase.close()