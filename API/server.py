import flask # import necessary libraries
from flask import request, jsonify, render_template #(no need)

app = flask.Flask(__name__) # initialise the Flask library
app.config["DEBUG"] = True # This version is not our final yet

# These 3 dictionaries will simulate our database. In real implementation  MySQL or phpMyAdmin will be used.
products = {"Apple": 5, "Orange": 10, "Grapes": 15, "Pen": 7} # Products we have on offer
accounts = {} # dictionary mapping between username and password of the user
credits = {} # dictionary mapping between username and account's credit (money) of the user


@app.route('/register', methods=['POST'])
def new_user():
    if accounts.get(request.form['username']) is None:
        accounts[request.form['username']] = request.form['password']
        credits[request.form['username']] = 0
        return "0"
    return "-1" # Error username already taken

    # Code for registering new users goes here

@app.route('/login', methods=['POST'])
def login():
    if accounts.get(request.form['username']) is None or accounts.get(request.form['username']) != request.form['password']:
        return "-2"
    return "0"
    # code for logging user in goes here

@app.route('/list', methods=['GET'])
def list_all_products():
    output = ''
    for product in products.keys():
        output += product + " : " + str(products.get(product)) + "/n"
    return output

@app.route('/profile', methods=['POST'])
def profile():
    output = "You are signed in as " + request.form['cookie'] + ' with credit balance ' + str(credits.get(request.form['cookie']))
    return output

@app.route('/add_credit', methods=[ 'POST'])
def add_credit():
    balance = credits.get(request.form['cookie'])
    balance += int(request.form['amount'])
    credits[request.form['cookie']] = balance
    return "Credit added, your balance is: " + str(balance)

@app.route('/buy', methods=['POST'])
def buy_product():
    if products.get(request.form['product']) is None:
        return "ERROR: Product not found"
    if products.get(request.form['product']) > credits.get(request.form['cookie']):
        return "ERROR: Insufficient funds"
    balance = credits.get(request.form['cookie'])
    balance -= products.get(request.form['product'])
    credits[request.form['cookie']] = balance
    return "Item purchased, your balance is: " + str(balance)


# Create a function (like the 2 above) for each of these options:

# code for adding credit to account goes here

# code for printing profile information (username and how many credits we have) goes here

# code for buying an item goes here

# code for listing out all products goes here

app.run() # run the program