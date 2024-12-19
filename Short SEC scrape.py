# Import necessary libraries
from pandas import *
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime,timezone
import regex
import winsound
import threading
import webbrowser

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


author = ""
tp_ticker = []

# sec_filing = ["1.01:", "1.02:", "2.04:", "2.05", "3.01:", "4.02:", "7.01:", "8.01,","9.01:"]
# Initialize headline tracking list for J Capital
jcapital_headline = [0]*2

def jcapital():
    while True:
        try:
            url = "https://www.jcapitalresearch.com/company-reports.html"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"J Capital: Received status code {resp.status_code}")
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the div with class 'paragraph'
            paragraph_div = soup.find('div', class_='paragraph')
            if not paragraph_div:
                print("J Capital: Could not find 'div' with class 'paragraph'.")
                time.sleep(3.03)
                continue

            # Find the first <a> tag within this div
            a_tag = paragraph_div.find('a', href=True)
            if not a_tag:
                print("J Capital: Could not find 'a' tag with href.")
                time.sleep(3.03)
                continue

            article_url = a_tag['href']
            if not article_url.startswith('http'):
                article_url = 'https://www.jcapitalresearch.com' + article_url

            jcapital_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if jcapital_headline[0] != jcapital_headline[1]:
                print(now, "\t", "J Capital", "\t", jcapital_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            jcapital_headline[0] = jcapital_headline[1]
            time.sleep(3.03)
        except Exception as e:
            import traceback
            print(f"Error in jcapital(): {e}")
            traceback.print_exc()
            time.sleep(3.03)
# Initialize headline tracking list for Capybara
capybara_headline = [0]*2

def capybara():
    while True:
        try:
            url = "https://capybararesearch.com/"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Capybara: Received status code {resp.status_code}")
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the first article div
            article_div = soup.find('div', class_='relative w-100 mb4')
            if not article_div:
                print("Capybara: Could not find 'div' with class 'relative w-100 mb4'.")
                time.sleep(3.03)
                continue

            # Find the text content div
            text_div = article_div.find('div', class_='blah w-100 w-60-ns pl3-ns')
            if not text_div:
                print("Capybara: Could not find 'div' with class 'blah w-100 w-60-ns pl3-ns'.")
                time.sleep(3.03)
                continue

            # Find the <a> tag within the text content div
            a_tag = text_div.find('a', href=True)
            if not a_tag:
                print("Capybara: Could not find 'a' tag with href in text content.")
                time.sleep(3.03)
                continue

            article_url = a_tag['href']
            if not article_url.startswith('http'):
                article_url = 'https://capybararesearch.com' + article_url

            # Extract the headlines from the <h1> tags within the <a> tag
            h1_tags = a_tag.find_all('h1')
            if not h1_tags:
                print("Capybara: Could not find 'h1' tags within 'a' tag.")
                time.sleep(3.03)
                continue

            # Combine the text from both h1 tags
            capybara_headline[1] = ' '.join(h1.get_text(strip=True) for h1 in h1_tags)
            now = datetime.now().time()
            if capybara_headline[0] != capybara_headline[1]:
                print(now, "\t", "Capybara", "\t", capybara_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            capybara_headline[0] = capybara_headline[1]
            time.sleep(3.03)
        except Exception as e:
            import traceback
            print(f"Error in capybara(): {e}")
            traceback.print_exc()
            time.sleep(3.03)


# 3. Added Bleecker Street Function
def bleecker():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://www.bleeckerstreetresearch.com/research", headers=headers)
            if resp.status_code != 200:
                print(f"Bleecker: Received status code {resp.status_code}")
                time.sleep(5.1)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            # Find the first article
            article = soup.find('article', class_='blog-item')
            if not article:
                print("Bleecker: Could not find 'article' with class 'blog-item'.")
                time.sleep(5.1)
                continue

            # Find the 'a' tag with the link to the article
            a_tag = article.find('a', href=True)
            if not a_tag:
                print("Bleecker: Could not find 'a' tag with href in 'article'.")
                time.sleep(5.1)
                continue

            href = a_tag['href']
            if not href.startswith('http'):
                article_url = 'https://www.bleeckerstreetresearch.com' + href
            else:
                article_url = href

            bleecker_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if bleecker_headline[0] != bleecker_headline[1]:
                print(now, "\t", "Bleecker", "\t", bleecker_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            bleecker_headline[0] = bleecker_headline[1]
            time.sleep(5.1)
        except Exception as e:
            print("Error in bleecker():", e)
            time.sleep(5.1)


# 4. Added Muddy Waters Function
def muddywaters():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://muddywatersresearch.com/research/", headers=headers)
            if resp.status_code != 200:
                print(f"MuddyWaters: Received status code {resp.status_code}")
                time.sleep(5.1)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            # Find the first article
            article = soup.find('div', class_='reports-table__cell reports-table__cell--title')
            if not article:
                print("MuddyWaters: Could not find the article container.")
                time.sleep(5.1)
                continue

            # Find the 'a' tag with the link to the article
            a_tag = article.find('a', href=True)
            if not a_tag:
                print("MuddyWaters: Could not find 'a' tag with href.")
                time.sleep(5.1)
                continue

            article_url = a_tag['href']
            muddywaters_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if muddywaters_headline[0] != muddywaters_headline[1]:
                print(now, "\t", "MuddyWaters", "\t", muddywaters_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            muddywaters_headline[0] = muddywaters_headline[1]
            time.sleep(5.1)
        except Exception as e:
            print("Error in muddywaters():", e)
            time.sleep(5.1)


# 5. Added Grizzly Research Function
def grizzly():
    while True:
        try:
            # Use the URL you provided
            url = "https://grizzlyreports.com/category/research/"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': 'https://google.com',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            }
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Grizzly: Received status code {resp.status_code}")
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the first 'div' with class 'post__head'
            div_post_head = soup.find('div', class_='post__head')
            if not div_post_head:
                print("Grizzly: Could not find 'div' with class 'post__head'.")
                time.sleep(3.03)
                continue

            # Find the 'h3' tag with class 'post__title typescale-2' inside 'div_post_head'
            h3_title = div_post_head.find('h3', class_='post__title typescale-2')
            if not h3_title:
                print("Grizzly: Could not find 'h3' with class 'post__title typescale-2'.")
                time.sleep(3.03)
                continue

            # Find the 'a' tag inside the 'h3' tag
            a_tag = h3_title.find('a', href=True)
            if not a_tag:
                print("Grizzly: Could not find 'a' tag with href in 'h3'.")
                time.sleep(3.03)
                continue

            article_url = a_tag['href']
            grizzly_headline[1] = a_tag.get_text(strip=True)

            now = datetime.now().time()
            if grizzly_headline[0] != grizzly_headline[1]:
                print(now, "\t", "Grizzly", "\t", grizzly_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            grizzly_headline[0] = grizzly_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in grizzly():", e)
            time.sleep(3.03)

# 6. Added Fuzzy Panda Function
def fuzzypanda():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://fuzzypandaresearch.com/", headers=headers)
            if resp.status_code != 200:
                print(f"FuzzyPanda: Received status code {resp.status_code}")
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the first div with class starting with 'post-'
            article = soup.find('div', class_=lambda x: x and x.startswith('post-'))
            if not article:
                print("FuzzyPanda: Could not find 'div' tag with class starting with 'post-'.")
                time.sleep(3.03)
                continue

            # Find the 'h2' tag with class 'entry-title' inside the article
            h2_tag = article.find('h2', class_='entry-title')
            if not h2_tag:
                print("FuzzyPanda: Could not find 'h2' tag with class 'entry-title'.")
                time.sleep(3.03)
                continue

            # Find the 'a' tag inside the h2 tag
            a_tag = h2_tag.find('a', href=True)
            if not a_tag:
                print("FuzzyPanda: Could not find 'a' tag with href in 'h2'.")
                time.sleep(3.03)
                continue

            article_url = a_tag['href']
            fuzzypanda_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if fuzzypanda_headline[0] != fuzzypanda_headline[1]:
                print(now, "\t", "FuzzyPanda", "\t", fuzzypanda_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            fuzzypanda_headline[0] = fuzzypanda_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in fuzzypanda():", e)
            time.sleep(3.03)

def scorpion():
    while True:
        try:
            resp = requests.get("https://scorpioncapital.com/research", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            # Find all <p class="sqsrte-small">
            p_tags = soup.find_all('p', class_='sqsrte-small')
            if not p_tags:
                print("Scorpion: Could not find 'p' tags with class 'sqsrte-small'.")
                time.sleep(3.03)
                continue
            pdf_links = []
            for p_tag in p_tags:
                a_tag = p_tag.find('a', href=True)
                if a_tag and a_tag['href'].endswith('.pdf'):
                    pdf_links.append(a_tag['href'])
            if not pdf_links:
                print("Scorpion: Could not find any PDF links.")
                time.sleep(3.03)
                continue
            # Use the first PDF link
            article_url = pdf_links[0]
            if not article_url.startswith('http'):
                article_url = 'https:' + article_url
            scorpion_headline[1] = a_tag.text.strip()
            now = datetime.now().time()
            if scorpion_headline[0] != scorpion_headline[1]:
                print(now, "\t", "Scorpion", "\t", scorpion_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            scorpion_headline[0] = scorpion_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in scorpion():", e)
            time.sleep(3.03)

# 2. Updated Kerrisdale Function
def kerrisdale():
    while True:
        try:
            resp = requests.get("https://www.kerrisdalecap.com/blog/", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            # Find the first 'div' with class 'each-post'
            find = soup.find('div', class_='each-post')
            if not find:
                print("Kerrisdale: Could not find 'div' with class 'each-post'.")
                time.sleep(7.6)
                continue
            # Extract the article URL from the onclick attribute
            a_tag = find.find('a', onclick=True)
            if not a_tag:
                print("Kerrisdale: Could not find 'a' tag with 'onclick' attribute.")
                time.sleep(7.6)
                continue
            onclick_text = a_tag['onclick']
            # Extract URL from onclick attribute using regex
            import re
            match = re.search(r"toggleExcerpt\([^,]+,[^,]+,jQuery\(this\),'([^']+)'", onclick_text)
            if match:
                article_url = match.group(1)
            else:
                print("Kerrisdale: Could not extract URL from onclick.")
                time.sleep(7.6)
                continue
            # Fetch the article page to find the full report link
            article_resp = requests.get(article_url, headers={"User-Agent": "Mozilla/6.0"})
            article_soup = BeautifulSoup(article_resp.content, 'lxml')
            read_full_report_link = article_soup.find('a', class_='css3-button', text='Read Full Report')
            if not read_full_report_link:
                print("Kerrisdale: Could not find 'a' tag for 'Read Full Report'.")
                time.sleep(6.1)
                continue
            full_report_url = read_full_report_link['href']
            kerrisdale_headline[1] = a_tag.text.strip()
            now = datetime.now().time()
            if kerrisdale_headline[0] != kerrisdale_headline[1]:
                print(now, "\t", "Kerrisdale", "\t", kerrisdale_headline[1])
                print("Article URL:", full_report_url)
                webbrowser.open_new_tab(full_report_url)
                winsound.Beep(2500, 200)
            kerrisdale_headline[0] = kerrisdale_headline[1]
            time.sleep(7.6)
        except Exception as e:
            print("Error in kerrisdale():", e)
            time.sleep(7.6)

# 3. Updated Culper Function
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
                time.sleep(3.03)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the 'a' tag that contains the latest report link
            a_tag = soup.find('a', attrs={'data-aid': 'DOWNLOAD_DOCUMENT_LINK_WRAPPER_RENDERED'}, href=True)
            if not a_tag:
                print("Culper: Could not find the latest report link.")
                time.sleep(3.03)
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
                time.sleep(3.03)
                continue

            culper_headline[1] = span_tag.get_text(strip=True)
            now = datetime.now().time()
            if culper_headline[0] != culper_headline[1]:
                print(now, "\t", "Culper", "\t", culper_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            culper_headline[0] = culper_headline[1]
            time.sleep(3.03)
        except Exception as e:
            import traceback
            print(f"Error in culper(): {e}")
            traceback.print_exc()
            time.sleep(3.03)


# 4. Updated Spruce Function
def spruce():
    while True:
        try:
            resp = requests.get("https://www.sprucepointcap.com/research", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            # Find the first 'div' with class 'research-list-wrap'
            find = soup.find('div', class_='research-list-wrap')
            if not find:
                print("Spruce: Could not find 'div' with class 'research-list-wrap'.")
                time.sleep(3.03)
                continue
            # Find the 'a' tag within this div
            find_link = find.find('a', href=True)
            if not find_link:
                print("Spruce: Could not find 'a' tag with href.")
                time.sleep(3.03)
                continue
            href = find_link['href']
            article_url = 'https://www.sprucepointcap.com' + href
            # Get the headline from 'h3' tag within 'a' tag
            title_tag = find_link.find('h3', class_='research-h3')
            if not title_tag:
                print("Spruce: Could not find 'h3' tag with class 'research-h3'.")
                time.sleep(3.03)
                continue
            spruce_headline[1] = title_tag.text.strip()
            now = datetime.now().time()
            if spruce_headline[0] != spruce_headline[1]:
                print(now, "\t", "Spruce", "\t", spruce_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            spruce_headline[0] = spruce_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in spruce():", e)
            time.sleep(3.03)

# 5. Updated SEC8k Function with Form Type Filter
def sec8k():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo  # Ensure you're using Python 3.9+
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

    # Define the adjust_url function
    def adjust_url(url):
        # Check if the URL contains 'ix?doc='
        if 'ix?doc=' in url:
            # Extract the actual document URL
            base_url = 'https://www.sec.gov'
            doc_path = url.split('ix?doc=')[-1]
            adjusted_url = base_url + doc_path
            return adjusted_url
        else:
            return url

    # Define a helper function to match keywords with flexible whitespace
    def keyword_in_text(text, keyword):
        # Escape special regex characters in the keyword
        pattern = re.escape(keyword)
        # Replace escaped spaces with \s+ to match any whitespace
        pattern = pattern.replace(r'\ ', r'\s+')
        # Compile the regex pattern
        regex = re.compile(pattern, re.IGNORECASE)
        # Search using regex
        match = regex.search(text)
        return match

    headers = {
        'Host': 'www.sec.gov',
        'User-Agent': 'Your Name; your.email@example.com',  # Replace with your actual name and email
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
    }

    # List of form types to filter
    form_type_filters = ["8-K", "10-K", "10-Q", "144"]

    opened_links = set()
    script_start_time = datetime.now(timezone.utc)
    last_processed_time = script_start_time  # Initialize last_processed_time
    first_run = True  # Flag variable

    # Keywords to search for (ensure all are in lowercase)
    orange_keywords = ["notification of late filing", "late filing"]
    green_keywords = ["acquisition", "merger"]
    # Split red keywords into two lists
    red_position_keywords = ["chief executive officer", "chief financial officer"]
    red_action_keywords = ["transition", "resign", "step down", "resignation", "interim"]

    # Your sec_filing list
    sec_filing = [
        "5.02", "8.01"
    ]  # You can add more items like "1.01", "2.02", etc.

    # Load CIK-to-Ticker mapping
    cik_ticker_mapping = load_cik_ticker_mapping()

    while True:
        try:
            # Fetch and parse the SEC feed
            url = ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=8-K&company="
                   "&dateb=&owner=include&start=0&count=40&output=atom")
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"SEC 8K: Error fetching RSS feed: {resp.status_code} {resp.reason}")
                time.sleep(3.03)
                continue
            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'xml')  # Use 'xml' parser
            entries = soup.find_all('entry')
            if not entries:
                print("SEC 8K: No entries found in the feed.")
                time.sleep(3.03)
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

                # Get the updated time of the entry (SEC publish timestamp)
                updated_datetime_str = top_entry.updated.get_text()
                updated_datetime = datetime.strptime(updated_datetime_str, '%Y-%m-%dT%H:%M:%S%z')

                # **Modified Time Check**
                # Skip filings older than the last processed time
                if updated_datetime <= last_processed_time:
                    continue

                # Initialize items_text
                items_text = ''

                # **Modified Section: Apply item filtering only for 8-K filings**
                if '8-K' in form_type:
                    # Parse the summary to extract items
                    summary = top_entry.summary
                    if summary and summary.get_text():
                        # Clean up the summary text
                        summary_text = summary.get_text()
                        # Replace HTML entities and remove tags
                        summary_text = BeautifulSoup(summary_text, 'html.parser').get_text()
                        # Remove extra whitespace
                        summary_text = ' '.join(summary_text.split())

                        # Extract items from the summary
                        # Items are lines that start with 'Item '
                        items = re.findall(r'Item [\d\.]+: .*?(?=(?:Item [\d\.]+:|$))', summary_text)
                        if not items:
                            continue  # Skip to the next entry

                        # Check if any of the items include any of the strings in sec_filing
                        filing_items_found = [item for item in items if
                                              any(sec_item in item for sec_item in sec_filing)]
                        if not filing_items_found:
                            continue  # Skip if none of the items match

                        # Join the matching items for output
                        items_text = ', '.join([item.split(':')[0].replace('Item ', '') for item in filing_items_found])
                    else:
                        # No summary available; skip this entry
                        continue
                # **End of Modified Section**

                # Only process if this is a new link
                if top_link not in opened_links:
                    # Record the print timestamp (current time)
                    print_timestamp = datetime.now(timezone.utc)

                    # Calculate time difference in seconds
                    time_diff_seconds = (print_timestamp - updated_datetime).total_seconds()

                    # Convert times to EST
                    updated_datetime_est = updated_datetime.astimezone(ZoneInfo('America/New_York'))
                    print_timestamp_est = print_timestamp.astimezone(ZoneInfo('America/New_York'))

                    # Extract company name and CIK from RSS feed
                    title_text = top_entry.title.get_text()
                    # Example title format: "8-K - Company Name (0001234567) (Filer)"
                    title_pattern = re.compile(r'^(.*?)\s*-\s*(.*?)\s*\((\d+)\)\s*\(Filer\)$')
                    match = title_pattern.match(title_text)
                    if match:
                        form_type_extracted = match.group(1).strip()
                        company_name = match.group(2).strip()
                        cik_number = match.group(3).strip().lstrip('0')  # Remove leading zeros
                    else:
                        # If the title does not match the expected pattern
                        company_name = "Unknown Company"
                        cik_number = None
                        form_type_extracted = "Unknown Form"

                    # **Add this check to skip companies not in the mapping**
                    if cik_number not in cik_ticker_mapping:
                        # **Update last_processed_time even if skipping**
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue  # Skip this filing

                    # Get ticker symbol from the preloaded mapping
                    ticker = cik_ticker_mapping[cik_number]

                    # Fetching page content to get the document URL
                    page_resp = requests.get(top_link, headers=headers)
                    if page_resp.status_code != 200:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue
                    page_soup = BeautifulSoup(page_resp.content, 'lxml')  # Use 'lxml' parser

                    # Find the document table
                    table = page_soup.find('table', class_='tableFile')
                    if not table:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue
                    # Find the row with the text version of the desired document
                    rows = table.find_all('tr')
                    doc_url = None
                    for row in rows[1:]:
                        cols = row.find_all('td')
                        if len(cols) >= 4:
                            doc_type = cols[3].text.strip()
                            if doc_type == form_type:
                                # Find the link to the text version
                                doc_link = None
                                formats_cell = cols[2]
                                for a_tag in formats_cell.find_all('a'):
                                    href = a_tag.get('href', '')
                                    if 'Archives' in href and href.endswith('.txt'):
                                        doc_link = href
                                        break
                                if not doc_link:
                                    # Fallback to HTML version if text version not found
                                    doc_link = cols[2].find('a', href=True)['href']
                                doc_url = 'https://www.sec.gov' + doc_link
                                break  # Exit after finding the document

                    if not doc_url:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue  # Skip if we couldn't find the document URL

                    # Adjust the document URL if necessary
                    doc_url = adjust_url(doc_url)

                    # Fetch the document content
                    doc_resp = requests.get(doc_url, headers=headers)
                    if doc_resp.status_code != 200:
                        last_processed_time = max(last_processed_time, updated_datetime)
                        continue
                    doc_content = doc_resp.content.decode('utf-8', errors='ignore')  # Get decoded content

                    # Remove namespaces
                    doc_content = re.sub(r'\sxmlns(:\w+)?="[^"]+"', '', doc_content)  # Remove namespace declarations
                    doc_content = re.sub(r'</?(\w+):', '<', doc_content)  # Remove namespace prefixes

                    # Parse with BeautifulSoup using 'lxml' parser
                    soup = BeautifulSoup(doc_content, 'lxml')

                    # Remove script and style elements
                    for script_or_style in soup(['script', 'style']):
                        script_or_style.decompose()

                    # Extract text
                    text = soup.get_text(separator=' ', strip=True)

                    # Remove non-printable characters
                    text = ''.join(filter(lambda x: x in string.printable, text))

                    # Clean up the text content
                    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with single space

                    # Convert to lowercase for case-insensitive searching
                    text_lower = text.lower()

                    # Search for keywords using the helper function
                    red_position_found = any(keyword_in_text(text_lower, keyword) for keyword in red_position_keywords)
                    red_action_found = any(keyword_in_text(text_lower, keyword) for keyword in red_action_keywords)
                    red_found = red_position_found and red_action_found  # Both must be true for red_found to be true

                    green_found = any(keyword_in_text(text_lower, keyword) for keyword in green_keywords)
                    orange_found = any(keyword_in_text(text_lower, keyword) for keyword in orange_keywords)

                    # Emphasize the ticker
                    ticker_formatted = f"{Style.BRIGHT}{ticker}{Style.RESET_ALL}"

                    # Create the main output with visual markers
                    output = (f"=== TICKER: {ticker_formatted} - {form_type_extracted} - Item {items_text} ===\n"
                              f"Company: {company_name}\n"
                              f"SEC Time: {updated_datetime_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Print Time: {print_timestamp_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Delay: {int(time_diff_seconds)}s\n"
                              f"URL: {doc_url}")

                    # Determine the color code based on the highest priority keyword found
                    if orange_found:
                        color_code = Back.YELLOW + Fore.BLACK  # Yellow background, black text
                    elif red_found:
                        color_code = Back.RED + Fore.BLACK  # Red background, black text
                    elif green_found:
                        color_code = Back.GREEN + Fore.BLACK  # Green background, black text
                    else:
                        color_code = ''  # No color

                    # Apply bold to the entire output
                    output = Style.BRIGHT + output + Style.RESET_ALL

                    # Print the output with the corresponding colors
                    if color_code:
                        print(f"{color_code}{output}")
                    else:
                        print(output)

                    # Open the document in the browser
                    webbrowser.open_new_tab(doc_url)
                    # winsound.Beep(2500, 200)  # Uncomment if you want a beep sound (requires 'winsound' module on Windows)
                    opened_links.add(top_link)

                    # **Update last_processed_time after processing**
                    last_processed_time = max(last_processed_time, updated_datetime)

                    break  # Found the document we're interested in
                else:
                    # **Update last_processed_time even if link was already opened**
                    last_processed_time = max(last_processed_time, updated_datetime)
                    continue

            time.sleep(1)  # Reduced sleep time to 1 second

        except Exception as e:
            import traceback
            print(f"Error in sec8k(): {e}")
            traceback.print_exc()
            time.sleep(3.03)


def load_cik_ticker_mapping():
    import requests
    cik_ticker = {}
    try:
        # Download the CIK-Ticker mapping file from the SEC website
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
            ticker_idx = fields.index('ticker')
            exchange_idx = fields.index('exchange')  # Get the index of the 'exchange' field
            for entry in data['data']:
                exchange_field = entry[exchange_idx]
                if exchange_field:
                    exchange = exchange_field.strip()
                    if exchange in ['Nasdaq', 'NYSE']:
                        cik_field = entry[cik_idx]
                        ticker_field = entry[ticker_idx]
                        if cik_field and ticker_field:
                            cik = str(cik_field).strip()
                            cik = cik.lstrip('0')  # Remove leading zeros
                            ticker = ticker_field.strip()
                            cik_ticker[cik] = ticker
                        else:
                            # Skip entries with missing CIK or ticker
                            continue
                else:
                    # Skip entries where exchange is None or empty
                    continue
        else:
            print(f"Failed to download CIK-Ticker mapping. Status code: {resp.status_code}")
    except Exception as e:
        print(f"Error loading CIK-Ticker mapping: {e}")

    return cik_ticker




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


# def citron():
#     while True:
#         try:
#             resp = requests.get("https://citronresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
#             soup = BeautifulSoup(resp.content, 'lxml')
#             find = soup.find(class_="avia_textblock")
#             if not find:
#                 print("Citron: Could not find 'avia_textblock' class.")
#                 time.sleep(3.03)
#                 continue
#             find2 = find.find("h2")
#             if not find2:
#                 print("Citron: Could not find 'h2' tag.")
#                 time.sleep(3.03)
#                 continue
#             find_link = find2.find("a", href=True)
#             if not find_link:
#                 print("Citron: Could not find 'a' tag with href in 'h2'.")
#                 time.sleep(3.03)
#                 continue
#             citron_headline[1] = find_link.text.strip()
#             article_url = find_link['href']
#             if not article_url.startswith('http'):
#                 article_url = 'https://citronresearch.com' + article_url
#             now = datetime.now().time()
#             if citron_headline[0] != citron_headline[1]:
#                 print(now, "\t", "Citron", "\t", citron_headline[1])
#                 print("Article URL:", article_url)
#                 webbrowser.open_new_tab(article_url)
#                 winsound.Beep(2500, 200)
#             citron_headline[0] = citron_headline[1]
#             time.sleep(3.03)
#         except Exception as e:
#             print("Error in citron():", e)
#             time.sleep(3.03)



def iceberg():
    while True:
        try:
            resp = requests.get("https://iceberg-research.com/", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            find = soup.find('div', class_='xpro-post-grid-content')
            if not find:
                print("Iceberg: Could not find 'div' with class 'xpro-post-grid-content'.")
                time.sleep(3.03)
                continue
            find_link = find.find('a', href=True)
            if not find_link:
                print("Iceberg: Could not find 'a' tag with href in the post content.")
                time.sleep(3.03)
                continue
            article_url = find_link['href']
            iceberg_headline[1] = find_link.find('h2', class_='xpro-post-grid-title').text.strip()
            now = datetime.now().time()
            if iceberg_headline[0] != iceberg_headline[1]:
                print(now, "\t", "Iceberg", "\t", iceberg_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            iceberg_headline[0] = iceberg_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in iceberg():", e)
            time.sleep(3.03)

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
                winsound.Beep(2500, 200)
            statnews_headline[0] = statnews_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in statnews():", e)
            time.sleep(3.03)

def hindenburg():
    while True:
        try:
            resp = requests.get("https://hindenburgresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
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
                print(now, "\t", "Hindenburg", "\t", hindenburg_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            hindenburg_headline[0] = hindenburg_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in hindenburg():", e)
            time.sleep(3.03)

def wolfpack():
    while True:
        try:
            resp = requests.get("https://www.wolfpackresearch.com/items", headers={"User-Agent": "Mozilla/6.0"})
            soup = BeautifulSoup(resp.content, 'lxml')
            # Find the latest report link
            find = soup.find('div', class_='comp-ls2evfpq')
            if not find:
                print("Wolfpack: Could not find 'div' with class 'comp-ls2evfpq'.")
                time.sleep(5.1)
                continue
            find_link = find.find('a', href=True)
            if not find_link:
                print("Wolfpack: Could not find 'a' tag with href.")
                time.sleep(5.1)
                continue
            article_url = find_link['href']
            if not article_url.startswith('http'):
                article_url = 'https://www.wolfpackresearch.com' + article_url
            wolfpack_headline[1] = find_link.find('span', class_='wJVzSK wixui-button__label').text.strip()
            now = datetime.now().time()
            if wolfpack_headline[0] != wolfpack_headline[1]:
                print(now, "\t", "Wolfpack", "\t", wolfpack_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            wolfpack_headline[0] = wolfpack_headline[1]
            time.sleep(5.1)
        except Exception as e:
            print("Error in wolfpack():", e)
            time.sleep(5.1)







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
                winsound.Beep(2500, 200)
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
                winsound.Beep(2500, 200)
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
                winsound.Beep(2500, 200)
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
                winsound.Beep(2500, 200)
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
                winsound.Beep(2500, 200)
            bleepcomp_headline[0] = bleepcomp_headline[1]
            time.sleep(3.03)
        except Exception as e:
            print("Error in bleepcomp():", e)
            time.sleep(3.03)

def hntrbrk():
    while True:
        try:
            resp = requests.get("https://hntrbrk.com/feed/", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(resp.content, 'lxml-xml')
            results = soup.find("item")
            if not results:
                print("Hunterbrook: Could not find 'item' tag.")
                time.sleep(3.03)
                continue
            hntrbrk_headline[1] = results.title.string.strip()
            link = results.link.string.strip()
            find = results.find("description")
            if not find:
                print("Hunterbrook: Could not find 'description' tag.")
                time.sleep(5)
                continue
            desc = find.string.strip()
            now = datetime.now().time()
            if hntrbrk_headline[0] != hntrbrk_headline[1]:
                print(now, "\t", "Hunterbrook", "\t", hntrbrk_headline[1])
                print("Description:", desc)
                print("Article URL:", link)
                print("Attempting to open link:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(2500, 400)
            hntrbrk_headline[0] = hntrbrk_headline[1]
            time.sleep(5)
        except Exception as e:
            import traceback
            print(f"Error in hntrbrk(): {e}")
            traceback.print_exc()
            time.sleep(3.03)
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
#                 winsound.Beep(2500, 200)
#             lauren_balik_headline[0] = lauren_balik_headline[1]
#             time.sleep(5)  # Check every 5 minutes
#         except Exception as e:
#             print("Error in lauren_balik():", e)
#             time.sleep(5)
ming_chi_kuo_headline = ["", ""]

def ming_chi_kuo():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            url = "https://medium.com/feed/@mingchikuo"
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Ming Chi Kuo: Received status code {resp.status_code}")
                time.sleep(5)
                continue
            soup = BeautifulSoup(resp.content, 'xml')

            # Find the latest item
            item = soup.find('item')
            if not item:
                print("Ming Chi Kuo: Could not find 'item' tag.")
                time.sleep(5)
                continue

            title_tag = item.find('title')
            link_tag = item.find('link')
            if not title_tag or not link_tag:
                print("Ming Chi Kuo: Could not find 'title' or 'link' tag.")
                time.sleep(5)
                continue

            title = title_tag.text.strip()
            link = link_tag.text.strip()
            ming_chi_kuo_headline[1] = title
            now = datetime.now().time()
            if ming_chi_kuo_headline[0] != ming_chi_kuo_headline[1]:
                print(now, "\t", "Ming Chi Kuo", "\t", ming_chi_kuo_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(2500, 200)
            ming_chi_kuo_headline[0] = ming_chi_kuo_headline[1]
            time.sleep(5)  # Check every 5 seconds
        except Exception as e:
            print("Error in ming_chi_kuo():", e)
            time.sleep(3.52)
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
                winsound.Beep(2500, 200)
            mark_kleinman_headline[0] = mark_kleinman_headline[1]
            time.sleep(5)

        except Exception as e:
            print("Error in mark_kleinman():", e)
            time.sleep(3.01)

# Start the threads
# citron_thread = threading.Thread(target=citron)
# citron_thread.start()

scorpion_thread = threading.Thread(target=scorpion)
scorpion_thread.start()

# iceberg_thread = threading.Thread(target=iceberg)
# iceberg_thread.start()

hindenburg_thread = threading.Thread(target=hindenburg)
hindenburg_thread.start()

wolfpack_thread = threading.Thread(target=wolfpack)
wolfpack_thread.start()

culper_thread = threading.Thread(target=culper)
culper_thread.start()

kerrisdale_thread = threading.Thread(target=kerrisdale)
kerrisdale_thread.start()


# usps_thread = threading.Thread(target=usps)
# usps_thread.start()

# cdc_thread = threading.Thread(target=cdc)
# cdc_thread.start()

# fda_thread = threading.Thread(target=fda)
# fda_thread.start()
#
# fda2_thread = threading.Thread(target=fda2)
# fda2_thread.start()

spruce_thread = threading.Thread(target=spruce)
spruce_thread.start()

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

hntrbrk_thread = threading.Thread(target=hntrbrk)
hntrbrk_thread.start()

# Starting new threads for the added websites
bleecker_thread = threading.Thread(target=bleecker)
bleecker_thread.start()

# muddywaters_thread = threading.Thread(target=muddywaters)
# muddywaters_thread.start()
#
# grizzly_thread = threading.Thread(target=grizzly)
# grizzly_thread.start()

fuzzypanda_thread = threading.Thread(target=fuzzypanda)
fuzzypanda_thread.start()

# Start the threads for the new functions
jcapital_thread = threading.Thread(target=jcapital)
jcapital_thread.start()

capybara_thread = threading.Thread(target=capybara)
capybara_thread.start()

# lauren_balik_thread = threading.Thread(target=lauren_balik)
# lauren_balik_thread.start()

#
# tiktok_thread = threading.Thread(target=tiktok_court, daemon=True)
# tiktok_thread.start()
#
# ming_chi_kuo_thread = threading.Thread(target=ming_chi_kuo)
# ming_chi_kuo_thread.start()

mark_kleinman_thread = threading.Thread(target=mark_kleinman)
mark_kleinman_thread.start()