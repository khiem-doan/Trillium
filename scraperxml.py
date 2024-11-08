import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
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
def fuzzypanda():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://fuzzypandaresearch.com/", headers=headers)
            if resp.status_code != 200:
                print(f"FuzzyPanda: Received status code {resp.status_code}")
                time.sleep(3)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')

            # Find the first div with class starting with 'post-'
            article = soup.find('div', class_=lambda x: x and x.startswith('post-'))
            if not article:
                print("FuzzyPanda: Could not find 'div' tag with class starting with 'post-'.")
                time.sleep(3)
                continue

            # Find the 'h2' tag with class 'entry-title' inside the article
            h2_tag = article.find('h2', class_='entry-title')
            if not h2_tag:
                print("FuzzyPanda: Could not find 'h2' tag with class 'entry-title'.")
                time.sleep(3)
                continue

            # Find the 'a' tag inside the h2 tag
            a_tag = h2_tag.find('a', href=True)
            if not a_tag:
                print("FuzzyPanda: Could not find 'a' tag with href in 'h2'.")
                time.sleep(3)
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
            time.sleep(3)
        except Exception as e:
            print("Error in fuzzypanda():", e)
            time.sleep(3)
def muddywaters():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://muddywatersresearch.com/research/", headers=headers)
            if resp.status_code != 200:
                print(f"MuddyWaters: Received status code {resp.status_code}")
                time.sleep(3)
                continue

            soup = BeautifulSoup(resp.content, 'xml')

            item = soup.find('item')
            if not item:
                print("MuddyWaters: Could not find 'item' tag.")
                time.sleep(3)
                continue

            title = item.find('title').text.strip()
            link = item.find('link').text.strip()
            muddywaters_headline[1] = title
            now = datetime.now().time()
            if muddywaters_headline[0] != muddywaters_headline[1]:
                print(now, "\t", "MuddyWaters", "\t", muddywaters_headline[1])
                print("Article URL:", link)
                webbrowser.open_new_tab(link)
                winsound.Beep(2500, 200)
            muddywaters_headline[0] = muddywaters_headline[1]
            time.sleep(3)
        except Exception as e:
            print("Error in muddywaters():", e)
            if resp.status_code == 403:
                print(f"Received status code 403 for {url}")
                print("Response Headers:", resp.headers)
                print("Response Content:", resp.text[:500])
                time.sleep(3)
                continue
            time.sleep(3)
def culper():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            resp = requests.get("https://culperresearch.com/", headers=headers)
            if resp.status_code != 200:
                print(f"Culper: Received status code {resp.status_code}")
                time.sleep(3)
                continue

            soup = BeautifulSoup(resp.content, 'html.parser')
            # Find all 'a' tags with href containing '.pdf'
            a_tags = soup.find_all('a', href=True)
            pdf_links = []
            for a_tag in a_tags:
                href = a_tag['href']
                if '.pdf' in href:
                    pdf_links.append(a_tag)
            if not pdf_links:
                print("Culper: Could not find any PDF links.")
                time.sleep(3)
                continue
            # Use the first PDF link
            a_tag = pdf_links[0]
            article_url = a_tag['href']
            if not article_url.startswith('http'):
                article_url = 'https:' + article_url
            # Get the headline from 'aria-label' attribute or text
            culper_headline[1] = a_tag.get('aria-label', '').strip()
            if not culper_headline[1]:
                culper_headline[1] = a_tag.get_text(strip=True)
            now = datetime.now().time()
            if culper_headline[0] != culper_headline[1]:
                print(now, "\t", "Culper", "\t", culper_headline[1])
                print("Article URL:", article_url)
                webbrowser.open_new_tab(article_url)
                winsound.Beep(2500, 200)
            culper_headline[0] = culper_headline[1]
            time.sleep(3)
        except Exception as e:
            print("Error in culper():", e)
            time.sleep(3)


muddy_thread = threading.Thread(target=muddywaters)
muddy_thread.start()

fuzzypanda_thread = threading.Thread(target=fuzzypanda)
fuzzypanda_thread.start()
culper_thread = threading.Thread(target=culper)
culper_thread.start()

