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
import re

def printLine():
    print("--------------------------------------------------")

# Get int from string; assume exactly one int in string
def getIntFromString(input_string):
    match = re.search(r'\d+', input_string)
    # Check for match
    if match:
        return int(match.group())
    else:
        return -999

# Load content from URL using proxies
def getSoup(URL, proxies):
    soup = None
    try:
        page = requests.get(URL, proxies=proxies)
        soup = BeautifulSoup(page.content, "html.parser")
    except:
        printLine()
        print("ERROR:")
        print("    Failed to get data from '{0}'".format(URL))
        print("    using these proxies: {0}.".format(proxies))
        print("Make sure that you are running an ssh tunnel with port forwarding to access this site.")
        printLine()
    return soup

# Search based on ID
def getIDMatches(soup, id_name):
    results = soup.find(id=id_name)
    return results

# Search based on tag and class
def getClassMatches(results, tag, class_name):
    elements = results.find_all(tag, class_=class_name)
    return elements

# Get list of FEDs from data
def getFEDs(data):
    FEDs = []
    for x in data:
        if "FED ID" in x:
            FED = getIntFromString(x)
            if FED >= 0:
                FEDs.append(FED)
            else:
                print("WARNING: In getFEDs(), FED ID '{0}' is not >= 0.".format(FED))
    return FEDs

# Get list of integer values from data for a given string pattern
# Assume unique patterns
# Include all values (even less than 0) as place holders for missing values
def getIntValues(data, pattern):
    values = []
    for x in data:
        if pattern in x:
            value = getIntFromString(x)
            values.append(value)
            if value < 0:
                print("WARNING: In getIntValues(), '{0}' '{1}' is < 0.".format(pattern, value))
    return values

# Add FEDs to data map
def addFEDs(fed_data, FEDs):
    for FED in FEDs:
        fed_data[FED] = {}

# Add values to data map
# Assume that FED_ID and values have the same length
def addValues(fed_data, key, FED_ID, values):
    n_FED_ID = len(FED_ID)
    n_values = len(values)
    if n_FED_ID != n_values:
        print("ERROR: FED_ID length ({0}) and values ({1}) are not equal.".format(n_FED_ID, n_values))
        return
    for i, FED in enumerate(FED_ID):
        value = values[i]
        if FED >= 0:
            if value < 0:
                print("WARNING: In addValues(), for key '{0}', value '{1}' is < 0.".format(key, value))
            if FED in fed_data:
                fed_data[FED][key] = value
            else:
                print("ERROR: The FED {0} is not in fed_data.".format(FED))

# Gett FED status info
def getFEDStatusInfo(URL, proxies):
    verbose = False
    soup = getSoup(URL, proxies)
    results = getIDMatches(soup, "xdaq-main")
    tables = getClassMatches(results, "table", "pixel-item-table xdaq-table")
    n_tables = len(tables)

    data = []
    for table in tables:
        body = table.find("tbody")
        rows = body.find_all("tr")
        n_rows = len(rows)
        for row in rows:
            columns = row.find_all("td")
            columns = [element.get_text(separator=": ", strip=True) for element in columns]
            #data.append([element for element in columns if element])
            for entry in columns:
                if entry:
                    data.append(entry)
                if verbose:
                    print(entry)
        if verbose:
            printLine()

    print("Number of tables: {0}".format(n_tables))
    
    return data

# Example: get FED status info
def getFEDErrorInfoExample(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getIDMatches(soup, "xdaq-main")
    tables = getClassMatches(results, "table", "pixel-tab-table")
    n_tables = len(tables)
    print("Number of tables: {0}".format(n_tables))

    i = 0
    for table in tables:
        title = table.find("p", class_="tcds-item-table-title")
        description = table.find("p", class_="tcds-item-table-description")
        if title:
            print("i = {0}; title = {1}, description = {2}".format(i, title.text, description.text))
            #print(table)
        i += 1

# Get FED error tables
def getFEDErrorTables(URL, proxies):
    soup = getSoup(URL, proxies)
    results = getIDMatches(soup, "xdaq-main")
    tables = results.find_all("table")
    n_tables = len(tables)
    n_matches = 0
    pattern = "pixfedTable" 
    output = []
    
    #print("Number of total tables: {0}".format(n_tables))

    for table in tables:
        table_html = str(table)
        if pattern in table_html:
            table_soup = BeautifulSoup(table_html, "html.parser")
            parsed = table_soup.find_all("div", attrs={"class":"tcds-item-table-wrapper"})
            #print("Length of parsed list: {0}".format(len(parsed)))
            #print(str(parsed[0]))
            for x in parsed:
                output.append(str(x))

            n_matches += 1
    
    #print("Number of matches to '{0}': {1}".format(pattern, n_matches))
    #print("Length of output: {0}".format(len(output)))

    return output

def processTableList(table_list):
    # print the first element to see an example:
    #print(table_list[0])
    printHead = True
    printBody = True
    for table_html in table_list:
        table_head = getHTMLSection(table_html, "thead")
        table_body = getHTMLSection(table_html, "tbody")
        if printHead:
            print(table_head)
        if printBody:
            print(table_body)
    return

# Get section from HTML; assume exactly two matches to tag.
def getHTMLSection(html, tag):
    verbose = False
    required_positions = 2
    positions   = [m.start() for m in re.finditer(tag, html)]
    n_positions = len(positions)

    # check for the required number of positions
    if n_positions != required_positions:
        print("WARNING: There are {0} positions, but there should be {1} positions.".format(n_positions, required_positions))
    
    # get HTML section using tag positions
    start   = positions[0] - 1
    end     = positions[1] + len(tag) + 1
    html_section = html[start:end]
    
    if verbose:
        print("tag = {0}, start = {1}, end = {2}".format(tag, start, end))
    
    return html_section

def getFEDErrorInfo(URL, proxies):
    table_list = getFEDErrorTables(URL, proxies)
    processTableList(table_list)

def showTableClasses(URL, proxies):
    soup = getSoup(URL, proxies)
    tables = soup.find_all("table")
    n_tables = len(tables)

    print("Classes of each table:")

    for table in tables:
        print(table.get("class"))

    print("Number of tables: {0}".format(n_tables))

def main():
    URL = "http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71"
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }
    getFEDStatusInfo(URL, proxies)
    #getFEDErrorInfoExample(URL, proxies)
    #showTableClasses(URL, proxies)
    #getFEDErrorInfo(URL, proxies)

if __name__ == "__main__":
    main()


