from bs4 import BeautifulSoup
import requests
import sys

def main():
    # Empty URL
    # URL = ""
    
    # Example input data
    URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    
    # Assignment input data
    # URL = "https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub"
    
    decodeMessageFromDoc(URL)

def decodeMessageFromDoc(URL):
    verbose = False

    # Check for empty URL
    if not URL:
        print("Error: The URL is empty.")
        sys.exit(1)

    table = getTable(URL)

    if verbose:
        # print(table.prettify())
        printTable(table)
    
    character_column = 1
    data = getData(table, character_column)
    if verbose:
        for row in data:
            print(row)
    
    max_x, max_y = getMaxXY(data)
    if verbose:
        print(f"max_x: {max_x}")
        print(f"max_y: {max_y}")

    size_x = max_x + 1
    size_y = max_y + 1
    character = ' '
    grid = createGrid(size_x, size_y, character)
    assignCharacters(grid, data, character_column)
    if verbose:
        for row in grid:
            print(row)

    printGrid(grid)

def getTable(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
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

def getMaxXY(data):
    x_values = []
    y_values = []
    for row in data:
        x_values.append(row[0])
        y_values.append(row[-1])
    max_x = max(x_values)
    max_y = max(y_values)
    return [max_x, max_y]

def createGrid(size_x, size_y, character):
    grid = []
    for i in range(size_x):
        row = size_y * [character]
        grid.append(row)
    return grid

def assignCharacters(grid, data, character_column):
    for row in data:
        x = row[0]
        y = row[-1]
        character = row[character_column]
        grid[x][y] = character

def printGrid(grid):
    # Get size of grid
    size_x = len(grid)
    size_y = len(grid[0])
    # Iterate over y values in descending order
    for j in range(size_y - 1, -1, -1):
        # Iterate over x values in ascending order
        for i in range(size_x):
            character = grid[i][j]
            print(character, end='')
        print()

if __name__ == "__main__":
    main()
