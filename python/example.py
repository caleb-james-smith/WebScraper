# example.py

# Example web scraper in python3
# See the tutorial for this example here:
# https://realpython.com/beautiful-soup-web-scraper-python/
# Fake job website used for this example:
# https://realpython.github.io/fake-jobs/

import requests
from bs4 import BeautifulSoup

URL             = "https://realpython.github.io/fake-jobs/"
page            = requests.get(URL)
soup            = BeautifulSoup(page.content, "html.parser")
results         = soup.find(id="ResultsContainer")
job_elements    = results.find_all("div", class_="card-content")

n_job_elements = len(job_elements)

#print(page)
#print(page.text)
#print(page.content)
#print(soup)
#print(results.prettify())
#print(job_elements)

print("Number of job elements: {0}".format(n_job_elements))
print()

for job_element in job_elements:
    #print(job_element, end="\n"*2)
    title_element       = job_element.find("h2",    class_="title")
    company_element     = job_element.find("h3",    class_="company")
    location_element    = job_element.find("p",     class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

