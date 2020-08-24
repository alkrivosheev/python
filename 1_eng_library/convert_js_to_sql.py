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
query = cursor.execute("CREATE TABLE Dictionary(Expression varbinary(100) NOT NULL,  Definition varbinary(5000) NOT NULL)")
# cursor.execute("TRUNCATE TABLE new_base.Dictionary;")
con.commit()
for item in data:
    # if item == 'field':
        print(item, "::",''.join(data[item]))
        q_text = "INSERT INTO new_base.Dictionary (Expression,Definition) VALUES ('%s','%s');" % (''.join(item).replace("'", " "), ''.join(data[item]).replace("'", " "))
        cursor.execute(q_text)

con.commit()
cursor.close()
con.close()