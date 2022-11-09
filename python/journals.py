# journals.py

# Caleb James Smith
# November 8, 2022
# Made for Katherine Taylor Price.

# Scrape journal websites, specifically The University of Chicago Press Journals.
# Access through the University of Kansas.
# https://ku.edu/
# https://www-journals-uchicago-edu.www2.lib.ku.edu/
# https://www-journals-uchicago-edu.www2.lib.ku.edu/loi/jmh
# https://www-journals-uchicago-edu.www2.lib.ku.edu/toc/jmh/2020/92/1

import requests
from bs4 import BeautifulSoup

def scrape(url):
    print("Scraping data from {0}".format(url))
    page            = requests.get(url)
    soup            = BeautifulSoup(page.content, "html.parser")
    #results         = soup.find(id="main")
    #elements    = results.find_all("div", class_="form-action-item__wrapper")
    #elements    = soup.find_all("div", class_="form-action-item__body")
    #elements    = soup.find_all("div", class_="card-body")
    #elements    = soup.find_all("li", class_="form-action-item")

    #print(page)
    #print(page.text)
    #print(page.content)
    #print(elements)
    #print(len(elements))

    login = soup.find(id="fm1")

    # KU Single Sign-On Page
    print(soup.head.title)
    print(soup.find("head").find("title"))
    print(login.h3)

def main():
    print("Go go go!")
    url = "https://www-journals-uchicago-edu.www2.lib.ku.edu/toc/jmh/2020/92/1"
    scrape(url)

if __name__ == '__main__':
    main()

