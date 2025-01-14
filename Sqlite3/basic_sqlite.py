import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS customers (
          first_name text,
          last_name text,
          email text)
          """)
# Datatypes in SQLite - NULL , INTEGER , REAL - DECIMALS, TEXT , BLOB
# c.execute("INSERT INTO customers VALUES ('John', 'Doe', 'john@example.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Smith', 'mary@example.com')")
# c.execute("INSERT INTO customers VALUES ('Taylor', 'Jones', 'taylor@example.com')")

# many_customers = [
#     ('Arnav', 'Karwa', 'arnav@example.com'),
#     ('William', 'John', 'william@example.com'),
#     ('Will', 'Smith', 'will@example.com'),
#     ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())
# print(c.fetchone()[0])

# items = c.fetchall()
# for item in items:
#     print(item[0] + " " + item[1])

conn.commit()
conn.close()
