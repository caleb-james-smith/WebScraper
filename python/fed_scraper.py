# fed_scraper.py

# Get data from FED Supervisor error tables.

# https://stackoverflow.com/questions/38794015/pythons-requests-missing-dependencies-for-socks-support-when-using-socks5-fro
# https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module

import requests
from bs4 import BeautifulSoup

proxies = {
    "http" : "socks5h://127.0.0.1:1030",
    "https": "socks5h://127.0.0.1:1030"
}

URL         = "http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71"
page        = requests.get(URL, proxies=proxies)
soup        = BeautifulSoup(page.content, "html.parser")
results     = soup.find(id="xdaq-main")
elements    = results.find_all("div", class_="tcds-item-table-title")

n_elements = len(elements)

#print(page)
#print(page.text)
#print(page.content)
#print(soup)
print(results)
#print(results.prettify())
#print(elements)

#print("Number of job elements: {0}".format(n_elements))


