# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import threading
import time
import webbrowser
import winsound
from datetime import datetime

# Initialize headline tracking lists
nytimes_headline = ["", ""]
wsj_business_headline = ["", ""]
wsj_markets_headline = ["", ""]
marketwatch_headline = ["", ""]
reuters_headline = ["", ""]
bloomberg_markets_headline = ["", ""]
bloomberg_industries_headline = ["", ""]
wapo_business_headline = ["", ""]
wapo_national_headline = ["", ""]

# Add filter keywords for each publisher
# Only headlines containing these keywords will trigger the opening of a new tab (when enabled)
filter_keywords = ["economy", "market", "stocks", "finance"]  # Modify as needed

# Define functions

def nytimes():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"NYTimes: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("NYTimes: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("NYTimes: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            nytimes_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if nytimes_headline[0] != nytimes_headline[1]:
                # Highlight the publisher name with a specific color (e.g., blue)
                print(f"\033[94m{now} NYTimes\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                nytimes_headline[0] = nytimes_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in nytimes():", e)
            time.sleep(5)

def wsj_business():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"WSJ Business: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("WSJ Business: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("WSJ Business: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            wsj_business_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if wsj_business_headline[0] != wsj_business_headline[1]:
                # Highlight the publisher name with a specific color (e.g., green)
                print(f"\033[92m{now} WSJ Business\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                wsj_business_headline[0] = wsj_business_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in wsj_business():", e)
            time.sleep(5)

def wsj_markets():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.a.dj.com/rss/RSSMarketsMain.xml"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"WSJ Markets: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("WSJ Markets: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("WSJ Markets: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            wsj_markets_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if wsj_markets_headline[0] != wsj_markets_headline[1]:
                # Highlight the publisher name with a specific color (e.g., cyan)
                print(f"\033[96m{now} WSJ Markets\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                wsj_markets_headline[0] = wsj_markets_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in wsj_markets():", e)
            time.sleep(5)

def marketwatch():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.content.dowjones.io/public/rss/mw_bulletins"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"MarketWatch: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("MarketWatch: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("MarketWatch: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            marketwatch_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if marketwatch_headline[0] != marketwatch_headline[1]:
                # Highlight the publisher name with a specific color (e.g., magenta)
                print(f"\033[95m{now} MarketWatch\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                marketwatch_headline[0] = marketwatch_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in marketwatch():", e)
            time.sleep(5)

def reuters():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://news.google.com/rss/search?q=site%3Areuters.com&hl=en-US&gl=US&ceid=US%3Aen"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Reuters: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("Reuters: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("Reuters: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            reuters_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if reuters_headline[0] != reuters_headline[1]:
                # Highlight the publisher name with a specific color (e.g., yellow)
                print(f"\033[93m{now} Reuters\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                reuters_headline[0] = reuters_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in reuters():", e)
            time.sleep(5)



def bloomberg_markets():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.bloomberg.com/markets/news.rss"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Bloomberg Markets: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("Bloomberg Markets: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("Bloomberg Markets: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            bloomberg_markets_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if bloomberg_markets_headline[0] != bloomberg_markets_headline[1]:
                # Highlight the publisher name with a specific color (e.g., red)
                print(f"\033[91m{now} Bloomberg Markets\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                bloomberg_markets_headline[0] = bloomberg_markets_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in bloomberg_markets():", e)
            time.sleep(5)

def bloomberg_industries():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.bloomberg.com/industries/news.rss"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Bloomberg Industries: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("Bloomberg Industries: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("Bloomberg Industries: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            bloomberg_industries_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if bloomberg_industries_headline[0] != bloomberg_industries_headline[1]:
                # Highlight the publisher name with a specific color (e.g., green)
                print(f"\033[92m{now} Bloomberg Industries\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                bloomberg_industries_headline[0] = bloomberg_industries_headline[1]
            time.sleep(5)  # Check every 5 minutes
        except Exception as e:
            print("Error in bloomberg_industries():", e)
            time.sleep(5)

def wapo_business():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.washingtonpost.com/rss/business"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"WaPo Business: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("WaPo Business: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            if not title_tag or not link_tag:
                print("WaPo Business: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            wapo_business_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if wapo_business_headline[0] != wapo_business_headline[1]:
                # Highlight the publisher name with a specific color (e.g., cyan)
                print(f"\033[96m{now} WaPo Business\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                wapo_business_headline[0] = wapo_business_headline[1]
            time.sleep(30)  # Check every 5 minutes
        except Exception as e:
            print("Error in wapo_business():", e)
            time.sleep(5)

def wapo_national():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://feeds.washingtonpost.com/rss/national"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"WaPo National: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("WaPo National: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            pubDate_tag = item.find('pubDate')
            category_tags = item.find_all('category')
            if not title_tag or not link_tag:
                print("WaPo National: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            pubDate = pubDate_tag.text.strip() if pubDate_tag else "No Date"
            categories = [cat.text.strip() for cat in category_tags]
            wapo_national_headline[1] = title
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if wapo_national_headline[0] != wapo_national_headline[1]:
                # Check if the article is under the "Investigation" category
                if "Investigation" in categories:
                    # Highlight the whole headline in bright color (e.g., red background)
                    print(f"\033[1;97;41m{now} WaPo National\t {title}\033[0m")
                else:
                    # Highlight the publisher name with a specific color (e.g., blue)
                    print(f"\033[94m{now} WaPo National\033[0m \t {title}")
                print(f"Link: {link}")

                # Check if the title contains any of the filter keywords
                if any(keyword.lower() in title.lower() for keyword in filter_keywords):
                    # Uncomment the following lines to enable opening the link
                    # webbrowser.open_new_tab(link)
                    # winsound.Beep(2500, 200)
                    pass  # Remove this pass statement if uncommenting the above lines

                wapo_national_headline[0] = wapo_national_headline[1]
            time.sleep(30)  # Check every 5 minutes
        except Exception as e:
            print("Error in wapo_national():", e)
            time.sleep(5)

# Start the threads
nytimes_thread = threading.Thread(target=nytimes)
nytimes_thread.start()

wsj_business_thread = threading.Thread(target=wsj_business)
wsj_business_thread.start()

wsj_markets_thread = threading.Thread(target=wsj_markets)
wsj_markets_thread.start()

marketwatch_thread = threading.Thread(target=marketwatch)
marketwatch_thread.start()

reuters_thread = threading.Thread(target=reuters)
reuters_thread.start()

bloomberg_markets_thread = threading.Thread(target=bloomberg_markets)
bloomberg_markets_thread.start()

bloomberg_industries_thread = threading.Thread(target=bloomberg_industries)
bloomberg_industries_thread.start()

wapo_business_thread = threading.Thread(target=wapo_business)
wapo_business_thread.start()

wapo_national_thread = threading.Thread(target=wapo_national)
wapo_national_thread.start()

