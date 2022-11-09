# authenticate.py

# Tutorial on authenticating with python for web scraping.
# https://betterprogramming.pub/web-scraping-behind-authentication-with-python-be5f82eb85f0

import requests

# Create the session object
#s = requests.Session()

# Example request
#url = "https://www.google.com/"
#response = s.get(url)

cookies = {
    '_octo': 'GH1.1.293799198.1644252830',
    '_device_id': 'b407fd077e14d101b0a0820aeb962def',
    'color_mode': '%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'preferred_color_mode': 'dark',
    'tz': 'America%2FChicago',
    'has_recent_activity': '1',
    'logged_in': 'no',
    '_gh_sess': 'KwwSU5PvWM4Dckd1iodl0BG1eim8XUT8xjW8OGHcZQBDKCTimEV9ieZoxOFNZwmuRWmGzXf%2FN6igx2whrqP9xVKYYeC3L6m3yWr%2FkD2vi7oDiKHUQ3uV6WVhwwuqblwf4J4INhXUtfSRM0mgLlSnqWfWqqLEd2sca4xhsc6HxvH96AcoPxo0iuFus6Uo4XRmvB9NLcMrOknekfbNdGfqtoBnPsto92eMawh2BaS41yTNNSiK5Ntnru4OwGdFviQxHrQhqfqOq%2BkKHiFSifG4pg%3D%3D--KP%2Fha1Mc73SXgzUn--Z8ixPC88yZsE4qRKjFOBjw%3D%3D',
}

headers = {
    'authority': 'github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_octo=GH1.1.293799198.1644252830; _device_id=b407fd077e14d101b0a0820aeb962def; color_mode=%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=dark; tz=America%2FChicago; has_recent_activity=1; logged_in=no; _gh_sess=KwwSU5PvWM4Dckd1iodl0BG1eim8XUT8xjW8OGHcZQBDKCTimEV9ieZoxOFNZwmuRWmGzXf%2FN6igx2whrqP9xVKYYeC3L6m3yWr%2FkD2vi7oDiKHUQ3uV6WVhwwuqblwf4J4INhXUtfSRM0mgLlSnqWfWqqLEd2sca4xhsc6HxvH96AcoPxo0iuFus6Uo4XRmvB9NLcMrOknekfbNdGfqtoBnPsto92eMawh2BaS41yTNNSiK5Ntnru4OwGdFviQxHrQhqfqOq%2BkKHiFSifG4pg%3D%3D--KP%2Fha1Mc73SXgzUn--Z8ixPC88yZsE4qRKjFOBjw%3D%3D',
    'origin': 'https://github.com',
    'referer': 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

data = {
    'commit': 'Sign in',
    'authenticity_token': 'hzDw8G8yzIE_jLNXK99PsOTPyVDTwGNROQI4sOVy-VumumLSfoBwT_YJ3EK5cqm772vCUfXkwt0ykVr_ZSwpog',
    'login': 'caleb-james-smith',
    'password': 'fear-god-1',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'supported',
    'return_to': 'https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home',
    'allow_signup': '',
    'client_id': '',
    'integration': '',
    'required_field_e108': '',
    'timestamp': '1667970305823',
    'timestamp_secret': 'e8d5622e5c94f49e2365ea57c0345a4a1d67cb756878740d0644bf50e821a9cd',
}

# Create the session object
s = requests.Session()

url = "https://github.com/session"

response = s.post(url, cookies=cookies, headers=headers, data=data)
print(response)

#response = s.post(url, cookies=cookies, headers=headers, data=data)
#print(response)

#url = "https://github.com/caleb-james-smith/git-commands"
#url = "https://github.com/caleb-james-smith/WebScraper"
#url = "https://github.com/caleb-james-smith/CalebSmithDissertation"

#response = s.post(url, cookies=cookies, headers=headers, data=data)
#print(response)

