import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("C:\\Users\\Student\\Documents\\Luciana\\Intech\\ShoppingDatabase.sqlite")
    cursorObject = conn.cursor()
    
    # createTable = "CREATE TABLE products(name varchar(255), price int)"
    # cursorObject.execute(createTable)

    # createAccountsTable = "CREATE TABLE accounts(username varchar(255), password varchar(255))"
    # cursorObject.execute(createAccountsTable)

    # createBasketTable = "CREATE TABLE basket(username varchar(255), product varchar(255))"
    # cursorObject.execute(createBasketTable)

    # insertInto = "INSERT INTO products VALUES('T-shirt', 50), ('Jumper', 90), ('Pencil', 5)"
    # cursorObject.execute(insertInto)

    getAll = "SELECT * FROM accounts"
    queryResults = cursorObject.execute(getAll)
    for  result in queryResults:
        print(result)

    conn.commit()
except Error as e:
    print(e)
