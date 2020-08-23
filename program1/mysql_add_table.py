import mysql.connector#pip install mysql-connector-python

con = mysql.connector.connect(
    user = "root",
    password = "root",
    host = "localhost",
    port = "3308",
    database = "new_base"
)

cursor = con.cursor()
# query = cursor.execute("CREATE TABLE Dictionary(Expression varbinary(100) NOT NULL,  Definition varbinary(5000) NOT NULL)")

# cursor.execute("INSERT INTO new_base.Dictionary (Expression, Definition) VALUES ('hello', 'This is text hello');")
# con.commit()

cursor.execute("SELECT Expression, Definition FROM Dictionary")
# results = cursor.fetchall()
# print(results)
for (Expression, Definition) in cursor:
    print("{}, {} ".format(Expression, Definition))

cursor.close()
con.close()

# if results:
#     for result in results:
#         print(result[0],"::",result[1])