from bs4 import BeautifulSoup
import requests
import sys

def main():
    URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    decodeMessageFromDoc(URL)

def decodeMessageFromDoc(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = getTable(soup)

    # print(table.prettify())
    printTable(table)
    character_column = 1
    data = getData(table, character_column)
    for row in data:
        print(row)

def getTable(soup):
    tables = soup.find_all("table")
    n_tables = len(tables)

    # Require exactly one table
    if n_tables == 0:
        print("Error: No tables found when parsing HTML (expected one table).")
        sys.exit(1)
    elif n_tables > 1:
        print("Error: Multiple tables found when parsing HTML (expected one table).")
        sys.exit(1)

    return tables[0]

def printTable(table):
    rows = table.find_all("tr")
    for row in rows:
        spans = row.find_all("span")
        for span in spans:
            entry = span.text.strip()
            print("{0}, ".format(entry), end='')
        print()

def getData(table, character_column):
    data = []
    rows = table.find_all("tr")
    for i, row in enumerate(rows):
        # Skip first row (headers)
        if i == 0:
            continue
        
        data_row = []

        spans = row.find_all("span")
        for j, span in enumerate(spans):
            entry = span.text.strip()
            # Convert coordinates to integer
            if j != character_column:
                entry = int(entry)
            data_row.append(entry)

        data.append(data_row)
    
    return data

if __name__ == "__main__":
    main()
