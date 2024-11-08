# Import necessary libraries
from pandas import *
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
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
kerrisdaleL_headline = [0]*2
kerrisdaleS_headline = [0]*2
sp_headline = [0]*2
usps_headline = [0]*2
cdc_headline = [0]*2
info_headline = [0]*2
electrek_headline = [0]*2
insideev_headline = [0]*2
fda_headline = [0]*2
fda2_headline = [0]*2
bleecker_headline = [0]*2
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

author = ""
tp_ticker = []

sec_filing = ["1.01:", "1.02:", "2.04:", "2.05", "3.01:", "4.02:", "7.01:", "8.01:"]

def sec8k():
    count = 0
    while True:
        resp = requests.get(
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=8-k&company=&dateb=&owner=include&start=0&count=40&output=atom",
            headers={
                'User-Agent': 'Sample Company Name Khiem Doan, doan.khiem@gmail.com',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'www.sec.gov'
            })
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("entry")
        find2 = find.find("title")
        find3 = find.find("summary")
        list1 = find3.text.split()
        item = list(set(list1).intersection(sec_filing))
        sec8k_headline[1] = find2.text.strip()
        now = datetime.now().time()
        if sec8k_headline[0] != sec8k_headline[1] and count != 0 and len(item) != 0:
            print(now, "\t", "SEC 8K", "\t", sec8k_headline[1])
            winsound.Beep(2500, 200)
            print(item)
        sec8k_headline[0] = sec8k_headline[1]
        count += 1
        time.sleep(1.5)

def secRW():
    count = 0
    while True:
        resp = requests.get(
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=RW&company=&dateb=&owner=include&start=0&count=40&output=atom",
            headers={
                'User-Agent': 'Sample Company Name Khiem Doan, doan.khiem@gmail.com',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'www.sec.gov'
            })
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("entry")
        if find is None:
            print("No 'entry' element found.")
            time.sleep(5)
            continue
        find2 = find.find("title")
        secRW_headline[1] = find2.text.strip()
        now = datetime.now().time()
        if secRW_headline[0] != secRW_headline[1] and count != 0:
            print(now, "\t", "SEC RW", "\t", secRW_headline[1])
            stock = secRW_headline[1].split("-", 1)[1]
            stock2 = stock.split("(")[0].strip()
            url = f"https://www.google.com/search?q={stock2} stock"
            webbrowser.open_new_tab(url)
            winsound.Beep(2500, 200)
        secRW_headline[0] = secRW_headline[1]
        count += 1
        time.sleep(1.5)

def citron():
    count = 0
    while True:
        resp = requests.get("https://citronresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="avia_textblock")
        find2 = find.find("h2")
        citron_headline[1] = find2.text.strip()
        now = datetime.now().time()
        if citron_headline[0] != citron_headline[1] and count != 0:
            print(now, "\t", "Citron", "\t", citron_headline[1])
            winsound.Beep(2500, 200)
        citron_headline[0] = citron_headline[1]
        count += 1
        time.sleep(1.5)

def scorpion():
    count = 0
    while True:
        resp = requests.get("https://scorpioncapital.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="image-subtitle sqs-dynamic-text")
        scorpion_headline[1] = find.text.strip()
        now = datetime.now().time()
        if scorpion_headline[0] != scorpion_headline[1] and count != 0:
            print(now, "\t", "Scorpion", "\t", scorpion_headline[1])
            winsound.Beep(2500, 200)
        scorpion_headline[0] = scorpion_headline[1]
        count += 1
        time.sleep(1.5)

def iceberg():
    count = 0
    while True:
        resp = requests.get("https://iceberg-research.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h2")
        iceberg_headline[1] = find.text.strip()
        now = datetime.now().time()
        if iceberg_headline[0] != iceberg_headline[1] and count != 0:
            print(now, "\t", "Iceberg", "\t", iceberg_headline[1])
            winsound.Beep(2500, 200)
        iceberg_headline[0] = iceberg_headline[1]
        count += 1
        time.sleep(1.5)

def statnews():
    count = 0
    while True:
        resp = requests.get("https://www.statnews.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        statnews_headline[1] = find.title.text.strip()
        now = datetime.now().time()
        if statnews_headline[0] != statnews_headline[1] and count != 0:
            print(now, "\t", "Statnews", "\t", statnews_headline[1])
            winsound.Beep(2500, 200)
        statnews_headline[0] = statnews_headline[1]
        count += 1
        time.sleep(1.5)

def hindenburg():
    count = 0
    while True:
        resp = requests.get("https://hindenburgresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h1")
        find2 = find.find("a", href=True)
        hindenburg_headline[1] = find2.text.strip()
        now = datetime.now().time()
        if hindenburg_headline[0] != hindenburg_headline[1] and count != 0:
            print(now, "\t", "Hindenburg", "\t", hindenburg_headline[1])
            stock = hindenburg_headline[1].split(":")[0]
            url = f"https://www.google.com/search?q={stock.strip()} stock"
            webbrowser.open_new_tab(url)
            winsound.Beep(2500, 200)
        hindenburg_headline[0] = hindenburg_headline[1]
        count += 1
        time.sleep(1.5)

def wolfpack():
    count = 0
    while True:
        resp = requests.get("https://wolfpackresearch.com/research/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h4")
        wolfpack_headline[1] = find.text.strip()
        now = datetime.now().time()
        if wolfpack_headline[0] != wolfpack_headline[1] and count != 0:
            print(now, "\t", "Wolfpack", "\t", wolfpack_headline[1])
            winsound.Beep(2500, 200)
        wolfpack_headline[0] = wolfpack_headline[1]
        count += 1
        time.sleep(1.5)

def whitediam():
    count = 0
    while True:
        resp = requests.get("https://seekingalpha.com/author/white-diamond-research.xml", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        whitediam_headline[1] = find.title.text.strip()
        now = datetime.now().time()
        if whitediam_headline[0] != whitediam_headline[1] and count != 0:
            print(now, "\t", "White Dmnd", "\t", whitediam_headline[1])
            winsound.Beep(2500, 200)
        whitediam_headline[0] = whitediam_headline[1]
        count += 1
        time.sleep(1.5)

def culper():
    count = 0
    while True:
        resp = requests.get("https://culperresearch.com/latest-research", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("strong")
        culper_headline[1] = find.text.strip()
        now = datetime.now().time()
        if culper_headline[0] != culper_headline[1] and count != 0:
            print(now, "\t", "Culper", "\t", culper_headline[1])
            winsound.Beep(2500, 200)
        culper_headline[0] = culper_headline[1]
        count += 1
        time.sleep(1.5)

def kerrisdaleL():
    count = 0
    while True:
        resp = requests.get("https://www.kerrisdalecap.com/blog/?cat=long", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h2")
        kerrisdaleL_headline[1] = find.text.strip()
        now = datetime.now().time()
        if kerrisdaleL_headline[0] != kerrisdaleL_headline[1] and count != 0:
            print(now, "\t", "KerrisdaleL", "\t", kerrisdaleL_headline[1])
            winsound.Beep(2500, 200)
        kerrisdaleL_headline[0] = kerrisdaleL_headline[1]
        count += 1
        time.sleep(1.5)

def kerrisdaleS():
    count = 0
    while True:
        resp = requests.get("https://www.kerrisdalecap.com/blog/?cat=short", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h2")
        kerrisdaleS_headline[1] = find.text.strip()
        now = datetime.now().time()
        if kerrisdaleS_headline[0] != kerrisdaleS_headline[1] and count != 0:
            print(now, "\t", "KerrisdaleS", "\t", kerrisdaleS_headline[1])
            winsound.Beep(2500, 200)
        kerrisdaleS_headline[0] = kerrisdaleS_headline[1]
        count += 1
        time.sleep(1.5)

def usps():
    count = 0
    while True:
        resp = requests.get("https://about.usps.com/news/latestnews.rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        usps_headline[1] = find.title.text.strip()
        now = datetime.now().time()
        if usps_headline[0] != usps_headline[1] and count != 0:
            print(now, "\t", "USPS", "\t", usps_headline[1])
            winsound.Beep(2500, 200)
        usps_headline[0] = usps_headline[1]
        count += 1
        time.sleep(1.5)

def cdc():
    count = 0
    while True:
        resp = requests.get("https://tools.cdc.gov/api/v2/resources/media/132608.rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        cdc_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if cdc_headline[0] != cdc_headline[1] and count != 0:
            print(now, "\t", "CDC", "\t", cdc_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        cdc_headline[0] = cdc_headline[1]
        count += 1
        time.sleep(1.5)

def information():
   count = 0
   while True:
       resp = requests.get("https://www.theinformation.com/features/exclusive", headers={"User-Agent": "Mozilla/4.0"})
       soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
       find = soup.find(class_="no-link track-click")
       info_headline[1] = find.text.strip()
       info = "https://www.theinformation.com"
       link = info + find.get("href")
       now = datetime.now().time()
       if info_headline[0] != info_headline[1] and count != 0:
           print(now, "\t", "The Information", "\t", info_headline[1])
           print(link)
           winsound.Beep(2500, 200)
       info_headline[0] = info_headline[1]
       count += 1
       time.sleep(5)

def electrek():
    count = 0
    while True:
        resp = requests.get("https://electrek.co/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        electrek_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if electrek_headline[0] != electrek_headline[1] and count != 0:
            print(now, "\t", "Electrek", "\t", electrek_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        electrek_headline[0] = electrek_headline[1]
        count += 1
        time.sleep(1.5)

def insideev():
    count = 0
    while True:
        resp = requests.get("https://insideevs.com/rss/news/all/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        insideev_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if insideev_headline[0] != insideev_headline[1] and count != 0:
            print(now, "\t", "InsideEV", "\t", insideev_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        insideev_headline[0] = insideev_headline[1]
        count += 1
        time.sleep(1.5)

def fda():
    count = 0
    while True:
        resp = requests.get(
            "https://www.fda.gov/advisory-committees/advisory-committee-calendar",
            headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("tbody")
        find2 = find.find("tr")
        find3 = find2.find("td")
        fda_headline[1] = find3.text.strip()
        now = datetime.now().time()
        if fda_headline[0] != fda_headline[1] and count != 0:
            print(now, "\t", "FDA", "\t", fda_headline[1])
            winsound.Beep(2500, 200)
        fda_headline[0] = fda_headline[1]
        count += 1
        time.sleep(1.5)

def fda2():
    count = 0
    while True:
        resp = requests.get(
            "https://search.fda.gov/search?utf8=%E2%9C%93&affiliate=fda1&query=761178&commit=Search",
            headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="title")
        fda2_headline[1] = find.text.strip()
        link = find.find("a", href=True)['href']
        now = datetime.now().time()
        if fda2_headline[0] != fda2_headline[1] and count != 0:
            print(now, "\t", "FDA", "\t", fda2_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        fda2_headline[0] = fda2_headline[1]
        count += 1
        time.sleep(1.5)

def bleecker():
    count = 0
    while True:
        resp = requests.get("https://bleeckerstreetresearch.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        bleecker_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if bleecker_headline[0] != bleecker_headline[1] and count != 0:
            print(now, "\t", "Bleecker", "\t", bleecker_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        bleecker_headline[0] = bleecker_headline[1]
        count += 1
        time.sleep(1.5)

def ftc():
    count = 0
    while True:
        resp = requests.get("https://www.ftc.gov/news-events/news/press-releases", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="view-content")
        find2 = find.find("a", href=True)
        ftc_headline[1] = find2.text.strip()
        link = "https://www.ftc.gov" + find2.get("href")
        now = datetime.now().time()
        if ftc_headline[0] != ftc_headline[1] and count != 0:
            print(now, "\t", "FTC", "\t", ftc_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        ftc_headline[0] = ftc_headline[1]
        count += 1
        time.sleep(1.5)

def faa():
    count = 0
    while True:
        resp = requests.get("https://www.faa.gov/newsroom/press_releases/rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        faa_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if faa_headline[0] != faa_headline[1] and count != 0:
            print(now, "\t", "FAA", "\t", faa_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        faa_headline[0] = faa_headline[1]
        count += 1
        time.sleep(1.5)

def sava():
    count = 0
    while True:
        resp = requests.get("https://www.cassavasciences.com/rss/news-releases.xml", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        sava_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        now = datetime.now().time()
        if sava_headline[0] != sava_headline[1] and count != 0:
            print(now, "\t", "SAVA", "\t", sava_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        sava_headline[0] = sava_headline[1]
        count += 1
        time.sleep(1.5)

def bearcave():
    count = 0
    while True:
        resp = requests.get("https://thebearcave.substack.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="post-preview-title")
        bearcave_headline[1] = find.text.strip()
        now = datetime.now().time()
        if bearcave_headline[0] != bearcave_headline[1] and count != 0:
            print(now, "\t", "Bearcave", "\t", bearcave_headline[1])
            winsound.Beep(2500, 200)
        bearcave_headline[0] = bearcave_headline[1]
        count += 1
        time.sleep(2)

def spruce():
    count = 0
    while True:
        resp = requests.get("https://www.sprucepointcap.com/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="main_box")
        find3 = soup.find(class_="box_content_title")
        find2 = find.find(class_="box_content_subtitle")
        spruce_headline[1] = find2.text.strip()
        text = find3.text.strip()
        now = datetime.now().time()
        if spruce_headline[0] != spruce_headline[1] and count != 0:
            print(now, "\t", "Spruce", "\t", spruce_headline[1])
            print(text)
            winsound.Beep(2500, 200)
        spruce_headline[0] = spruce_headline[1]
        count += 1
        time.sleep(1.5)

def benzinga():
    count = 0
    while True:
        resp = requests.get("https://www.benzinga.com/feed", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, 'xml')
        item = soup.find('item')
        if item is None:
            print("Could not find any news items.")
            time.sleep(5)
            continue
        benzinga_headline[1] = item.title.get_text(strip=True)
        link = item.link.get_text(strip=True)
        now = datetime.now().time()
        if benzinga_headline[0] != benzinga_headline[1] and count != 0:
            print(now, "\t", "Benzinga", "\t", benzinga_headline[1])
            print(link)
            winsound.Beep(2500, 200)
        benzinga_headline[0] = benzinga_headline[1]
        count += 1
        time.sleep(1.5)

def nytimes():
    count = 0
    while True:
        resp = requests.get(
            "https://www.nytimes.com/section/business",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        soup = BeautifulSoup(resp.content, 'lxml')

        # Find all article elements
        articles = soup.find_all('article')
        if not articles:
            print("Could not find any articles.")
            time.sleep(5)
            continue

        article = articles[0]  # Get the first article

        # Find the headline within the article
        headline = article.find(['h2', 'h3'])
        if headline is None:
            print("Could not find the headline in the article.")
            time.sleep(5)
            continue

        nytimes_headline[1] = headline.get_text(strip=True)

        # Extract the summary
        summary = article.find('p')
        if summary:
            text = summary.get_text(strip=True)
        else:
            text = ''

        # Extract the link
        link_tag = article.find('a', href=True)
        if link_tag:
            link = link_tag['href']
            if not link.startswith('http'):
                link = 'https://www.nytimes.com' + link
        else:
            link = ''

        now = datetime.now().time()
        if nytimes_headline[0] != nytimes_headline[1] and count != 0:
            print(now, "\t", "NYTimes", "\t", nytimes_headline[1])
            winsound.Beep(2500, 200)
            print(text)
            print(link)

        nytimes_headline[0] = nytimes_headline[1]
        count += 1
        time.sleep(1.5)

def nypost():
    count = 0
    while True:
        resp = requests.get("https://nypost.com/tag/mergers-acquisitions/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="story__headline headline headline--archive")
        find2 = find.find("a")
        nypost_headline[1] = find2.text.strip()
        find3 = soup.find(class_="story__excerpt body")
        text = find3.text.strip()
        now = datetime.now().time()
        if nypost_headline[0] != nypost_headline[1] and count != 0:
            print(now, "\t", "NY Post", "\t", nypost_headline[1])
            winsound.Beep(2500, 200)
            print(text)
        nypost_headline[0] = nypost_headline[1]
        count += 1
        time.sleep(1.5)

def pershing():
    count = 0
    while True:
        resp = requests.get("https://pershingsquareholdings.com/company-reports/letters-to-shareholders/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="wpb_column vc_column_container vc_col-sm-9")
        find2 = find.find("p")
        pershing_headline[1] = find2.text.strip()
        link = find2.find("a", href=True).get("href")
        now = datetime.now().time()
        if pershing_headline[0] != pershing_headline[1] and count != 0:
            print(now, "\t", "Pershing", "\t", pershing_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        pershing_headline[0] = pershing_headline[1]
        count += 1
        time.sleep(1.5)

def aircurrent():
    count = 0
    while True:
        resp = requests.get("https://theaircurrent.com/")
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h3")
        find2 = find.find("a", href=True)
        aircurrent_headline[1] = find2.text.strip()
        link = find2.get("href")
        now = datetime.now().time()
        if aircurrent_headline[0] != aircurrent_headline[1] and count != 0:
            print(now, "\t", "Air Current", "\t", aircurrent_headline[1])
            winsound.Beep(2500, 400)
            print(link)
        aircurrent_headline[0] = aircurrent_headline[1]
        count += 1
        time.sleep(1.5)

def cnbc():
    count = 0
    while True:
        resp = requests.get(
            "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114",
            headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.find("item")
        cnbc_headline[1] = find.title.text.strip()
        link = find.link.text.strip()
        text = find.description.text.strip()
        now = datetime.now().time()
        if cnbc_headline[0] != cnbc_headline[1] and count != 0:
            print(now, "\t", "CNBC", "\t", cnbc_headline[1])
            winsound.Beep(2500, 400)
            print(link)
            print(text)
        cnbc_headline[0] = cnbc_headline[1]
        count += 1
        time.sleep(1.5)

def freeport():
    count = 0
    while True:
        resp = requests.get("http://www.newsrouter.com/Newsrouter_uploads/77/newsroom.asp", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("tr", class_="bodyText")
        find2 = find.findAll("td")
        find3 = find2[1]
        freeport_headline[1] = find3.text.strip()
        link = find3.find("a", href=True)
        now = datetime.now().time()
        if freeport_headline[0] != freeport_headline[1] and count != 0:
            print(now, "\t", "Freeport LNG", "\t", freeport_headline[1])
            winsound.Beep(2500, 400)
            freeportlng = "http://www.newsrouter.com/Newsrouter_uploads/77/"
            print(freeportlng.strip() + link.get("href").strip())
        freeport_headline[0] = freeport_headline[1]
        count += 1
        time.sleep(1.5)

def mingchi():
    count = 0
    while True:
        resp = requests.get("https://medium.com/@mingchikuo", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("article")
        find2 = find.find("h2")
        mingchi_headline[1] = find2.text.strip()
        link = find.find("a", href=True).get("href")
        now = datetime.now().time()
        if mingchi_headline[0] != mingchi_headline[1] and count != 0:
            print(now, "\t", "Ming Chi Kuo", "\t", mingchi_headline[1])
            winsound.Beep(2500, 400)
            medium = "https://medium.com"
            print(medium.strip() + link.strip())
        mingchi_headline[0] = mingchi_headline[1]
        count += 1
        time.sleep(1.5)

def icahn():
    count = 0
    while True:
        resp = requests.get("https://carlicahn.com/letters", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find("h2")
        icahn_headline[1] = find.text.strip()
        now = datetime.now().time()
        if icahn_headline[0] != icahn_headline[1] and count != 0:
            print(now, "\t", "Carl Icahn", "\t", icahn_headline[1])
            winsound.Beep(2500, 400)
        icahn_headline[0] = icahn_headline[1]
        count += 1
        time.sleep(1.5)

def srpt():
   count = 0
   while True:
       resp = requests.get(
           "https://www.fda.gov/advisory-committees/advisory-committee-calendar",
           headers={"User-Agent": "Mozilla/6.0"})
       soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
       find = soup.find("tbody")
       find2 = find.find("a", href=True)
       srpt_headline[1] = find2.text.strip()
       now = datetime.now().time()
       if srpt_headline[0] != srpt_headline[1] and count != 0:
           print(now, "\t", "FDA Adcomm", "\t", srpt_headline[1])
           winsound.Beep(2500, 400)
           print("https://www.fda.gov" + find2.get("href"))
       srpt_headline[0] = srpt_headline[1]
       count += 1
       time.sleep(1.5)

def msft():
    count = 0
    while True:
        resp = requests.get(
            "https://www.microsoft.com/en-us/investor/earnings/FY-2024-Q1/press-release-webcast",
            headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="c-list f-bare")
        find2 = find.findAll("a", href=True)
        msft_headline[1] = find2[2].text.strip()
        now = datetime.now().time()
        if msft_headline[0] != msft_headline[1] and count != 0:
            print(now, "\t", "MSFT", "\t", msft_headline[1])
            winsound.Beep(2500, 400)
            print(find2[2].get("href"))
        msft_headline[0] = msft_headline[1]
        count += 1
        time.sleep(1.5)

def nikkei():
    count = 0
    while True:
        resp = requests.get("https://asia.nikkei.com/rss/feed/nar?_gl=1", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
        find = soup.findAll("title")
        nikkei_headline[1] = find[1].text.strip()
        now = datetime.now().time()
        if nikkei_headline[0] != nikkei_headline[1] and count != 0:
            print(now, "\t", "Nikkei", "\t", nikkei_headline[1])
            winsound.Beep(2500, 400)
        nikkei_headline[0] = nikkei_headline[1]
        count += 1
        time.sleep(1.5)

def bleepcomp():
   count = 0
   while True:
       resp = requests.get("https://www.bleepingcomputer.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
       soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
       find = soup.find("item")
       bleepcomp_headline[1] = find.title.text.strip()
       link = find.link.text.strip()
       now = datetime.now().time()
       if bleepcomp_headline[0] != bleepcomp_headline[1] and count != 0:
           print(now, "\t", "Bleeping Comp", "\t", bleepcomp_headline[1])
           winsound.Beep(2500, 200)
           print(link)
       bleepcomp_headline[0] = bleepcomp_headline[1]
       count += 1
       time.sleep(1.5)

def punchbowl():
    count = 0
    while True:
        resp = requests.get("https://punchbowl.news/news/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, 'lxml')  # Modified parser
        find = soup.find(class_="mlArticleLanding__more-from-the")
        find2 = find.find("a", href=True)
        link = find2.get("href")
        punchbowl_headline[1] = find2.find("h5").text.strip()
        now = datetime.now().time()
        if punchbowl_headline[0] != punchbowl_headline[1] and count != 0:
            print(now, "\t", "Punchbowl", "\t", punchbowl_headline[1])
            winsound.Beep(2500, 400)
            print(link)
        punchbowl_headline[0] = punchbowl_headline[1]
        count += 1
        time.sleep(1.5)

def hntrbrk():
   count = 0
   while True:
       resp = requests.get("https://hntrbrk.com/feed/", headers={"User-Agent": "Mozilla/4.0"})
       soup = BeautifulSoup(resp.content, 'lxml-xml')  # Modified parser
       results = soup.find("item")
       hntrbrk_headline[1] = results.title.text.strip()
       find = results.find("description")
       desc = find.text.strip()
       now = datetime.now().time()
       if hntrbrk_headline[0] != hntrbrk_headline[1] and count != 0:
           print(now, "\t", "Hunterbrook", "\t", hntrbrk_headline[1])
           print(desc)
           winsound.Beep(2500, 400)
       hntrbrk_headline[0] = hntrbrk_headline[1]
       count += 1
       time.sleep(1.5)

# Start the threads
# Uncomment the functions you wish to run

citron_thread = threading.Thread(target=citron)
citron_thread.start()

scorpion_thread = threading.Thread(target=scorpion)
scorpion_thread.start()

iceberg_thread = threading.Thread(target=iceberg)
iceberg_thread.start()

# statnews_thread = threading.Thread(target=statnews)
# statnews_thread.start()

hindenburg_thread = threading.Thread(target=hindenburg)
hindenburg_thread.start()

wolfpack_thread = threading.Thread(target=wolfpack)
wolfpack_thread.start()

# whitediam_thread = threading.Thread(target=whitediam)
# whitediam_thread.start()

culper_thread = threading.Thread(target=culper)
culper_thread.start()

kerrisdaleL_thread = threading.Thread(target=kerrisdaleL)
kerrisdaleL_thread.start()

kerrisdaleS_thread = threading.Thread(target=kerrisdaleS)
kerrisdaleS_thread.start()

usps_thread = threading.Thread(target=usps)
usps_thread.start()

cdc_thread = threading.Thread(target=cdc)
cdc_thread.start()

# info_thread = threading.Thread(target=information)
# info_thread.start()

# electrek_thread = threading.Thread(target=electrek)
# electrek_thread.start()

# insideev_thread = threading.Thread(target=insideev)
# insideev_thread.start()

fda_thread = threading.Thread(target=fda)
fda_thread.start()

fda2_thread = threading.Thread(target=fda2)
fda2_thread.start()

# bleecker_thread = threading.Thread(target=bleecker)
# bleecker_thread.start()

# ftc_thread = threading.Thread(target=ftc)
# ftc_thread.start()

# sava_thread = threading.Thread(target=sava)
# sava_thread.start()

# bearcave_thread = threading.Thread(target=bearcave)
# bearcave_thread.start()

spruce_thread = threading.Thread(target=spruce)
spruce_thread.start()

benzinga_thread = threading.Thread(target=benzinga)
benzinga_thread.start()

nytimes_thread = threading.Thread(target=nytimes)
nytimes_thread.start()

pershing_thread = threading.Thread(target=pershing)
pershing_thread.start()

nypost_thread = threading.Thread(target=nypost)
nypost_thread.start()

aircurrent_thread = threading.Thread(target=aircurrent)
aircurrent_thread.start()

sec8k_thread = threading.Thread(target=sec8k)
sec8k_thread.start()

secRW_thread = threading.Thread(target=secRW)
secRW_thread.start()

cnbc_thread = threading.Thread(target=cnbc)
cnbc_thread.start()

# freeport_thread = threading.Thread(target=freeport)
# freeport_thread.start()

# mingchi_thread = threading.Thread(target=mingchi)
# mingchi_thread.start()

# icahn_thread = threading.Thread(target=icahn)
# icahn_thread.start()

# srpt_thread = threading.Thread(target=srpt)
# srpt_thread.start()

# msft_thread = threading.Thread(target=msft)
# msft_thread.start()

# nikkei_thread = threading.Thread(target=nikkei)
# nikkei_thread.start()

bleepcomp_thread = threading.Thread(target=bleepcomp)
bleepcomp_thread.start()

# faa_thread = threading.Thread(target=faa)
# faa_thread.start()

# punchbowl_thread = threading.Thread(target=punchbowl)
# punchbowl_thread.start()

hntrbrk_thread = threading.Thread(target=hntrbrk)
hntrbrk_thread.start()

webbrowser.open_new_tab