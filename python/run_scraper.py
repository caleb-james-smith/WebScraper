# run_scraper.py

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PixelInfrastructure

from fed_scraper import getFEDStatusInfo, getFEDs, getIntValues, addFEDs, addValues

def getProxies():
    # Proxies for SOCKS5
    # Use localhost (127.0.0.1) and the port that you are forwarding
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }
    return proxies

def getFEDSupervisorURLs():
    # See the list of FEDSupervisor URLs here:
    # https://twiki.cern.ch/twiki/bin/view/CMS/PixelInfrastructure
    FEDSupervisorURLs = {
        1  : "http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71",
        2  : "http://srv-s2b18-34-01.cms:1971/urn:xdaq-application:lid=72",
        3  : "http://srv-s2b18-33-01.cms:1971/urn:xdaq-application:lid=73",
        4  : "http://srv-s2b18-32-01.cms:1971/urn:xdaq-application:lid=74",
        5  : "http://srv-s2b18-41-01.cms:1971/urn:xdaq-application:lid=75",
        6  : "http://srv-s2b18-40-01.cms:1971/urn:xdaq-application:lid=76",
        7  : "http://srv-s2b18-39-01.cms:1971/urn:xdaq-application:lid=77",
        8  : "http://srv-s2b18-38-01.cms:1971/urn:xdaq-application:lid=78",
        9  : "http://srv-s2b18-31-01.cms:1971/urn:xdaq-application:lid=79",
        10 : "http://srv-s2b18-30-01.cms:1971/urn:xdaq-application:lid=80",
        11 : "http://srv-s2b18-29-01.cms:1971/urn:xdaq-application:lid=81",
        12 : "http://srv-s2b18-28-01.cms:1971/urn:xdaq-application:lid=82",
    }
    return FEDSupervisorURLs

def getSimpleMap(fed_data, data_key):
    simple_map = {k: v[data_key] for k, v in fed_data.items()}
    return simple_map

# sort based on values
def getSortedMap(fed_data, data_key, reverse):
    simple_map = getSimpleMap(fed_data, data_key)
    sorted_map = {k: v for k, v in sorted(simple_map.items(), key=lambda item: item[1], reverse=reverse)}
    #print("simple_map: {0}".format(simple_map))
    #print("sorted_map: {0}".format(sorted_map))
    return sorted_map

def runScraper():
    print("Running scraper.")

    fed_data = {}
    FEDs = []
    FED_ID = []
    Event_Errors = []
    key_FED_ID = "FED ID"
    key_Event_Errors = "Event errors"
    
    proxies = getProxies()
    FEDSupervisorURLs = getFEDSupervisorURLs()

    # Loop over pages (FEDSupervisorURLs)
    for key in FEDSupervisorURLs:
        URL = FEDSupervisorURLs[key]
        data = getFEDStatusInfo(URL, proxies)
        
        values = getFEDs(data)
        FEDs += values
        
        values = getIntValues(data, key_FED_ID)
        FED_ID += values
        
        values = getIntValues(data, key_Event_Errors)
        Event_Errors += values

    FEDs.sort()
    n_FEDs = len(FEDs)
    n_FED_ID = len(FED_ID)
    n_Event_Errors = len(Event_Errors)

    addFEDs(fed_data, FEDs)
    addValues(fed_data, key_Event_Errors, FED_ID, Event_Errors)
    sortedByErrors = getSortedMap(fed_data, key_Event_Errors, True)

    # print FEDs and errors; sorted by FEDs
    #for FED in FEDs:
    #    FED_Event_Errors = fed_data[FED][key_Event_Errors]
    #    print("FED {0}, {1}: {2}".format(FED, key_Event_Errors, FED_Event_Errors))
    
    # print FEDs and errors; sorted by errors
    for FED in sortedByErrors:
        errors = sortedByErrors[FED]
        print("FED {0}, {1}: {2}".format(FED, key_Event_Errors, errors))

    #print(FEDs)
    #print(FED_ID)
    #print(Event_Errors)
    print("Number of FEDs: {0}".format(n_FEDs))
    print("Number of FED_ID: {0}".format(n_FED_ID))
    print("Number of Event_Errors: {0}".format(n_Event_Errors))

def main():
    runScraper()

if __name__ == "__main__":
    main()


