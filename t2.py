import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime,timezone
import regex
import winsound
import threading
import webbrowser

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
                print(f"SEC 8K: Found {len(entries)} entries.")

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
                    page_soup = BeautifulSoup(page_resp.content, 'html.parser')
                    # Find the document table
                    table = page_soup.find('table', class_='tableFile', summary='Document Format Files')
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
            print("Error in sec8k():", e)
            time.sleep(3)
sec8k_thread = threading.Thread(target=sec8k)
sec8k_thread.start()

