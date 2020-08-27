import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='new_base' user='postgres' password='example' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,qyantity,price):
    conn = psycopg2.connect("dbname='new_base' user='postgres' password='example' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,qyantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='new_base' user='postgres' password='example' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='new_base' user='postgres' password='example' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item='%s'" % (item))#or ,(item,)) - tuple
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='new_base' user='postgres' password='example' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity='%s', price='%s' WHERE item='%s'" % (quantity,price,item))
    conn.commit()
    conn.close()


# create_table()
# insert("Coffe3",4,10.5)
# update(9,18,"Coffe2")
delete("Coffe3")
print(view())