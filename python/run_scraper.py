# run_scraper.py

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PixelInfrastructure

from fed_scraper import getFEDStatusInfo, getFEDs, getIntValues, addFEDs, addValues

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

    fed_data = {}

    FEDs = []
    FED_ID = []
    Event_Errors = []

    key_FED_ID = "FED ID"
    key_Event_Errors = "Event errors"

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

    for FED in FEDs:
        FED_Event_Errors = fed_data[FED][key_Event_Errors]
        print("FED {0}, {1}: {2}".format(FED, key_Event_Errors, FED_Event_Errors))

    #print(FEDs)
    #print(FED_ID)
    #print(Event_Errors)
    print("Number of FEDs: {0}".format(n_FEDs))
    print("Number of FED_ID: {0}".format(n_FED_ID))
    print("Number of Event_Errors: {0}".format(n_Event_Errors))


def main():
    run()

if __name__ == "__main__":
    main()


