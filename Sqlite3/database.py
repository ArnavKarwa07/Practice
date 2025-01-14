import sqlite3

def showall():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def addone(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

def deleted(fname):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE first_name = (?)", (fname,))
    conn.commit()
    conn.close()

def addmany(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", list)
    conn.commit()
    conn.close()
