# run_scraper.py

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PixelInfrastructure

from fed_scraper import getFEDStatusInfo, getFEDs, getIntValues

def run():
    print("Running")
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }
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

    FEDs = []
    FEDStructure = []
    EventErrorStructure = []

    for key in FEDSupervisorURLs:
        URL = FEDSupervisorURLs[key]
        data = getFEDStatusInfo(URL, proxies)
        
        fed_list = getFEDs(data)
        FEDs += fed_list
        
        fed_structure = getIntValues(data, "FED ID")
        FEDStructure += fed_structure
        
        event_error_structure = getIntValues(data, "Event errors")
        EventErrorStructure += event_error_structure

    FEDs.sort()
    n_FEDs = len(FEDs)
    n_FEDStructure = len(FEDStructure)
    n_EventErrorStructure = len(EventErrorStructure)

    #for FED in FEDs:
    #    print("FED {0}".format(FED))

    print(FEDs)
    print(FEDStructure)
    print(EventErrorStructure)
    print("Number of FEDs: {0}".format(n_FEDs))
    print("Number of FEDStructure: {0}".format(n_FEDStructure))
    print("Number of EventErrorStructure: {0}".format(n_EventErrorStructure))

def main():
    run()

if __name__ == "__main__":
    main()


