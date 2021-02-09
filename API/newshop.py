import flask
from flask import request, jsonify, render_template
import sqlite3 
from sqlite3 import Error




app = flask.Flask(__name__) 
app.config["DEBUG"] = True

conn = None
cursorObject = None
try:
    conn = sqlite3.connect("C:\\Users\\Student\\Documents\\Luciana\\Intech\\ShoppingDatabase.sqlite")
    cursorObject = conn.cursor()
except Error as e:
    print(e)
    



@app.route('/register', methods=['POST'])
def new_user():
    findAccounts = "SELECT * FROM accounts WHERE username = " + request.form['username']
    results = cursorObject.execute(findAccounts)
    if len(results) > 0:
        return -1
        # "ERROR User not found"

    else: 
        addUser = "INSERT INTO accounts VALUES" + request.form['username'] + ',' + request.form['password'] + ')'
        cursorObject.execute(addUser)
        return 0
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    if accounts.get(request.form['username']) is None or accounts.get(request.form['username']) != request.form['password']:
        return "-2"
    return "0"

@app.route('/list', methods=['GET'])
def list_all_products():
    output = ''
    for product in products.keys():
        output += product + " : " + '$' + str(products.get(product)) + "/n"
    return output

@app.route('/profile', methods=['POST'])
def profile():
    output = "You are signed in as " + request.form['cookie'] + ' with these products in basket: '
    for product in basket.get(request.form['cookie']):
        output += product + "/n"
    return output

@app.route( '/cancel', methods=['POST'])
def delete_item():
    if products.get(request.form['product']) is None:
        return "ERROR product doesn't exist"
    else:
        myBasket = basket.get(request.form['cookie'])
        myBasket.remove(request.form['product'])
        basket[request.form['cookie']] = myBasket
        return "The item has been discard from your purchase"

@app.route('/buy', methods=['POST'])
def buy_product():
    if products.get(request.form['product']) is None:
        return "ERROR: Product not found"
    myBasket = basket.get(request.form['cookie'])
    myBasket.append(request.form['product'])
    basket[request.form['cookie']] = myBasket
    return "Item added"

app.run()