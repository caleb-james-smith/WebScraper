# fed_scraper.py

# Get data from FED Supervisor error tables.

# Useful info:
# https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module
# https://stackoverflow.com/questions/12601316/how-to-make-python-requests-work-via-socks-proxy
# https://stackoverflow.com/questions/38794015/pythons-requests-missing-dependencies-for-socks-support-when-using-socks5-fro

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

def getPageInfo(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getResults(soup, "xdaq-main")
    tables = getElements(results, "table", "pixel-tab-table")
    #tables = results.find_all("table", id="pixelFedTable")
    n_tables = len(tables)

    for table in tables:
        body = table.find("tbody")
        rows = body.find_all("tr")
        n_rows = len(rows)
        for row in rows:
            print(row.text)
        print("Number of rows: {0}".format(n_rows))

    print("Number of tables: {0}".format(n_tables))

def main():
    URL = "http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71"
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }
    getPageInfo(URL, proxies)

if __name__ == "__main__":
    main()

