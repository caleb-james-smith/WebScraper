# example.py

# Example web scraper in python3
# See the tutorial for this example here:
# https://realpython.com/beautiful-soup-web-scraper-python/
# Fake job website used for this example:
# https://realpython.github.io/fake-jobs/

import requests
from bs4 import BeautifulSoup

def getSoup(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def getResults(soup, id_name):
    results = soup.find(id=id_name)
    return results

def getElements(results, class_name):
    elements = results.find_all("div", class_=class_name)
    return elements

def getPageInfo(URL):
    soup = getSoup(URL)
    results = getResults(soup, "ResultsContainer")
    job_elements = getElements(results, "card-content")
    n_job_elements = len(job_elements)
    
    for job_element in job_elements:
        title_element       = job_element.find("h2",    class_="title")
        company_element     = job_element.find("h3",    class_="company")
        location_element    = job_element.find("p",     class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()
    
    print("Number of job elements: {0}".format(n_job_elements))
    print()


def main():
    URL = "https://realpython.github.io/fake-jobs/"
    getPageInfo(URL)

if __name__ == "__main__":
    main()

