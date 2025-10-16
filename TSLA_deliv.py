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
import traceback
from zoneinfo import ZoneInfo

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
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 10; 22033PC75G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36 YaBrowser/20.1"},
    {"ua": "Mozilla/5.0 (Linux; arm_64; Android 12; 24030PN60G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 10; SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"},
    {"ua": "Mozilla/5.0 (Linux; Android 12; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36"},
]

ua = random.choice(USER_AGENTS_DATA)['ua']
headers = {'User-Agent': ua}
# Initialize colorama globally
colorama.init(autoreset=True)

# Global headline tracker for Tesla
tesla_headline = ["", ""]

def tesla():
    # Create a session with a retry adapter to reduce timeout errors
    session = requests.Session()
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set session headers using a rotating user-agent (assumes USER_AGENTS_DATA is defined)
    ua = random.choice(USER_AGENTS_DATA)['ua']
    session.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://ir.tesla.com/press',
        'Connection': 'keep-alive',
        # Additional headers to mimic a real browser:
        'sec-ch-ua': '"Chromium";v="115", "Not A;Brand";v="24", "Google Chrome";v="115"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1'
    })

    # URL to scrape
    base_url = "https://ir.tesla.com/press"

    while True:
        try:
            resp = session.get(base_url, timeout=.6)
            if resp.status_code != 200:
                print(f"Tesla: Received status code {resp.status_code}")
                time.sleep(random.uniform(1.5, 2.6))
                continue

            soup = BeautifulSoup(resp.content, "lxml")
            # (Rest of your code remains unchanged.)
            rows = soup.find_all("div", class_="views-row")
            production_item = None
            for row in rows:
                teaser = row.find("section", class_="press-release-teaser")
                if teaser:
                    h4_tag = teaser.find("h4", class_="press-release-teaser__title")
                    if h4_tag:
                        a_tag = h4_tag.find("a", href=True)
                        if a_tag and "production" in a_tag.get_text(strip=True).lower():
                            production_item = a_tag
                            break
            if not production_item:
                print("Tesla: Could not find a press release with 'Production' in the headline.")
                time.sleep(random.uniform(1.5, 2.6))
                continue

            title = production_item.get_text(strip=True)
            link = production_item['href']
            if not link.startswith("http"):
                link = "https://ir.tesla.com" + link

            tesla_headline[1] = title
            now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S %Z")
            if tesla_headline[0] != tesla_headline[1]:
                print(f"{now} \t Tesla \t {title}")
                print(f"Link: {link}")
                webbrowser.open_new_tab(link)

                # Now scrape the article page to get the delivery number
                resp_article = session.get(link, timeout=2.6)
                if resp_article.status_code != 200:
                    print(f"Tesla Article: Received status code {resp_article.status_code}")
                else:
                    article_soup = BeautifulSoup(resp_article.content, "lxml")
                    table = article_soup.find("table", class_="tds-table")
                    if table:
                        rows_table = table.find_all("tr")
                        delivery_number = None
                        for tr in rows_table:
                            if "total" in tr.get_text(strip=True).lower():
                                cells = tr.find_all("td")
                                if len(cells) >= 3:
                                    delivery_number = cells[2].get_text(strip=True)
                                    break
                        if delivery_number:
                            try:
                                # Remove commas and convert to integer
                                delivery_val = int(delivery_number.replace(",", "").strip())
                            except Exception as ex:
                                print("Error converting delivery number:", ex)
                                delivery_val = 0
                            # Determine highlight color based on value
                            if delivery_val > 5000000:
                                color = Back.GREEN + Fore.BLACK
                            elif 460000 <= delivery_val <= 500000:
                                color = Back.YELLOW + Fore.BLACK
                            else:  # delivery_val < 350000
                                color = Back.RED + Fore.BLACK

                            highlighted = f"{Style.BRIGHT}{color}{delivery_number}{Style.RESET_ALL}"
                            for _ in range(5):
                                print(highlighted)
                            winsound.Beep(1200, 100)
                            winsound.Beep(1200, 100)
                            winsound.Beep(1200, 100)
                        else:
                            print("Tesla: Could not extract delivery number from table.")
                    else:
                        print("Tesla: Could not find the delivery table in the article.")
                tesla_headline[0] = tesla_headline[1]
            time.sleep(random.uniform(.2, .5))
        except Exception as e:
            print("Error in tesla():", e)
            traceback.print_exc()
            time.sleep(random.uniform(1.5, 2.6))

tesla_thread = threading.Thread(target=tesla)
tesla_thread.start()
