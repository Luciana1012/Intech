import requests # import the necessary library

cookie = None # Save your username as cookie in your code!

1   
# Ask user which options/operations they would like to do. Keep looping until the user decided to exit
while True:
    mode = input("Please select an operation")
    if mode == "1":
        response = requests.get("https://www.healthcare.gov/api/articles.json")
        print(response.text)
    elif mode == "2":
        response = requests.get("https://www.healthcare.gov/api/topics.json")
        print(response.text)
    elif mode == "3":
        response = requests.get("https://www.healthcare.gov/es/glossary/accreditation.json")
        print(response.text)
    elif mode == "x":
        break
    else:
        print("Mode selected is invalid, please try again")