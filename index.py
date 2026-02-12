import requests
from bs4 import BeautifulSoup

# Type: String
url = "https://books.toscrape.com/"

#Type: Request, takes in url as argument
response = requests.get(url)

#
soup = BeautifulSoup(response.text, 'html.parser') #response.text is a string

# List of Books
books = []
books_boxes = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

for book in books_boxes:
    book_title = book.h3.a["title"]
    books.append(book_title)

def printFiveBooks():
    for x in books[:5]:
        print(x)


def printRequest():
    try: 
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        print("Success: ", response.json())

    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)

printFiveBooks()

#<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
#<h3>