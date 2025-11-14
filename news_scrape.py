# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import threading
import webbrowser
import winsound
from datetime import datetime, timedelta, timezone
import random
from curl_cffi import requests as curlreq
from curl_cffi.requests.exceptions import Timeout as CurlTimeout, RequestException
from urllib.parse import urljoin
# Initialize headline tracking lists
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
nytimes_headline = ["", ""]
wsj_business_headline = ["", ""]
wsj_markets_headline = ["", ""]
marketwatch_headline = ["", ""]
reuters_headline = ["", ""]
bloomberg_markets_headline = ["", ""]
bloomberg_industries_headline = ["", ""]
wapo_business_headline = ["", ""]
wapo_national_headline = ["", ""]
information_headline = ["", ""]
whitehouse_headline = ["", ""]
fda_headline = ["", ""]
nvda_headline = ["", ""]


# Add filter keywords for each publisher
# Only headlines containing these keywords will trigger the opening of a new tab (when enabled)
filter_keywords = ["economy", "market", "stocks", "finance"]  # Modify as needed
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

from soundboard import SOUNDS

# Define functions
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import random
import traceback
import colorama
from colorama import Fore, Back, Style



# create a global seen set so we don’t repost the same headline
nytimes_seen = set()
nytimes_seen = set()

def nytimes():
    colorama.init(autoreset=True)
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code != 200:
                print(f"NYTimes: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            soup = BeautifulSoup(resp.content, 'xml')
            item = soup.find('item')
            if not item:
                print("NYTimes: No <item> found.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            title = item.title.text.strip()
            link  = item.link.text.strip()
            if title in nytimes_seen:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lower = title.lower()
            is_critical = any(kw.lower() in lower for kw in CRITICAL_KEYWORDS)

            if is_critical:
                highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                print(f"{now} NYTimes\t{highlighted}")
                print(f"Link: {link}")
                webbrowser.open_new_tab(link)
                try:
                    import winsound
                    winsound.Beep(1000, 200)
                except ImportError:
                    pass
            else:
                print(f"\033[94m{now} NYTimes\033[0m\t{title}")
                print(f"Link: {link}")

            nytimes_seen.add(title)
            time.sleep(random.uniform(3.68, 5.43))

        except Exception as e:
            print("Error in nytimes():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.68, 5.43))

#
# def wsj_business():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"WSJ Business: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("WSJ Business: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("WSJ Business: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             wsj_business_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if wsj_business_headline[0] != wsj_business_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., green)
#                 print(f"\033[92m{now} WSJ Business\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 wsj_business_headline[0] = wsj_business_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in wsj_business():", e)
#             time.sleep(5)
#
# def wsj_markets():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.a.dj.com/rss/RSSMarketsMain.xml"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"WSJ Markets: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("WSJ Markets: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("WSJ Markets: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             wsj_markets_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if wsj_markets_headline[0] != wsj_markets_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., cyan)
#                 print(f"\033[96m{now} WSJ Markets\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 wsj_markets_headline[0] = wsj_markets_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in wsj_markets():", e)
#             time.sleep(5)
#
# def marketwatch():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.content.dowjones.io/public/rss/mw_bulletins"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"MarketWatch: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("MarketWatch: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("MarketWatch: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             marketwatch_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if marketwatch_headline[0] != marketwatch_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., magenta)
#                 print(f"\033[95m{now} MarketWatch\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 marketwatch_headline[0] = marketwatch_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in marketwatch():", e)
#             time.sleep(5)
#
# def reuters():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://news.google.com/rss/search?q=site%3Areuters.com&hl=en-US&gl=US&ceid=US%3Aen"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"Reuters: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("Reuters: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("Reuters: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             reuters_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if reuters_headline[0] != reuters_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., yellow)
#                 print(f"\033[93m{now} Reuters\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 reuters_headline[0] = reuters_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in reuters():", e)
#             time.sleep(5)
#
#
#
# def bloomberg_markets():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.bloomberg.com/markets/news.rss"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"Bloomberg Markets: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("Bloomberg Markets: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("Bloomberg Markets: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             bloomberg_markets_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if bloomberg_markets_headline[0] != bloomberg_markets_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., red)
#                 print(f"\033[91m{now} Bloomberg Markets\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 bloomberg_markets_headline[0] = bloomberg_markets_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in bloomberg_markets():", e)
#             time.sleep(5)
#
# def bloomberg_industries():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.bloomberg.com/industries/news.rss"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"Bloomberg Industries: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("Bloomberg Industries: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("Bloomberg Industries: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             bloomberg_industries_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if bloomberg_industries_headline[0] != bloomberg_industries_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., green)
#                 print(f"\033[92m{now} Bloomberg Industries\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 bloomberg_industries_headline[0] = bloomberg_industries_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in bloomberg_industries():", e)
#             time.sleep(5)
#
# def wapo_business():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.washingtonpost.com/rss/business"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"WaPo Business: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("WaPo Business: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             if not title_tag or not link_tag:
#                 print("WaPo Business: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             wapo_business_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             if wapo_business_headline[0] != wapo_business_headline[1]:
#                 # Highlight the publisher name with a specific color (e.g., cyan)
#                 print(f"\033[96m{now} WaPo Business\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 wapo_business_headline[0] = wapo_business_headline[1]
#             time.sleep(30)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in wapo_business():", e)
#             time.sleep(5)
#
# def wapo_national():
#     while True:
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0'
#             }
#             url = "https://feeds.washingtonpost.com/rss/national"
#             resp = requests.get(url, headers=headers)
#             if resp.status_code != 200:
#                 print(f"WaPo National: Received status code {resp.status_code}")
#                 time.sleep(5)
#                 continue
#             soup = BeautifulSoup(resp.content, 'xml')
#
#             # Find the latest item
#             item = soup.find('item')
#             if not item:
#                 print("WaPo National: Could not find 'item' tag.")
#                 time.sleep(5)
#                 continue
#
#             title_tag = item.find('title')
#             link_tag = item.find('link')
#             pubDate_tag = item.find('pubDate')
#             category_tags = item.find_all('category')
#             if not title_tag or not link_tag:
#                 print("WaPo National: Could not find 'title' or 'link' tag.")
#                 time.sleep(5)
#                 continue
#
#             title = title_tag.text.strip()
#             link = link_tag.text.strip()
#             pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
#             categories = [cat.text.strip() for cat in category_tags]
#             wapo_national_headline[1] = title
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#             if wapo_national_headline[0] != wapo_national_headline[1]:
#                 # Check if the article is under the "Investigation" category
#                 if "Investigation" in categories:
#                     # Highlight the whole headline in bright color (e.g., red background)
#                     print(f"\033[1;97;41m{now} WaPo National\t {title}\033[0m")
#                 else:
#                     # Highlight the publisher name with a specific color (e.g., blue)
#                     print(f"\033[94m{now} WaPo National\033[0m \t {title}")
#                 print(f"Link: {link}")
#
#                 # Check if the title contains any of the filter keywords
#                 if any(keyword.lower() in title.lower() for keyword in filter_keywords):
#                     # Uncomment the following lines to enable opening the link
#                     # webbrowser.open_new_tab(link)
#                     # winsound.Beep(2500, 200)
#                     pass  # Remove this pass statement if uncommenting the above lines
#
#                 wapo_national_headline[0] = wapo_national_headline[1]
#             time.sleep(30)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in wapo_national():", e)
#             time.sleep(5)
nikkei_headline = ["", ""]
statnews_headline = ["", ""]
nypost_headline = ["", ""]
# ----------------- Nikkei Function -----------------


# Global variable to track the last headline for Nikkei Asia

# Global critical keywords to trigger special behavior
CRITICAL_KEYWORDS = ["deal", "acquisition", "partnership", "merger", "partner", "collaborate", "collaboration","tariff","acquired","sources",
                     "breaking","exclusive","investigation","investigating","investigates","probe","stake", "departure","steps down","departs",
                     "scoop","private"," AI ","data center", "GPU","Google","Apple","Nvidia","AMD","Tesla","autonomous","robotaxi","Microsoft",
                     "Oracle","Stargate","Waymo","Perplexity","OpenAI","Perplexity","Broadcom","Coinbase","Coreweave","Baidu","IBM","TSM",
                     "joint venture","integrate","integrating","launch","expand","ChatGPT","Meta","Trump administration",
                     "takeover","in talks","agreement","deal"]

### ———— Nikkei ————
nikkei_seen = set()

def nikkei():
    colorama.init(autoreset=True)
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = "https://asia.nikkei.com/Latestheadlines"
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code != 200:
                print(f"Nikkei: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')
            container = soup.find("div", class_="LatestHeadlinesMainContent_latestHeadlinesList__Xvx9W")
            item = container and container.find("div", class_="Headline_cardContainer__1HdUb")
            a_tag = item and item.find("h4", class_=lambda v: v and "Headline_cardArticleHeadline" in v).find("a", href=True)
            if not a_tag:
                print("Nikkei: Could not scrape headline.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            title = a_tag.get_text(strip=True)
            if title in nikkei_seen:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            link = a_tag['href']
            if not link.startswith("http"):
                link = "https://asia.nikkei.com" + link

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lower = title.lower()
            is_critical = any(kw.lower() in lower for kw in CRITICAL_KEYWORDS)

            if is_critical:
                highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                print(f"{now} Nikkei Asia\t{highlighted}")
                print(f"Link: {link}")
                webbrowser.open_new_tab(link)
                try:
                    import winsound
                    SOUNDS.play("Nikkei", stop_current=True)
                except ImportError:
                    pass
            else:
                print(f"\033[95m{now} Nikkei Asia\033[0m\t{title}")
                print(f"Link: {link}")

            nikkei_seen.add(title)
            time.sleep(random.uniform(4.38, 5.83))

        except Exception as e:
            print("Error in nikkei():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.68, 5.43))

def fda():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import time
    import random
    import webbrowser
    import traceback
    from colorama import Fore, Back, Style
    import colorama
    try:
        import winsound
    except ImportError:
        winsound = None

    # Initialize Colorama (for coloring output)
    colorama.init(autoreset=True)

    # FDA press announcements URL (page 0)
    url = "https://www.fda.gov/news-events/fda-newsroom/press-announcements?page=0"

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            print(f"FDA: Received status code {resp.status_code}")
            return

        # Parse the response using the HTML parser
        soup = BeautifulSoup(resp.content, 'html.parser')

        # Locate the container holding the press announcement listings.
        # The FDA page has a "view-content" container with one or more "item-list" divs.
        view_content = soup.find('div', class_='view-content')
        if not view_content:
            print("FDA: Could not find the view-content container.")
            return

        # Find the first item-list (assumed to contain the latest announcements)
        item_list = view_content.find('div', class_='item-list')
        if not item_list:
            print("FDA: Could not find an item-list container.")
            return

        # Within the first item-list, locate the first unordered list (ul)
        ul = item_list.find('ul')
        if not ul:
            print("FDA: Could not find an unordered list in the item-list.")
            return

        # Find the first list item (li) inside the ul
        li = ul.find('li')
        if not li:
            print("FDA: Could not find a list item.")
            return

        # Get the <a> tag that contains the top announcement link (and title)
        a_tag = li.find('a', href=True)
        if not a_tag:
            print("FDA: Could not find the link in the list item.")
            return

        title = a_tag.get_text(strip=True)
        link = a_tag['href']

        # Convert relative URLs to absolute URLs if needed.
        if not link.startswith("http"):
            link = "https://www.fda.gov" + link

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{now} FDA Press Announcement: {title}")
        print(f"Link: {link}")

        webbrowser.open_new_tab(link)
        if winsound is not None:
            winsound.Beep(1000, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(1000, 200)

    except Exception as e:
        print("Error in fda():", e)
        traceback.print_exc()




def whitehouse_news():
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

    colorama.init(autoreset=True)

    url = "https://www.whitehouse.gov/news/"

    # Global headline storage for White House (initialize if not already defined)
    try:
        whitehouse_headline
    except NameError:
        whitehouse_headline = ["", ""]

    while True:
        try:
            headers = {'User-Agent': random.choice(USER_AGENTS_DATA)['ua']}
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code != 200:
                print(f"WhiteHouse: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            # Use lxml parser for faster parsing
            soup = BeautifulSoup(resp.content, 'lxml')

            # Find the container with the list of posts
            container = soup.select_one("ul.wp-block-post-template")
            if not container:
                print("WhiteHouse: Could not find the article container.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            # Select the first list item (the top article)
            article = container.find("li")
            if not article:
                print("WhiteHouse: Could not find an article item.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            # Look for the headline within an h2 element with class "wp-block-post-title"
            h2_tag = article.find("h2", class_="wp-block-post-title")
            if not h2_tag:
                print("WhiteHouse: Could not find the headline element.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            # Find the anchor tag with the link
            a_tag = h2_tag.find("a", href=True)
            if not a_tag:
                print("WhiteHouse: Could not find the article link in the headline.")
                time.sleep(random.uniform(3.68, 5.43))
                continue

            title = a_tag.get_text(strip=True)
            link = a_tag['href']
            if not link.startswith("http"):
                link = "https://www.whitehouse.gov" + link

            whitehouse_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if whitehouse_headline[0] != whitehouse_headline[1]:
                highlighted_title = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                print(f"{now} WhiteHouse \t {highlighted_title}")
                print(f"Link: {link}")
                webbrowser.open_new_tab(link)
                SOUNDS.play("White house", stop_current=True)
                whitehouse_headline[0] = whitehouse_headline[1]
            time.sleep(random.uniform(4.68, 5.73))
        except Exception as e:
            print("Error in whitehouse_news():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.68, 5.43))

# ----------------- StatNews Function -----------------
stat_keywords = ['obesity','trial','weight loss','weight-loss','discontinuation','study','dosing','SAEs','Serious Adverse Events','results',"ai",
                 "vaccine","CDC","FDA","Trump","phase","report"]





def statnews():
    import requests
    import random
    import time
    import winsound
    import webbrowser
    import traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style

    # --- Setup session with retry + rotating UA ---
    session = requests.Session()
    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    request_count = 0
    max_requests_per_session = 6
    feed_url = "https://www.statnews.com/feed/"
    statnews_seen = set()

    while True:
        try:
            # rotate session & UA every few requests
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(feed_url, timeout=10)
            if resp.status_code != 200:
                print(f"StatNews: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")[:2]  # take the two newest

            # notify in chronological order (older first)
            for item in reversed(items):
                title = item.find("title").get_text(strip=True)
                link  = item.find("link").get_text(strip=True)

                # skip if we've already seen this exact headline
                if title in statnews_seen:
                    continue
                statnews_seen.add(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # check against both critical and stat keywords
                is_special = (
                    any(kw.lower() in title.lower() for kw in CRITICAL_KEYWORDS) or
                    any(kw.lower() in title.lower() for kw in stat_keywords)
                )

                if is_special:
                    # highlight and alert
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now} StatNews\t{highlighted}")
                    webbrowser.open_new_tab(link)
                    SOUNDS.play("stat news", stop_current=True)
                else:
                    print(f"{now} StatNews\t{title}")

                print(f"Link: {link}")

            request_count += 1
            time.sleep(random.uniform(3.7, 5.4))

        except Exception as e:
            print("Error in statnews():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.7, 5.4))

# global seen‐list of titles
mm_seen_titles = []

# your keywords
MM_KEYWORDS = [
    "reschedule",
    "rescheduling",
    "legalization",
    "breaking",
    "exclusive",
    "legalize"
]
techcrunch_headline = ["", ""]
techcrunch_seen = set()

def techcrunch():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import time
    import random
    import webbrowser
    import winsound
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style
    import traceback

    # --- State & configuration ---
    techcrunch_seen = set()
    request_count = 0
    max_requests_per_session = 6

    session = requests.Session()
    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    feed_url = "https://techcrunch.com/feed/"

    while True:
        try:
            # rotate session & UA every N requests
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(feed_url, timeout=15)
            if resp.status_code != 200:
                print(f"TechCrunch: Received status code {resp.status_code}")
                time.sleep(random.uniform(2.9, 3.65))
                continue

            # parse RSS feed
            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")
            newest_two = items[:2]

            # announce in chronological order (older first)
            for item in reversed(newest_two):
                title = item.find("title").get_text(strip=True)
                link  = item.find("link").get_text(strip=True)

                if title in techcrunch_seen:
                    continue
                techcrunch_seen.add(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                is_critical = any(kw.lower() in title.lower() for kw in CRITICAL_KEYWORDS)

                if is_critical:
                    # highlight & notify
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now}\tTechCrunch\t{highlighted}")
                    webbrowser.open_new_tab(link)
                    SOUNDS.play("tech crunch", stop_current=True)
                else:
                    print(f"{now}\tTechCrunch\t{title}")

                print("Link:", link)

            request_count += 1
            time.sleep(random.uniform(2.9, 3.65))

        except Exception as e:
            print("Error in techcrunch():", e)
            traceback.print_exc()
            time.sleep(random.uniform(2.9, 3.65))
def openai_news():
    import time, random, traceback, webbrowser
    from datetime import datetime
    from urllib.parse import urlparse, urlunparse
    from xml.etree import ElementTree as ET
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)

    # --- Config ---
    rss_url = "https://openai.com/news/rss.xml"
    sleep_range = (3.2, 4.4)

    # --- State ---
    last_seen_link = None
    announced_proxy = False  # to avoid spamming the 403->proxy line

    # --- Session (use cloudscraper if available; fall back to requests) ---
    try:
        import cloudscraper
        session = cloudscraper.create_scraper()
    except Exception:
        import requests
        session = requests.Session()

    # user provided list of UAs
    session.headers.update({
        "User-Agent": random.choice(USER_AGENTS_DATA)["ua"],
        "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Connection": "keep-alive",
        "Referer": "https://openai.com/news/",
    })

    def httpsify(url: str) -> str:
        # Ensure https scheme (your logs showed http:// links)
        try:
            p = urlparse(url)
            if not p.scheme:
                p = p._replace(scheme="https")
            elif p.scheme == "http":
                p = p._replace(scheme="https")
            return urlunparse(p)
        except Exception:
            return url

    def fetch_rss():
        """Return (xml_text, used_proxy: bool)."""
        nonlocal announced_proxy
        try:
            r = session.get(rss_url, timeout=20)
            if r.status_code == 403:
                proxied = "https://r.jina.ai/http://openai.com/news/rss.xml"
                rp = session.get(proxied, timeout=20)
                if not announced_proxy:
                    print("[NEWS] OpenAI: 403 on rss.xml → using r.jina.ai proxy once")
                    announced_proxy = True
                return rp.text, True
            if r.status_code != 200:
                print(f"[NEWS] OpenAI RSS status {r.status_code}, len={len(getattr(r,'content',b''))}")
                return "", False
            return r.text, False
        except Exception as e:
            print("[NEWS] OpenAI RSS fetch error:", e)
            return "", False

    while True:
        try:
            xml_text, _ = fetch_rss()
            if not xml_text:
                time.sleep(random.uniform(*sleep_range)); continue

            # Parse RSS
            try:
                root = ET.fromstring(xml_text)
            except Exception as pe:
                # If feed proxy returned Markdown (extremely rare), just wait and retry
                print("[NEWS] OpenAI RSS parse error; first 300 chars:\n" + xml_text[:300])
                time.sleep(random.uniform(*sleep_range)); continue

            # RSS 2.0: channel/item[0]
            channel = root.find("channel")
            if channel is None:
                # Atom fallback: feed/entry[0]
                entry = root.find("{http://www.w3.org/2005/Atom}entry")
                if entry is None:
                    print("[NEWS] OpenAI RSS: no channel/entry found")
                    time.sleep(random.uniform(*sleep_range)); continue
                # Atom
                title_el = entry.find("{http://www.w3.org/2005/Atom}title")
                link_el = entry.find("{http://www.w3.org/2005/Atom}link")
                title = (title_el.text or "").strip() if title_el is not None else ""
                link = httpsify(link_el.attrib.get("href", "").strip()) if link_el is not None else ""
            else:
                # RSS 2.0
                item = channel.find("item")
                if item is None:
                    print("[NEWS] OpenAI RSS: no items yet")
                    time.sleep(random.uniform(*sleep_range)); continue
                title_el = item.find("title")
                link_el  = item.find("link")
                title = (title_el.text or "").strip() if title_el is not None else ""
                link  = httpsify((link_el.text or "").strip() if link_el is not None else "")

            if not title or not link:
                print("[NEWS] OpenAI RSS: item missing title/link")
                time.sleep(random.uniform(*sleep_range)); continue

            # Only announce if new
            if link != last_seen_link:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[NEWS] {now}\tOpenAI\t{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}")
                print("[NEWS] Link:", link)
                # optional side-effects
                try: webbrowser.open_new_tab(link)
                except Exception: pass
                try:
                    # Try your custom cue first
                    SOUNDS.play("open ai", stop_current=True)
                except Exception as ex:
                    # Log why audio failed, then speak the words via OS TTS
                    print("[NEWS] SOUNDS.play('open ai') failed ->", repr(ex))
                    try:
                        import platform, subprocess, sys
                        phrase = "Open AI"
                        sys_plat = platform.system()

                        if sys_plat == "Darwin":  # macOS
                            subprocess.Popen(["say", phrase])
                        elif sys_plat == "Windows":
                            # Use PowerShell SAPI (no extra deps)
                            ps = (
                                "Add-Type -AssemblyName System.Speech; "
                                "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                                f'$speak.Speak("{phrase}");'
                            )
                            subprocess.Popen(["powershell", "-NoProfile", "-Command", ps])
                        else:
                            # Linux: try spd-say, then espeak
                            try:
                                subprocess.Popen(["spd-say", phrase])
                            except Exception:
                                subprocess.Popen(["espeak", phrase])
                    except Exception as tts_ex:
                        print("[NEWS] TTS fallback failed ->", repr(tts_ex))

                except Exception: pass
                last_seen_link = link

            time.sleep(random.uniform(*sleep_range))

        except Exception as e:
            print("Error in openai_news_latest_all():", e)
            traceback.print_exc()
            time.sleep(random.uniform(*sleep_range))



def nvidia_news_latest_only():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time, random, re, webbrowser, traceback
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)

    base_url = "https://nvidianews.nvidia.com/"
    sleep_range = (3.64, 4.76)

    # --- State ---
    try:
        nvidia_headline
    except NameError:
        nvidia_headline = ["", ""]

    request_count = 0
    max_requests_per_session = 8

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
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Referer': 'https://nvidianews.nvidia.com/'})

    def parse_date(s: str):
        s = (s or "").strip()
        try:
            return datetime.strptime(s, "%B %d, %Y")
        except Exception:
            return None

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"[NEWS] NVIDIA: Received status code {resp.status_code}")
                time.sleep(random.uniform(*sleep_range))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            latest = soup.select_one("section#latestNews .tiles")
            if not latest:
                print("[NEWS] NVIDIA: Could not find Latest News tiles.")
                time.sleep(random.uniform(*sleep_range))
                continue

            # Build list and pick newest
            items = []
            for art in latest.select("article.tiles-item"):
                a = art.select_one("h3.tiles-item-text-title a[href]")
                if not a:
                    continue
                title = a.get_text(strip=True)
                link = a["href"].strip()
                date_div = art.select_one(".tiles-item-text-date")
                dt = parse_date(date_div.get_text(strip=True) if date_div else "")
                items.append({"title": title, "link": link, "dt": dt})

            if not items:
                print("[NEWS] NVIDIA: No article cards parsed.")
                time.sleep(random.uniform(*sleep_range))
                continue

            # newest only
            items.sort(key=lambda x: (x["dt"] is not None, x["dt"]), reverse=True)
            newest = items[0]

            now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")
            if nvidia_headline[0] != newest["title"]:
                highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{newest['title']}{Style.RESET_ALL}"
                print(f"[NEWS] {now}\tNVIDIA\t{highlighted}")
                print("[NEWS] Link:", newest["link"])
                try:
                    webbrowser.open_new_tab(newest["link"])
                except Exception:
                    pass
                try:
                    SOUNDS.play("nvidia", stop_current=True)
                except Exception:
                    print("\a")
                nvidia_headline[0] = newest["title"]
            # else: stay quiet when nothing new

            request_count += 1
            time.sleep(random.uniform(*sleep_range))

        except Exception as e:
            print("Error in nvidia_news_latest_only():", e)
            traceback.print_exc()
            time.sleep(random.uniform(*sleep_range))



def marijuanamoment():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 6

    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
    feed_url = "https://www.marijuanamoment.net/feed/"

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(feed_url, timeout=10)
            if resp.status_code != 200:
                print(f"MM: status {resp.status_code}")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")

            # take the two newest entries
            newest_two = items[:2]

            # notify in chronological order (older of the two first)
            for item in reversed(newest_two):
                title = item.find("title").get_text(strip=True)
                link  = item.find("link").get_text(strip=True)

                # skip if we've already announced this exact headline
                if title in mm_seen_titles:
                    continue

                mm_seen_titles.append(title)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # highlight in green if any keyword appears
                if any(kw.lower() in title.lower() for kw in MM_KEYWORDS):
                    print(f"\033[92m{now} MM\033[0m\t{title}")
                    webbrowser.open_new_tab(link)
                else:
                    print(f"{now} MM\t{title}")

                print(f"Link: {link}")
                try:
                    SOUNDS.play("marijuana", stop_current=True)

                except:
                    print("\a")

            request_count += 1
            time.sleep(random.uniform(3.7, 5.4))

        except Exception as e:
            print("Error in marijuanamoment():", e)
            time.sleep(random.uniform(3.7, 5.4))

import urllib.parse
import re
import traceback

# keep track of which headlines we've already seen
semafor_seen = set()

def semafor_rohan():
    colorama.init(autoreset=True)
    semafor_seen = set()

    # Session + retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429,500,502,503,504],
        allowed_methods=["GET","HEAD","OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.semafor.com/author/rohan-goswami',
        'Connection': 'keep-alive'
    })

    base_url = "https://www.semafor.com/author/rohan-goswami"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Semafor: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.25, 4.55))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            grid = soup.find("div", class_=re.compile(r"styles_ledeArticleGrid"))
            if not grid:
                print("Semafor: Could not find the article grid")
                time.sleep(random.uniform(3.25, 4.55))
                continue

            # ◀ only pick the first story link, not the mailto/twitter ones
            a_tag = grid.find("a", href=re.compile(r"^/article/"))
            if not a_tag:
                print("Semafor: No article link found")
                time.sleep(random.uniform(3.25, 4.55))
                continue

            # extract headline
            h2 = a_tag.find("h2", class_=re.compile(r"styles_headline__"))
            title = h2.get_text(strip=True) if h2 else a_tag.get_text(strip=True)

            # build full URL
            href = a_tag["href"]
            article_url = urllib.parse.urljoin(base_url, href)

            # avoid duplicates
            if title in semafor_seen:
                time.sleep(random.uniform(3.25, 4.55))
                continue

            # timestamp
            now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")

            # always highlight in red background + white text
            highlighted = f"{Style.BRIGHT}{Back.RED}{Fore.BLACK}{title}{Style.RESET_ALL}"
            print(f"{now} Semafor\t{highlighted}")
            print(f"Link: {article_url}")

            # open & beep
            webbrowser.open_new_tab(article_url)
            SOUNDS.play("semafor", stop_current=True)

            semafor_seen.add(title)
            time.sleep(random.uniform(3.25, 4.55))

        except Exception as e:
            print(f"Error in semafor_rohan(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(3.25, 4.55))
# keep track of which headlines we've already seen
semafor_seen = set()

def semafor_gillian():
    import urllib.parse
    from zoneinfo import ZoneInfo
    colorama.init(autoreset=True)

    # (kept same local shadowing as your rohan version)
    semafor_seen = set()

    # Session + retry adapter
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

    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua'],
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.semafor.com/author/gillian-tan',
        'Connection': 'keep-alive'
    })

    base_url = "https://www.semafor.com/author/gillian-tan"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Semafor: Received status code {resp.status_code}")
                time.sleep(random.uniform(2.25, 3.15))
                continue

            soup = BeautifulSoup(resp.content, "lxml")

            # same approach: find the lede grid, then the first /article/ link inside it
            grid = soup.find("div", class_=re.compile(r"styles_ledeArticleGrid"))
            if not grid:
                print("Semafor: Could not find the article grid")
                time.sleep(random.uniform(2.25, 3.15))
                continue

            a_tag = grid.find("a", href=re.compile(r"^/article/"))
            if not a_tag:
                print("Semafor: No article link found")
                time.sleep(random.uniform(2.25, 3.15))
                continue

            # extract headline
            h2 = a_tag.find("h2", class_=re.compile(r"styles_headline__"))
            title = h2.get_text(strip=True) if h2 else a_tag.get_text(strip=True)

            # build full URL
            href = a_tag["href"]
            article_url = urllib.parse.urljoin(base_url, href)

            # avoid duplicates
            if title in semafor_seen:
                time.sleep(random.uniform(2.25, 3.15))
                continue

            # timestamp
            now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")

            # highlight (kept same red background + black text)
            highlighted = f"{Style.BRIGHT}{Back.RED}{Fore.BLACK}{title}{Style.RESET_ALL}"
            print(f"{now} Semafor\t{highlighted}")
            print(f"Link: {article_url}")

            # open & play sound (same behavior)
            webbrowser.open_new_tab(article_url)
            SOUNDS.play("semafor", stop_current=True)

            semafor_seen.add(title)
            time.sleep(random.uniform(2.25, 3.15))

        except Exception as e:
            print(f"Error in semafor_gillian(): {e}")
            traceback.print_exc()
            time.sleep(random.uniform(2.25, 3.15))

# ----------------- FHFA News Release Scraper -----------------
fhfa_seen = set()

def fhfa():
    import requests
    import random
    import time
    import winsound
    import webbrowser
    import traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style

    # --- Setup session with retry + rotating UA ---
    session = requests.Session()
    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
    })

    request_count = 0
    max_requests_per_session = 6
    fhfa_url = "https://www.fhfa.gov/news/news-release"

    while True:
        try:
            # rotate session & UA every so often
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
                })
                request_count = 0

            resp = session.get(fhfa_url, timeout=15)
            if resp.status_code != 200:
                print(f"FHFA: Received status code {resp.status_code}")
                time.sleep(random.uniform(4, 6))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            items = soup.select("li.news-listing-page-item")  # all the releases

            for item in items:
                # title + link
                h2 = item.find("h2", class_="news-list__item-header")
                a = h2.find("a", href=True) if h2 else None
                if not a:
                    continue

                title = a.get_text(strip=True)
                link = a["href"]
                if not link.startswith("http"):
                    link = "https://www.fhfa.gov" + link

                # pub date (optional display)
                time_tag = item.find("time")
                pub_date = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else ""

                # skip if already seen
                if title in fhfa_seen:
                    continue

                fhfa_seen.add(title)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # highlight & announce
                highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                print(f"{now}  FHFA PR\t{highlighted}\t{pub_date}")
                print(f"Link: {link}")

                # open and beep
                webbrowser.open_new_tab(link)
                SOUNDS.play("fhfa", stop_current=True)

            request_count += 1
            time.sleep(random.uniform(2.4, 3.6))

        except Exception as e:
            print("Error in fhfa():", e)
            traceback.print_exc()
            time.sleep(random.uniform(2.4, 3.6))

# ----------------- NY Post Function -----------------
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import webbrowser
import winsound
import colorama
from colorama import Fore, Back, Style
import random
import threading

# Initialize colorama globally
colorama.init(autoreset=True)


# Exclusion keywords (check both headline and URL)
exclude_keywords = ["pagesix", "entertainment", "alexa", "astrology", "celebrity", "betting", "decider", "shopping"]

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import webbrowser
import winsound
import colorama
from colorama import Fore, Back, Style
import random
import threading

# Initialize colorama globally
colorama.init(autoreset=True)

# Global headline tracker for NY Post and a set to track seen (headline, URL) pairs
nypost_headline = ["", ""]
nypost_seen = set()

# Exclusion keywords (check both headline and URL)
exclude_keywords = ["pagesix", "entertainment", "alexa", "astrology", "celebrity", "betting", "decider", "shopping","sports"]
def nypost():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import time
    import webbrowser
    import random
    from colorama import Fore, Back, Style
    # Make sure these global variables are defined somewhere in your code:
    #   USER_AGENTS_DATA, exclude_keywords, CRITICAL_KEYWORDS, nypost_seen, nypost_headline

    # Initialize a requests session with a randomly selected User-Agent
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 5  # Adjust as needed
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
    })

    while True:
        try:
            # Rebuild session when request count exceeds the threshold
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
                })
                request_count = 0

            url = "https://nypost.com/feed/"
            resp = session.get(url, timeout=5.7)
            if resp.status_code != 200:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            soup = BeautifulSoup(resp.content, 'xml')
            item = soup.find('item')
            if not item:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            if not title_tag or not link_tag:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()

            # Skip the feed item if any exclude keywords are present
            if any(kw.lower() in title.lower() or kw.lower() in link.lower() for kw in exclude_keywords):
                time.sleep(random.uniform(3.68, 5.43))
                continue

            # Skip already processed headlines
            if (title, link) in nypost_seen:
                time.sleep(random.uniform(3.68, 5.43))
                continue

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if nypost_headline[0] != title:
                # Highlight the title if it contains a critical keyword
                if any(kw in title.lower() for kw in CRITICAL_KEYWORDS):
                    highlighted_title = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now} NY Post \t {highlighted_title}")
                    print(f"Link: {link}")
                    webbrowser.open_new_tab(link)
                    try:
                        import winsound
                        SOUNDS.play("NY post", stop_current=True)
                    except ImportError:
                        pass
                else:
                    print(f"\033[94m{now} NY Post\033[0m \t {title}")
                    print(f"Link: {link}")
                    # Optionally, uncomment to auto-open
                    # webbrowser.open_new_tab(link)
                nypost_headline[0] = title
                nypost_seen.add((title, link))
            time.sleep(random.uniform(3.68, 5.43))
            request_count += 1

        except Exception as e:
            print("Error in nypost():", e)
            time.sleep(random.uniform(3.68, 5.43))
import requests, random, time, winsound, webbrowser, re
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# global tracker
yuyuan_headline = ["", ""]

def yuyuan():
    session = requests.Session()
    request_count = 0
    max_requests_per_session = 6

    # retry strategy
    retry = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    # this is the container ID for user 7040797671’s timeline
    api_url = (
        "https://m.weibo.cn/api/container/getIndex"
        "?containerid=1076037040797671&page=1"
    )

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(api_url, timeout=10)
            if resp.status_code != 200:
                print(f"Yuyuan: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            data = resp.json()
            cards = data.get("data", {}).get("cards", [])
            # find the first “normal” post
            post_card = next((c for c in cards if c.get("card_type") == 9), None)
            if not post_card:
                print("Yuyuan: no post card found in JSON.")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            mblog = post_card.get("mblog", {})
            post_id = mblog.get("id")
            raw_text = mblog.get("text", "")
            # strip any HTML tags
            full_text = re.sub(r'<[^>]+>', '', raw_text).strip()

            # track by post_id
            yuyuan_headline[1] = post_id
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if yuyuan_headline[0] != yuyuan_headline[1]:
                post_url = f"https://m.weibo.cn/status/{post_id}"
                print(f"{now} Yuyuan\t{full_text}")
                print(f"Link: {post_url}")
                webbrowser.open_new_tab(post_url)
                try:
                    winsound.Beep(1000, 200)
                    winsound.Beep(1000, 200)
                    winsound.Beep(1000, 200)
                except:
                    pass
                yuyuan_headline[0] = yuyuan_headline[1]

            request_count += 1
            time.sleep(random.uniform(3.7, 5.4))

        except Exception as e:
            print("Error in yuyuan():", e)
            time.sleep(random.uniform(3.7, 5.4))


# Example global variables initialization (replace or adjust as needed):
# USER_AGENTS_DATA = [ {"ua": "Mozilla/5.0 (...)"}, {...}, ... ]
# exclude_keywords = ["keyword1", "keyword2"]
# CRITICAL_KEYWORDS = ["critical1", "critical2"]
# nypost_seen = set()
# nypost_headline = [""]  # Use a list or similar mutable container for persisting the last headline

def information():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import webbrowser
    import winsound
    import random
    import colorama
    from colorama import Fore, Back, Style

    # Initialize colorama
    colorama.init(autoreset=True)

    # Use a random user agent from your USER_AGENTS_DATA list
    # ua = random.choice(USER_AGENTS_DATA)['ua']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Referer": "https://www.theinformation.com/",
        "Connection": "keep-alive",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }

    # URL for The Information's recent view
    base_url = "https://www.theinformation.com/?view=recent"

    # Global variable to track the last processed headline.
    try:
        information_headline
    except NameError:
        information_headline = ["", ""]

    while True:
        try:
            resp = requests.get(base_url, headers=headers, timeout=10)
            if resp.status_code != 200:
                print(f"The Information: Received status code {resp.status_code}")
                time.sleep(random.uniform(4.68, 5.43))
                continue

            soup = BeautifulSoup(resp.content, 'lxml')

            # Look for the feed container; based on your sample HTML, it's in a div with class "gh-feed"
            feed = soup.find("div", class_="gh-feed")
            if not feed:
                # If the feed container is not yet populated, wait a bit
                time.sleep(random.uniform(4.68, 5.43))
                continue

            # Find the first article in the feed (adjust this if more than one article is desired)
            article = feed.find("article")
            if not article:
                time.sleep(random.uniform(4.68, 5.43))
                continue

            # Find the main link (<a> tag) inside the article.
            a_tag = article.find("a", href=True)
            if not a_tag:
                time.sleep(random.uniform(4.68, 5.43))
                continue

            # Extract the headline text and URL.
            headline = a_tag.get_text(strip=True)
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = "https://www.theinformation.com" + article_url

            # Get the current time in Eastern Time for display.
            now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")

            # If this headline is new, output it and open the link.
            if information_headline[0] != headline:
                print(f"{now} The Information \t {headline}")
                print(f"Link: {article_url}\n")
                webbrowser.open_new_tab(article_url)
                # winsound.Beep(2500, 200)
                information_headline[0] = headline

            # Sleep for a minute before checking again.
            time.sleep(60)
        except Exception as e:
            print("Error in information():", e)
            time.sleep(random.uniform(4.68, 5.43))

ftc_headline = ["", ""]
def ftc():
    import requests
    import random
    import time
    import winsound
    import webbrowser
    import traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry

    # --- Setup session with retry + rotating UA ---
    session = requests.Session()
    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    request_count = 0
    max_requests_per_session = 6
    url = "https://www.ftc.gov/news-events/news/press-releases"
    seen_titles = set()

    while True:
        try:
            # Rotate session & UA every so often
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})
                request_count = 0

            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"FTC PR: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            soup = BeautifulSoup(resp.content, "html.parser")
            # only take the first two press‐release articles
            articles = soup.find_all("article", class_="node--type-press-release")[:2]

            for art in articles:
                h3 = art.find("h3", class_="node-title")
                if not h3:
                    continue
                a = h3.find("a", href=True)
                if not a:
                    continue

                title = a.get_text(strip=True)
                link = a["href"]
                if not link.startswith("http"):
                    link = "https://www.ftc.gov" + link

                # skip if already seen
                if title in seen_titles:
                    continue
                seen_titles.add(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{now} \tFTC PR\t{title}")
                print(f"Link: {link}")

                # open and beep for every new one
                webbrowser.open_new_tab(link)
                SOUNDS.play("ftc", stop_current=True)

            request_count += 1
            time.sleep(random.uniform(4.7, 5.86))

        except Exception as e:
            print("Error in ftc_press_releases():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.7, 5.4))
# put this by your other globals
logic_seen_links = set()

def logic():
    """
    Scrape all top 'Exclusive' cards from:
      https://thelogic.co/category/news/exclusive/
    - No critical keyword filtering: every unseen article triggers print + open + sound
    - Dedupe by absolute link via logic_seen_links
    - cloudscraper if available; otherwise requests with retries
    - Gentle polling cadence to match your other scrapers
    """
    import time, random, webbrowser, traceback
    from datetime import datetime
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup

    # --- session setup (cloudscraper preferred) ---
    session = None
    try:
        import cloudscraper
        session = cloudscraper.create_scraper()
    except Exception:
        pass

    if session is None:
        import requests
        from requests.adapters import HTTPAdapter, Retry
        session = requests.Session()
        retry = Retry(
            total=4,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

    # headers (reusing your UA pool)
    session.headers.update({
        "User-Agent": random.choice(USER_AGENTS_DATA)["ua"],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://thelogic.co/",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Connection": "keep-alive",
    })

    base = "https://thelogic.co"
    url  = f"{base}/category/news/exclusive/"

    def fetch_text(u, timeout=15):
        try:
            r = session.get(u, timeout=timeout)
            r.raise_for_status()
            return r.text
        except Exception:
            return ""

    while True:
        try:
            html = fetch_text(url, timeout=15)
            if not html:
                # brief backoff and retry next loop
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(html, "lxml")

            # find all article cards on the page
            cards = soup.select("article.article-teaser h2.article-teaser__title a[href]")
            if not cards:
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # process each card in order of appearance (top-first)
            for a in cards:
                title = a.get_text(strip=True)
                href  = a["href"].strip()
                link  = href if href.startswith("http") else urljoin(base, href)

                # skip already seen links
                if link in logic_seen_links:
                    continue
                logic_seen_links.add(link)

                # print, open, sound — for ALL articles (no filtering)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{now} Logic\t{title}")
                print(f"Link: {link}")

                try:
                    webbrowser.open_new_tab(link)
                except Exception:
                    pass
                try:
                    SOUNDS.play("logic", stop_current=True)
                except Exception:
                    pass

            # poll cadence ~3.5–4.25 min (match your other pollers)
            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in logic():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))


# Global variable to track the last processed headline for Variety
variety_headline = ["", ""]
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

# Global variable to track the last headline for Variety
variety_headline = ["", ""]
def variety():
    # Create a session with a retry adapter
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    from requests.adapters import HTTPAdapter
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://variety.com/',
        'Connection': 'keep-alive'
    })

    base_url = "https://variety.com"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Variety: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            ul = soup.find("ul", class_="o-tease-news-list")
            if not ul:
                print("Variety: Could not find the news list container.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            li = ul.find("li")
            if not li:
                print("Variety: Could not find a news item.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            h3_tag = li.find("h3", class_="c-title")
            if not h3_tag:
                print("Variety: Could not find the headline element.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            a_tag = h3_tag.find("a", href=True)
            if not a_tag:
                print("Variety: Could not find the article link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            variety_headline[1] = a_tag.get_text(strip=True)
            article_url = a_tag['href']
            if not article_url.startswith("http"):
                article_url = "https://variety.com" + article_url

            # ── New filter: only Digital category ───────────────────────────────
            if '/digital/' not in article_url:
                # Not a Digital story, skip it
                time.sleep(random.uniform(3.5, 4.25))
                continue
            # ─────────────────────────────────────────────────────────────────────

            now = datetime.now(ZoneInfo("America/New_York"))
            if variety_headline[0] != variety_headline[1]:
                if any(kw in variety_headline[1].lower() for kw in CRITICAL_KEYWORDS):
                    highlighted_title = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{variety_headline[1]}{Style.RESET_ALL}"
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Variety \t {highlighted_title}")
                    print("Link:", article_url)
                    webbrowser.open_new_tab(article_url)
                    SOUNDS.play("variety", stop_current=True)
                else:
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t Variety \t {variety_headline[1]}")
                    print("Link:", article_url)
                    # webbrowser.open_new_tab(article_url)
                    SOUNDS.play("variety", stop_current=True)
                variety_headline[0] = variety_headline[1]

            time.sleep(random.uniform(3.5, 4.25))
        except Exception as e:
            print(f"Variety: Exception occurred: {e}")
            time.sleep(random.uniform(3.5, 4.25))


cms_headline = ["", ""]

def cms():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import random
    import webbrowser
    import winsound
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style
    import traceback

    # --- Session with retry ---
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

    # --- Headers & UA ---
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.cms.gov/about-cms/contact/newsroom',
        'Connection': 'keep-alive'
    })

    base_url = "https://www.cms.gov/about-cms/contact/newsroom"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"CMS: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            wrapper = soup.find("div", class_="views-infinite-scroll-content-wrapper")
            if not wrapper:
                print("CMS: Could not find the articles container.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            row = wrapper.find("div", class_="views-row")
            if not row:
                print("CMS: Could not find a newsroom item.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Extract date, title, link
            time_tag = row.find("time", datetime=True)
            date_str = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else time_tag.get_text(strip=True)
            title = row.find("h3").get_text(strip=True)
            a_tag = row.find("a", class_="newsroom-main-view-link", href=True)
            if not a_tag:
                print("CMS: Could not find the article link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            article_url = a_tag["href"]
            if article_url.startswith("/"):
                article_url = "https://www.cms.gov" + article_url

            cms_headline[1] = title
            now = datetime.now(ZoneInfo("America/New_York"))

            if cms_headline[0] != cms_headline[1]:
                if any(kw in title.lower() for kw in CRITICAL_KEYWORDS):
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t CMS \t {highlighted} \t {date_str}")
                    print("Link:", article_url)
                    webbrowser.open_new_tab(article_url)
                else:
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t CMS \t {title} \t {date_str}")
                    print("Link:", article_url)

                # beep in either case
                SOUNDS.play("cms", stop_current=True)
                cms_headline[0] = cms_headline[1]

            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in cms():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
# -----------------------------
# Keywords for FrontOfficeSports
# -----------------------------
frontoffice_keywords = [
    # fill with whatever you want; examples:
    "exclusive", "scoop", "deal", "merger", "acquires", "acquisition",
    "rights", "streaming", "sale", "auction", "round", "raises",
    "sponsor", "sponsorship", "partnership", "sec filing", "ipo","gambling","tax","betting","bets","gamblers","wagers","levy"
]

# keep track of what we've already seen
fos_seen_titles = []

def frontofficesports(keywords=None):
    if keywords is None:
        keywords = frontoffice_keywords
    # normalize once
    kw_lower = [k.lower() for k in keywords]

    session = requests.Session()
    request_count = 0
    max_requests_per_session = 6

    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
    })

    url = "https://frontofficesports.com/"

    while True:
        try:
            if request_count >= max_requests_per_session:
                session.close()
                session = requests.Session()
                session.mount("https://", adapter)
                session.mount("http://", adapter)
                session.headers.update({
                    'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
                })
                request_count = 0

            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"FOS: status {resp.status_code}")
                time.sleep(random.uniform(3.7, 5.4))
                continue

            soup = BeautifulSoup(resp.text, "html.parser")

            # find *all* exclusive cards
            cards = soup.find_all("div", class_="cardv2-wrapper")
            exclusive_cards = [c for c in cards if c.find("span", class_="card-pill--exclusive")]

            # if there's a featured exclusive, only open that; otherwise open every exclusive
            featured = soup.select_one("div.home-hero23__featured .cardv2-wrapper")
            if featured:
                cards_to_process = [featured]
            else:
                cards_to_process = exclusive_cards

            for card in cards_to_process:
                heading = card.find("a", class_="card-heading")
                if not heading:
                    continue
                title = heading.get_text(strip=True)
                link  = heading.get("href")

                if not title or title in fos_seen_titles:
                    continue
                fos_seen_titles.append(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lower_title = title.lower()

                # ---------- CRITICAL KEYWORD LOGIC (like your marijuana_moment snippet) ----------
                is_critical = any(kw in lower_title for kw in kw_lower)

                if is_critical:
                    highlighted_title = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now} FOS \t {highlighted_title}")
                    print(f"Link: {link}")
                    # only open and play sound on keyword hit
                    webbrowser.open_new_tab(link)
                    try:
                        SOUNDS.play("front office", stop_current=True)
                    except Exception:
                        # fall back to console bell if your soundboard isn't available
                        print("\a", end="")
                else:
                    # no tab, no sound—just print in blue
                    print(f"\033[94m{now} FOS\033[0m \t {title}")
                    print(f"Link: {link}")
                # -------------------------------------------------------------------------------

            request_count += 1
            time.sleep(random.uniform(3.7, 5.4))

        except Exception as e:
            print("Error in frontofficesports():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.7, 5.4))
cms_headline = ["", ""]

def cms():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    from zoneinfo import ZoneInfo
    import time
    import random
    import webbrowser
    import winsound
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style
    import traceback

    # --- Session with retry ---
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

    # --- Headers & UA ---
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.cms.gov/about-cms/contact/newsroom',
        'Connection': 'keep-alive'
    })

    base_url = "https://www.cms.gov/about-cms/contact/newsroom"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"CMS: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            wrapper = soup.find("div", class_="views-infinite-scroll-content-wrapper")
            if not wrapper:
                print("CMS: Could not find the articles container.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            row = wrapper.find("div", class_="views-row")
            if not row:
                print("CMS: Could not find a newsroom item.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # Extract date, title, link
            time_tag = row.find("time", datetime=True)
            date_str = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else time_tag.get_text(strip=True)
            title = row.find("h3").get_text(strip=True)
            a_tag = row.find("a", class_="newsroom-main-view-link", href=True)
            if not a_tag:
                print("CMS: Could not find the article link.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            article_url = a_tag["href"]
            if article_url.startswith("/"):
                article_url = "https://www.cms.gov" + article_url

            cms_headline[1] = title
            now = datetime.now(ZoneInfo("America/New_York"))

            if cms_headline[0] != cms_headline[1]:
                if any(kw in title.lower() for kw in CRITICAL_KEYWORDS):
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t CMS \t {highlighted} \t {date_str}")
                    print("Link:", article_url)
                    webbrowser.open_new_tab(article_url)
                else:
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S %Z')} \t CMS \t {title} \t {date_str}")
                    print("Link:", article_url)
                    webbrowser.open_new_tab(article_url)

                # beep in either case
                SOUNDS.play("cms", stop_current=True)
                cms_headline[0] = cms_headline[1]

            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in cms():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
import urllib.parse
# global state for last seen headline

# global state
zuck_headline = ["", ""]

# keywords to watch for
ZUCK_KEYWORDS = {
    "hyperscale",
    "AI",           # exact‑match via regex
    "compute",
    "nvidia",
    "amd",
    "supercomputer",
    "chips",
    "GPU",
    "CPU",
    "cluster",
    "capital",
    "billion",
    "acquisition"
}

# --- Session with retry (exactly like cms) ---
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

# --- Headers & UA (mirror cms) ---
ua = random.choice(USER_AGENTS_DATA)['ua']
session.headers.update({
    'User-Agent': ua,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.threads.com/@zuck?hl=en',
    'Connection': 'keep-alive'
})

def zuck():
    base_url = "https://www.threads.com/@zuck?hl=en"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Zuck: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")

            # more robust: use a CSS selector for the column body
            container = soup.select_one('div[aria-label="Column body"]')
            if not container:
                print("Zuck: could not find the column body.")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # first post link
            post_link = container.select_one('a[href^="/@zuck/post/"]')
            if not post_link:
                print("Zuck: no posts found")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            post_url = "https://www.threads.com" + post_link["href"]

            # pull the text out of the <div class="x1a6qonq"> that follows
            text_div = container.find(
                "div", class_=lambda c: c and "x1a6qonq" in c.split()
            )
            text = text_div.get_text(strip=True) if text_div else "[no text]"

            zuck_headline[1] = text
            now = datetime.now(ZoneInfo("America/New_York"))
            ts = now.strftime('%Y-%m-%d %H:%M:%S %Z')

            if zuck_headline[0] != zuck_headline[1]:
                # keyword check
                hit = False
                lower = text.lower()
                for kw in ZUCK_KEYWORDS:
                    if kw == "AI":
                        if re.search(r"\bAI\b", text):
                            hit = True
                            break
                    else:
                        if kw.lower() in lower:
                            hit = True
                            break

                if hit:
                    hl = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{text}{Style.RESET_ALL}"
                    print(f"{ts}\tZUCK\t{hl}")
                else:
                    print(f"{ts}\tZUCK\t{text}")
                print("Link:", post_url)

                webbrowser.open_new_tab(post_url)
                winsound.Beep(1000, 200)
                zuck_headline[0] = zuck_headline[1]

            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in zuck():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
# … your existing imports …

# track last seen Xinhua headline
xinhua_headline = ["", ""]

# keywords to trigger beep/open
XINHUA_KEYWORDS = ["US", "tariffs", "deal", "Trump", "agreement", "negotiation"]

def xinhua():
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
        'Referer': 'https://english.news.cn/list/latestnews.htm',
        'Connection': 'keep-alive'
    })

    base_url = "https://english.news.cn/list/latestnews.htm"

    while True:
        try:
            resp = session.get(base_url, timeout=15)
            if resp.status_code != 200:
                print(f"Xinhua: Received status code {resp.status_code}")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            item = soup.find("div", class_="item")
            if not item:
                print("Xinhua: Could not find any .item")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            tit = item.find("div", class_="tit")
            if not tit:
                print("Xinhua: Missing .tit container")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            a_tag = tit.find("a", href=True)
            if not a_tag:
                print("Xinhua: No <a> in .tit")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # get title & normalized URL
            title = a_tag.get_text(strip=True)
            href = a_tag["href"]
            article_url = urllib.parse.urljoin(base_url, href)

            # only proceed on new headlines
            xinhua_headline[1] = title
            if xinhua_headline[0] != xinhua_headline[1]:
                lowercase = title.lower()
                # look for any trigger keyword
                if any(kw.lower() in lowercase for kw in XINHUA_KEYWORDS):
                    now = datetime.now(ZoneInfo("America/New_York"))
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now:%Y-%m-%d %H:%M:%S %Z} \t Xinhua \t {highlighted}")
                    print("Link:", article_url)
                    webbrowser.open_new_tab(article_url)
                    winsound.Beep(1000, 200)
                else:
                    print(f"Xinhua: skipping (no keyword) — {title}")
                # update last seen
                xinhua_headline[0] = xinhua_headline[1]

            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print(f"Xinhua: Exception occurred: {e}")
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
endpts_headline = [""]    # only need one slot now

def endpts():
    import requests
    import random
    import time
    import winsound
    import webbrowser
    import traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from colorama import Fore, Back, Style

    # match channel<span> text after lowercasing & space→hyphen
    CHANNEL_FILTER = {"deals", "r&d", "fda+", "pharma", "news-briefing", "law"}

    seen = endpts_headline

    while True:
        try:
            resp = requests.get(
                "https://endpoints.news/news/",
                headers={'User-Agent': random.choice(USER_AGENTS_DATA)['ua']},
                timeout=10
            )
            resp.raise_for_status()
            soup = BeautifulSoup(resp.content, "lxml")

            # only scrape the “latest” grid
            items = soup.select("div.epn_result_list.epn_4_column .epn_item")

            # pick the first item whose channel matches your filter
            selected = None
            for item in items:
                chans = [
                    span.get_text(strip=True)
                        .lower()
                        .replace(" ", "-")
                    for span in item.select(".epn_channel span")
                ]
                if set(chans) & CHANNEL_FILTER:
                    selected = item
                    break

            if not selected:
                print("No matching Endpts item right now.")
                time.sleep(random.uniform(2.5, 3.25))
                continue

            # pull its headline/link
            a = selected.select_one("h3 a")
            if not a:
                print("Endpts: couldn’t find headline link on selected item.")
                time.sleep(5)
                continue

            title = a.get_text(strip=True)
            link  = a["href"]
            if not link.startswith("http"):
                link = "https://endpoints.news" + link

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if title != seen[0]:
                # optional: highlight “rescheduling”
                if "rescheduling" in title.lower():
                    title = f"{Fore.BLACK}{Back.GREEN}{Style.BRIGHT}{title}{Style.RESET_ALL}"

                print(f"\033[94m{now} Endpts\033[0m\t{title}")
                print(f"Link: {link}")

                # beep & open
                SOUNDS.play("endpoints", stop_current=True)
                webbrowser.open_new_tab(link)

                seen[0] = title

            time.sleep(random.uniform(2.5, 3.25))

        except Exception as e:
            print("Error in endpts():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))


# keep track of which headlines we’ve already seen
times_seen = set()

def times():
    import requests
    import random
    import time
    import winsound
    import webbrowser
    import traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style

    # --- session + retry logic ---
    session = requests.Session()
    retry_strategy = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
    })

    url = "https://www.thetimes.com/business-money/"

    while True:
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.content, "lxml")

            # grab lead article + any css-13fsqun cards
            blocks = []
            lead = soup.select_one("div[data-testid='lead-article']")
            if lead:
                blocks.append(lead)
            blocks.extend(soup.select("div.css-13fsqun"))

            for block in blocks:
                info = block.select_one("div.article-info")
                # only proceed if there's an EXCLUSIVE tag
                if not info or not info.find(string=lambda t: "EXCLUSIVE" in t.upper()):
                    continue

                # find the headline text + link
                a = block.select_one("a.article-headline, a.css-1vzp0s9, a.css-19kydsy")
                if not a:
                    continue
                span = a.find("span")
                title = span.get_text(strip=True) if span else a.get_text(strip=True)
                link  = a["href"]
                if not link.startswith("http"):
                    link = "https://www.thetimes.com" + link

                # skip duplicates
                if title in times_seen:
                    continue
                times_seen.add(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # always highlight exclusive ones
                highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                print(f"{now} Times\t{highlighted}")
                print(f"Link: {link}")

                # open and beep
                webbrowser.open_new_tab(link)
                SOUNDS.play("times", stop_current=True)

            # poll every 5–7 minutes
            time.sleep(random.uniform(300, 420))

        except Exception as e:
            print("Error in times():", e)
            traceback.print_exc()
            # wait a minute before retry
            time.sleep(random.uniform(3.5, 4.25))

semi_seen = set()

def semiaccurate():
    import requests, random, time, winsound, webbrowser, traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry

    # session + retries
    session = requests.Session()
    retry = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    feed_url = "https://www.semiaccurate.com/feed/"

    while True:
        try:
            resp = session.get(feed_url, timeout=10)
            resp.raise_for_status()

            # parse as XML
            soup = BeautifulSoup(resp.content, "xml")
            item = soup.find("item")
            if not item:
                time.sleep(random.uniform(3.9, 6.25))
                continue

            title = item.find("title").get_text(strip=True)
            link  = item.find("link").get_text(strip=True)

            # only announce if truly new
            if title not in semi_seen:
                semi_seen.add(title)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{now} SemiAccurate\t{title}")
                print(f"Link: {link}")

                # open & beep
                webbrowser.open_new_tab(link)
                SOUNDS.play("semiaccurate", stop_current=True)

            # pause before polling again
            time.sleep(random.uniform(4.6, 5.75))

        except Exception as e:
            print("Error in semiaccurate():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.85, 4.65))

cnbc_seen = set()

def cnbc_tech():
    import requests, random, time, winsound, webbrowser, traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style

    # session + retry
    session = requests.Session()
    retry = Retry(total=4, backoff_factor=1,
                  status_forcelist=[429,500,502,503,504],
                  allowed_methods=["GET","HEAD","OPTIONS"])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({'User-Agent': random.choice(USER_AGENTS_DATA)['ua']})

    url = "https://www.cnbc.com/technology/"

    while True:
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.content, "lxml")

            # grab the top featured card
            row = soup.select_one("div.TwoColumnImageDense-pageRow")
            if not row:
                time.sleep(random.uniform(3.5, 4.25))
                continue

            card = row.select_one("a.Card-title")
            if not card:
                time.sleep(random.uniform(3.5, 4.25))
                continue

            title = card.get_text(strip=True)
            link  = card["href"]
            if not link.startswith("http"):
                link = "https://www.cnbc.com" + link

            if title not in cnbc_seen:
                cnbc_seen.add(title)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                is_critical = any(kw.lower() in title.lower() for kw in CRITICAL_KEYWORDS)

                if is_critical:
                    highlighted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now} CNBC-Tech\t{highlighted}")
                    webbrowser.open_new_tab(link)
                    SOUNDS.play("cnbc", stop_current=True)
                else:
                    print(f"{now} CNBC-Tech\t{title}")

                print(f"Link: {link}")

            time.sleep(random.uniform(3.5, 4.25))  # poll every 3–5 minutes

        except Exception as e:
            print("Error in cnbc_tech():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
bi_seen = set()

def business_insider_tech():
    import requests, random, time, winsound, webbrowser, traceback
    from bs4 import BeautifulSoup
    from datetime import datetime
    from requests.adapters import HTTPAdapter, Retry
    from colorama import Fore, Back, Style

    # — Session + retry strategy —
    session = requests.Session()
    retry = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({
        'User-Agent': random.choice(USER_AGENTS_DATA)['ua']
    })

    url = "https://www.businessinsider.com/tech"
    while True:
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.content, "lxml")

            # container of all the "tout" articles
            container = soup.select_one("div.vertical-floats.primary-vertical")
            if not container:
                print("BI-Tech: container not found")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            # grab each article card
            articles = container.select("article.tout")
            if not articles:
                print("BI-Tech: no touts found")
                time.sleep(random.uniform(3.5, 4.25))
                continue

            for art in articles:
                # title + link
                a = art.select_one("h3.tout-title a")
                if not a:
                    continue
                title = a.get_text(strip=True)
                href  = a["href"]
                if not href.startswith("http"):
                    href = "https://www.businessinsider.com" + href

                # skip already seen
                if title in bi_seen:
                    continue
                bi_seen.add(title)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                is_excl = bool(art.select_one("div.stamp.as-exclusive"))
                if is_excl:
                    hl = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{title}{Style.RESET_ALL}"
                    print(f"{now} BI-Tech\t{hl}")
                    print(f"Link: {href}")
                    webbrowser.open_new_tab(href)
                    SOUNDS.play("business insider", stop_current=True)
                else:
                    print(f"{now} BI-Tech\t{title}")
                    print(f"Link: {href}")

            # poll every ~3.5–4.25 minutes
            time.sleep(random.uniform(3.5, 4.25))

        except Exception as e:
            print("Error in business_insider_tech():", e)
            traceback.print_exc()
            time.sleep(random.uniform(3.5, 4.25))
# --- StreetInsider scrapers: Hot M&A + Hot Corp. News ---
si_ma_seen   = set()
si_corp_seen = set()

def _build_si_session(http2=True, impersonate="chrome124"):
    """
    curl_cffi version-tolerant session constructor (same idea as axios).
    Tries http2/h2, then falls back to no explicit H2 flag.
    """
    kwargs = dict(impersonate=impersonate)
    s = None
    can_toggle_h2 = False

    for attempt in ({"http2": http2}, {"h2": http2}, {}):
        try:
            s = curlreq.Session(**kwargs, **attempt)
            can_toggle_h2 = bool(attempt)  # only True if a flag was accepted
            break
        except TypeError:
            continue
    if s is None:
        s = curlreq.Session(**kwargs)

    s._can_toggle_h2 = can_toggle_h2

    s.headers.update({
        "authority": "www.streetinsider.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "upgrade-insecure-requests": "1",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.streetinsider.com/",
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"),
        # uncomment if you see long-lived stalls:
        # "connection": "close",
    })
    # Warm cookies/consent best-effort
    try:
        s.get("https://www.streetinsider.com/", timeout=6)
    except Exception:
        pass
    return s

def _si_fetch(session, url, timeout=10, referer="https://www.streetinsider.com/"):
    """
    Direct fetch first; on 403 (or direct exception), try read-only mirror (r.jina.ai) once.
    Returns (bytes, used_fallback: bool).
    """
    try:
        r = session.get(url, timeout=timeout, headers={"Referer": referer})
        if r.status_code == 200:
            return r.content, False
        if r.status_code not in (401, 402, 403):
            r.raise_for_status()
    except Exception:
        # fall through to mirror
        pass

    # 403 or direct failure -> r.jina.ai mirror
    p = urlparse(url)
    mirror = f"https://r.jina.ai/{p.scheme}://{p.netloc}{p.path}"
    if p.query:
        mirror += f"?{p.query}"
    r2 = session.get(mirror, timeout=timeout)
    r2.raise_for_status()
    return r2.content, True

def _streetinsider_core(page_url, feed_name, seen_set, sound_name="street insider",
                        poll_range=(5.0, 7.0)):  # set to (3.0, 5.0) if you insist on super fast
    """
    Axios-like poller for a single SI page (Hot M&A or Hot Corp).
    Handles recycle, timeouts, H2 flip, WAF cool-downs, parsing, sound, dedupe.
    """
    session = _build_si_session(http2=True)
    use_http2 = True
    last_recycle = datetime.utcnow()
    req_count = 0
    consec_fail = 0

    while True:
        try:
            # recycle every N requests or after some time
            if req_count >= 400 or (datetime.utcnow() - last_recycle) > timedelta(minutes=20):
                session.close()
                session = _build_si_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0

            # quick request (single total timeout). retry once on CurlTimeout
            try:
                html, used_fallback = _si_fetch(session, page_url, timeout=8)
            except CurlTimeout:
                try:
                    html, used_fallback = _si_fetch(session, page_url, timeout=8)
                except CurlTimeout as e:
                    raise  # to outer handler

            # if direct fetch returned a WAF code we didn't catch, handle here
            # (we only get here with bytes, or _si_fetch raised)
            req_count += 1
            consec_fail = 0

            soup = BeautifulSoup(html, "lxml")
            # Same selector you used: StreetInsider list rows
            items = soup.select("dl.news_list > dt")

            if not items:
                # SI sometimes serves empty body when touchy -> brief cooldown
                print(f"[{feed_name}] no items found; short sleep")
                time.sleep(random.uniform(8, 12))
            else:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for dt in items:
                    a = dt.select_one("a.story_title")
                    if not a:
                        continue

                    href = (a.get("href") or "").strip()
                    classes = set(a.get("class") or [])

                    # skip premium/blurred rows
                    if "PremiumTip" in classes or "login.php" in href:
                        continue

                    if href.startswith("//"):
                        link = "https:" + href
                    elif href.startswith("http"):
                        link = href
                    else:
                        link = urljoin("https://www.streetinsider.com/", href)

                    title = a.get_text(strip=True)
                    if not title or title in seen_set:
                        continue
                    seen_set.add(title)

                    print(f"{now} {feed_name}\t{title}")
                    print(f"Link: {link}")
                    if used_fallback:
                        print(f"[{feed_name}] served via mirror fallback")

                    try:
                        SOUNDS.play(sound_name, stop_current=True)
                    except Exception:
                        pass

            # normal cadence
            time.sleep(random.uniform(*poll_range))

        except CurlTimeout as e:
            print(f"[{feed_name}] Timeout; recycle fast:", e)
            consec_fail += 1
            session.close()
            if consec_fail >= 3 and session._can_toggle_h2:
                use_http2 = not use_http2  # flip h2 <-> h1.1 after repeated timeouts
            session = _build_si_session(http2=use_http2)
            last_recycle = datetime.utcnow()
            req_count = 0
            time.sleep(random.uniform(4, 7))

        except RequestException as e:
            # covers curl_cffi network errors
            print(f"[{feed_name}] RequestException; soft backoff:", e)
            consec_fail += 1
            if consec_fail >= 2:
                session.close()
                session = _build_si_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))

        except Exception as e:
            print(f"[{feed_name}] Error:", e)
            traceback.print_exc()
            consec_fail += 1
            if consec_fail >= 2:
                session.close()
                session = _build_si_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))

# ----------------- Thin wrappers for your two SI feeds -----------------

def streetinsider_hot_ma(sound_name="street insider", poll_range=(4.0, 6.0)):
    _streetinsider_core(
        page_url="https://www.streetinsider.com/Hot+M+and+A/",
        feed_name="SI Hot M&A",
        seen_set=si_ma_seen,
        sound_name=sound_name,
        poll_range=poll_range,
    )

def streetinsider_hot_corp(sound_name="street insider", poll_range=(4.0, 6.0)):
    _streetinsider_core(
        page_url="https://www.streetinsider.com/Hot+Corp.+News",
        feed_name="SI Hot Corp",
        seen_set=si_corp_seen,
        sound_name=sound_name,
        poll_range=poll_range,
    )
# ======================================================================
import threading

si_ma_thread   = threading.Thread(target=streetinsider_hot_ma,   kwargs={"sound_name":"street insider", "poll_range":(4.0, 6.0)}, daemon=True)
si_corp_thread = threading.Thread(target=streetinsider_hot_corp, kwargs={"sound_name":"street insider", "poll_range":(4.0, 6.0)}, daemon=True)

# si_ma_thread.start()
# si_corp_thread.start()
# --- Add near your globals ---
axios_seen = set()
# pip install curl-cffi bs4 lxml
from curl_cffi import requests as curlreq
from curl_cffi.requests.exceptions import Timeout as CurlTimeout, RequestException
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time, random, traceback

axios_seen = set()
def _build_axios_session(http2=True, impersonate="chrome124"):
    """
    Works across curl_cffi versions:
    - old releases: support http2= (bool)
    - 0.14.x: http2 kw no longer accepted by BaseSession; some builds use h2=
    - fallback: no explicit H2 flag
    """
    kwargs = dict(impersonate=impersonate)
    s = None
    can_toggle_h2 = False

    # Try newest/oldest possibilities in order
    for attempt in ({"http2": http2}, {"h2": http2}, {}):
        try:
            s = curlreq.Session(**kwargs, **attempt)
            # if we created it with a recognized H2 flag, we can toggle later
            can_toggle_h2 = bool(attempt)
            break
        except TypeError:
            continue

    if s is None:
        # last-resort constructor
        s = curlreq.Session(**kwargs)

    # mark capability for later toggling
    s._can_toggle_h2 = can_toggle_h2

    s.headers.update({
        "authority": "www.axios.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "upgrade-insecure-requests": "1",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.axios.com/pro",
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"),
        # If you still see long-lived socket stalls, uncomment to force short connections:
        # "connection": "close",
    })
    try:
        # warm cookies/consent; best-effort
        s.get("https://www.axios.com/", timeout=6)
    except Exception:
        pass
    return s

def axios_all_deals(sound_name="axios", poll_range=(3.0, 5.0)):
    """
    Fast (3–5s) poller with self-healing against stalls/timeouts.
    """
    url = "https://www.axios.com/pro/all-deals"

    session = _build_axios_session(http2=True)
    use_http2 = True
    last_recycle = datetime.utcnow()
    req_count = 0
    consec_fail = 0

    while True:
        try:
            # ---- recycle policy: time-based or count-based
            if req_count >= 400 or (datetime.utcnow() - last_recycle) > timedelta(minutes=20):
                session.close()
                session = _build_axios_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0

            # ---- do a quick request with short timeouts
            # curl_cffi has a single timeout param = total; emulate quick retry ourselves
            try:
                resp = session.get(url, timeout=7)
            except CurlTimeout:
                # one fast retry on timeout
                try:
                    resp = session.get(url, timeout=7)
                except CurlTimeout as e:
                    raise  # bubble to outer except to trigger recycle/backoff

            # handle WAF / rate-limit codes distinctly
            if resp.status_code in (401, 402, 403, 429, 503):
                print(f"[Axios] {resp.status_code} from edge. Cooldown.")
                consec_fail += 1
                # short cool down, then continue
                time.sleep(random.uniform(12, 18))
                continue

            resp.raise_for_status()
            req_count += 1
            consec_fail = 0

            soup = BeautifulSoup(resp.content, "lxml")
            anchors = soup.select('a[data-cy="story-summary-header"], a[data-cy="story-promo-headline"]')

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for a in anchors:
                title = a.get_text(strip=True)
                href = a.get("href") or ""
                if href and not href.startswith("http"):
                    href = "https://www.axios.com" + href
                if not title or not href or title in axios_seen:
                    continue

                axios_seen.add(title)
                print(f"{now} Axios\t{title}")
                print(f"Link: {href}")
                try:
                    SOUNDS.play(sound_name, stop_current=True)
                except Exception:
                    pass

            # normal fast cadence
            time.sleep(random.uniform(*poll_range))

        except CurlTimeout as e:
            # timeout after hours => likely stale h2 stream or dropped keep-alive
            print("[Axios] Timeout; will recycle session quickly:", e)
            consec_fail += 1
            session.close()

            # after a few consecutive timeouts, flip protocol to avoid h2 stalls
            if consec_fail >= 3:
                use_http2 = not use_http2  # toggle h2 <-> h1.1
            session = _build_axios_session(http2=use_http2)
            last_recycle = datetime.utcnow()
            req_count = 0

            # brief backoff but stay snappy
            time.sleep(random.uniform(4, 7))

        except RequestException as e:
            # other curl_cffi errors
            print("[Axios] RequestException; soft backoff:", e)
            consec_fail += 1
            if consec_fail >= 2:
                # recycle on repeated generic failures
                session.close()
                session = _build_axios_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))

        except Exception as e:
            # catch-all so your supervisor never dies
            print("[Axios] Error in axios_all_deals():", e)
            traceback.print_exc()
            consec_fail += 1
            if consec_fail >= 2:
                session.close()
                session = _build_axios_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))



# somewhere in your startup:
# session = make_shared_session_like_your_other_scrapers()



# Example: run each in its own thread (like your other scrapers)
import threading
# # si_ma_thread   = threading.Thread(target=streetinsider_hot_ma,   daemon=True)
# # si_corp_thread = threading.Thread(target=streetinsider_hot_corp, daemon=True)
# si_ma_thread.start()
# si_corp_thread.start()
axios_thread = threading.Thread(target=axios_all_deals, daemon=True)
axios_thread.start()
bi_thread = threading.Thread(target=business_insider_tech, daemon=True)
bi_thread.start()
# run in its own thread
cnbc_thread = threading.Thread(target=cnbc_tech, daemon=True)
cnbc_thread.start()
# run it in its own thread so it won’t block your REPL
# semi_thread = threading.Thread(target=semiaccurate, daemon=True)
# semi_thread.start()

times_thread = threading.Thread(target=times)
times_thread.start()
logic_thread = threading.Thread(target=logic)
logic_thread.start()
#
#
# endpt_thread = threading.Thread(target=endpts)
# endpt_thread.start()

# To run the Variety function in its own thread:
variety_thread = threading.Thread(target=variety)
variety_thread.start()


# Start NY Post thread (similar modifications can be applied to other functions)
nypost_thread = threading.Thread(target=nypost)
nypost_thread.start()
whitehouse_thread = threading.Thread(target=whitehouse_news)
whitehouse_thread.start()
fda_thread = threading.Thread(target=fda)
fda_thread.start()
# ----------------- Start threads for the new functions -----------------
nikkei_thread = threading.Thread(target=nikkei)
statnews_thread = threading.Thread(target=statnews)
# nypost_thread = threading.Thread(target=nypost)
information_thread= threading.Thread(target=information)
# nikkei_thread.start()
statnews_thread.start()

# yuyuan_thread = threading.Thread(target=yuyuan)
# yuyuan_thread.start()
#
marijuanamoment_thread = threading.Thread(target=marijuanamoment)
marijuanamoment_thread.start()

cms_thread = threading.Thread(target=cms)
cms_thread.start()

# techcrunch_thread = threading.Thread(target=techcrunch)
# techcrunch_thread.start()

# xinhua_thread = threading.Thread(target=xinhua)
# xinhua_thread.start()
#
# semafor_rohan_thread = threading.Thread(target=semafor_rohan)
# semafor_rohan_thread.start()
# semafor_gillian_thread = threading.Thread(target=semafor_gillian)
# semafor_gillian_thread.start()
frontofficesports_thread = threading.Thread(target=frontofficesports)
frontofficesports_thread.start()

ftc_thread = threading.Thread(target=ftc)
ftc_thread.start()

# fhfa_thread = threading.Thread(target=fhfa)
# fhfa_thread.start()
openai_thread = threading.Thread(target=openai_news)
openai_thread.start()

# nvidia_thread = threading.Thread(target=nvidia_news_latest_only)
# nvidia_thread.start()
# zuck_thread = threading.Thread(target=zuck)
# zuck_thread.start()
# nypost_thread.start()
# information_thread.start()
# Start the threads
# nytimes_thread = threading.Thread(target=nytimes)
# nytimes_thread.start()
#
# wsj_business_thread = threading.Thread(target=wsj_business)
# wsj_business_thread.start()
#
# wsj_markets_thread = threading.Thread(target=wsj_markets)
# wsj_markets_thread.start()
#
# marketwatch_thread = threading.Thread(target=marketwatch)
# marketwatch_thread.start()
#
# reuters_thread = threading.Thread(target=reuters)
# reuters_thread.start()
#
# bloomberg_markets_thread = threading.Thread(target=bloomberg_markets)
# bloomberg_markets_thread.start()
#
# bloomberg_industries_thread = threading.Thread(target=bloomberg_industries)
# bloomberg_industries_thread.start()
#
# wapo_business_thread = threading.Thread(target=wapo_business)
# wapo_business_thread.start()
#
# wapo_national_thread = threading.Thread(target=wapo_national)
# wapo_national_thread.start()

