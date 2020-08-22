import mysql.connector#pip install mysql-connector-python

con = mysql.connector.connect(
    user = "root",
    password = "root",
    host = "localhost",
    port = "3308",
    database = "new_base"
)

cursor = con.cursor()

word = input("Enter a word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
    else:
        print("Not faund")