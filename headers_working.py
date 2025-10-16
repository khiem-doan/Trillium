# Import necessary libraries
from pandas import *
import requests
from bs4 import BeautifulSoup
import time
import regex
import winsound
import threading
import os
import urllib3
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import time
import webbrowser
import colorama
from colorama import Fore, Back, Style
import random
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import traceback


# Initialize headline tracking lists
citron_headline = [0]*2
scorpion_headline = [0]*2
iceberg_headline = [0]*2
statnews_headline = [0]*2
hindenburg_headline = [0]*2
wolfpack_headline = [0]*2
whitediam_headline = [0]*2
culper_headline = [0]*2
kerrisdale_headline = [0]*2
sp_headline = [0]*2
usps_headline = [0]*2
cdc_headline = [0]*2
info_headline = [0]*2
electrek_headline = [0]*2
insideev_headline = [0]*2
fda_headline = [0]*2
fda2_headline = [0]*2
ftc_headline = [0]*2
sava_headline = [0]*2
bearcave_headline = [0]*2
spruce_headline = [0]*2
benzinga_headline = [0]*2
nytimes_headline = [0]*2
pershing_headline = [0]*2
nypost_headline = [0]*2
aircurrent_headline = [0]*2
sec8k_headline = [0]*2
secRW_headline = [0]*2
cnbc_headline = [0]*2
freeport_headline = [0]*2
mingchi_headline = [0]*2
icahn_headline = [0]*2
srpt_headline = [0]*2
msft_headline = [0]*2
nikkei_headline = [0]*2
bleepcomp_headline = [0]*2
faa_headline = [0]*2
punchbowl_headline = [0]*2
hntrbrk_headline = [0]*2
bleecker_headline = [0]*2
muddywaters_headline = [0]*2
grizzly_headline = [0]*2
fuzzypanda_headline = [0]*2
tiktok_headline = [0]*2
betaville_headline = [0]*2
jcapital_headline = [0]*2
orca_headline = [0]*2
secspecific_headline = [0]*2
morpheus_headline = [0]*2

author = ""
tp_ticker = []

# sec_filing = ["1.01:", "1.02:", "2.04:", "2.05", "3.01:", "4.02:", "7.01:", "8.01,","9.01:"]
# Initialize headline tracking list for J Capital
USER_AGENTS_DATA = [
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.1"},
    {"ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.2"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edge/132.0.0.0"},
    {"ua": "Mozilla/5.0 (Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.1 Safari/537.36 Opera/89.0.444.0"},
    {"ua": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36 Edge/127.1.1.1"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Opera/80.1.1"},
    {"ua": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Mobile/Edge"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/100.0.4844.73 Mobile/15E148"},
    {"ua": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 SamsungBrowser/30.1"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"},
    {"ua": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile Safari/537.36 CriOS/101.0.4951.64"},
    {"ua": "Mozilla/5.0 (Linux; Android 10; moto e7 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 HuaweiBrowser/15.0.0.312"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 CriOS/132.0.0.0 Mobile/15E148 Safari/604."},
    {"ua": "Mozilla/5.0 (Linux; Android 10; 22033PC75G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36 YaBrowser/20.1"},
    {"ua": "Mozilla/5.0 (Linux; arm_64; Android 12; 24030PN60G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 10; SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 12; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"},
    {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edge/117.0.0.0"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"},
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Opera/102.0.0.0"},
    {"ua": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"},
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 13; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPad; CPU OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1"},
    {
        "ua": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:115.0) Gecko/20100101 Firefox/115.0"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16; rv:17.0) Gecko/20100101 Firefox/17.0"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 12; SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"},
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.0.0"},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPad; CPU OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1"},
    {
        "ua": "Mozilla/5.0 (Linux; Android 11; SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36"},
    {
        "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2; rv:16.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/604.1"}
]
#use
# session.headers.update({
#     'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
#     'Referer': 'https://google.com',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Connection': 'keep-alive',
#     'Cache-Control': 'no-cache',
#     'Pragma': 'no-cache'
# })
from soundboard import SOUNDS


ua = random.choice(USER_AGENTS_DATA)['ua']
headers = {'User-Agent': ua}
# Disable insecure request warnings (use with caution)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# def get_proxies_from_free_proxy_list():
#     url = "https://www.socks-proxy.net/"
#     try:
#         response = requests.get(url, timeout=15, verify=False)
#         response.raise_for_status()
#     except Exception as e:
#         print(f"Error fetching proxy list: {e}")
#         return []
#     soup = BeautifulSoup(response.text, 'lxml')
#     proxies = []
#     table = soup.find("table", class_="table table-striped table-bordered")
#     if not table:
#         print("Could not find the proxy table.")
#         return proxies
#     tbody = table.find("tbody")
#     if not tbody:
#         print("Could not find the table body.")
#         return proxies
#     rows = tbody.find_all("tr")
#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) >= 2:
#             ip = cols[0].text.strip()
#             port = cols[1].text.strip()
#             version = cols[4].text.strip()  # e.g., "Socks4"
#             if version.lower() == "socks4":
#                 proxy = {
#                     "http": f"socks4://{ip}:{port}",
#                     "https": f"socks4://{ip}:{port}"
#                 }
#                 proxies.append(proxy)
#     return proxies
#
# PROXIES = get_proxies_from_free_proxy_list()
# print("Scraped proxies:", PROXIES)
# PROXIES = [
#     {"http": "http://204.236.137.68:80", "https": "http://204.236.137.68:80"},
#     {"http": "http://43.153.11.82:13001", "https": "http://43.153.11.82:13001"},
#     {"http": "http://43.153.2.3:13001", "https": "http://43.153.2.3:13001"},
#     {"http": "http://43.153.14.194:13001", "https": "http://43.153.14.194:13001"},
#     {"http": "http://43.153.107.10:13001", "https": "http://43.153.107.10:13001"},
#     {"http": "http://43.153.85.114:13001", "https": "http://43.153.85.114:13001"},
#     {"http": "http://43.153.66.252:13001", "https": "http://43.153.66.252:13001"},
#     {"http": "http://43.153.48.105:13001", "https": "http://43.153.48.105:13001"},
#     {"http": "http://204.236.176.61:3128", "https": "http://204.236.176.61:3128"},
#     {"http": "http://13.56.47.50:3128", "https": "http://13.56.47.50:3128"},
#     {"http": "http://52.52.179.28:3128", "https": "http://52.52.179.28:3128"},
#     {"http": "http://18.144.153.151:3128", "https": "http://18.144.153.151:3128"},
#     {"http": "http://170.106.192.157:13001", "https": "http://170.106.192.157:13001"},
#     {"http": "http://43.153.45.169:13001", "https": "http://43.153.45.169:13001"},
#     {"http": "http://43.130.9.70:13001", "https": "http://43.130.9.70:13001"},
#     {"http": "http://49.51.75.240:13001", "https": "http://49.51.75.240:13001"},
#     {"http": "http://43.130.38.18:13001", "https": "http://43.130.38.18:13001"},
#     {"http": "http://43.135.184.36:13001", "https": "http://43.135.184.36:13001"},
#     {"http": "http://170.106.184.19:13001", "https": "http://170.106.184.19:13001"},
#     {"http": "http://170.106.82.224:13001", "https": "http://170.106.82.224:13001"},
#     {"http": "http://49.51.33.115:13001", "https": "http://49.51.33.115:13001"},
#     {"http": "http://43.135.134.152:13001", "https": "http://43.135.134.152:13001"},
#     {"http": "http://43.153.16.149:13001", "https": "http://43.153.16.149:13001"},
#     {"http": "http://43.153.48.129:13001", "https": "http://43.153.48.129:13001"},
#     {"http": "http://43.130.39.183:13001", "https": "http://43.130.39.183:13001"},
#     {"http": "http://170.106.73.178:13001", "https": "http://170.106.73.178:13001"},
#     {"http": "http://49.51.232.89:13001", "https": "http://49.51.232.89:13001"},
#     {"http": "http://49.51.250.227:13001", "https": "http://49.51.250.227:13001"},
#     {"http": "http://184.169.154.119:80", "https": "http://184.169.154.119:80"},
#     {"http": "http://159.89.239.166:18082", "https": "http://159.89.239.166:18082"},
#     {"http": "http://98.81.74.229:20202", "https": "http://98.81.74.229:20202"},
#     {"http": "http://38.152.72.187:2335", "https": "http://38.152.72.187:2335"},
#     # ... (continue adding all remaining proxies from your provided list)
#     {"http": "http://54.174.37.207:20005", "https": "http://54.174.37.207:20005"}
#     # For brevity, only the first 40 entries are shown.
# ]
#
# print("Scraped proxies:", PROXIES)


def jcapital():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 5  # Limit the number of requests per session
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            url = "https://www.jcapitalresearch.com/company-reports.html"
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"J Capital: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.89, 5.48))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            paragraph_div = soup.find('div', class_='paragraph')
            if not paragraph_div:
                print("J Capital: Could not find 'div' with class 'paragraph'.")
                time.sleep(random.uniform(3.89, 5.48))
                continue

            a_tag = paragraph_div.find('a', href=True)
            if not a_tag:
                print("J Capital: Could not find 'a' tag with href.")
                time.sleep(random.uniform(3.89, 5.48))
                continue

            article_url = a_tag['href']
            if not article_url.startswith('http'):
                article_url = 'https://www.jcapitalresearch.com' + article_url

            jcapital_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()

            if jcapital_headline[0] != jcapital_headline[1]:
                # Extract ticker from URL using '-terms-of-service'
                ticker = None
                parts = article_url.strip('/').split('/')
                if parts:
                    last_part = parts[-1]
                    if '-terms-of-service' in last_part:
                        prefix = last_part.split('-terms-of-service')[0]
                        if prefix:
                            ticker = prefix.upper()

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"J Capital: Could not extract ticker from URL '{article_url}'.")

                print(now, "\t", "J Capital", "\t", jcapital_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            jcapital_headline[0] = jcapital_headline[1]
            time.sleep(random.uniform(3.89, 5.48))
            request_count += 1

        except Exception as e:
            import traceback
            print(f"Error in jcapital(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(3.89, 5.48))

    session.close()  # Ensure the session is closed when done



# Initialize headline tracking list for Capybara
capybara_headline = [0]*2


# Ensure capybara_headline is defined globally or as needed
capybara_headline = ["", ""]
import random
import time
import winsound
import webbrowser
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
from colorama import Style, Back, Fore

# Ensure capybara_headline is defined globally or as needed
capybara_headline = ["", ""]

def capybara():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 4
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            url = "https://capybararesearch.com/"
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"Capybara: Received status code {resp.status_code}")
                time.sleep(random.uniform(5.36, 6.74))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            article_div = soup.find('div', class_='relative w-100 mb4')
            if not article_div:
                print("Capybara: Could not find 'div' with class 'relative w-100 mb4'.")
                time.sleep(random.uniform(5.36, 6.74))
                continue

            text_div = article_div.find('div', class_='blah w-100 w-60-ns pl3-ns')
            if not text_div:
                print("Capybara: Could not find 'div' with class 'blah w-100 w-60-ns pl3-ns'.")
                time.sleep(random.uniform(5.24, 6.74))
                continue

            a_tag = text_div.find('a', href=True)
            if not a_tag:
                print("Capybara: Could not find 'a' tag with href in text content.")
                time.sleep(random.uniform(5.24, 6.74))
                continue

            article_url = a_tag['href']
            if not article_url.startswith('http'):
                article_url = 'https://capybararesearch.com' + article_url

            h1_tags = a_tag.find_all('h1')
            if not h1_tags:
                print("Capybara: Could not find 'h1' tags within 'a' tag.")
                time.sleep(random.uniform(5.24, 6.74))
                continue

            capybara_headline[1] = ' '.join(h.get_text(strip=True) for h in h1_tags)
            now = datetime.now().time()

            if capybara_headline[0] != capybara_headline[1]:
                ticker = None
                ticker_div = text_div.find('div', class_='f5 fw5 mt2 mb3 gray')
                if ticker_div:
                    ticker_text = ticker_div.get_text(strip=True)
                    match = re.search(r'(NASDAQ|NYSE):\s*([A-Za-z0-9]+)', ticker_text, re.IGNORECASE)
                    if match:
                        ticker = match.group(2).upper()

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Capybara: Could not extract ticker from headline '{capybara_headline[1]}'.")

                print(now, "\t", "Capybara", "\t", capybara_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            capybara_headline[0] = capybara_headline[1]
            time.sleep(random.uniform(5.24, 6.74))
            request_count += 1

        except Exception as e:
            import traceback
            print(f"Error in capybara(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(5.24, 6.74))

    session.close()  # Ensure the session is closed when done


import random
import time
import winsound
import webbrowser
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from colorama import Style, Back, Fore

# Ensure bleecker_headline is defined globally or as needed
bleecker_headline = ["", ""]
def bleecker():
    import requests, random, time, webbrowser, winsound
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    from requests.adapters import HTTPAdapter, Retry
    from colorama import init, Fore, Back, Style

    init(autoreset=True)

    base_url = "https://www.bleeckerstreetresearch.com"
    index_url = base_url + "/research/"
    last_title = None

    # set up a session with retries + rotating UA
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    while True:
        try:
            # rotate UA every time through
            session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

            resp = session.get(index_url, timeout=15)
            if resp.status_code != 200:
                print(f"Bleecker: Received status code {resp.status_code}")
                time.sleep(5)
                continue

            soup = BeautifulSoup(resp.content, "html.parser")

            # pick the first blog-item
            article = soup.select_one("article.blog-item")
            if not article:
                print("Bleecker: Could not find an article.blog-item")
                time.sleep(5)
                continue

            # now pick the title link inside the <h1 class="blog-title">
            title_link = article.select_one("h1.blog-title a")
            if not title_link:
                print("Bleecker: Could not find h1.blog-title > a")
                time.sleep(5)
                continue

            title = title_link.get_text(strip=True)
            href  = title_link["href"]
            if not href.startswith("http"):
                href = base_url + href

            # only fire when it's changed
            if title != last_title:
                # ticker is whatever comes after /research/
                ticker = href.split("/research/")[-1].strip("/").upper()

                # print the yellow badge
                badge = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                print(badge); print(badge); print(badge)

                now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")
                print(f"{now}\tBleecker\t{title}")
                print("Article URL:", href)

                webbrowser.open_new_tab(href)
                try:
                    winsound.Beep(1500, 100)
                except:
                    pass

                last_title = title

            time.sleep(random.uniform(3.7, 4.7))

        except Exception as e:
            print("Error in bleecker():", e)
            time.sleep(5)

gotham_headline = ["", ""]
def gotham():
    import requests, re, time, random, webbrowser
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    from urllib.parse import urljoin
    import winsound, colorama
    from colorama import Fore, Back, Style
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    # initialize colors
    colorama.init(autoreset=True)

    # build a session with retries + rotating UA
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://",  HTTPAdapter(max_retries=retry))

    base_url = "https://www.gothamcityresearch.com/researchbeta/"
    last_article = None

    while True:
        # rotate UA each loop
        ua = random.choice(USER_AGENTS_DATA)['ua']
        session.headers.update({
            'User-Agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://www.gothamcityresearch.com',
            'Connection': 'keep-alive'
        })

        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Gotham: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.5))
                continue

            soup = BeautifulSoup(resp.text, 'lxml')

            # grab the first link to anything under /post/
            link = soup.find('a', href=re.compile(r'/post/'))
            if not link:
                print("Gotham: No article links found.")
                time.sleep(random.uniform(3.5, 4.5))
                continue

            article_url = urljoin(base_url, link['href'])
            title       = link.get_text(strip=True)

            # new article?
            if article_url != last_article:
                now = datetime.now(ZoneInfo("America/New_York"))
                ts = now.strftime("%Y-%m-%d %H:%M:%S %Z")
                print(f"{ts}\tGotham\t{title}")
                print("URL:", article_url)
                webbrowser.open_new_tab(article_url)
                try:
                    winsound.Beep(1500, 100)
                    winsound.Beep(1500, 100)
                    winsound.Beep(1500, 100)
                except:
                    pass
                last_article = article_url

            time.sleep(random.uniform(3.5, 4.5))

        except Exception as e:
            print("Error in gotham():", e)
            import traceback; traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.5))




# 4. Added Muddy Waters Function
import random
import time
import winsound
import webbrowser
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from colorama import Style, Back, Fore

# Ensure muddywaters_headline is defined globally or as needed
muddywaters_headline = ["", ""]

def muddywaters():
    # Assumes muddywaters_headline is defined as a global list: [previous, current]
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 6
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            # Request the main homepage instead of the /research/ page
            resp = session.get("https://muddywatersresearch.com/", timeout=16)
            if resp.status_code != 200:
                print(f"MuddyWaters: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.86, 5.65))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            # Find the container holding the reports; in the provided HTML it is the div with class "content-items"
            container = soup.find('div', class_='content-items')
            if not container:
                print("MuddyWaters: Could not find the 'content-items' container.")
                time.sleep(random.uniform(3.86, 5.65))
                continue

            # Get the first article element from the container
            article = container.find('article')
            if not article:
                print("MuddyWaters: Could not find any article element in the container.")
                time.sleep(random.uniform(3.86, 5.65))
                continue

            # Within the article, find the header's link with the report title
            header = article.find('header', class_='content-item__header')
            if not header:
                print("MuddyWaters: Could not find the header in the article.")
                time.sleep(random.uniform(3.86, 5.65))
                continue

            a_tag = header.find('a', class_='content-item__title-link', href=True)
            if not a_tag:
                print("MuddyWaters: Could not find the title link in the header.")
                time.sleep(random.uniform(3.86, 5.65))
                continue

            # The full URL is expected to be provided in the href attribute (if not, you might need to prepend the domain)
            article_url = a_tag['href']
            muddywaters_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()

            if muddywaters_headline[0] != muddywaters_headline[1]:
                ticker = None
                # Use a regex to find text within parentheses
                match = re.search(r'\(([^)]+)\)', muddywaters_headline[1])
                if match:
                    # Split the extracted text by space and take the first part
                    ticker = match.group(1).strip().split()[0].upper()

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"MuddyWaters: Could not extract ticker from headline '{muddywaters_headline[1]}'.")

                print(now, "\t", "MuddyWaters", "\t", muddywaters_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

            muddywaters_headline[0] = muddywaters_headline[1]
            time.sleep(random.uniform(3.86, 5.65))
            request_count += 1

        except Exception as e:
            print("Error in muddywaters():", e)
            time.sleep(random.uniform(3.86, 5.65))

    session.close()  # This line is unreachable due to the infinite loop



# 5. Added Grizzly Research Function
import random
import time
import winsound
import webbrowser
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from colorama import Style, Back, Fore

# Ensure grizzly_headline is defined globally or as needed
grizzly_headline = ["", ""]

def grizzly():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 4
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            url = "https://grizzlyreports.com/category/research/"
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"Grizzly: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.8, 4.95))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            div_post_head = soup.find('div', class_='post__head')
            if not div_post_head:
                print("Grizzly: Could not find 'div' with class 'post__head'.")
                time.sleep(random.uniform(3.8, 4.95))
                continue

            h3_title = div_post_head.find('h3', class_='post__title typescale-2')
            if not h3_title:
                print("Grizzly: Could not find 'h3' with class 'post__title typescale-2'.")
                time.sleep(random.uniform(3.8, 4.95))
                continue

            a_tag = h3_title.find('a', href=True)
            if not a_tag:
                print("Grizzly: Could not find 'a' tag with href in 'h3'.")
                time.sleep(random.uniform(3.8, 4.95))
                continue

            article_url = a_tag['href']
            grizzly_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()

            if grizzly_headline[0] != grizzly_headline[1]:
                ticker = None
                # Assuming ticker extraction logic is based on headline or URL
                match = re.search(r'\(([^)]+)\)', grizzly_headline[1])
                if match:
                    ticker = match.group(1).strip().upper()
                else:
                    # Fallback: use the first word as a ticker candidate
                    words = grizzly_headline[1].split()
                    if words:
                        first_word = words[0].strip().upper()
                        if first_word in cik_ticker_mapping.values():
                            ticker = first_word

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Grizzly: Could not extract ticker from headline '{grizzly_headline[1]}'.")

                print(now, "\t", "Grizzly", "\t", grizzly_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            grizzly_headline[0] = grizzly_headline[1]
            time.sleep(random.uniform(3.8, 4.95))
            request_count += 1

        except Exception as e:
            print("Error in grizzly():", e)
            time.sleep(random.uniform(3.8, 4.95))

    session.close()  # Ensure the session is closed when done


# 6. Added Fuzzy Panda Function
def fuzzypanda():
    import random
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 5 # Limit the number of requests per session
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get("https://fuzzypandaresearch.com/")
            if resp.status_code != 200:
                print(f"FuzzyPanda: Received status code {resp.status_code}")
                time.sleep(random.uniform(5.25, 6.75))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            article = soup.find('div', class_=lambda x: x and x.startswith('post-'))
            if not article:
                print("FuzzyPanda: Could not find 'div' tag with class starting with 'post-'.")
                time.sleep(random.uniform(5.25, 6.75))
                continue

            h2_tag = article.find('h2', class_='entry-title')
            if not h2_tag:
                print("FuzzyPanda: Could not find 'h2' tag with class 'entry-title'.")
                time.sleep(random.uniform(5.25, 6.75))
                continue

            a_tag = h2_tag.find('a', href=True)
            if not a_tag:
                print("FuzzyPanda: Could not find 'a' tag with href in 'h2'.")
                time.sleep(random.uniform(5.25, 6.75))
                continue

            article_url = a_tag['href']
            fuzzypanda_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if fuzzypanda_headline[0] != fuzzypanda_headline[1]:
                ticker = None
                import re
                match = re.search(r'\(([^)]+)\)', fuzzypanda_headline[1])
                if match:
                    ticker = match.group(1).strip().upper()
                else:
                    words = fuzzypanda_headline[1].split()
                    if words:
                        first_word = words[0].strip().upper()
                        if first_word in cik_ticker_mapping.values():
                            ticker = first_word

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                print(now, "\t", "FuzzyPanda", "\t", fuzzypanda_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

            fuzzypanda_headline[0] = fuzzypanda_headline[1]
            time.sleep(random.uniform(5.25, 6.75))
            request_count += 1
        except Exception as e:
            print("Error in fuzzypanda():", e)
            time.sleep(random.uniform(5.25, 6.75))


def scorpion():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 4  # Limit the number of requests per session
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get("https://scorpioncapital.com/research", timeout=10)
            if resp.status_code != 200:
                print(f"Scorpion: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.1, 5.65))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')

            # Find all <p class="sqsrte-small">
            p_tags = soup.find_all('p', class_='sqsrte-small')
            if not p_tags:
                print("Scorpion: Could not find 'p' tags with class 'sqsrte-small'.")
                time.sleep(random.uniform(3.1, 5.65))
                continue

            # Extract PDF links
            pdf_links = []
            for p_tag in p_tags:
                a_tag = p_tag.find('a', href=True)
                if a_tag and a_tag['href'].lower().endswith('.pdf'):
                    pdf_links.append(a_tag['href'])

            if not pdf_links:
                print("Scorpion: Could not find any PDF links.")
                time.sleep(random.uniform(3.1, 5.65))
                continue

            # Use the first PDF link
            article_url = pdf_links[0]
            filename = os.path.basename(article_url)  # Extract filename (e.g., "TMDX.pdf")
            scorpion_headline[1] = filename

            now = datetime.now().time()
            if scorpion_headline[0] != scorpion_headline[1]:
                ticker_candidate = os.path.splitext(filename)[0].upper()  # Remove '.pdf' and convert to uppercase

                # Format the ticker
                formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker_candidate}{Style.RESET_ALL}"
                print(formatted)
                print(formatted)
                print(formatted)

                # Output details
                print(now, "\t", "Scorpion", "\t", ticker_candidate)
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            # Update the processed headline
            scorpion_headline[0] = scorpion_headline[1]
            time.sleep(random.uniform(2.1, 5.65))
            request_count += 1

        except Exception as e:
            print("Error in scorpion():", e)
            time.sleep(random.uniform(3.1, 5.65))

    session.close()




# 2. Updated Kerrisdale Function
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 2. Updated Kerrisdale Function with Retry Adapter and Increased Timeout
def kerrisdale():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import time, random, webbrowser, winsound
    import colorama
    from colorama import Fore, Back, Style
    import re
    import traceback

    colorama.init(autoreset=True)

    # Initialize the session with a retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=5,              # Total number of retries
        backoff_factor=1,     # Wait 1*2^retry_number seconds between retries
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    request_count = 0
    max_requests_per_session = 11  # Limit the number of requests per session

    while True:
        try:
            session.proxies = random.choice(PROXIES)
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                request_count = 0

            ua = random.choice(USER_AGENTS_DATA)['ua']
            session.headers.update({'User-Agent': ua})  # Update session headers

            # Increase timeout to 15 seconds for the blog page request
            resp = session.get("https://www.kerrisdalecap.com/blog/", timeout=15)
            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find('div', class_='each-post')
            if not find:
                print("Kerrisdale: Could not find 'div' with class 'each-post'.")
                time.sleep(random.uniform(4.75, 5.75))
                continue

            a_tag = find.find('a', onclick=True)
            if not a_tag:
                print("Kerrisdale: Could not find 'a' tag with 'onclick' attribute.")
                time.sleep(random.uniform(4.75, 5.75))
                continue

            onclick_text = a_tag['onclick']
            match = re.search(r"toggleExcerpt\([^,]+,[^,]+,jQuery\(this\),'([^']+)'", onclick_text)
            if match:
                article_url = match.group(1)
            else:
                print("Kerrisdale: Could not extract URL from onclick.")
                time.sleep(random.uniform(4.75, 5.75))
                continue

            # Increase timeout to 15 seconds for the article request
            article_resp = session.get(article_url, timeout=15)
            article_soup = BeautifulSoup(article_resp.content, 'lxml')
            read_full_report_link = article_soup.find('a', class_='css3-button', string='Read Full Report')

            if not read_full_report_link:
                print("Kerrisdale: Could not find 'a' tag for 'Read Full Report'.")
                time.sleep(random.uniform(4.75, 5.75))
                continue

            full_report_url = read_full_report_link['href']
            # (The duplicate assignment below is intentional to mimic your original code)
            full_report_url = read_full_report_link['href']
            kerrisdale_headline[1] = a_tag.text.strip()
            now = datetime.now().time()
            if kerrisdale_headline[0] != kerrisdale_headline[1]:
                parts = full_report_url.strip('/').split('/')
                ticker = parts[-1].upper() if parts else None
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                print(now, "\t", "Kerrisdale", "\t", kerrisdale_headline[1])
                print("Article URL:", full_report_url)
                webbrowser.open_new_tab(full_report_url)
                winsound.Beep(1500, 100)

            kerrisdale_headline[0] = kerrisdale_headline[1]
            time.sleep(random.uniform(4.75, 5.75))
            request_count += 1
        except Exception as e:
            print("Error in kerrisdale():", e)
            traceback.print_exc()
            time.sleep(random.uniform(4.75, 5.75))
    session.close()  # Ensure the session is closed when done.
glassdoor_headline = ["", ""]

def glassdoor():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time, random, re, webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    colorama.init(autoreset=True)

    # ——— Build session with retry + rotating UA ———
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.glasshouseresearch.com',
        'Connection': 'keep-alive'
    })

    base_site = "https://www.glasshouseresearch.com"
    index_url = f"{base_site}/"

    last_pdf = None

    while True:
        try:
            resp = session.get(index_url, timeout=15)
            if resp.status_code != 200:
                print(f"Glassdoor: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.5))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            # find the first PDF link containing '_final'
            a = soup.find("a", href=re.compile(r"_final.*\.pdf$"))
            if not a:
                print("Glassdoor: No report link found.")
                time.sleep(random.uniform(3.5, 4.5))
                continue

            href = a["href"]
            pdf_url = href if href.startswith("http") else base_site + href

            # skip duplicates
            if pdf_url == last_pdf:
                time.sleep(random.uniform(3.5, 4.5))
                continue

            # extract ticker (text before '_final')
            filename = href.rsplit("/", 1)[-1]
            ticker = filename.split("_final", 1)[0].upper()

            # three‐times highlight
            formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
            print(formatted)
            print(formatted)
            print(formatted)

            now = datetime.now(ZoneInfo("America/New_York"))
            ts = now.strftime("%Y-%m-%d %H:%M:%S %Z")
            print(f"{ts}\tGlassdoor\t{ticker} report")
            print("PDF URL:", pdf_url)

            webbrowser.open_new_tab(pdf_url)
            winsound.Beep(1500, 100)
            winsound.Beep(1500, 100)
            winsound.Beep(1500, 100)

            last_pdf = pdf_url
            time.sleep(random.uniform(3.5, 4.5))

        except Exception as e:
            print("Error in glassdoor():", e)
            import traceback; traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.5))
# Global variable to track the last processed headline for Blue Orca
blue_orca_headline = ["", ""]

def blue_orca():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    import random
    import re
    import traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    colorama.init(autoreset=True)

    # --- Session + retry adapter ---
    session = requests.Session()
    retry_strategy = Retry(
        total=5, backoff_factor=1,
        status_forcelist=[429,500,502,503,504],
        allowed_methods=["GET","HEAD","OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # rotate UAs
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.blueorcacapital.com/',
        'Connection': 'keep-alive'
    })

    base_url = "https://www.blueorcacapital.com/"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Blue Orca: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.7, 4.65))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            container = soup.find("div", class_="cs-hero-type-2__container")
            if not container:
                print("Blue Orca: could not find the report container.")
                time.sleep(random.uniform(3.7, 4.65))
                continue

            articles = container.find_all("article", class_="cs-entry")
            if not articles:
                print("Blue Orca: no report articles found.")
                time.sleep(random.uniform(3.7, 4.65))
                continue

            article = articles[0]
            a_tag = article.find("a", class_="cs-overlay-link", href=True)
            if not a_tag:
                print("Blue Orca: could not find the report link.")
                time.sleep(random.uniform(3.7, 4.65))
                continue

            title_tag = article.find("h2", class_="cs-entry__title")
            latest_title = title_tag.get_text(strip=True) if title_tag else a_tag.get_text(strip=True)
            blue_orca_headline[1] = latest_title

            # build full URL
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = "https://www.blueorcacapital.com" + article_url

            # try front‑page ticker
            ticker = None
            for div in article.find_all("div", class_="cs-entry__inner"):
                txt = div.get_text(strip=True)
                m = re.match(r'^[A-Z]{2,5}:\s*(\S+)$', txt)
                if m:
                    ticker = m.group(1)
                    break

            # fallback: fetch article page and pull from the <h2> inside .report-header
            if not ticker:
                page_resp = session.get(article_url, timeout=15)
                if page_resp.status_code == 200:
                    page_soup = BeautifulSoup(page_resp.content, 'lxml')
                    hdr = page_soup.select_one("div.report-header h2")
                    if hdr:
                        # e.g. "Nutex Health Inc | NASDAQ: NUTX"
                        text = hdr.get_text(" ", strip=True)
                        m2 = re.search(r":\s*([A-Z\.]+)", text)
                        if m2:
                            ticker = m2.group(1)

            now = datetime.now(ZoneInfo("America/New_York"))

            # if it’s new, announce it
            if blue_orca_headline[0] != blue_orca_headline[1]:
                if ticker:
                    out = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(out); print(out); print(out)
                else:
                    print(f"Blue Orca: could not extract ticker from front‑page or article page.")
                print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Blue Orca \t {blue_orca_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

            blue_orca_headline[0] = blue_orca_headline[1]
            time.sleep(random.uniform(3.7, 4.65))

        except Exception as e:
            print("Error in blue_orca():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.7, 4.65))
# To run Blue Orca in its own thread:
import threading
# blue_orca_thread = threading.Thread(target=blue_orca)
# blue_orca_thread.start()


# 3. Updated Culper Function
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
def culper():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import time
    import webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    import random
    import re
    import traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    from urllib3.exceptions import ProtocolError  # Newly added import

    colorama.init(autoreset=True)

    # Initialize session and add retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,              # Total number of retries
        backoff_factor=1,     # Wait time: 1 * (2 ** retry_number)
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set initial headers
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    })

    request_count = 0
    max_requests_per_session = 6  # Adjust as needed

    # Global headline storage (assuming culper_headline is defined globally)
    try:
        culper_headline
    except NameError:
        culper_headline = ["", ""]

    url = "https://culperresearch.com/latest-research"

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                })
                request_count = 0

            # Increase timeout to 15 seconds for slower responses
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"Culper: Received status code {resp.status_code}")
                time.sleep(random.uniform(4.5, 5.25))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            # Changed: now find the first anchor with the correct data-aid attribute.
            a_tag = soup.find('a', attrs={'data-aid': 'DOWNLOAD_DOCUMENT_LINK_WRAPPER_RENDERED'}, href=True)
            if not a_tag:
                print("Culper: Could not find the latest report link.")
                time.sleep(random.uniform(4.5, 5.25))
                continue

            article_url = a_tag['href']
            if article_url.startswith('//'):
                article_url = 'https:' + article_url
            elif article_url.startswith('/'):
                article_url = 'https://culperresearch.com' + article_url

            # Get the headline from the preceding <p> tag with the desired data-aid attribute.
            p_tag = a_tag.find('span', attrs={'data-aid': 'DOWNLOAD_FILE_NAME_RENDERED'})
            if not p_tag:
                print("Culper: Could not find the headline in the download block.")
                time.sleep(random.uniform(4.5, 5.25))
                continue

            culper_headline[1] = p_tag.get_text(strip=True)
            now = datetime.now().time()

            if culper_headline[0] != culper_headline[1]:
                ticker = None
                match = re.search(r'\(([^)]+)\)', culper_headline[1])
                if match:
                    ticker = match.group(1).strip().upper()

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Culper: Could not extract ticker from headline '{culper_headline[1]}'.")
                    # Optionally, skip further actions if ticker is not found

                print(f"{now} \t Culper \t {culper_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            culper_headline[0] = culper_headline[1]
            time.sleep(random.uniform(4.5, 5.25))
            request_count += 1

        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError,
                requests.exceptions.ChunkedEncodingError,
                ProtocolError) as e:
            print(f"Connection error in culper(): {e}")
            time.sleep(random.uniform(4.5, 5.25))
            continue

        except Exception as e:
            print(f"Error in culper(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(4.5, 5.25))
            continue

    session.close()  # Unreachable due to infinite loop



def spruce():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 10  # Adjust as needed
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    })
    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                })
                request_count = 0
            # --- Update proxies ---
            if PROXIES:
                session.proxies = random.choice(PROXIES)
            else:
                print("Warning: No proxies available; proceeding without proxy.")
            url = "https://www.sprucepointcap.com/research"
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"Spruce: Received status code {resp.status_code}")
                time.sleep(random.uniform(4.1, 5.65))
                continue
            soup = BeautifulSoup(resp.content, 'lxml')
            container = soup.find('div', class_='research-list-wrap')
            if not container:
                print("Spruce: Could not find 'div' with class 'research-list-wrap'.")
                time.sleep(random.uniform(4.1, 5.65))
                continue
            find_link = container.find('a', href=True)
            if not find_link:
                print("Spruce: Could not find 'a' tag with href.")
                time.sleep(random.uniform(4.1, 5.65))
                continue
            href = find_link['href']
            article_url = 'https://www.sprucepointcap.com' + href
            title_tag = find_link.find('h3', class_='research-h3')
            if not title_tag:
                print("Spruce: Could not find 'h3' tag with class 'research-h3'.")
                time.sleep(random.uniform(4.1, 5.65))
                continue
            spruce_headline[1] = title_tag.text.strip()
            now = datetime.now().time()
            if spruce_headline[0] != spruce_headline[1]:
                ticker = None
                designation_div = container.find('div', class_='stock-designation')
                if designation_div:
                    sub_divs = designation_div.find_all('div')
                    if len(sub_divs) >= 2:
                        ticker = sub_divs[1].get_text(strip=True)
                if not ticker:
                    page_resp = session.get(article_url, timeout=15)
                    if page_resp.status_code == 200:
                        page_soup = BeautifulSoup(page_resp.content, 'html.parser')
                        text = page_soup.get_text()
                        match = re.search(r'(NASDAQ|NYSE):\s*([A-Za-z0-9]+)', text)
                        if match:
                            ticker = match.group(2).upper()
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Spruce: Could not extract ticker from headline '{spruce_headline[1]}'.")
                print(f"{now} \t Spruce \t {spruce_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
            spruce_headline[0] = spruce_headline[1]
            time.sleep(random.uniform(4.1, 5.65))
            request_count += 1
        except Exception as e:
            print(f"Error in spruce(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(4.1, 5.65))
def sec8k():
    # --- Section 1: Imports and Initialization ---
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, timezone, time as dt_time
    from zoneinfo import ZoneInfo  # Python 3.9+
    import re
    import time
    import webbrowser
    import colorama
    from colorama import Fore, Back, Style
    import string
    from bs4 import XMLParsedAsHTMLWarning
    import warnings
    import random
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    colorama.init(autoreset=True)

    # --- Section 2: Helper functions ---
    def adjust_url(url):
        if 'ix?doc=' in url:
            base_url = 'https://www.sec.gov'
            doc_path = url.split('ix?doc=')[-1]
            return base_url + doc_path
        else:
            return url

    def keyword_in_text(text, keyword):
        pattern = re.escape(keyword)
        pattern = pattern.replace(r'\ ', r'\s+')
        regex = re.compile(pattern, re.IGNORECASE)
        return regex.search(text)
    def play_form_sound(form_label: str):
        """
        Plays the correct sound for a filing form.
        8-K or 8  -> "s e c 8k"
        4         -> "form 4"
        424B5     -> "424b5"
        Falls back to a short beep if SOUNDS isn't available.
        """
        try:
            # Normalize like: "8-K/A" -> "8K", "424B5" stays "424B5"
            norm = re.sub(r'[^A-Za-z0-9]', '', str(form_label).upper())
            if norm in ("8K", "8"):
                sound_name = "s e c 8k"
            elif norm == "4":
                sound_name = "form 4"
            elif norm == "424B5":
                sound_name = "424b5"
            else:
                return  # nothing to play for other forms

            try:
                SOUNDS.play(sound_name, stop_current=True)
            except Exception:
                # Fallback so you still get an audible cue if SOUNDS isn't defined/available
                try:
                    import winsound
                    winsound.Beep(1500, 120)
                except Exception:
                    pass
        except Exception:
            pass

    # --- Section 3: Create session and set headers ---
    session = requests.Session()
    ua = random.choice(USER_AGENTS_DATA)['ua']
    my_contact = "John Doe; john.doe@example.com"  # Replace with your actual info
    session.headers.update({
        'User-Agent': f'{ua} ({my_contact})',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.sec.gov',
        'Connection': 'keep-alive'
    })

    # --- Section 4: Retry strategy for session ---
    retry_strategy = Retry(
        total=5,  # Total number of retries
        backoff_factor=1,  # Wait 1*retry_number seconds between retries
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)

    # --- Section 5: Feed URL and initial variables ---
    feed_url = ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=&company="
                "&dateb=&owner=include&start=0&count=40&output=atom")
    allowed_forms = {"8-K", "4", "S-3", "6-K", "424B4","13F","424B5","EFFECT","effect","F1","F-1","F-1MEF","S-1"}
    opened_links = set()
    last_processed_time = datetime.now(timezone.utc)
    first_run = True

    # --- Section 6: Keyword lists and filters ---
    orange_keywords = ["notification of late filing", "late filing","delisting letter"]
    green_keywords = ["expects to report","intends to reaffirm","preliminary",
                      "all of the assets","non-binding letter of intent","private equity firm","LOI",
                      "annual revenue","guidance","will end the quarter","now expects full-year", "now expects quarterly",
                      "Nvidia", "AMD", "Microsoft", "Amazon", "Google", "Musk", "Altman", "Nasa", "SpaceX", "OpenAI",
                      "Oracle", "Tesla", "Robotaxi", "Uber", "autonomous",
                      "palantir", "bitcoin", "treasury", "cryptocurrency", "Baidu", "pentagon", "DoD",
                      "Department of defense", "Anthropic", "Perplexity", "TSM", "Marvell",
                      "data center", "Trump", "White House","Altman","Musk"
                      ]
    red_keywords = [
        "DOJ investigation", "SEC investigation", "CEO resignation", "internal investigation",
        "fraud investigation", "audit", "material weakness", "emerging risks", "material impact",
        "withdraw guidance", "not reaffirming", "suspends dividend", "gross misconduct","lower than previously expected",
        "withdrawing guidance", "withdraw outlook", "withdrawing outlook", "withdrawing full", "withdraw full",
        "floor price","determined to delist","no longer be relied upon","Prior Financial Statements","non-reliance"

    ]
    red_position_keywords = ["chief executive officer", "chief financial officer"]
    red_action_keywords = ["transition", "resign", "step down", "resignation", "interim"]
    sec_filing = ["5.02", "8.01", "1.01", "2.02", "3.01","7.01","4.02"]

    filter_keywords = {
        # Existing keywords...
        "withdraw guidance","withdrawing guidance","withdraw outlook","withdrawing outlook","withdrawing full","withdraw full",
        "expects to report","intends to reaffirm","defaulted", "preliminary", "entered into an inducement offer",
        "wildfire", "wildland fires", "wildland fire",
        "discontinue","restarted", "new chief financial officer","new chief executive officer",
        "chapter 7", "chapter 11", "capital expenditures", "developing plans", "accelerate and expand",
        "expand investment", "warrants", "inducement letter", "purchase an aggregate","floor price"
        "terminated the employment of", "gross misconduct", "is working to mitigate",
        "continues to remain uncertain", "is now at risk", "updates on the current market",
        "market environment", "book-to-bill ratio", "business highlights", "operational and financial update",
        "operational performance", "underlying demand trends continue", "negative impact",
        "now expects revenue", "the company continues", "business update", "revised its outlook",
        "comp sales", "higher than previously expected", "lower than previously expected",
        "are expected to be", "increasing levels", "more pressure", "less pressure",
        "updates to guidance", "updates to its guidance", "reconciles expected",
        "now expects full-year", "now expects quarterly", "uspi", "u.s. prescribing information","adverse event","FAERS",
        "warnings and precautions", "adverse reactions", "vasculitis", "fda",
        "drug administration", "acquisition", "workforce", "suspends dividend",
        "restructuring plan", "announced the departure", "estimates that it will incur",
        "delisting letter", "material impact", "impact of the incident",
        "unauthorized activity", "resume normal operations", "regulatory authorities",
        "is working with law enforcement", "cyberattack", "patent", "delay",
        "regulatory", "floor price", "lower financial projections", "impairment charge",
        "revised projection", "ketamine", "psilocybin", "not reaffirming", "withdrawing", "shares issuable",
        "determined to delist",
        # Additional keywords...
        "leadership change", "executive compensation", "executive appointment", "merger agreement",
        "strategic partnership", "stock buyback", "share repurchase", "financial restructuring",
        "cost reduction", "operational restructuring", "supply chain disruption", "material weakness",
        "class action lawsuit", "regulatory investigation", "earnings restatement",
        "non-compliance", "regulatory action", "regulatory fine", "environmental impact",
        "litigation settlement", "data breach", "cybersecurity incident", "revenue decline",
        "financial outlook", "downgraded outlook", "guidance revision", "liquidity issues",
        "capital raise", "debt offering", "equity offering", "credit facility", "loan covenant",
        "financial covenant breach", "cash flow issues", "delisting notice", "stock suspension",
        "emerging risks", "asset sale", "disposition of assets", "plant closure", "facility closure",
        "key contract", "partnership termination", "contract dispute", "restructuring charge",
        "severance costs", "layoff plan", "corporate governance", "ethics violations",
        "ceo resignation", "cfo resignation", "interim chief executive officer", "shareholder meeting",
        "proxy filing", "stockholder vote", "activist investor", "board change", "new board member",
        "internal investigation", "whistleblower", "regulatory compliance", "compliance failure",
        "reorganization plan", "fraud investigation", "sec investigation", "audit committee",
        "independent audit", "doj investigation", "all of the assets","non-binding letter of intent","private equity firm","LOI",
        "no longer be relied upon","Prior Financial Statements",
        "non-recurring charges","cost savings",
        "Updated Outlook","now expects","annual revenue","strong start","guidance","will end the quarter","debt","revenue",
        "Department of Justice","non-reliance",
        "Nvidia","AMD","Microsoft","Amazon","Google","Musk","Altman","Nasa","SpaceX","OpenAI","Oracle","Tesla","Robotaxi","Uber","autonomous",
        "palantir","bitcoin","treasury","cryptocurrency","Baidu","pentagon","DoD","Department of defense","Anthropic","Perplexity","TSM","Marvell",
        "data center","Trump","White House","Altman","Musk","Ellison","Jensen Huang","Bezos","Lisa Su","Bill Gates","Spacex","Broadcom",
        "Coinbase","Pentagon","Department of Defense","Waymo","Netflix","Army","Navy","Air Force","Space Force","Disney"
    }

    buy_amount = 1000000
    sell_amount = -50000000

    # --- Section 7: Load ticker mapping ---
    cik_ticker_mapping, company_name_to_ticker = load_cik_ticker_mapping()

    request_count = 0
    max_requests_per_session = 20
    title_pattern = re.compile(r'^(.*?)\s*-\s*(.*?)\s*\((\d+)\)\s*\((.*?)\)$', re.IGNORECASE)
    allowed_tags = {"filer", "reporting", "issuer", "subject"}

    # --- Section 8: Main polling loop ---
    while True:
        try:
            # --- Section 8a: Rotate session if too many requests ---
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                ua = random.choice(USER_AGENTS_DATA)['ua']
                session.headers.update({
                    'User-Agent': f'{ua} ({my_contact})',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Referer': 'https://www.sec.gov',
                    'Connection': 'keep-alive'
                })
                session.mount("https://", adapter)
                request_count = 0

            # --- Section 8b: Fetch feed ---
            resp = session.get(feed_url, timeout=15)
            if resp.status_code != 200:
                print(f"SEC 8K: Error fetching RSS feed: {resp.status_code} {resp.reason}")
                time.sleep(3.03)
                continue

            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'xml')
            entries = soup.find_all('entry')
            if not entries:
                print("SEC 8K: No entries found in the feed.")
                time.sleep(3.03)
                continue
            else:
                if first_run:
                    print(f"SEC 8K: Found {len(entries)} entries.")
                    first_run = False

            sec8k_items = None

            # --- Section 8c: Process each entry ---
            for top_entry in entries:
                link_tag = top_entry.find('link')
                if link_tag and link_tag.get('href'):
                    top_link = link_tag['href']
                else:
                    continue

                form_type = top_entry.category.get('term', 'Unknown').strip()

                if form_type not in allowed_forms:
                    continue

                    # <<< ADDED: if it’s a 13F filing, only proceed if the CIK is NVDA’s (1045810)
                if form_type.startswith("13F"):
                    title_text = top_entry.title.get_text(strip=True)
                    m = title_pattern.match(title_text)
                    cik_num = m.group(3).lstrip('0') if m else None
                    if cik_num != "1045810":
                        continue

                updated_datetime_str = top_entry.updated.get_text()
                updated_datetime = datetime.strptime(updated_datetime_str, '%Y-%m-%dT%H:%M:%S%z')
                if updated_datetime <= last_processed_time:
                    continue

                items_text = "N/A"
                # --- Section 8d: Filter 8-K by Item codes ---
                if form_type == "8-K":
                    summary = top_entry.summary
                    if summary and summary.get_text():
                        summary_text = BeautifulSoup(summary.get_text(), 'html.parser').get_text()
                        summary_text = ' '.join(summary_text.split())
                        items = re.findall(r'Item [\d\.]+: .*?(?=(?:Item [\d\.]+:|$))', summary_text)
                        if items:
                            sec8k_items = [
                                item for item in items
                                if any(sec_item in item for sec_item in sec_filing)
                            ]
                            if sec8k_items:
                                items_text = ', '.join(
                                    item.split(':')[0].replace('Item ', '').strip()
                                    for item in sec8k_items
                                )
                            else:
                                continue
                        else:
                            continue

                        current_est = datetime.now(ZoneInfo('America/New_York')).time()
                        if current_est < dt_time(16, 0):
                            unique_items = {
                                item.split(':')[0].replace('Item ', '').strip()
                                for item in sec8k_items
                            }
                            if unique_items == {"2.02", "9.01"}:
                                continue
                    else:
                        continue

                # --- Section 8e: Skip already opened links ---
                if top_link not in opened_links:
                    print_timestamp = datetime.now(timezone.utc)
                    time_diff_seconds = (print_timestamp - updated_datetime).total_seconds()
                    updated_datetime_est = updated_datetime.astimezone(ZoneInfo('America/New_York'))
                    print_timestamp_est = print_timestamp.astimezone(ZoneInfo('America/New_York'))
                    title_text = top_entry.title.get_text(strip=True)
                    match = title_pattern.match(title_text)
                    if not match:
                        continue

                    form_type_extracted = match.group(1).strip()
                    company_name = match.group(2).strip()
                    cik_number = match.group(3).strip().lstrip('0')
                    ending_tag = match.group(4).strip().lower()
                    if form_type_extracted == "4" and ending_tag != "issuer":
                        continue
                    if ending_tag not in allowed_tags:
                        continue

                    if cik_number not in cik_ticker_mapping:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    ticker = cik_ticker_mapping[cik_number]

                    # --- Section 8f: Format ticker highlighting for 8‑K ---
                    if form_type == "8-K" and sec8k_items is not None:
                        if any(("3.01" in item or "1.02" in item) for item in sec8k_items):
                            ticker_formatted = "\n".join(
                                [f"{Style.BRIGHT}{Back.RED}{Fore.BLACK}{ticker}{Style.RESET_ALL}" for _ in range(3)]
                            )
                        elif any("1.01" in item for item in sec8k_items):
                            ticker_formatted = "\n".join(
                                [f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK}{ticker}{Style.RESET_ALL}" for _ in range(3)]
                            )
                        elif any("8.01" in item for item in sec8k_items):
                            ticker_formatted = "\n".join(
                                [f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}" for _ in range(3)]
                            )
                        else:
                            # Non-highlighted ticker for 8-K should be white
                            ticker_formatted = f"{Style.BRIGHT}{Fore.WHITE}{ticker}{Style.RESET_ALL}"
                    else:
                        # If not an 8-K filing or if no special items, ticker is non-highlighted → white text
                        ticker_formatted = f"{Style.BRIGHT}{Fore.WHITE}{ticker}{Style.RESET_ALL}"

                    # --- Section 8g: Fetch filing page and locate document URL (REPLACEMENT) ---
                    def _find_primary_doc_url(page_html: bytes, wanted_type: str) -> str | None:
                        """
                        Robustly locate the main document URL on a filing index page.
                        Works with both tableFile and tableFile2 layouts. Tries, in order:
                          1) Row whose Type exactly matches wanted_type (e.g., 424B5)
                          2) Any document link whose filename contains wanted_type (e.g., *_424b5.htm)
                          3) A row whose Description mentions 'prospectus' and link is .htm/.html
                        Returns absolute https://www.sec.gov/... URL or None.
                        """
                        from bs4 import BeautifulSoup
                        import re

                        soup = BeautifulSoup(page_html, "lxml")

                        # consider both common SEC tables
                        tables = soup.select("table.tableFile, table.tableFile2")
                        for tbl in tables:
                            # map header names to indices (handles column shuffles)
                            header = tbl.find("tr")
                            if not header:
                                continue
                            headers = [th.get_text(strip=True).lower() for th in header.find_all(["th", "td"])]
                            idx = {name: i for i, name in enumerate(headers)}

                            # best-guess indices with tolerant fallbacks
                            i_doc = next((i for k, i in idx.items() if "document" in k), 2)
                            i_type = next((i for k, i in idx.items() if k == "type" or "type" in k), 3)
                            i_desc = next((i for k, i in idx.items() if "description" in k), 1)

                            # pass 1: exact Type match
                            for row in tbl.find_all("tr")[1:]:
                                cols = row.find_all("td")
                                if len(cols) <= max(i_doc, i_type, i_desc):
                                    continue
                                type_txt = cols[i_type].get_text(strip=True).upper() if i_type < len(cols) else ""
                                a = cols[i_doc].find("a", href=True) if i_doc < len(cols) else None
                                href = a["href"] if a else ""
                                if href and not href.startswith("http"):
                                    href = "https://www.sec.gov" + href
                                if type_txt == wanted_type.upper() and href:
                                    return href

                            # pass 2: filename contains wanted type (e.g., *_424b5.htm)
                            for row in tbl.find_all("tr")[1:]:
                                cols = row.find_all("td")
                                if len(cols) <= i_doc:
                                    continue
                                a = cols[i_doc].find("a", href=True)
                                if not a:
                                    continue
                                href = a["href"]
                                if not href.startswith("http"):
                                    href = "https://www.sec.gov" + href
                                if wanted_type.lower() in href.lower():
                                    return href

                            # pass 3: description mentions prospectus + html link
                            for row in tbl.find_all("tr")[1:]:
                                cols = row.find_all("td")
                                if len(cols) <= max(i_doc, i_desc):
                                    continue
                                desc = cols[i_desc].get_text(strip=True).lower() if i_desc < len(cols) else ""
                                a = cols[i_doc].find("a", href=True)
                                if not a:
                                    continue
                                href = a["href"]
                                if not href.startswith("http"):
                                    href = "https://www.sec.gov" + href
                                if "prospectus" in desc and re.search(r"\.html?$", href, re.I):
                                    return href

                        return None

                    # fetch the filing index page
                    page_resp = session.get(top_link, timeout=15)
                    if page_resp.status_code != 200:
                        print(
                            f"[SEC] {form_type}: index page request failed ({page_resp.status_code}) for {title_text}")
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    # pick the primary document URL using robust logic
                    doc_url = _find_primary_doc_url(page_resp.content, form_type)

                    # if not found, log and fall back to index (so it’s visible rather than silently skipped)
                    if not doc_url:
                        print(
                            f"[SEC] {form_type}: could not locate primary document on index — using index page for {title_text}")
                        doc_url = top_link

                    # normalize inline XBRL “ix?doc=” style URLs and fetch the doc
                    doc_url = adjust_url(doc_url)
                    doc_resp = session.get(doc_url, timeout=15)
                    if doc_resp.status_code != 200:
                        print(
                            f"[SEC] {form_type}: primary document request failed ({doc_resp.status_code}) for {title_text}")
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue
                    # --- End Section 8g replacement ---

                    # --- Section 8h: Parse and clean document text ---
                    doc_content = doc_resp.content.decode('utf-8', errors='ignore')
                    doc_content = re.sub(r'\sxmlns(:\w+)?="[^"]+"', '', doc_content)
                    doc_content = re.sub(r'</?(\w+):', '<', doc_content)
                    soup_doc = BeautifulSoup(doc_content, 'lxml')
                    for script_or_style in soup_doc(['script', 'style']):
                        script_or_style.decompose()
                    text = soup_doc.get_text(separator=' ', strip=True)
                    text = ''.join(filter(lambda x: x in string.printable, text))
                    text = re.sub(r'\s+', ' ', text)
                    text_lower = text.lower()

                    if cik_number == "1045810" and form_type.startswith("13F"):
                        # 1) Find the info-table rows (skip the header rows)
                        info_table = soup_doc.find('table', summary=re.compile(r'Information Table', re.IGNORECASE))
                        issuer_names = []
                        if info_table:
                            rows = info_table.find_all('tr')
                            # header rows are the first 4; the 5th onward are data rows
                            for row in rows[4:]:
                                # the first <td class="FormData"> is the issuer name
                                cell = row.find('td', class_='FormData')
                                if cell:
                                    issuer_names.append(cell.get_text(strip=True))

                        # 2) Map each issuer to a ticker with your fallback logic
                        issuer_tickers = []
                        for name in issuer_names:
                            norm = normalize_company_name(name)  # same helper you already have
                            ticker = company_name_to_ticker.get(norm)
                            if not ticker:
                                slug = name.upper().replace(' ', '').strip()
                                all_tcks = set(company_name_to_ticker.values())
                                if slug in all_tcks:
                                    ticker = slug
                                else:
                                    # try expansions
                                    for exp in (" INC.", " INC", " INCORPORATED",
                                                " CORP.", " CORP", " CORPORATION",
                                                " LTD.", " LTD", " PLC", " SA", ""):
                                        candidate = (slug + exp).strip()
                                        if candidate in company_name_to_ticker:
                                            ticker = company_name_to_ticker[candidate]
                                            break
                                if not ticker:
                                    # substring match fallback
                                    for comp_name, comp_tck in company_name_to_ticker.items():
                                        if slug in comp_name:
                                            ticker = comp_tck
                                            break
                            issuer_tickers.append(ticker or "None")

                        # 3) Print them right after your usual output
                        print("\n[NVDA 13F] Full list of issuers and mapped tickers:")
                        for nm, tk in zip(issuer_names, issuer_tickers):
                            print(f"  {nm} : {tk}")
                        print()  # blank line

                    # --- Section 8i: Process Form 4 details if applicable ---
                    if form_type_extracted.strip() == "4":
                        rp_section = soup_doc.find(
                            lambda tag: tag.name == "td" and "Name and Address of Reporting Person" in tag.get_text()
                        )
                        if rp_section:
                            rp_link = rp_section.find("a", href=re.compile("getcompany"))
                            reporting_person = rp_link.get_text(strip=True) if rp_link else "Not found"
                        else:
                            reporting_person = "Not found"

                        rel_td = soup_doc.find(
                            lambda tag: tag.name == "td"
                                        and tag.has_attr("style")
                                        and "color:" in tag["style"].lower()
                                        and "blue" in tag["style"].lower()
                                        and tag.get_text(strip=True) != ""
                        )
                        relation = rel_td.get_text(strip=True) if rel_td else "Not found"

                        table_i_header = soup_doc.find(
                            lambda tag: tag.name == "th" and "Table I" in tag.get_text()
                        )
                        if table_i_header:
                            trans_table = table_i_header.find_parent("table")
                            if trans_table:
                                trans_rows = trans_table.find_all("tr")[1:]
                                acq_sum = sale_sum = acq_price_val = sale_price_val = 0.0
                                for trow in trans_rows:
                                    tcols = trow.find_all("td")
                                    if len(tcols) >= 8:
                                        shares_str = tcols[5].get_text(strip=True).replace(",", "")
                                        indicator = tcols[6].get_text(strip=True).upper()
                                        price_str = re.sub(r'[^\d\.]', '', tcols[7].get_text(strip=True))
                                        try:
                                            shares_val = float(shares_str) if shares_str else 0.0
                                        except:
                                            shares_val = 0.0
                                        try:
                                            price_val = float(price_str) if price_str and price_str != "-" else 0.0
                                        except:
                                            price_val = 0.0
                                        if indicator == "A":
                                            acq_sum += shares_val
                                            if price_val > 0:
                                                acq_price_val = price_val
                                        elif indicator == "D":
                                            sale_sum += shares_val
                                            if price_val > 0:
                                                sale_price_val = price_val

                                net_shares = acq_sum - sale_sum
                                used_price = sale_price_val if sale_price_val > 0 else acq_price_val
                                try:
                                    dollar_amount = net_shares * used_price
                                except:
                                    dollar_amount = 0.0

                                extra_info = (
                                    f"Reporting Person: {reporting_person}\n"
                                    f"Relation: {relation}\n"
                                    f"Transaction: Net shares: {net_shares} at ${used_price:.3f} per share, Total: ${dollar_amount:.2f}\n"
                                )
                            else:
                                extra_info = "Form 4 extra details not available\n"
                        else:
                            extra_info = "Form 4 extra details not available\n"

                        if not (dollar_amount > buy_amount or dollar_amount < sell_amount):
                            last_processed_time = max(last_processed_time, updated_datetime)
                            continue

                        # For Form 4 filings, if highlighted (based on transaction), use background with black text;
                        # otherwise ensure non-highlighted tickers are white.
                        if dollar_amount < 0:
                            company_color = Back.RED + Fore.WHITE  # For negative dollar amount (highlighted)
                        elif dollar_amount > 0:
                            company_color = Back.GREEN + Fore.WHITE  # For positive (highlighted)
                        else:
                            company_color = ""
                        if company_color == "":
                            ticker_formatted = f"{Style.BRIGHT}{Fore.WHITE}{ticker}{Style.RESET_ALL}"
                        else:
                            ticker_formatted = f"{company_color}{ticker}{Style.RESET_ALL}"
                        company_name_colored = f"{company_color}{company_name}{Style.RESET_ALL}"
                    else:
                        company_name_colored = company_name

                    # --- Section 8j: Additional filtering for 6‑K and 8‑K ---
                    if form_type in ("6-K", "8-K"):
                        if not any(keyword in text_lower for keyword in filter_keywords):
                            last_processed_time = max(last_processed_time, updated_datetime)
                            continue

                    # --- Section 8k: Determine overall color highlight ---
                    # Only retain extra_info/dollar_amount for Form 4; clear for everything else
                    if form_type_extracted.strip() != "4":
                        extra_info = ""
                        dollar_amount = 0.0
                    else:
                        extra_info = extra_info if 'extra_info' in locals() else ""
                        dollar_amount = dollar_amount if 'dollar_amount' in locals() else 0.0

                    # Now decide highlight color based on keywords in the full text
                    red_found = any(keyword_in_text(text_lower, kw) for kw in red_keywords)
                    green_found = any(keyword_in_text(text_lower, kw) for kw in green_keywords)
                    orange_found = any(keyword_in_text(text_lower, kw) for kw in orange_keywords)

                    if orange_found:
                        color_code = Back.YELLOW + Fore.BLACK
                    elif red_found:
                        color_code = Back.RED + Fore.BLACK
                    elif green_found:
                        color_code = Back.GREEN + Fore.BLACK
                    else:
                        color_code = ''

                    # Apply background+black‐text when highlighted; otherwise white text on no background
                    if color_code:
                        ticker_formatted = f"{color_code}{ticker}{Style.RESET_ALL}"
                        company_name_colored = f"{color_code}{company_name}{Style.RESET_ALL}"
                    else:
                        ticker_formatted = f"{Style.BRIGHT}{Fore.WHITE}{ticker}{Style.RESET_ALL}"
                        company_name_colored = company_name

                    # --- Section 8l: Construct and print output ---
                    # (everything up through URL stays the same)
                    output = (
                        f"=== TICKER: {ticker_formatted} - {form_type_extracted} - Item {items_text} ===\n"
                        f"Company: {company_name_colored}\n"
                        f"{extra_info}"
                        f"SEC Time: {updated_datetime_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                        f"Print Time: {print_timestamp_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                        f"Delay: {int(time_diff_seconds)}s\n"
                        f"URL: {doc_url}\n"
                    )

                    # --- NEW: Words section begin ---
                    # find which filter_keywords actually appear in the filing text
                    matched = [kw for kw in filter_keywords if keyword_in_text(text_lower, kw)]
                    highlighted = []
                    for kw in matched:
                        if any(keyword_in_text(kw.lower(), red_kw) for red_kw in red_keywords):
                            highlighted.append(f"{Back.RED}{kw}{Style.RESET_ALL}")
                        elif any(keyword_in_text(kw.lower(), green_kw) for green_kw in green_keywords):
                            highlighted.append(f"{Back.GREEN}{kw}{Style.RESET_ALL}")
                        elif any(keyword_in_text(kw.lower(), orange_kw) for orange_kw in orange_keywords):
                            highlighted.append(f"{Back.YELLOW}{kw}{Style.RESET_ALL}")
                        else:
                            highlighted.append(kw)
                    if highlighted:
                        output += "Words: " + ", ".join(highlighted) + "\n"
                    # --- NEW: Words section end ---

                    # finalize coloring and print exactly as before
                    output = Style.BRIGHT + output + Style.RESET_ALL
                    if orange_found:
                        print(f"{Back.YELLOW + Fore.BLACK}{output}")
                    elif red_found:
                        print(f"{Back.RED + Fore.BLACK}{output}")
                    elif green_found:
                        print(f"{Back.GREEN + Fore.BLACK}{output}")
                    else:
                        print(output)
                        # >>> PLAY THE FORM-SPECIFIC SOUND HERE <<<
                    play_form_sound(form_type_extracted or form_type)

                    webbrowser.open_new_tab(doc_url)
                    try:
                        import winsound
                        # winsound.Beep(1500, 100)
                    except ImportError:
                        pass
                    webbrowser.open_new_tab(doc_url)
                    try:
                        import winsound
                        # winsound.Beep(1500, 100)
                    except ImportError:
                        pass

                    opened_links.add(top_link)
                    last_processed_time = max(last_processed_time, updated_datetime)
                else:
                    last_processed_time = max(last_processed_time, updated_datetime)
                    continue

            # --- Section 8m: Pause and increment request counter ---
            time.sleep(1)
            request_count += 1

        except Exception as e:
            import traceback
            print(f"Error in sec8k(): {e}")
            traceback.print_exc()
            time.sleep(3.03)

    # --- Section 9: Cleanup (unreachable) ---
    session.close()  # Unreachable due to infinite loop




def load_cik_ticker_mapping():
    import requests
    cik_ticker = {}
    company_name_to_ticker = {}

    try:
        url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        headers = {
            'User-Agent': 'Your Name; your.email@example.com',  # Replace with your actual name and email
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'www.sec.gov'
        }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            fields = data['fields']
            cik_idx = fields.index('cik')
            name_idx = fields.index('name')
            ticker_idx = fields.index('ticker')
            exchange_idx = fields.index('exchange')

            for entry in data['data']:
                exchange_field = entry[exchange_idx]
                if not exchange_field:
                    continue
                exchange = exchange_field.strip()
                if exchange not in ['Nasdaq', 'NYSE']:
                    continue

                cik_field = entry[cik_idx]
                name_field = entry[name_idx]
                ticker_field = entry[ticker_idx]

                if cik_field and name_field and ticker_field:
                    cik_str = str(cik_field).lstrip('0')
                    ticker = str(ticker_field).strip().upper()

                    # Skip tickers ending in "W", "WS", or "WT"
                    if ticker.endswith("W") or ticker.endswith("WS") or ticker.endswith("WT"):
                        continue

                    cik_ticker[cik_str] = ticker
                    company_name = str(name_field).strip().upper()
                    company_name_to_ticker[company_name] = ticker
        else:
            print(f"Failed to download CIK-Ticker mapping. Status code: {resp.status_code}")

    except Exception as e:
        print(f"Error loading CIK-Ticker mapping: {e}")

    return cik_ticker, company_name_to_ticker

cik_ticker_mapping, company_name_to_ticker = load_cik_ticker_mapping()



def sec_specific():
    """
    A modified version of your SEC8k function that:
      1. Does not filter by form type or item.
      2. Only processes entries whose CIK (extracted from the title) is in our target list.
         For testing, we monitor SMCI (CIK: "1375365") and Goldman Sachs (CIK: "886982").
    """
    import random
    from datetime import datetime, timezone, time as dt_time, timedelta
    from zoneinfo import ZoneInfo
    import re
    import time
    import webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    import string
    from bs4 import XMLParsedAsHTMLWarning
    import warnings

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    colorama.init(autoreset=True)

    def adjust_url(url):
        # If the URL doesn't start with 'http', assume it's relative and prepend the base URL.
        if not url.startswith('http'):
            return 'https://www.sec.gov' + url
        return url

    def keyword_in_text(text, keyword):
        pattern = re.escape(keyword)
        pattern = pattern.replace(r'\ ', r'\s+')
        regex = re.compile(pattern, re.IGNORECASE)
        return regex.search(text)

    # Create a session exactly like in sec8k
    session = requests.Session()
    ua = random.choice(USER_AGENTS_DATA)['ua']
    my_contact = "John Doe; john.doe@example.com"  # Replace with your actual info
    session.headers.update({
        'User-Agent': f'{ua} ({my_contact})',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.sec.gov',
        'Connection': 'keep-alive'
    })

    # Update target CIKs to include Goldman Sachs (886982) and SMCI (1375365)
    target_ciks = ["1045810","1640147"]

    opened_links = set()
    # For testing, set last_processed_time to 6 hours ago.
    last_processed_time = datetime.now(timezone.utc) - timedelta(hours=6)
    first_run = True

    # Build the unfiltered feed URL
    feed_url = ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&company="
                "&dateb=&owner=include&start=0&count=40&output=atom")

    request_count = 0
    max_requests_per_session = 20

    # Use a more forgiving regex to capture the ending tag
    title_pattern = re.compile(r'^(.*?)\s*-\s*(.*?)\s*\((\d+)\)\s*\((.*?)\)$')
    allowed_tags = {"filer", "reporting", "issuer", "subject", "filed by"}


    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                ua = random.choice(USER_AGENTS_DATA)['ua']
                session.headers.update({
                    'User-Agent': f'{ua} ({my_contact})',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Referer': 'https://www.sec.gov',
                    'Connection': 'keep-alive'
                })
                request_count = 0

            resp = session.get(feed_url, timeout=10)
            if resp.status_code != 200:
                print(f"SEC Specific: Error fetching RSS feed: {resp.status_code} {resp.reason}")
                time.sleep(3.03)
                continue

            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'xml')
            entries = soup.find_all('entry')
            if not entries:
                time.sleep(3.03)
                continue
            else:
                if first_run:
                    print(f"SEC Specific: Found {len(entries)} entries.")
                    first_run = False

            for top_entry in entries:
                link_tag = top_entry.find('link')
                if link_tag and link_tag.get('href'):
                    top_link = link_tag['href']
                else:
                    continue

                updated_datetime_str = top_entry.updated.get_text()
                updated_datetime = datetime.strptime(updated_datetime_str, '%Y-%m-%dT%H:%M:%S%z')
                if updated_datetime <= last_processed_time:
                    continue

                if top_link not in opened_links:
                    print_timestamp = datetime.now(timezone.utc)
                    time_diff_seconds = (print_timestamp - updated_datetime).total_seconds()
                    updated_datetime_est = updated_datetime.astimezone(ZoneInfo('America/New_York'))
                    print_timestamp_est = print_timestamp.astimezone(ZoneInfo('America/New_York'))
                    # Use strip() to remove extra whitespace
                    title_text = top_entry.title.get_text(strip=True)

                    match = title_pattern.match(title_text)
                    if match:
                        form_type_extracted = match.group(1).strip()
                        company_name = match.group(2).strip()
                        cik_number = match.group(3).strip().lstrip('0')
                        ending_tag = match.group(4).strip().lower()
                        # Instead of printing a debug message, just skip silently if not allowed:
                        if ending_tag not in allowed_tags:
                            continue
                    else:
                        # Skip entries that don’t match without printing anything:
                        continue

                    # Debug: show which CIK we extracted
                    # print(f"DEBUG: Extracted CIK: {cik_number}")

                    if cik_number not in target_ciks:
                        continue

                    if form_type_extracted == "4":
                        # For Form 4 filings, use the company name as ticker (or mark as "N/A")
                        ticker = company_name.upper()
                    else:
                        if cik_number not in cik_ticker_mapping:
                            print(f"CIK {cik_number} not in mapping; skipping entry.")
                            last_processed_time = max(last_processed_time, updated_datetime)
                            continue
                        ticker = cik_ticker_mapping[cik_number]

                    ticker = cik_ticker_mapping[cik_number]
                    page_resp = session.get(top_link, timeout=10)
                    if page_resp.status_code != 200:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    page_soup = BeautifulSoup(page_resp.content, 'lxml')
                    table = page_soup.find('table', class_='tableFile')
                    if not table:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    rows = table.find_all('tr')
                    doc_url = None
                    if form_type.startswith("13F") and cik_number == "1045810":
                        info_row = table.find('tr', lambda r: r.find('td', string=re.compile(r'\bINFORMATION TABLE\b')))
                        if info_row:
                            href = info_row.find('a', href=True)['href']
                            # the link text is "information_table.html"
                            doc_url = 'https://www.sec.gov' + href
                    else:
                        # <<< ORIGINAL BEHAVIOR for all other filings
                        for row in table.find_all('tr')[1:]:
                            cols = row.find_all('td')
                            if len(cols) >= 4:
                                doc_type = cols[3].get_text(strip=True)
                                if doc_type == form_type:
                                    # prefer XML or TXT as before
                                    link_candidates = [a['href'] for a in cols[2].find_all('a', href=True)]
                                    xml_link = next((l for l in link_candidates if l.endswith('.xml')), None)
                                    txt_link = next((l for l in link_candidates if l.endswith('.txt')), None)
                                    chosen = xml_link or txt_link
                                    if chosen:
                                        doc_url = 'https://www.sec.gov' + chosen
                                    break

                    if not doc_url:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    doc_url = adjust_url(doc_url)
                    doc_resp = session.get(doc_url, timeout=10)
                    if doc_resp.status_code != 200:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue

                    doc_content = doc_resp.content.decode('utf-8', errors='ignore')
                    doc_content = re.sub(r'\sxmlns(:\w+)?="[^"]+"', '', doc_content)
                    doc_content = re.sub(r'</?(\w+):', '<', doc_content)
                    soup_doc = BeautifulSoup(doc_content, 'lxml')
                    for script_or_style in soup_doc(['script', 'style']):
                        script_or_style.decompose()
                    text = soup_doc.get_text(separator=' ', strip=True)
                    text = ''.join(filter(lambda x: x in string.printable, text))
                    text = re.sub(r'\s+', ' ', text)
                    ticker_formatted = f"{Style.BRIGHT}{ticker}{Style.RESET_ALL}"
                    output = (f"=== TICKER: {ticker_formatted} - {form_type_extracted} ===\n"
                              f"Company: {company_name}\n"
                              f"SEC Time: {updated_datetime_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Print Time: {print_timestamp_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Delay: {int(time_diff_seconds)}s\n"
                              f"URL: {doc_url}")
                    print(output)
                    webbrowser.open_new_tab(doc_url)
                    winsound.Beep(1500, 100)
                    opened_links.add(top_link)
                    last_processed_time = max(last_processed_time, updated_datetime)
                    break  # Process one new filing per loop iteration
                else:
                    last_processed_time = max(last_processed_time, updated_datetime)
                    continue

            time.sleep(1)
            request_count += 1
        except Exception as e:
            import traceback
            print(f"Error in sec_specific(): {e}")
            traceback.print_exc()
            time.sleep(3.03)

    session.close()  # Unreachable due to infinite loop


# if __name__ == "__main__":
#     sec_specific()




def tiktok_court():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, timezone
    import re
    import time
    import webbrowser
    import colorama
    from colorama import Fore, Back, Style
    import string
    from bs4 import XMLParsedAsHTMLWarning
    import warnings

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

    colorama.init(autoreset=True)

    # RSS feed for TikTok Inc. v. Merrick Garland
    feed_url = "https://www.courtlistener.com/docket/68506893/feed/"

    # Headers for the request
    headers = {
        'User-Agent': 'Your Name; your.email@example.com',  # Replace with your actual name and email
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    # Track the last processed time so we don't re-process old entries
    last_processed_time = datetime.now(timezone.utc)

    # Helper function to parse published time
    def parse_published_time(dt_str):
        # Example: 2024-09-27T00:00:00-07:00
        # Use %z to parse the timezone offset
        return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S%z")

    while True:
        try:
            # Fetch the RSS feed
            resp = requests.get(feed_url, headers=headers)
            if resp.status_code != 200:
                print(f"TiKTok Court: Error fetching feed: {resp.status_code} {resp.reason}")
                time.sleep(5)
                continue

            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'xml')  # Parse as XML
            entries = soup.find_all('entry')
            if not entries:
                # No entries found
                time.sleep(5)
                continue

            # Process each entry
            # We'll sort entries by published time just in case
            # (Atom feeds usually sorted by updated time, but we'll be careful)
            # Extract (entry, published_datetime) pairs
            entry_times = []
            for e in entries:
                pub_str = e.find('published').get_text()
                pub_dt = parse_published_time(pub_str)
                entry_times.append((e, pub_dt))
            # Sort by published time ascending
            entry_times.sort(key=lambda x: x[1])

            # Now iterate through sorted entries, only print those newer than last_processed_time
            for entry, pub_dt in entry_times:
                if pub_dt <= last_processed_time:
                    # Already processed or old entry
                    continue

                # This is a new entry
                title = entry.find('title').get_text(strip=True)
                link_tag = entry.find('link', {'rel': 'alternate'})
                entry_url = link_tag['href'] if link_tag else None
                summary_tag = entry.find('summary')
                summary_text = summary_tag.get_text(" ", strip=True) if summary_tag else ""

                # Remove non-printable characters
                summary_text = ''.join(filter(lambda x: x in string.printable, summary_text))
                # Clean up whitespace in summary
                summary_text = re.sub(r'\s+', ' ', summary_text)

                # Highlight the entry
                # We'll just use yellow background as we did for orange in sec8k
                color_code = Back.YELLOW + Fore.BLACK
                output = (f"=== NEW COURT ENTRY ===\n"
                          f"Title: {title}\n"
                          f"Published: {pub_dt.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
                          f"Summary: {summary_text}\n"
                          f"URL: {entry_url}")
                output = Style.BRIGHT + output + Style.RESET_ALL

                if color_code:
                    print(f"{color_code}{output}")
                else:
                    print(output)

                # Open the link if available
                if entry_url:
                    webbrowser.open_new_tab(entry_url)

                # Update last_processed_time to this entry's time
                last_processed_time = max(last_processed_time, pub_dt)

            # Sleep before checking again
            time.sleep(10)
        except Exception as e:
            import traceback
            print(f"Error in tiktok_court(): {e}")
            traceback.print_exc()
            time.sleep(5)
def citron():
    # Initialize the session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=4,  # Total number of retries
        backoff_factor=1,  # Exponential backoff factor (wait = {backoff factor} * (2 ** (retry number)))
        status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry
        allowed_methods=["HEAD", "GET", "OPTIONS"]  # HTTP methods to retry
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Initial headers with User-Agent rotation
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    })

    # *** To bypass potential IP bans (as seen with Iceberg and Spruce), consider using a proxy.
    # For example:
    # proxies = {
    #     "http": "http://your_proxy_address:port",
    #     "https": "http://your_proxy_address:port",
    # }
    # session.proxies.update(proxies)
    # *******************************************

    request_count = 0
    max_requests_per_session = 4  # Adjust as needed

    while True:
        try:
            # Refresh session after reaching max requests
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                })
                request_count = 0
                # print("Citron: Session refreshed.")

            url = "https://citronresearch.com/"
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"Citron: Received status code {resp.status_code}")
                time.sleep(random.uniform(4.6, 6.4))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            # NEW: Look for a link (anchor tag) that points to a PDF in the uploads folder.
            find_link = soup.find("a", href=re.compile(r'/wp-content/uploads/.*\.pdf$', re.IGNORECASE))
            if not find_link:
                print("Citron: Could not find PDF link in the page.")
                time.sleep(random.uniform(4.6, 6.4))
                continue

            citron_headline[1] = find_link.text.strip()
            article_url = find_link['href']
            if not article_url.startswith('http'):
                article_url = 'https://citronresearch.com' + article_url

            now = datetime.now().time()

            if citron_headline[0] != citron_headline[1]:
                ticker = None
                # Extract ticker using regex from the headline text (expecting it in parentheses)
                match = re.search(r'\(([^)]+)\)', citron_headline[1])
                if match:
                    ticker = match.group(1).strip().upper()

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Citron: Could not extract ticker from headline '{citron_headline[1]}'.")
                    # Optionally, skip further actions if ticker is not found
                    # continue

                print(f"{now} \t Citron \t {citron_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            citron_headline[0] = citron_headline[1]
            time.sleep(random.uniform(4.6, 6.4))
            request_count += 1

        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError) as e:
            print(f"Connection error in citron(): {e}")
            time.sleep(random.uniform(4.6, 6.4))
            continue  # Continue the loop after handling the error

        except Exception as e:
            import traceback
            print(f"Error in citron(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(4.6, 6.4))
            continue  # Continue the loop after handling the error

    session.close()  # This line is unreachable due to the infinite loop

#
# def bear_cave_debug():
#     url = "https://thebearcave.substack.com/"
#     session = requests.Session()
#     session.headers.update({
#         'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
#         'Referer': 'https://google.com',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     })
#
#     try:
#         resp = session.get(url, timeout=15)
#         print("HTTP Status Code:", resp.status_code)
#         if resp.status_code != 200:
#             print(f"Error: Received status code {resp.status_code}")
#             return
#
#         # Print a snippet of the HTML to check for our expected element
#         html_content = resp.text
#         # You can save this to a file if the HTML is very long:
#         # with open("debug_bear_cave.html", "w", encoding="utf-8") as f:
#         #     f.write(html_content)
#         snippet = html_content[:1000]  # first 1000 characters
#         print("HTML Snippet:\n", snippet)
#
#         # Check if the expected attribute exists in the HTML
#         if 'data-testid="post-preview-title"' not in html_content:
#             print("Debug: 'data-testid=\"post-preview-title\"' not found in the static HTML.")
#         else:
#             print("Debug: Found 'data-testid=\"post-preview-title\"' in the HTML.")
#
#         # Proceed with BeautifulSoup parsing
#         soup = BeautifulSoup(html_content, 'lxml')
#         title_link = soup.find("a", {"data-testid": "post-preview-title"})
#         if not title_link:
#             print("Bear Cave: Could not find post preview title link.")
#         else:
#             print("Bear Cave: Found post preview title link!")
#             print("Link href:", title_link.get("href"))
#             # Optionally, print the full tag:
#             print("Full tag:", title_link)
#     except Exception as e:
#         print("Error in bear_cave_debug():", e)
#
# if __name__ == "__main__":
#     bear_cave_debug()
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# def bear_cave_selenium():
#     # Set up headless Chrome
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#
#     # You may need to adjust the path to your chromedriver
#     driver = webdriver.Chrome(options=chrome_options)
#
#     url = "https://thebearcave.substack.com/"
#     driver.get(url)
#
#     # Give time for the page to load dynamic content
#     time.sleep(5)
#
#     # Get the full HTML after JavaScript has run
#     html = driver.page_source
#     print("Rendered HTML snippet:\n", html[:1000])
#
#     try:
#         # Now try to find the element with data-testid "post-preview-title"
#         element = driver.find_element("css selector", 'a[data-testid="post-preview-title"]')
#         print("Found post preview title link!")
#         print("Link href:", element.get_attribute("href"))
#     except Exception as e:
#         print("Bear Cave: Could not find post preview title link.")
#         print("Error:", e)
#
#     driver.quit()
#
#
# if __name__ == "__main__":
#     bear_cave_selenium()
# def iceberg():
#     global iceberg_headline
#     iceberg_headline = [None, None]
#     session = requests.Session()
#     retry_strategy = Retry(
#         total=5,
#         backoff_factor=1,
#         status_forcelist=[429, 500, 502, 503, 504],
#         allowed_methods=["HEAD", "GET", "OPTIONS"]
#     )
#     adapter = HTTPAdapter(max_retries=retry_strategy)
#     session.mount("https://", adapter)
#     session.mount("http://", adapter)
#     session.headers.update({
#         'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
#         'Referer': 'https://google.com',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Connection': 'keep-alive',
#         'Cache-Control': 'no-cache',
#         'Pragma': 'no-cache'
#     })
#     request_count = 0
#     max_requests_per_session = 10
#     while True:
#         try:
#             if request_count >= max_requests_per_session:
#                 session.close()
#                 session = requests.Session()
#                 session.mount("https://", adapter)
#                 session.mount("http://", adapter)
#                 session.headers.update({
#                     'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
#                     'Referer': 'https://google.com',
#                     'Accept-Language': 'en-US,en;q=0.9',
#                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#                     'Connection': 'keep-alive',
#                     'Cache-Control': 'no-cache',
#                     'Pragma': 'no-cache'
#                 })
#                 request_count = 0
#             # --- Update proxies ---
#             if PROXIES:
#                 session.proxies = random.choice(PROXIES)
#             else:
#                 print("Warning: No proxies available; proceeding without proxy.")
#             url = "https://iceberg-research.com/"
#             resp = session.get(url, timeout=15)
#             if resp.status_code != 200:
#                 print(f"Iceberg: Received status code {resp.status_code}")
#                 time.sleep(random.uniform(3.7, 5.65))
#                 continue
#             soup = BeautifulSoup(resp.content, 'lxml')
#             post = soup.find('div', class_='xpro-post-grid-content')
#             if not post:
#                 print("Iceberg: Could not find 'div' with class 'xpro-post-grid-content'.")
#                 time.sleep(random.uniform(3.7, 5.65))
#                 continue
#             link_tag = post.find('a', href=True)
#             if not link_tag:
#                 print("Iceberg: Could not find 'a' tag with href in the post content.")
#                 time.sleep(random.uniform(3.7, 5.65))
#                 continue
#             article_url = link_tag['href']
#             if not article_url.startswith('http'):
#                 article_url = 'https://iceberg-research.com' + article_url
#             headline_tag = link_tag.find('h2', class_='xpro-post-grid-title')
#             if not headline_tag:
#                 print("Iceberg: Could not find 'h2' tag with class 'xpro-post-grid-title'.")
#                 time.sleep(random.uniform(3.7, 5.65))
#                 continue
#             headline = headline_tag.text.strip()
#             iceberg_headline[1] = headline
#             ticker_match = re.search(r'\$([A-Za-z0-9]+)', headline)
#             ticker = ticker_match.group(1).upper() if ticker_match else None
#             now = datetime.now().time()
#             if iceberg_headline[0] != iceberg_headline[1]:
#                 if ticker:
#                     formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}${ticker}{Style.RESET_ALL}"
#                     print(formatted)
#                     print(formatted)
#                     print(formatted)
#                 else:
#                     print(f"Iceberg: Could not extract ticker from headline '{iceberg_headline[1]}'.")
#                 print(f"{now} \t Iceberg \t {iceberg_headline[1]}")
#                 print("Article URL:", article_url)
#                 webbrowser.open_new_tab(article_url)
#                 winsound.Beep(1500, 100)
#             iceberg_headline[0] = iceberg_headline[1]
#             time.sleep(random.uniform(3.7, 5.65))
#             request_count += 1
#         except (requests.exceptions.ConnectionError,
#                 requests.exceptions.Timeout,
#                 requests.exceptions.HTTPError) as e:
#             print(f"Iceberg: Connection error: {e}")
#             time.sleep(random.uniform(3.7, 5.65))
#             continue
#         except Exception as e:
#             print(f"Iceberg: Error: {e}")
#             traceback.print_exc()
#             time.sleep(random.uniform(3.7, 5.65))
#             continue
#     session.close()


def statnews():
    while True:
        try:
            resp = requests.get("https://www.statnews.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            find = soup.find("item")
            if not find:
                print("Statnews: Could not find 'item' tag.")
                time.sleep(3.03)
                continue
            statnews_headline[1] = find.title.text.strip()
            link = find.link.text.strip()
            now = datetime.now().time()
            if statnews_headline[0] != statnews_headline[1]:
                print(now, "\t", "Statnews", "\t", statnews_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
            statnews_headline[0] = statnews_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in statnews():", e)
            time.sleep(3.03)
morpheus_headline = [0]*2

def morpheus():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo
    import time
    import webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    import random
    import re
    import traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    # Initialize colorama for terminal output
    colorama.init(autoreset=True)

    # Create a session with a random user-agent and attach a retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.morpheus-research.com/',
        'Connection': 'keep-alive'
    })

    # Global variable to store the last processed headline
    try:
        morpheus_headline
    except NameError:
        morpheus_headline = ["", ""]

    # The target website URL for Morpheus Research
    base_url = "https://www.morpheus-research.com/"

    while True:
        try:
            # Get the base page with increased timeout
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Morpheus: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')

            # Look for the top article – first try an article with class "gh-latest"
            article = soup.find("article", class_="gh-latest")
            if not article:
                # Fallback: look in the "gh-feed" container for a post preview
                feed = soup.find("div", class_="gh-feed")
                if feed:
                    article = feed.find("div", class_="post-preview")
            if not article:
                time.sleep(random.uniform(3.5, 4.25))
                continue

            a_tag = article.find("a", href=True)
            if not a_tag:
                print("Morpheus: Could not find the report link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Get the report title from the <h2> element with class "gh-article-title"
            h2_tag = a_tag.find("h2", class_="gh-article-title")
            if not h2_tag:
                print("Morpheus: Could not find the report title.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            morpheus_headline[1] = h2_tag.get_text(strip=True)
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = base_url.rstrip("/") + "/" + article_url.lstrip("/")

            now = datetime.now(ZoneInfo("America/New_York"))
            if morpheus_headline[0] != morpheus_headline[1]:
                ticker = None

                # --- New Ticker Extraction from Article Content ---
                try:
                    art_resp = session.get(article_url, timeout=15)
                    if art_resp.status_code == 200:
                        art_soup = BeautifulSoup(art_resp.content, 'lxml')
                        # Look for a <p> containing "Summary" (case-insensitive)
                        summary_p = art_soup.find("p", string=re.compile("Summary", re.I))
                        if summary_p:
                            # Instead of expecting an immediate <li>, get the next sibling that is a <ul>
                            ul_tag = summary_p.find_next_sibling("ul")
                            if ul_tag:
                                li_tag = ul_tag.find("li")
                                if li_tag:
                                    li_text = li_tag.get_text(strip=True)
                                    # Use a regex to capture the ticker from a string like "(NYSE: SEI)"
                                    match_ticker = re.search(r'\((?:NYSE|Nasdaq):\s*([A-Z]+)\)', li_text)
                                    if match_ticker:
                                        ticker = match_ticker.group(1)
                except Exception as ex:
                    print("Error extracting ticker from article content:", ex)

                # --- Fallback: Ticker Matching from URL ---
                if not ticker:
                    parts = article_url.strip("/").split("/")
                    brand_slug = parts[-1] if parts else ""
                    brand_slug_upper = brand_slug.upper()
                    ticker = None
                    all_tickers = set(company_name_to_ticker.values())
                    if brand_slug_upper in all_tickers:
                        ticker = brand_slug_upper
                    else:
                        expansions = [
                            " INC.", " INC", " INCORPORATED",
                            " CORP.", " CORP", " CORPORATION",
                            " LTD.", " LTD", " PLC", " SA",
                            ""
                        ]
                        for exp in expansions:
                            candidate_name = (brand_slug_upper + exp).strip()
                            if candidate_name in company_name_to_ticker:
                                ticker = company_name_to_ticker[candidate_name]
                                break
                        if not ticker:
                            for comp_name, comp_tck in company_name_to_ticker.items():
                                if brand_slug_upper in comp_name:
                                    print(f"DEBUG: brand_slug_upper={brand_slug_upper} found inside => {comp_name}")
                                    ticker = comp_tck
                                    break

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Morpheus: Could not match ticker from URL or article content for '{article_url}'.")

                print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Morpheus \t {morpheus_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

            morpheus_headline[0] = morpheus_headline[1]
            time.sleep(random.uniform(3.5, 4.25))
        except Exception as e:
            print("Error in morpheus():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))


manatee_headline = ["", ""]  # keep same pattern as morpheus

def manatee():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import webbrowser
    import colorama
    from colorama import Fore, Back, Style
    import random
    import re
    import traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    # init colors
    colorama.init(autoreset=True)

    # session + retries
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET","HEAD","OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent'      : ua,
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'en-US,en;q=0.9',
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer'         : 'https://manateeresearch.com/',
        'Connection'      : 'keep-alive'
    })

    # ensure the headline buffer exists
    try:
        manatee_headline
    except NameError:
        manatee_headline = ["", ""]

    base_url = "https://manateeresearch.com/"

    # helpers
    def abs_url(href: str) -> str:
        if not href:
            return ""
        if href.startswith("http://") or href.startswith("https://"):
            return href
        return base_url.rstrip("/") + "/" + href.lstrip("/")

    # robust ticker extraction from article HTML
    def extract_ticker_from_article(html_text: str) -> str | None:
        # 1) Try explicit exchange patterns
        pat_exch = re.compile(
            r'\b(?:NYSE|NASDAQ|Nasdaq|NYSEAMER|AMEX|ASX|LSE|TSX):\s*([A-Z][A-Z0-9.\-]{0,5})\b'
        )
        m = pat_exch.search(html_text)
        if m:
            return m.group(1)

        # 2) Try parentheses patterns like "(TICKER)" if it looks stocky
        pat_paren = re.compile(r'\(([A-Z][A-Z0-9.\-]{0,5})\)')
        for m in pat_paren.finditer(html_text):
            cand = m.group(1)
            if 1 <= len(cand) <= 6:
                return cand

        # 3) Try $TICK pattern
        m = re.search(r'\$([A-Z][A-Z0-9.\-]{0,5})\b', html_text)
        if m:
            return m.group(1)

        return None

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Manatee: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")

            # Try several WordPress-ish selectors in order of specificity.
            a_tag = None
            title_text = None

            # A) Anything inside the “Reports” section following the Reports heading
            reports_h2 = soup.find("h2", id=re.compile(r"h-reports", re.I))
            if reports_h2:
                # look for the first post link after Reports heading
                following_links = reports_h2.find_all_next("a", href=True, limit=10)
                for a in following_links:
                    href = a["href"]
                    # skip nav/anchor/mail links
                    if href.startswith("#") or href.startswith("mailto:"):
                        continue
                    # prefer post links (WordPress often uses /YYYY/MM/DD/slug/ or /?p=ID)
                    if re.search(r'/\d{4}/\d{2}/\d{2}/', href) or re.search(r'[?&]p=\d+', href):
                        a_tag = a
                        break

            # B) Typical core blocks: wp-block-post-title
            if not a_tag:
                a_tag = soup.select_one("a.wp-block-post-title[href]")

            # C) Classic theme: h2.entry-title > a
            if not a_tag:
                a_tag = soup.select_one("h2.entry-title a[href]")

            # D) Fallback: any article > a[href]
            if not a_tag:
                art = soup.find("article")
                if art:
                    a_tag = art.find("a", href=True)

            if not a_tag:
                # Site is still empty or markup changed
                time.sleep(random.uniform(3.5, 4.25))
                continue

            title_text = a_tag.get_text(strip=True) or "Manatee Research"
            article_url = abs_url(a_tag.get("href"))

            # set current headline
            manatee_headline[1] = title_text

            # only trigger on change
            if manatee_headline[0] != manatee_headline[1]:
                ticker = None

                # Try to pull ticker from the article page
                try:
                    art_resp = session.get(article_url, timeout=15)
                    if art_resp.status_code == 200:
                        art_soup = BeautifulSoup(art_resp.content, "lxml")
                        # Plain text from the article content container (common WP blocks)
                        content = []
                        for sel in [
                            "div.entry-content",
                            "div.wp-block-post-content",
                            "main",
                            "article"
                        ]:
                            node = art_soup.select_one(sel)
                            if node:
                                content.append(node.get_text(" ", strip=True))
                        if not content:
                            content.append(art_soup.get_text(" ", strip=True))
                        big_text = " ".join(content)
                        ticker = extract_ticker_from_article(big_text)
                except Exception as ex:
                    print("Manatee: error extracting ticker from article:", ex)

                # Fallback: infer from URL slug vs your company_name_to_ticker map
                if not ticker:
                    parts = article_url.strip("/").split("/")
                    slug = next((p for p in reversed(parts) if p and p != "amp"), "")
                    brand_slug_upper = slug.upper().replace("-", " ").replace("_", " ")
                    all_tickers = set(company_name_to_ticker.values())

                    if brand_slug_upper in all_tickers:
                        ticker = brand_slug_upper
                    else:
                        expansions = [
                            " INC.", " INC", " INCORPORATED",
                            " CORP.", " CORP", " CORPORATION",
                            " LTD.", " LTD", " PLC", " SA",
                            ""
                        ]
                        found = False
                        for exp in expansions:
                            candidate_name = (brand_slug_upper + exp).strip()
                            if candidate_name in company_name_to_ticker:
                                ticker = company_name_to_ticker[candidate_name]
                                found = True
                                break
                        if not found:
                            for comp_name, comp_tck in company_name_to_ticker.items():
                                if brand_slug_upper and brand_slug_upper in comp_name:
                                    ticker = comp_tck
                                    break

                # Print ticker loud if found
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted); print(formatted); print(formatted)
                else:
                    print(f"Manatee: Could not match ticker for '{article_url}'.")

                now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")
                print(f"{now}\tManatee\t{manatee_headline[1]}")
                print("Article URL:", article_url)

                # open + sound
                try:
                    webbrowser.open_new_tab(article_url)
                except Exception:
                    pass

                try:
                    # If you’ve wired your soundboard: play “manatee”
                    SOUNDS.play("manatee", stop_current=True)
                except Exception:
                    # plain beep fallback
                    try:
                        import winsound
                        winsound.Beep(1500, 100)
                    except Exception:
                        print("\a")  # terminal bell

            # shift the window
            manatee_headline[0] = manatee_headline[1]
            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in manatee():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))


# To run the function, simply call:
#
#

def hindenburg():
    import random
    session = requests.Session()
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})  # Persistent session headers

    while True:
        try:
            resp = session.get("https://hindenburgresearch.com/")
            if resp.status_code != 200:
                print(f"Hindenburg: Received status code {resp.status_code}")
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find("h1")
            if not find:
                print("Hindenburg: Could not find the h1 tag.")
                time.sleep(3.03)
                continue

            find2 = find.find("a", href=True)
            if not find2:
                print("Hindenburg: Could not find the a tag within h1.")
                time.sleep(3.03)
                continue

            hindenburg_headline[1] = find2.text.strip()
            article_url = find2['href']
            if not article_url.startswith('http'):
                article_url = 'https://hindenburgresearch.com' + article_url

            now = datetime.now().time()
            if hindenburg_headline[0] != hindenburg_headline[1]:
                parts = article_url.strip('/').split('/')
                brand_slug = parts[-1] if parts else ""
                brand_slug_upper = brand_slug.upper()

                # Ticker matching logic
                ticker = None
                all_tickers = set(company_name_to_ticker.values())
                if brand_slug_upper in all_tickers:
                    ticker = brand_slug_upper
                else:
                    expansions = [
                        " INC.", " INC", " INCORPORATED",
                        " CORP.", " CORP", " CORPORATION",
                        " LTD.", " LTD", " PLC", " SA",
                        ""
                    ]
                    for exp in expansions:
                        candidate_name = (brand_slug_upper + exp).strip()
                        if candidate_name in company_name_to_ticker:
                            ticker = company_name_to_ticker[candidate_name]
                            break

                    if not ticker:
                        for comp_name, comp_tck in company_name_to_ticker.items():
                            if brand_slug_upper in comp_name:
                                print(f"DEBUG: brand_slug_upper={brand_slug_upper} found inside => {comp_name}")
                                ticker = comp_tck
                                break

                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Hindenburg: Could not match '{brand_slug}' to a known ticker. (No expansions or substring match)")

                print(now, "\t", "Hindenburg", "\t", hindenburg_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            hindenburg_headline[0] = hindenburg_headline[1]
            time.sleep(3.03)

        except Exception as e:
            print("Error in hindenburg():", e)
            time.sleep(3.03)


# Initialize headline tracking list for Wolfpack
wolfpack_headline = ["", ""]

def wolfpack():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 5  # Adjust as needed
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    })

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                })
                request_count = 0

            url = "https://www.wolfpackresearch.com/items"
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"Wolfpack: Received status code {resp.status_code}")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find('div', class_='comp-ls2evfpq')
            if not find:
                print("Wolfpack: Could not find 'div' with class 'comp-ls2evfpq'.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            find_link = find.find('a', href=True)
            if not find_link:
                print("Wolfpack: Could not find 'a' tag with href.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            article_url = find_link['href']
            if not article_url.startswith('http'):
                article_url = 'https://www.wolfpackresearch.com' + article_url

            # Fetch article page to get the ticker
            page_resp = session.get(article_url, timeout=10)
            if page_resp.status_code != 200:
                print("Wolfpack: Could not fetch article page.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            page_text = page_resp.text
            ticker = None
            match = re.search(r'\((?:Nasdaq|NYSE):\s*([A-Za-z0-9]+)\)', page_text, re.IGNORECASE)
            if match:
                ticker = match.group(1).upper()
            else:
                short_match = re.search(r'Wolfpack\s+is\s+short\s+([A-Za-z0-9]+)', page_text, re.IGNORECASE)
                if short_match:
                    ticker = short_match.group(1).upper()

            wolfpack_headline[1] = article_url
            now = datetime.now().time()

            if wolfpack_headline[0] != wolfpack_headline[1]:
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Wolfpack: Could not extract ticker from article '{article_url}'.")

                print(f"{now} \t Wolfpack \t {wolfpack_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

            wolfpack_headline[0] = wolfpack_headline[1]
            time.sleep(random.uniform(2.5, 3.25))
            request_count += 1

        except Exception as e:
            print("Error in wolfpack():", e)
            time.sleep(random.uniform(2.5, 3.25))

    session.close()  # This line is unreachable due to the infinite loop





def usps():
    while True:
        try:
            resp = requests.get("https://about.usps.com/news/latestnews.rss", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            find = soup.find("item")
            if not find:
                print("USPS: Could not find 'item' tag.")
                time.sleep(3.03)
                continue
            usps_headline[1] = find.title.text.strip()
            link = find.link.text.strip()
            now = datetime.now().time()
            if usps_headline[0] != usps_headline[1]:
                print(now, "\t", "USPS", "\t", usps_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            usps_headline[0] = usps_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in usps():", e)
            time.sleep(3.03)

def cdc():
    while True:
        try:
            resp = requests.get("https://tools.cdc.gov/api/v2/resources/media/132608.rss", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            find = soup.find("item")
            if not find:
                print("CDC: Could not find 'item' tag.")
                time.sleep(3.03)
                continue
            cdc_headline[1] = find.title.text.strip()
            link = find.link.text.strip()
            now = datetime.now().time()
            if cdc_headline[0] != cdc_headline[1]:
                print(now, "\t", "CDC", "\t", cdc_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)
            cdc_headline[0] = cdc_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in cdc():", e)
            time.sleep(3.03)

def fda():
    while True:
        try:
            resp = requests.get(
                "https://www.fda.gov/advisory-committees/advisory-committee-calendar",
                headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find("tbody")
            if not find:
                print("FDA: Could not find 'tbody' tag.")
                time.sleep(3.03)
                continue
            find2 = find.find("tr")
            if not find2:
                print("FDA: Could not find 'tr' tag within 'tbody'.")
                time.sleep(3.03)
                continue
            find3 = find2.find("td")
            if not find3:
                print("FDA: Could not find 'td' tag within 'tr'.")
                time.sleep(3.03)
                continue
            fda_headline[1] = find3.text.strip()
            link_tag = find2.find("a", href=True)
            if not link_tag:
                print("FDA: Could not find 'a' tag with href.")
                time.sleep(3.03)
                continue
            article_url = "https://www.fda.gov" + link_tag['href']
            now = datetime.now().time()
            if fda_headline[0] != fda_headline[1]:
                print(now, "\t", "FDA", "\t", fda_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
            fda_headline[0] = fda_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in fda():", e)
            time.sleep(3.03)

def fda2():
    while True:
        try:
            resp = requests.get(
                "https://search.fda.gov/search?utf8=%E2%9C%93&affiliate=fda1&query=761178&commit=Search",
                headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find(class_="title")
            if not find:
                print("FDA2: Could not find 'title' class.")
                time.sleep(3.03)
                continue
            fda2_headline[1] = find.text.strip()
            link_tag = find.find("a", href=True)
            if not link_tag:
                print("FDA2: Could not find 'a' tag with href.")
                time.sleep(3.03)
                continue
            article_url = link_tag['href']
            now = datetime.now().time()
            if fda2_headline[0] != fda2_headline[1]:
                print(now, "\t", "FDA2", "\t", fda2_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
            fda2_headline[0] = fda2_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in fda2():", e)
            time.sleep(3.03)

def bleepcomp():
    while True:
        try:
            resp = requests.get("https://www.bleepingcomputer.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            find = soup.find("item")
            if not find:
                print("Bleeping Computer: Could not find 'item' tag.")
                time.sleep(3.03)
                continue
            bleepcomp_headline[1] = find.title.text.strip()
            link = find.link.text.strip()
            now = datetime.now().time()
            if bleepcomp_headline[0] != bleepcomp_headline[1]:
                print(now, "\t", "Bleeping Computer", "\t", bleepcomp_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
            bleepcomp_headline[0] = bleepcomp_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in bleepcomp():", e)
            time.sleep(3.03)
def hntrbrk():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import webbrowser
    import winsound
    import colorama
    from colorama import Fore, Back, Style
    import random
    import re
    import traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    colorama.init(autoreset=True)

    # Initialize session and attach a retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,              # Total number of retries
        backoff_factor=1,     # Exponential backoff factor: wait = 1 * (2 ** retry_number)
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Update session headers
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'application/rss+xml,application/xml;q=0.9,*/*;q=0.8',
    })

    request_count = 0
    max_requests_per_session = 5 # Adjust as needed

    # Global headline storage (assumed defined globally; otherwise, define here)
    try:
        hntrbrk_headline
    except NameError:
        hntrbrk_headline = ["", ""]

    url = "https://hntrbrk.com/feed/"

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'application/rss+xml,application/xml;q=0.9,*/*;q=0.8',
                })
                request_count = 0

            # Increase the timeout to 15 seconds for slower responses
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"Hunterbrook: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.1, 4.34))
                continue

            soup = BeautifulSoup(resp.content, 'lxml-xml')
            results = soup.find("item")
            if not results:
                print("Hunterbrook: Could not find 'item' tag.")
                time.sleep(random.uniform(3.1, 4.34))
                continue

            hntrbrk_headline[1] = results.title.string.strip()
            link = results.link.string.strip()
            find = results.find("description")
            if not find:
                print("Hunterbrook: Could not find 'description' tag.")
                time.sleep(random.uniform(3.1, 4.34))
                continue

            desc = find.string.strip()
            now = datetime.now(ZoneInfo("America/New_York")).time()

            if hntrbrk_headline[0] != hntrbrk_headline[1]:
                # Use regex on the description text to extract the ticker following a '$'
                m = re.search(r'\$([A-Za-z0-9]+)\b', desc)
                ticker = m.group(1).upper() if m else None
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Hunterbrook: Could not extract ticker from description. Link: '{link}'.")

                print(f"{now} \t Hunterbrook \t {hntrbrk_headline[1]}")
                print("Description:", desc)
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)

            hntrbrk_headline[0] = hntrbrk_headline[1]
            time.sleep(random.uniform(3.1, 4.34))
            request_count += 1

        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError,
                requests.exceptions.ChunkedEncodingError) as e:
            print(f"Connection error in hntrbrk(): {e}")
            time.sleep(random.uniform(3.1, 4.34))
            continue

        except Exception as e:
            print(f"Error in hntrbrk(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(3.1, 4.34))
            continue

    session.close()  # Unreachable due to infinite loop



lauren_balik_headline = ["", ""]

# def lauren_balik():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://medium.com/feed/@laurengreerbalik"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"Lauren Balik: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("Lauren Balik: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             if not title_tag or not link_tag:
#                 print("Lauren Balik: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             lauren_balik_headline[1] = title
#             now = datetime.now().time()
#             if lauren_balik_headline[0] != lauren_balik_headline[1]:
#                 print(now, "\t", "Lauren Balik", "\t", lauren_balik_headline[1])
#                 print("Article URL:", link)
#                 webbrowser.open_new_tab(link)
#                     winsound.Beep(1500, 100)
#                 winsound.Beep(1500, 100)
#                 winsound.Beep(1500, 100)
#             lauren_balik_headline[0] = lauren_balik_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in lauren_balik():", e)
#             time.sleep(5)
ming_chi_kuo_headline = ["", ""]
def ming_chi_kuo():
    while True:
        try:
            import random
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://medium.com/feed/@mingchikuo"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Ming Chi Kuo: Received status code {resp.status_code}")
                time.sleep(random.uniform(2.5, 3.25))
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("Ming Chi Kuo: Could not find 'item' tag.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            if not title_tag or not link_tag:
                print("Ming Chi Kuo: Could not find 'title' or 'link' tag.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            ming_chi_kuo_headline[1] = title
            now = datetime.now().time()
            if ming_chi_kuo_headline[0] != ming_chi_kuo_headline[1]:
                print(now, "\t", "Ming Chi Kuo", "\t", ming_chi_kuo_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(1500, 100)
            ming_chi_kuo_headline[0] = ming_chi_kuo_headline[1]
            time.sleep(random.uniform(2.5, 3.25))  # Random interval
        except Exception as e:
            print("Error in ming_chi_kuo():", e)
            time.sleep(random.uniform(2.5, 3.25))  # Random interval

mark_kleinman_headline = ["", ""]

def mark_kleinman():
    while True:
        try:
            url = "https://news.sky.com/author/mark-kleinman-494"
            headers = {"User-Agent": "Mozilla/5.0"}
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Mark Kleinman: Received status code {resp.status_code}")
                time.sleep(5)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the first article tile
            # Each article is under a div with class 'sdc-site-tiles__item sdc-site-tile...'
            article = soup.find('div', class_='sdc-site-tiles__item')
            if not article:
                print("Mark Kleinman: Could not find article container.")
                time.sleep(5)
                continue

            # Find the headline link
            headline_tag = article.find('h3', class_='sdc-site-tile__headline')
            if not headline_tag:
                print("Mark Kleinman: Could not find headline tag.")
                time.sleep(5)
                continue

            link_tag = headline_tag.find('a', class_='sdc-site-tile__headline-link', href=True)
            if not link_tag:
                print("Mark Kleinman: Could not find link tag in headline.")
                time.sleep(5)
                continue

            title = link_tag.find('span', class_='sdc-site-tile__headline-text')
            if not title:
                print("Mark Kleinman: Could not find title span.")
                time.sleep(5)
                continue

            article_title = title.get_text(strip=True)
            article_url = link_tag['href']
            if not article_url.startswith('http'):
                article_url = "https://news.sky.com" + article_url

            now = datetime.now().time()
            mark_kleinman_headline[1] = article_title
            if mark_kleinman_headline[0] != mark_kleinman_headline[1]:
                print(now, "\t", "Mark Kleinman", "\t", mark_kleinman_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
            mark_kleinman_headline[0] = mark_kleinman_headline[1]
            time.sleep(5)

        except Exception as e:
            print("Error in mark_kleinman():", e)
            time.sleep(3.01)
###############################################################################
# 0) Outside the function, define the headline-tracking list for barak_ravid
###############################################################################
barak_ravid_headline = [None]  # Just store the single last processed headline
def barak_ravid_rss():
    session = requests.Session()  # Initialize the session
    request_count = 0
    max_requests_per_session = 20  # Adjust as needed

    # Update session headers
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'application/rss+xml,application/xml;q=0.9,*/*;q=0.8',
    })

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'application/rss+xml,application/xml;q=0.9,*/*;q=0.8',
                })
                request_count = 0

            feed_url = "https://api.axios.com/feed/"
            resp = session.get(feed_url, timeout=10)
            if resp.status_code != 200:
                print(f"Barak Ravid (RSS): Received status code {resp.status_code}")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")
            if not items:
                print("Barak Ravid (RSS): No <item> entries found in feed.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            # We'll track if we found any Barak item, so we don't keep opening older ones
            barak_item_found = False

            # Usually, RSS feeds place newest items first, so we'll iterate in order
            for item in items:
                creator_tag = item.find("dc:creator")
                if creator_tag and creator_tag.get_text(strip=True) == "Barak Ravid":
                    # This is the newest Barak Ravid item; process once and break
                    title_tag = item.find("title")
                    link_tag = item.find("link")

                    if not (title_tag and link_tag):
                        break  # Malformed item, skip

                    headline = title_tag.get_text(strip=True)
                    article_url = link_tag.get_text(strip=True)

                    # Check if this is new
                    if barak_ravid_headline[0] != headline:
                        now = datetime.now().time()
                        formatted_headline = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{headline}{Style.RESET_ALL}"
                        print(formatted_headline)
                        print(formatted_headline)
                        print(formatted_headline)

                        print(f"{now} \t Barak Ravid (RSS) \t {headline}")
                        print("Article URL:", article_url)
                        webbrowser.open_new_tab(article_url)
                        winsound.Beep(1500, 100)

                        barak_ravid_headline[0] = headline

                    barak_item_found = True
                    break  # Stop after the first (newest) Barak item

            if not barak_item_found:
                # If no new article from Barak found, you can optionally debug-print here
                # print("No new Barak Ravid article at this time.")
                pass

            # Sleep
            time.sleep(random.uniform(4.5, 5.25))  # Random interval
            request_count += 1

        except Exception as e:
            print("Error in barak_ravid_rss():", e)
            traceback.print_exc()
            time.sleep(random.uniform(4.5, 5.25))  # Random interval

    session.close()  # This line is unreachable due to the infinite loop

# Global variable to track the last processed headline for Ningi
ningi_headline = ["", ""]
from zoneinfo import ZoneInfo

def ningi():
    # Initialize colorama for terminal output
    colorama.init(autoreset=True)

    # Create a session with a retry adapter to reduce timeout errors
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set session headers – using rotating user agents from USER_AGENTS_DATA
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://ningiresearch.com/',
        'Connection': 'keep-alive'
    })

    # Target URL for Ningi Research reports
    base_url = "https://ningiresearch.com/category/reports/"

    while True:
        try:
            # Increase timeout to 15 seconds for slower responses
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Ningi: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')

            # The reports are contained in an unordered list (ul) with class "wp-block-post-template"
            ul = soup.find("ul", class_="wp-block-post-template")
            if not ul:
                print("Ningi: Could not find the report list container.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Assume the first <li> is the latest report
            li = ul.find("li", class_="wp-block-post")
            if not li:
                print("Ningi: Could not find a report item.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Within the li, the report title and link are inside an <h2> with class "wp-block-post-title"
            h2_tag = li.find("h2", class_="wp-block-post-title")
            if not h2_tag:
                print("Ningi: Could not find the report title element.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            a_tag = h2_tag.find("a", href=True)
            if not a_tag:
                print("Ningi: Could not find the report link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Update the headline tracker
            ningi_headline[1] = a_tag.get_text(strip=True)
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = "https://ningiresearch.com" + article_url

            now = datetime.now(ZoneInfo("America/New_York"))
            # Process only if there's a new headline
            if ningi_headline[0] != ningi_headline[1]:
                ticker = None
                # Try to extract ticker from the headline text by matching text inside parentheses
                # Expected format: "… (NASDAQ: COCO) – …" then ticker is COCO.
                match = re.search(r'\((?:NASDAQ|NYSE):\s*([A-Za-z0-9]+)\)', ningi_headline[1])
                if match:
                    ticker = match.group(1).strip().upper()
                else:
                    print(f"Ningi: Could not extract ticker from headline '{ningi_headline[1]}'.")

                # Print the ticker three times if found
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Ningi \t {ningi_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)

            ningi_headline[0] = ningi_headline[1]
            time.sleep(random.uniform(3.5, 4.25))
        except Exception as e:
            print("Error in ningi():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))

# To run Ningi in its own thread:
# at the top of your file
snowcap_headline = [None, None]
def snowcap():
    import requests, random, time, re, webbrowser, winsound
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    from colorama import init, Fore, Back, Style
    from urllib.parse import urljoin

    init(autoreset=True)

    base = "https://www.snowcapresearch.com/shortcampaigns"
    index_url = base + "/"
    max_requests_per_session = 8
    request_count = 0

    # Start session + retry + rotating UA
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://",  HTTPAdapter(max_retries=retry))

    while True:
        try:
            # rotate session occasionally
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", HTTPAdapter(max_retries=retry))
                session.mount("http://",  HTTPAdapter(max_retries=retry))
                request_count = 0

            session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
            resp = session.get(index_url, timeout=15)
            if resp.status_code != 200:
                print(f"Snowcap: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.7, 4.7))
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # find the very first <h2> under any .sqs-html-content
            h2 = soup.select_one('div.sqs-html-content h2')
            if not h2:
                print("Snowcap: no <h2> found in any content block.")
                time.sleep(random.uniform(3.7, 4.7))
                continue

            # that block is our "article"
            article = h2.find_parent('div', class_='sqs-html-content')
            full_title = h2.get_text(" ", strip=True)

            # extract ticker inside parentheses
            m = re.search(r'\((?:[^:]+:)?\s*([A-Z0-9]+)\s*\)', full_title)
            ticker = m.group(1) if m else None

            # find the first link in that same block
            a = article.find('a', href=True)
            if not a:
                print("Snowcap: no <a> in the title block.")
                time.sleep(random.uniform(3.7, 4.7))
                continue
            href = a['href']
            article_url = urljoin(base, href)

            # is it new?
            snowcap_headline[1] = full_title
            if snowcap_headline[1] != snowcap_headline[0]:
                now = datetime.now(ZoneInfo("America/New_York"))
                ts = now.strftime("%Y-%m-%d %H:%M:%S %Z")

                if ticker:
                    badge = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(badge); print(badge); print(badge)
                else:
                    print(f"Snowcap: could not extract ticker from '{full_title}'")

                print(f"{ts}\tSnowcap\t{full_title}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                try:
                    winsound.Beep(1500, 100)
                    winsound.Beep(1500, 100)
                    winsound.Beep(1500, 100)
                except:
                    pass

            snowcap_headline[0] = snowcap_headline[1]
            request_count += 1
            time.sleep(random.uniform(3.7, 4.7))

        except Exception as e:
            print("Error in snowcap():", e)
            time.sleep(random.uniform(3.7, 4.7))




def betaville():
    session = requests.Session()  # Use session for persistent connections
    request_count = 0
    max_requests_per_session = 6  # Adjust as needed

    # Update session headers
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Referer': 'https://google.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    })

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                    'Referer': 'https://google.com',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                })
                request_count = 0

            url = "https://www.betaville.co.uk/"
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"Betaville: Received status code {resp.status_code}")
                time.sleep(random.uniform(9.5, 12.75))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')

            # Find all posts
            posts = soup.find_all('div', class_='Post_post__v5D6j')
            if not posts:
                print("Betaville: No posts found.")
                time.sleep(random.uniform(9.5, 12.75))
                continue

            # Process only the first "Uncooked Alert" post
            for post in posts:
                # Filter only "Uncooked Alert" posts
                title_tag = post.find('h2', class_='Post_title__OkzEN')
                if not title_tag or "uncooked alert" not in title_tag.text.lower():
                    continue

                headline = title_tag.text.strip()
                link_tag = title_tag.find('a', href=True)
                if not link_tag:
                    print("Betaville: Could not find 'a' tag in the headline.")
                    continue
                article_url = link_tag['href']
                if not article_url.startswith('http'):
                    article_url = 'https://www.betaville.co.uk' + article_url

                # Check if this headline has already been processed
                if betaville_headline[0] == headline:
                    # print(f"Betaville: Skipping already processed headline: {headline}")
                    break

                # Extract company name from the headline
                match = re.search(r"alert:\s*(.*?)\s+said", headline, re.IGNORECASE)
                company_name = match.group(1).strip() if match else None
                if not company_name:
                    print(f"Betaville: Could not extract company name from headline '{headline}'.")
                    continue

                # Match company name with ticker
                ticker = None
                expansions = [
                    " INC.", " INC", " INCORPORATED",
                    " CORP.", " CORP", " CORPORATION",
                    " LTD.", " LTD", " PLC", " SA",
                    ""
                ]
                company_name_upper = company_name.upper()
                for exp in expansions:
                    candidate_name = (company_name_upper + exp).strip()
                    if candidate_name in company_name_to_ticker:
                        ticker = company_name_to_ticker[candidate_name]
                        break

                if not ticker:
                    # Fallback: partial match
                    for comp_name, comp_tck in company_name_to_ticker.items():
                        if company_name_upper in comp_name:
                            ticker = comp_tck
                            break

                now = datetime.now().time()
                if ticker:
                    formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                    print(formatted)
                    print(formatted)
                    print(formatted)
                else:
                    print(f"Betaville: Could not match company name '{company_name}' to a known ticker.")

                # Output details
                print(f"{now} \t Betaville \t {headline}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)

                # Update the processed headline
                betaville_headline[0] = headline


                # Stop processing after the first valid "Uncooked Alert"
                break

            time.sleep(random.uniform(9.5, 12.75))
            request_count += 1

        except Exception as e:
            print(f"Error in betaville(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(9.5, 12.75))

    session.close()  # This line is unreachable due to the infinite loop

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import time
import webbrowser
import winsound
import colorama
from colorama import Fore, Back, Style
import random
import re
import traceback
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading

# Global variable to track the last processed headline for Hank Greenberg
hank_greenberg_headline = ["", ""]

def hank_greenberg():
    # Initialize colorama for terminal output
    colorama.init(autoreset=True)

    # Create a session and add a retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,                # Total number of retries
        backoff_factor=1,       # Wait time: 1 * (2 ** retry_number)
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set session headers using a rotating user agent
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.herbgreenberg.com/',
        'Connection': 'keep-alive'
    })

    # The target URL for Herb Greenberg’s Red Flag Alert page
    base_url = "https://www.herbgreenberg.com/s/red-flag-alert"

    while True:
        try:
            # Use an increased timeout of 15 seconds for slower responses
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Hank Greenberg: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Parse the page with BeautifulSoup using the lxml parser
            soup = BeautifulSoup(resp.content, 'lxml')

            # Find the first article link using the data-testid attribute
            # (from the provided outerHTML, the link with data-testid="post-preview-title" is the one we want)
            a_tag = soup.select_one('a[data-testid="post-preview-title"]')
            if not a_tag:
                print("Hank Greenberg: Could not find the article link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Update the headline tracker and extract the article URL
            hank_greenberg_headline[1] = a_tag.get_text(strip=True)
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = "https://www.herbgreenberg.com" + article_url

            now = datetime.now(ZoneInfo("America/New_York"))
            # Only trigger an update if there's a new headline
            if hank_greenberg_headline[0] != hank_greenberg_headline[1]:
                print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Hank Greenberg \t {hank_greenberg_headline[1]}")
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
                winsound.Beep(1500, 100)
            hank_greenberg_headline[0] = hank_greenberg_headline[1]
            time.sleep(random.uniform(3.5, 4.25))
        except Exception as e:
            print("Error in hank_greenberg():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))

    session.close()  # This line is unreachable due to the infinite loop

# To run Hank Greenberg in its own thread:


# Start the threads
# citron_thread = threading.Thread(target=citron)
# citron_thread.start()
#
# scorpion_thread = threading.Thread(target=scorpion)
# scorpion_thread.start()

# iceberg_thread = threading.Thread(target=iceberg)
# iceberg_thread.start()

# hindenburg_thread = threading.Thread(target=hindenburg)
# hindenburg_thread.start()
#
# wolfpack_thread = threading.Thread(target=wolfpack)
# wolfpack_thread.start()

# culper_thread = threading.Thread(target=culper)
# culper_thread.start()
# snowcap_thread = threading.Thread(target=snowcap)
# snowcap_thread.start()
# kerrisdale_thread = threading.Thread(target=kerrisdale)
# kerrisdale_thread.start()


# usps_thread = threading.Thread(target=usps)
# usps_thread.start()

# cdc_thread = threading.Thread(target=cdc)
# cdc_thread.start()

# fda_thread = threading.Thread(target=fda)
# fda_thread.start()
#
# fda2_thread = threading.Thread(target=fda2)
# fda2_thread.start()

# spruce_thread = threading.Thread(target=spruce)
# spruce_thread.start()

# benzinga_thread = threading.Thread(target=benzinga)
# benzinga_thread.start()
#
# nytimes_thread = threading.Thread(target=nytimes)
# nytimes_thread.start()
#
# pershing_thread = threading.Thread(target=pershing)
# pershing_thread.start()
#
# nypost_thread = threading.Thread(target=nypost)
# nypost_thread.start()
#
# aircurrent_thread = threading.Thread(target=aircurrent)
# aircurrent_thread.start()

sec8k_thread = threading.Thread(target=sec8k)
sec8k_thread.start()

# secRW_thread = threading.Thread(target=secRW)
# secRW_thread.start()
#
# cnbc_thread = threading.Thread(target=cnbc)
# cnbc_thread.start()

# bleepcomp_thread = threading.Thread(target=bleepcomp)
# bleepcomp_thread.start()

# hntrbrk_thread = threading.Thread(target=hntrbrk)
# hntrbrk_thread.start()

# Starting new threads for the added websites
bleecker_thread = threading.Thread(target=bleecker)
bleecker_thread.start()
# 
# muddywaters_thread = threading.Thread(target=muddywaters)
# muddywaters_thread.start()
#
# grizzly_thread = threading.Thread(target=grizzly)
# grizzly_thread.start()
#
# fuzzypanda_thread = threading.Thread(target=fuzzypanda)
# fuzzypanda_thread.start()

# # Start the threads for the new functions
# jcapital_thread = threading.Thread(target=jcapital)
# jcapital_thread.start()
#
# blueorca_thread = threading.Thread(target=blue_orca)
# blueorca_thread.start()

# capybara_thread = threading.Thread(target=capybara)
# capybara_thread.start()

morpheus_thread = threading.Thread(target=morpheus)
morpheus_thread.start()
manatee_thread = threading.Thread(target=manatee)
manatee_thread.start()
# ningi_thread = threading.Thread(target=ningi)
# ningi_thread.start()

glassdoor_thread = threading.Thread(target=glassdoor)
glassdoor_thread.start()

# gotham_thread = threading.Thread(target=gotham)
# gotham_thread.start()





# bear_cave_thread = threading.Thread(target=bear_cave)
# bear_cave_thread.start()


# lauren_balik_thread = threading.Thread(target=lauren_balik)
# lauren_balik_thread.start()

#
# tiktok_thread = threading.Thread(target=tiktok_court, daemon=True)
# tiktok_thread.start()
#
# ming_chi_kuo_thread = threading.Thread(target=ming_chi_kuo)
# ming_chi_kuo_thread.start()

# mark_kleinman_thread = threading.Thread(target=mark_kleinman)
# mark_kleinman_thread.start()

# barak_ravid_thread = threading.Thread(target=barak_ravid_rss)
# barak_ravid_thread.start()

# beta_thread = threading.Thread(target=betaville)
# beta_thread.start()

# secspecific_thread = threading.Thread(target=sec_specific)
# secspecific_thread.start()

# hank_greenberg_thread = threading.Thread(target=hank_greenberg)
# hank_greenberg_thread.start()
