# fed_scraper.py

# Get data from FED Supervisor error tables.

# Useful info:
# https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module
# https://stackoverflow.com/questions/12601316/how-to-make-python-requests-work-via-socks-proxy
# https://stackoverflow.com/questions/38794015/pythons-requests-missing-dependencies-for-socks-support-when-using-socks5-fro
# https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
# https://stackoverflow.com/questions/65727862/scraping-table-with-beautifulsoup-how-to-separate-the-elements-with-a-newline

import requests
from bs4 import BeautifulSoup

def getSoup(URL, proxies):
    page = requests.get(URL, proxies=proxies)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def getResults(soup, id_name):
    results = soup.find(id=id_name)
    return results

def getElements(results, tag, class_name):
    elements = results.find_all(tag, class_=class_name)
    return elements

def getFEDStatusInfo(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getResults(soup, "xdaq-main")
    tables = getElements(results, "table", "pixel-item-table xdaq-table")
    n_tables = len(tables)

    data = []
    for table in tables:
        body = table.find("tbody")
        rows = body.find_all("tr")
        n_rows = len(rows)
        for row in rows:
            columns = row.find_all("td")
            columns = [element.get_text(separator=": ", strip=True) for element in columns]
            data.append([element for element in columns if element])
            for entry in columns:
                print(entry)

    print("Number of tables: {0}".format(n_tables))


# id = "pixfedTable"
# class = "xdaq-table tcds-item-table sortable pixelmonitor-table-compact"
def getFEDErrorInfo(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getResults(soup, "xdaq-main")
    tables = getElements(results, "table", "pixel-tab-table")
    n_tables = len(tables)
    print("Number of tables: {0}".format(n_tables))

    i = 0
    for table in tables:
        title = table.find("p", class_="tcds-item-table-title")
        description = table.find("p", class_="tcds-item-table-description")
        if title:
            print("i = {0}; title = {1}, description = {2}".format(i, title.text, description.text))
        i += 1

def testTables(URL, proxies):
    soup = getSoup(URL, proxies)
    tables = soup.find_all("table")
    n_tables = len(tables)

    print("Classes of each table:")

    for table in tables:
        print(table.get("class"))

    print("Number of tables: {0}".format(n_tables))

def test(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getResults(soup, "xdaq-main")
    tables = results.find_all("table")
    n_tables = len(tables)
    print(tables)
    print("Number of tables: {0}".format(n_tables))

def main():
    URL = "http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71"
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }
    #getFEDStatusInfo(URL, proxies)
    #getFEDErrorInfo(URL, proxies)
    #testTables(URL, proxies)
    test(URL, proxies)

if __name__ == "__main__":
    main()

