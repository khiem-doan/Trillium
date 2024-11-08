# Import necessary libraries
from pandas import *
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timezone
import regex
import winsound
import threading
import webbrowser
import os  # For alternative method to open URLs
import traceback  # For enhanced exception handling

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

author = ""
tp_ticker = []

sec_filing = ["1.01:", "1.02:", "2.04:", "2.05", "3.01:", "4.02:", "7.01:", "8.01:"]

# 1. Updated Hunterbrook Function
def hntrbrk():
    while True:
        try:
            resp = requests.get("https://hntrbrk.com/feed/", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            results = soup.find("item")
            if not results:
                print("Hunterbrook: Could not find 'item' tag.")
                time.sleep(2)
                continue
            hntrbrk_headline[1] = results.title.string.strip()
            link = results.link.string.strip()
            find = results.find("description")
            if not find:
                print("Hunterbrook: Could not find 'description' tag.")
                time.sleep(2)
                continue
            desc = find.string.strip()
            now = datetime.now().time()
            if hntrbrk_headline[0] != hntrbrk_headline[1]:
                print(now, "\t", "Hunterbrook", "\t", hntrbrk_headline[1])
                print("Description:", desc)
                print("Article URL:", link)
                print("Attempting to open link:", link)
                # Try alternative method if webbrowser doesn't work
                try:
                    webbrowser.open_new_tab(link)
                except Exception as e:
                    print(f"Webbrowser failed to open link: {e}")
                    os.system(f'start {link}')  # For Windows
                    # os.system(f'open {link}')  # For macOS
                    # os.system(f'xdg-open {link}')  # For Linux
                winsound.Beep(2500, 400)
            hntrbrk_headline[0] = hntrbrk_headline[1]
            time.sleep(2)
        except Exception as e:
            import traceback
            print(f"Error in hntrbrk(): {e}")
            traceback.print_exc()
            time.sleep(2)

# 2. Updated Culper Function
def culper():
    while True:
        try:
            url = "https://culperresearch.com/latest-research"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': 'https://google.com',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            }
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Culper: Received status code {resp.status_code}")
                time.sleep(3)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the 'a' tag that contains the latest report link
            a_tag = soup.find('a', attrs={'data-aid': 'DOWNLOAD_DOCUMENT_LINK_WRAPPER_RENDERED'}, href=True)
            if not a_tag:
                print("Culper: Could not find the latest report link.")
                time.sleep(3)
                continue

            article_url = a_tag['href']
            # Ensure the URL is complete
            if article_url.startswith('//'):
                article_url = 'https:' + article_url
            elif article_url.startswith('/'):
                article_url = 'https://culperresearch.com' + article_url

            # Get the headline
            span_tag = a_tag.find('span', attrs={'data-ux': 'Element'})
            if not span_tag:
                print("Culper: Could not find the headline.")
                time.sleep(3)
                continue

            culper_headline[1] = span_tag.get_text(strip=True)
            now = datetime.now().time()
            if culper_headline[0] != culper_headline[1]:
                print(now, "\t", "Culper", "\t", culper_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            culper_headline[0] = culper_headline[1]
            time.sleep(3)
        except Exception as e:
            import traceback
            print(f"Error in culper(): {e}")
            traceback.print_exc()
            time.sleep(3)

# 3. Updated SEC8k Function
def sec8k():
    headers = {
        'User-Agent': 'Sample Company Name Khiem Doan, doan.khiem@gmail.com',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }
    # List of form types to filter
    form_type_filters = ["8-K"]  # You can add or remove form types here

    opened_links = set()
    script_start_time = datetime.now(timezone.utc)
    first_run = True  # Flag variable

    while True:
        try:
            url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=8-K&company=&dateb=&owner=include&start=0&count=40&output=atom"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"SEC 8K: Error fetching RSS feed: {resp.status_code} {resp.reason}")
                time.sleep(3)
                continue
            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'lxml-xml')
            entries = soup.find_all('entry')
            if not entries:
                print("SEC 8K: No entries found in the feed.")
                time.sleep(3)
                continue
            else:
                if first_run:
                    print(f"SEC 8K: Found {len(entries)} entries.")
                    first_run = False  # Set the flag to False after the first run

            for top_entry in entries:
                # Fetch the top link from the entry
                link_tag = top_entry.find('link')
                if link_tag and link_tag.get('href'):
                    top_link = link_tag['href']
                else:
                    continue

                # Get the form type and filter by the desired form types
                form_type = top_entry.category.get('term', 'Unknown')
                if not any(f_type in form_type for f_type in form_type_filters):
                    continue  # Skip if the form type is not in the filter list

                # Get the updated time of the entry
                updated_datetime_str = top_entry.updated.get_text()
                updated_datetime = datetime.strptime(updated_datetime_str, '%Y-%m-%dT%H:%M:%S%z')

                # Skip filings older than the script start time
                if updated_datetime <= script_start_time:
                    continue

                # Only process if this is a new link
                if top_link not in opened_links:
                    print(f"SEC 8K: Processing new filing: {top_link}")
                    # Fetching page content
                    page_resp = requests.get(top_link, headers=headers)
                    if page_resp.status_code != 200:
                        print(f"SEC 8K: Failed to fetch page {top_link}")
                        continue
                    page_soup = BeautifulSoup(page_resp.content, 'lxml')
                    # Find the document table
                    table = page_soup.find('table', class_='tableFile')
                    if not table:
                        print(f"SEC 8K: Could not find document table for {top_link}")
                        continue
                    # Find the row with the desired document
                    rows = table.find_all('tr')
                    for row in rows[1:]:
                        cols = row.find_all('td')
                        if len(cols) >= 4:
                            doc_type = cols[3].text.strip()
                            if doc_type == '8-K':
                                doc_link = cols[2].find('a', href=True)['href']
                                doc_url = 'https://www.sec.gov' + doc_link
                                print(f"SEC 8K: Opening document {doc_url}")
                                webbrowser.open_new_tab(doc_url)
                                winsound.Beep(2500, 200)
                                opened_links.add(top_link)
                                break
                    else:
                        print(f"SEC 8K: No suitable document found for {top_link}")

            time.sleep(3)
        except Exception as e:
            import traceback
            print(f"Error in sec8k(): {e}")
            traceback.print_exc()
            time.sleep(3)

# Note: Functions for Grizzly and Muddy Waters are omitted due to CAPTCHA protection.

# The rest of your functions remain unchanged, but with enhanced exception handling.

# Start the threads
scorpion_thread = threading.Thread(target=scorpion)
scorpion_thread.start()

iceberg_thread = threading.Thread(target=iceberg)
iceberg_thread.start()

hindenburg_thread = threading.Thread(target=hindenburg)
hindenburg_thread.start()

wolfpack_thread = threading.Thread(target=wolfpack)
wolfpack_thread.start()

culper_thread = threading.Thread(target=culper)
culper_thread.start()

kerrisdale_thread = threading.Thread(target=kerrisdale)
kerrisdale_thread.start()

spruce_thread = threading.Thread(target=spruce)
spruce_thread.start()

sec8k_thread = threading.Thread(target=sec8k)
sec8k_thread.start()

bleepcomp_thread = threading.Thread(target=bleepcomp)
bleepcomp_thread.start()

hntrbrk_thread = threading.Thread(target=hntrbrk)
hntrbrk_thread.start()

# Starting new threads for the added websites
bleecker_thread = threading.Thread(target=bleecker)
bleecker_thread.start()

# Note: Threads for Grizzly and Muddy Waters are omitted due to CAPTCHA protection.

fuzzypanda_thread = threading.Thread(target=fuzzypanda)
fuzzypanda_thread.start()

