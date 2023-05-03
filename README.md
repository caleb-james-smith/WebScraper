# WebScraper

Code for scraping the web.

See the tutorial [here](https://realpython.com/beautiful-soup-web-scraper-python).

Install the required python3 packages.
```
pip3 install requests
pip3 install beautifulsoup4
pip3 install pysocks
```

Download the repository:
```
git clone https://github.com/caleb-james-smith/WebScraper.git
cd WebScraper
```

Run the example script:
```
python3 python/example.py 
```

Before running the PixelFEDSupervisor scraper,
you should start and ssh tunnel with port forwarding to access websites at P5.
Choose a port number greater than 1000 to use for the ssh tunnel.
In this example, we use port 1234; you should pick a different port number.
```
ssh -tt -Y <user>@lxplus.cern.ch -L1234:localhost:1234 "ssh -tt -Y -D 1234 <user>@cmsusr -4"
```

Then, in a browser using a proxy for the same port number (e.g. with FoxyProxy),
check that you can load one of the PixelFEDSupervisor pages,
for example http://srv-s2b18-37-01.cms:1971/urn:xdaq-application:lid=71.

Then run the PixelFEDSupervisor scraper:
```
python3 python/run_scraper.py
```

