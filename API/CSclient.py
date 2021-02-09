import requests

cookie = None

print("Welcome to CS Clothes Shopping")

while True:
    existing = input("are you an existing customer? y/n")
    if existing == "y" or existing == "Y" or existing == "yes":
        username = input("please enter your username: ")
        password = input ("please enter your password: ")
        payload = {"username" : username, "password" : password} 
        response = requests.post("http://127.0.0.1:5000/login", payload) 
        if response.text == '-2': 
            print("Wrong credentials let's try that again")
        else:
            cookie = username
            break 
    elif existing == "n" or existing == "N":
        newUsername = input("please create a new username: ")
        newPassword = input("please create a new password: ")
        payload = {"username" : newUsername, "password" : newPassword}
        response = requests.post("http://127.0.0.1:5000/register", payload) 
        if response.text == "-1": 
            print("username is already taken")
        else:
            cookie = newUsername
            break
    else:
        print("sorry I don't understand, let's try that again")

print("Press 1 to view all items on sale \nPress 2 to buy items \nPress 3 to cancel an order \nPress 4 to view my profile \nPress x to exit the program")

while True:
    mode = input("Please select an operation")
    if mode == "1":
        response = requests.get("http://127.0.0.1:5000/list")
        print(response.text)
    elif mode == "2":
        product = input("Please enter product name that you would like to purchase: ")
        payload = {"product": product, "cookie": cookie}
        response = requests.post("http://127.0.0.1:5000/buy", payload)
        print(response.text)
    elif mode == "3":
        product = input("Cancel operation: ")
        payload = {"product": product, "cookie": cookie}
        response = requests.post("http://127.0.0.1:5000/cancel", payload)
        print(response.text)
    elif mode == "4":
        payload = {"cookie": cookie}
        response = requests.post("http://127.0.0.1:5000/profile", payload)
        print(response.text)
    elif mode == "x":
        break
    else:
        print("Mode selected is invalid, please try again")
