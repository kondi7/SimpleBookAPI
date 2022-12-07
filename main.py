import requests
import json

URL = "https://simple-books-api.glitch.me"

def apiStatus():
    status = URL + "/status"
    response = requests.get(status)
    print("Status API to:", response)


def getBookList():
    booklist = URL + "/books"
    response = requests.get(booklist)
    print("Status listy to", response)
    print(response.text)

def getSingleBook():
    print("Wpisz typ ksiazki: ")
    type = input("")
    while type != "fiction" and type != "non-fiction":
        print("Wpisz poprawny typ ksiązki fiction lub non-fiction")
        type = input("")

    queryURL = URL + "/books" + f"?type={type}"
    response = requests.get(queryURL)
    bookdata = json.loads(response.text)[0]
    nazwa = bookdata["name"]
    id = bookdata["id"]
    typ = bookdata["type"]
    print(f"{nazwa}")
    print(f"id: {id}")
    print(f"typ: {typ}")

getSingleBook()
getBookList()
apiStatus()
