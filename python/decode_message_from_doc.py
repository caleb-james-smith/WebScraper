import requests
from bs4 import BeautifulSoup

def main():
    URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    decodeMessageFromDoc(URL)

def decodeMessageFromDoc(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        print(table.prettify())

if __name__ == "__main__":
    main()
