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
    output = "You are signed in as", request.form['username'], 'with credit balance', credits.get(request.form['username'])
    return output

# Create a function (like the 2 above) for each of these options:

# code for adding credit to account goes here

# code for printing profile information (username and how many credits we have) goes here

# code for buying an item goes here

# code for listing out all products goes here

app.run() # run the program