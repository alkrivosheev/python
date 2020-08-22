import mysql.connector#pip install mysql-connector-python
import json

data = json.load(open("program1/data.json"))

con = mysql.connector.connect(
    user = "root",
    password = "root",
    host = "localhost",
    port = "3308",
    database = "new_base"
)

cursor = con.cursor()
cursor.execute("TRUNCATE TABLE new_base.Dictionary;")
con.commit()
for item in data:
    print(item, "::",''.join(data[item]))
    cursor.execute("INSERT INTO new_base.Dictionary (Expression, Definition) VALUES ('%s', '%s');" % (item, ''.join(data[item])))
    con.commit()
cursor.close()
con.close()