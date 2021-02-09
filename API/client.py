import requests # import the necessary library

cookie = None # Save your username as cookie in your code!

print("Welcome to ABC Online Shopping")

# Ask user whether they're an existing customer or not. Either register or login.
while True:
    existing = input("are you an existing customer? y/n")
    if existing == "y" or existing == "Y" or existing == "yes":
        username = input("please enter your username: ")
        password = input ("please enter your password: ")
        payload = {"username" : username, "password" : password} #the content of the enquiry or message
        response = requests.post("http://127.0.0.1:5000/login", payload) #el http es el IPv4 de la computadora server y el puerto es 5000
        if response.text == '-2': #-2 significa que no es valido
            print("Wrong credentials let's try that again")
        else:
            cookie = username
            break 
    elif existing == "n" or existing == "N":
        newUsername = input("please create a new username: ")
        newPassword = input("please create a new password: ")
        payload = {"username" : newUsername, "password" : newPassword} #the content of the enquiry or message
        response = requests.post("http://127.0.0.1:5000/register", payload) #el http es el IPv4 de la computadora server y el puerto es 5000
        if response.text == "-1": #-1 not valid porque el nombre is already taken
            print("username is already taken")
    else:
        print("sorry I don't understand, let's try that again")
    # Code to do registration OR login goes here
    # Don't forget to put in a break statement to exit from this while loop

# Options that the users can make with our program
print("Press 1 to view all items on sale \nPress 2 to buy items \nPress 3 to add credit to my account \nPress 4 to view my profile \nPress x to exit the program")

# Ask user which options/operations they would like to do. Keep looping until the user decided to exit
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
        amount = input("How much credit would you like to add: ")
        payload = {"amount": amount, "cookie": cookie}
        response = requests.post("http://127.0.0.1:5000/add_credit", payload)
        print(response.text)
    elif mode == "4":
        payload = {"cookie": cookie}
        response = requests.post("http://127.0.0.1:5000/profile", payload)
        print(response.text)
    elif mode == "x":
        break
    else:
        print("Mode selected is invalid, please try again")


    # Code to perform each of the opertions goes here
    # Don't forget to put in a break statement to exit from this while loop if the user chose to exit (aka pressed x)