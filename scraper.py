# Import API

from pandas import *
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import regex
import winsound
import threading
import webbrowser


# citron_headline = [0]*2
scorpion_headline = [0]*2
# iceberg_headline = [0]*2
# statnews_headline = [0]*2
hindenburg_headline = [0]*2
wolfpack_headline = [0]*2
# whitediam_headline = [0]*2
# tipranks_headline = [0]*2
culper_headline = [0]*2
kerrisdaleL_headline = [0]*2
kerrisdaleS_headline = [0]*2
sp_headline = [0]*2
usps_headline = [0]*2
cdc_headline = [0]*2
bleecker_headline = [0]*2
info_headline = [0]*2
electrek_headline = [0]*2
insideev_headline = [0]*2
fda_headline = [0]*2
fda2_headline = [0]*2
bleecker_headline = [0]*2
ftc_headline = [0]*2
sava_headline = [0]*2
insider_headline = [0]*2
bearcave_headline = [0]*2
spruce_headline = [0]*2
benzinga_headline = [0]*2
nytimes_headline = [0]*2
pershing_headline = [0]*2
nypost_headline = [0]*2
# cnbc_retail_headline = [0]*2
# cnbc_media_headline = [0]*2
# cnbc_tech_headline = [0]*2
aircurrent_headline = [0]*2
# wapo_amzn_headline = [0]*2-
# wapo_tsla_headline = [0]*2
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
        resp = requests.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=8-k&company=&dateb=&owner=include&start=0&count=40&output=atom", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("entry")
        find2 = find.find("title")
        find3 = find.find("summary")
        list1 = find3.text.split()
        item = list(set(list1).intersection(sec_filing))
        sec8k_headline[1] = find2.text
        now = datetime.now().time()
        if sec8k_headline[0] != sec8k_headline[1] and count != 0 and len(item) != 0:
            print(now, "\t", "SEC 8K", "\t", sec8k_headline[1])
            winsound.Beep(2500, 200)
            print(item)
        sec8k_headline[0] = sec8k_headline[1]
        count = count + 1
        time.sleep(1.5)

def secRW():
    count = 0
    while True:
        resp = requests.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=RW&company=&dateb=&owner=include&start=0&count=40&output=atom",
        headers={"User-Agent": "Trillium jkim@trlm.com"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("entry")
        find2 = find.find("title")
        secRW_headline[1] = find2.text
        now = datetime.now().time()
        if secRW_headline[0] != secRW_headline[1] and count != 0:
            print(now, "\t", "SEC RW", "\t", secRW_headline[1])
            stock = secRW_headline[1].split("-")[1]
            stock2 = stock.split("(")[0]
            url = "https://www.google.com/search?q={}".format(stock2) + " stock"
            webbrowser.open_new_tab(url)
            winsound.Beep(2500, 200)
        secRW_headline[0] = secRW_headline[1]
        count = count + 1
        time.sleep(1.5)

def citron():
    count = 0
    while True:
        resp = requests.get("https://citronresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="avia_textblock")
        find2 = find.find("h2")
        citron_headline[1] = find2.text
        now = datetime.now().time()
        if citron_headline[0] != citron_headline[1] and count != 0:
            print(now, "\t", "Citron", "\t", citron_headline[1])
            winsound.Beep(2500, 200)
        citron_headline[0] = citron_headline[1]
        count = count + 1
        time.sleep(1.5)

def scorpion():
    count = 0
    while True:
        resp = requests.get("https://scorpioncapital.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="image-subtitle sqs-dynamic-text")
        scorpion_headline[1] = find.text
        now = datetime.now().time()
        if scorpion_headline[0] != scorpion_headline[1] and count != 0:
            print(now, "\t", "Scorpion", "\t", scorpion_headline[1])
            winsound.Beep(2500, 200)
        scorpion_headline[0] = scorpion_headline[1]
        count = count + 1
        time.sleep(1.5)

def iceberg():
    count = 0
    while True:
        resp = requests.get("https://iceberg-research.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h2")
        iceberg_headline[1] = find.text
        now = datetime.now().time()
        if iceberg_headline[0] != iceberg_headline[1] and count != 0:
            print(now, "\t", "Iceberg", "\t", iceberg_headline[1])
            winsound.Beep(2500, 200)
        iceberg_headline[0] = iceberg_headline[1]
        count = count + 1
        time.sleep(1.5)

def statnews():
    count = 0
    while True:
        resp = requests.get("https://www.statnews.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        statnews_headline[1] = find.title.text
        now = datetime.now().time()
        if statnews_headline[0] != statnews_headline[1] and count != 0:
            print(now, "\t", "Statnews", "\t", statnews_headline[1])
            winsound.Beep(2500, 200)
        statnews_headline[0] = statnews_headline[1]
        count = count + 1
        time.sleep(1.5)

def hindenburg():
    count = 0
    while True:
        resp = requests.get("https://hindenburgresearch.com/", headers={"User-Agent": "Mozilla/4.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h1")
        find2 = find.find("a", href=True)
        hindenburg_headline[1] = find2.text
        now = datetime.now().time()
        if hindenburg_headline[0] != hindenburg_headline[1] and count != 0:
            print(now, "\t", "Hindenburg", "\t", hindenburg_headline[1])
            stock = hindenburg_headline[1].split(":")[0]
            url = "https://www.google.com/search?q={}".format(stock) + " stock"
            webbrowser.open_new_tab(url)
            winsound.Beep(2500, 200)
        hindenburg_headline[0] = hindenburg_headline[1]
        count = count + 1
        time.sleep(1.5)

def wolfpack():
    count = 0
    while True:
        resp = requests.get("https://wolfpackresearch.com/research/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h4")
        wolfpack_headline[1] = find.text
        now = datetime.now().time()
        if wolfpack_headline[0] != wolfpack_headline[1] and count != 0:
            print(now, "\t", "Wolfpack", "\t", wolfpack_headline[1])
            winsound.Beep(2500, 200)
        wolfpack_headline[0] = wolfpack_headline[1]
        count = count + 1
        time.sleep(1.5)

def whitediam():
    count = 0
    while True:
        resp = requests.get("https://seekingalpha.com/author/white-diamond-research.xml", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        whitediam_headline[1] = find.title.text
        now = datetime.now().time()
        if whitediam_headline[0] != whitediam_headline[1] and count != 0:
            print(now, "\t", "White Dmnd", "\t", whitediam_headline[1])
            winsound.Beep(2500, 200)
        whitediam_headline[0] = whitediam_headline[1]
        count = count + 1
        time.sleep(1.5)

# def tipranks():
#     count = 0
#     while True:
#         tp_ticker = []
#         resp = requests.get("https://www.tipranks.com/news/author/michael-marcus", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#
#
#         for a in find2:
#             if len(a) == 3:
#                 tp_ticker.append(a.text)
#         if tipranks_headline[0] != tipranks_headline[1] and author == "Michael Marcus" and count != 0:
#             now = datetime.now().time()
#             print(now, "\t", "TipRanks", "\t", tp_ticker)
#             print(tipranks_headline[1])
#             winsound.Beep(2500, 400)
#         tipranks_headline[0] = tipranks_headline[1]
#         count = count + 1
#         time.sleep(1.5)

def culper():
    count = 0
    while True:
        resp = requests.get("https://culperresearch.com/latest-research", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("strong")
        culper_headline[1] = find.text
        now = datetime.now().time()
        if culper_headline[0] != culper_headline[1] and count != 0:
            print(now, "\t", "Culper", "\t", culper_headline[1])
            winsound.Beep(2500, 200)
        culper_headline[0] = culper_headline[1]
        count = count + 1
        time.sleep(1.5)

def kerrisdaleL():
    count = 0
    while True:
        resp = requests.get("https://www.kerrisdalecap.com/blog/?cat=long", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h2")
        kerrisdaleL_headline[1] = find.text
        now = datetime.now().time()
        if kerrisdaleL_headline[0] != kerrisdaleL_headline[1] and count != 0:
            print(now, "\t", "KerrisdaleL", "   ", kerrisdaleL_headline[1])
            winsound.Beep(2500, 200)
        kerrisdaleL_headline[0] = kerrisdaleL_headline[1]
        count = count + 1
        time.sleep(1.5)

def kerrisdaleS():
    count = 0
    while True:
        resp = requests.get("https://www.kerrisdalecap.com/blog/?cat=short", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h2")
        kerrisdaleS_headline[1] = find.text
        now = datetime.now().time()
        if kerrisdaleS_headline[0] != kerrisdaleS_headline[1] and count != 0:
            print(now, "\t", "KerrisdaleS", "   ", kerrisdaleS_headline[1])
            winsound.Beep(2500, 200)
        kerrisdaleS_headline[0] = kerrisdaleS_headline[1]
        count = count + 1
        time.sleep(1.5)


# filter for "Set to Join"
def sp():
    count = 0
    while True:
        resp = requests.get("https://www.spglobal.com/spdji/en/media-center/news-announcements/#indexNews",
                            headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        print(soup)
        find = soup.find(class_="filterable-list-row data-row")
        print(find)
        sp_headline[1] = find("a", href=True)
        print(sp_headline[1])
        now = datetime.now().time()
        if sp_headline[0] != sp_headline[1] and count != 0:
            print(now, "\t", "S&P", "\t", sp_headline[1])
            winsound.Beep(2500, 200)
        sp_headline[0] = sp_headline[1]
        count = count + 1
        time.sleep(1.5)

def usps():
    count = 0
    while True:
        resp = requests.get("https://about.usps.com/news/latestnews.rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        usps_headline[1] = find.title.text
        now = datetime.now().time()
        if usps_headline[0] != usps_headline[1] and count != 0:
            print(now, "\t", "USPS", "\t", usps_headline[1])
            winsound.Beep(2500, 200)
        usps_headline[0] = usps_headline[1]
        count = count + 1
        time.sleep(1.5)

def cdc():
    count = 0
    while True:
        resp = requests.get("https://tools.cdc.gov/api/v2/resources/media/132608.rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        cdc_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if cdc_headline[0] != cdc_headline[1] and count != 0:
            print(now, "\t", "CDC", "\t", cdc_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        cdc_headline[0] = cdc_headline[1]
        count = count + 1
        time.sleep(1.5)

def information():
   count = 0
   while True:
       resp = requests.get("https://www.theinformation.com/features/exclusive", headers={"User-Agent": "Mozilla/4.0"})
       soup = BeautifulSoup(resp.content, features="lxml")
       find = soup.find(class_="no-link track-click")
       info_headline[1] = find.text
       now = datetime.now().time()
       info = "https://www.theinformation.com"
       link = info + find.get("href")
       if info_headline[0] != info_headline[1] and count != 0:
           print(now, "\t", "The Information", "\t", info_headline[1])
           print(link)
           winsound.Beep(2500, 200)
       info_headline[0] = info_headline[1]
       count = count + 1
       time.sleep(5)

def electrek():
    count = 0
    while True:
        resp = requests.get("https://electrek.co/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        electrek_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if electrek_headline[0] != electrek_headline[1] and count != 0:
            print(now, "\t", "Electrek", "\t", electrek_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        electrek_headline[0] = electrek_headline[1]
        count = count + 1
        time.sleep(1.5)

def insideev():
    count = 0
    while True:
        resp = requests.get("https://insideevs.com/rss/news/all/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        insideev_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if insideev_headline[0] != insideev_headline[1] and count != 0:
            print(now, "\t", "InsideEV", "\t", insideev_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        insideev_headline[0] = insideev_headline[1]
        count = count + 1
        time.sleep(1.5)

# FDA AdComm Documents
def fda():
    count = 0
    while True:
        resp = requests.get("https://www.fda.gov/advisory-committees/advisory-committee-calendar/vaccines-and-related-biological-products-advisory-committee-september-17-2021-meeting-announcement", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("tbody")
        find2 = find.find("tr")
        find3 = find2.find("td")
        fda_headline[1] = find3.text
        now = datetime.now().time()
        if fda_headline[0] != fda_headline[1] and count != 0:
            print(now, "\t", "FDA", "\t", fda_headline[1])
            winsound.Beep(2500, 200)
        fda_headline[0] = fda_headline[1]
        count = count + 1
        time.sleep(1.5)

# Adcomm Scrap
# def fda():
#     count = 0
#     while True:
#         data = []
#         resp = requests.get("https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=report.page", headers={"User-Agent": "Mozilla/5.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find("tbody")
#         find2 = find.find("tr")
#         find3 = find2.findAll("td")
#         for i in find3:
#             data.append(i.text)
#         for i in range(3):
#             data.pop(1)
#         data.pop(2)
#         fda_headline[1] = data
#         now = datetime.now().time()
#         if fda_headline[0] != fda_headline[1] and count != 0:
#             print(now, "\t", "FDA", "\t", fda_headline[1])
#             winsound.Beep(2500, 400)
#         fda_headline[0] = fda_headline[1]
#         count = count + 1
#         time.sleep(1.5)

# BIIB Aducanumab specific search
def fda2():
    count = 0
    while True:
        resp = requests.get("https://search.fda.gov/search?utf8=%E2%9C%93&affiliate=fda1&query=761178&commit=Search",
                           headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="title")
        fda2_headline[1] = find.text
        find2 = find.find("a", href=True)
        link = find2
        now = datetime.now().time()
        if fda2_headline[0] != fda2_headline[1] and count != 0:
            print(now, "\t", "FDA", "\t", fda2_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        fda2_headline[0] = fda2_headline[1]
        count = count + 1
        time.sleep(1.5)

def bleecker():
    count = 0
    while True:
        resp = requests.get("https://bleeckerstreetresearch.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        bleecker_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if bleecker_headline[0] != bleecker_headline[1] and count != 0:
            print(now, "\t", "Bleecker", "\t", Bleecker_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        bleecker_headline[0] = bleecker_headline[1]
        count = count + 1
        time.sleep(1.5)

def ftc():
    count = 0
    while True:
        resp = requests.get("https://www.ftc.gov/news-events/news/press-releases", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="field-content")
        find2 = find.findAll("a", href=True)
        ftc_headline[1] = find2[1].text
        link = "https://www.ftc.gov" + find2[1].get("href")
        now = datetime.now().time()
        if ftc_headline[0] != ftc_headline[1] and count != 0:
            print(now, "\t", "FTC", "\t", ftc_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        ftc_headline[0] = ftc_headline[1]
        count = count + 1
        time.sleep(1.5)

def faa():
    count = 0
    while True:
        resp = requests.get("https://www.faa.gov/newsroom/press_releases/rss", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        faa_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if faa_headline[0] != faa_headline[1] and count != 0:
            print(now, "\t", "FAA", "\t", faa_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        faa_headline[0] = faa_headline[1]
        count = count + 1
        time.sleep(1.5)

# https://www.cassavasciences.com/rss/news-releases.xml
def sava():
    count = 0
    while True:
        resp = requests.get("https://www.cassavasciences.com/rss/news-releases.xml", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        sava_headline[1] = find.title.text
        link = find.link.text
        now = datetime.now().time()
        if sava_headline[0] != sava_headline[1] and count != 0:
            print(now, "\t", "SAVA", "\t", sava_headline[1])
            winsound.Beep(2500, 200)
            print(link)
        sava_headline[0] = sava_headline[1]
        count = count + 1
        time.sleep(1.5)

# def insider():
#     count = 0
#     while True:
#         resp = requests.get("https://markets.businessinsider.com/rss/news", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="xml")
#         find = soup.find("item")
#         insider_headline[1] = find.title.text
#         link = find.link.text
#         now = datetime.now().time()
#         if insider_headline[0] != insider_headline[1] and count != 0:
#             print(now, "\t", "Business Insider", "\t", insider_headline[1])
#             winsound.Beep(2500, 400)
#             print(link)
#         insider_headline[0] = insider_headline[1]
#         count = count + 1
#         time.sleep(1.5)

def bearcave():
    count = 0
    while True:
        resp = requests.get("https://thebearcave.substack.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="post-preview-content")
        find2 = find.find(class_="post-preview-title newsletter")
        bearcave_headline[1] = find2.text
        now = datetime.now().time()
        if bearcave_headline[0] != bearcave_headline[1] and count != 0:
            print(now, "\t", "Bearcave", "\n", bearcave_headline[1])
            winsound.Beep(2500, 200)
        bearcave_headline[0] = bearcave_headline[1]
        count = count + 1
        time.sleep(2)

def spruce():
    count = 0
    while True:
        resp = requests.get("https://www.sprucepointcap.com/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="main_box")
        find3 = soup.find(class_="box_content_title")
        find2 = find.find(class_="box_content_subtitle")
        spruce_headline[1] = find2.text
        text = find3.text
        print(spruce_headline[1])
        print(text)
        now = datetime.now().time()
        if spruce_headline[0] != spruce_headline[1] and count != 0:
            print(now, "\t", "Spruce", "\t", spruce_headline[1].strip())
            print(text.strip())
            winsound.Beep(2500, 200)
        spruce_headline[0] = spruce_headline[1]
        count = count + 1
        time.sleep(1.5)

def benzinga():
    count = 0
    while True:
        resp = requests.get("https://www.benzinga.com/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="CarouselWrapper__Title-sc-1t2xyai-1 gaybWS title")
        benzinga_headline[1] = find.text
        now = datetime.now().time()
        if benzinga_headline[0] != benzinga_headline[1] and count != 0:
            print(now, "\t", "Benzinga", "\t", benzinga_headline[1])
            winsound.Beep(2500, 200)
            print(text)
        benzinga_headline[0] = benzinga_headline[1]
        count = count + 1
        time.sleep(1.5)

def nytimes():
    count = 0
    while True:
        resp = requests.get("https://www.nytimes.com/section/business", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="css-1kv6qi e15t083i0")
        nytimes_headline[1] = find.text
        find2 = soup.find(class_="css-1pga48a e15t083i1")
        text = find2.text
        find3 = soup.find(class_="css-1l4spti")
        link = find3.find("a", href=True)
        now = datetime.now().time()
        nytimes = "https://www.nytimes.com"
        if nytimes_headline[0] != nytimes_headline[1] and count != 0:
            print(now, "\t", "NYTimes", "\t", nytimes_headline[1])
            winsound.Beep(2500, 200)
            print(text)
            print(nytimes.strip() + link.get("href").strip())
        nytimes_headline[0] = nytimes_headline[1]
        count = count + 1
        time.sleep(1.5)

def nypost():
    count = 0
    while True:
        resp = requests.get("https://nypost.com/tag/mergers-acquisitions/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="story__headline headline headline--archive")
        find2 = find.find("a")
        nypost_headline[1] = find2.text
        find3 = soup.find(class_="story__excerpt body")
        text = find3.text
        now = datetime.now().time()
        if nypost_headline[0] != nypost_headline[1] and count != 0:
            print(now, "\t", "NY Post", "\t", nypost_headline[1].strip())
            winsound.Beep(2500, 200)
            print(text.strip())
        nypost_headline[0] = nypost_headline[1]
        count = count + 1
        time.sleep(1.5)

def pershing():
    count = 0
    while True:
        resp = requests.get("https://pershingsquareholdings.com/company-reports/letters-to-shareholders/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="wpb_column vc_column_container vc_col-sm-9")
        find2 = find.find("p")
        pershing_headline[1] = find2.text
        link = find2.find("a", href=True)
        now = datetime.now().time()
        if pershing_headline[0] != pershing_headline[1] and count != 0:
            print(now, "\t", "Pershing", "\t", pershing_headline[1])
            winsound.Beep(2500, 200)
            print(link.get("href"))
        pershing_headline[0] = pershing_headline[1]
        count = count + 1
        time.sleep(1.5)

# def cnbc_retail():
#     count = 0
#     while True:
#         resp = requests.get("https://cnbc.com/lauren-thomas", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find(class_="RiverCard-titleContainer")
#         find2 = find.find("a")
#         cnbc_retail_headline[1] = find2.text
#         now = datetime.now().time()
#         if cnbc_retail_headline[0] != cnbc_retail_headline[1] and count != 0:
#             print(now, "\t", "CNBC Retail", "\t", cnbc_retail_headline[1])
#             winsound.Beep(2500, 400)
#         cnbc_retail_headline[0] = cnbc_retail_headline[1]
#         count = count + 1
#         time.sleep(1.5)

# def cnbc_media():
#     count = 0
#     while True:
#         resp = requests.get("http://cnbc.com/alex-sherman/", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find(class_="RiverCard-titleContainer")
#         find2 = find.find("a")
#         cnbc_media_headline[1] = find2.text
#         now = datetime.now().time()
#         if cnbc_media_headline[0] != cnbc_media_headline[1] and count != 0:
#             print(now, "\t", "CNBC Media", "\t", cnbc_media_headline[1])
#             winsound.Beep(2500, 400)
#         cnbc_media_headline[0] = cnbc_media_headline[1]
#         count = count + 1
#         time.sleep(1.5)
#
# # CNBC Technology: Annie covers AMZN
# def cnbc_tech():
#     count = 0
#     while True:
#         resp = requests.get("https://www.cnbc.com/annie-palmer/", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find(class_="RiverCard-titleContainer")
#         find2 = find.find("a")
#         cnbc_tech_headline[1] = find2.text
#         now = datetime.now().time()
#         if cnbc_tech_headline[0] != cnbc_tech_headline[1] and count != 0:
#             print(now, "\t", "CNBC Tech", "\t", cnbc_tech_headline[1])
#             winsound.Beep(2500, 400)
#         cnbc_tech_headline[0] = cnbc_tech_headline[1]
#         count = count + 1
#         time.sleep(1.5)

def aircurrent():
    count = 0
    while True:
        resp = requests.get("https://theaircurrent.com/")
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find("h3")
        find2 = find.find("a", href=True)
        aircurrent_headline[1] = find2.text
        link = find2.get("href")
        now = datetime.now().time()
        if aircurrent_headline[0] != aircurrent_headline[1] and count != 0:
            print(now, "\t", "Air Current", "\t", aircurrent_headline[1])
            winsound.Beep(2500, 400)
            print(link)
        aircurrent_headline[0] = aircurrent_headline[1]
        count = count + 1
        time.sleep(1.5)

# def wapo_amzn():
#     count = 0
#     while True:
#         resp = requests.get("https://www.washingtonpost.com/people/caroline-odonovan/", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find(class_="font-md2 font-bold font--headline lh-sm gray-darkest hover-blue mb-xs")
#         wapo_amzn_headline[1] = find.text
#         find2 = soup.find(class_="font-xxs font-light font--meta-text lh-sm gray-dark mb-xs mw-600")
#         text = find2.text
#         now = datetime.now().time()
#         if wapo_amzn_headline[0] != wapo_amzn_headline[1] and count != 0:
#             print(now, "\t", "WaPo AMZN", "\t", wapo_amzn_headline[1])
#             print(text)
#             winsound.Beep(2500, 400)
#         wapo_amzn_headline[0] = wapo_amzn_headline[1]
#         count = count + 1
#         time.sleep(1.5)
#
# def wapo_tsla():
#     count = 0
#     while True:
#         resp = requests.get("https://www.washingtonpost.com/people/faiz-siddiqui/", headers={"User-Agent": "Mozilla/6.0"})
#         soup = BeautifulSoup(resp.content, features="lxml")
#         find = soup.find(class_="font-md2 font-bold font--headline lh-sm gray-darkest hover-blue mb-xs")
#         wapo_tsla_headline[1] = find.text
#         find2 = soup.find(class_="font-xxs font-light font--meta-text lh-sm gray-dark mb-xs mw-600")
#         text = find2.text
#         now = datetime.now().time()
#         if wapo_tsla_headline[0] != wapo_tsla_headline[1] and count != 0:
#             print(now, "\t", "WaPo TSLA", "\t", wapo_tsla_headline[1])
#             print(text)
#             winsound.Beep(2500, 400)
#         wapo_tsla_headline[0] = wapo_tsla_headline[1]
#         count = count + 1
#         time.sleep(1.5)

def cnbc():
    count = 0
    while True:
        resp = requests.get("https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.find("item")
        cnbc_headline[1] = find.title.text
        link = find.link.text
        text = find.description.text
        now = datetime.now().time()
        if cnbc_headline[0] != cnbc_headline[1] and count != 0:
            print(now, "\t", "CNBC", "\t", cnbc_headline[1])
            winsound.Beep(2500, 400)
            print(link)
            print(text)
        cnbc_headline[0] = cnbc_headline[1]
        count = count + 1
        time.sleep(1.5)

def freeport():
    count = 0
    while True:
        resp = requests.get("http://www.newsrouter.com/Newsrouter_uploads/77/newsroom.asp", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features = "lxml")
        find = soup.find("tr", class_="bodyText")
        freeport_headline[1] = find.text
        find2 = find.findAll("td")
        find3 = find2[1]
        link = find3.find("a", href=True)
        now = datetime.now().time()
        if freeport_headline[0] != freeport_headline[1] and count != 0:
            print(now, "\t", "Freeport LNG", "\t", freeport_headline[1])
            winsound.Beep(2500, 400)
            freeportlng = "http://www.newsrouter.com/Newsrouter_uploads/77/"
            print(freeportlng.strip() + link.get("href").strip())
        freeport_headline[0] = freeport_headline[1]
        count = count + 1
        time.sleep(1.5)

def mingchi():
    count = 0
    while True:
        resp = requests.get("https://medium.com/@mingchikuo", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features = "lxml")
        find = soup.find("article")
        find2 = find.find(class_="au av aw ax ay az ba bb bc bd be bf bg bh bi")
        mingchi_headline[1] = find2.text
        link = find.find(class_="au av aw ax ay az ba bb bc bd be bf bg bh bi", href=True)
        now = datetime.now().time()
        if mingchi_headline[0] != mingchi_headline[1] and count != 0:
            print(now, "\t", "Ming Chi Kuo", "\t", mingchi_headline[1])
            winsound.Beep(2500, 400)
            medium = "https://medium.com"
            print(medium.strip() + link.get("href").strip())
        mingchi_headline[0] = mingchi_headline[1]
        count = count + 1
        time.sleep(1.5)

def icahn():
    count = 0
    while True:
        resp = requests.get("https://carlicahn.com/letters", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features = "lxml")
        find = soup.find("h2")
        icahn_headline[1] = find.text
        now = datetime.now().time()
        if icahn_headline[0] != icahn_headline[1] and count != 0:
            print(now, "\t", "Carl Icahn", "\t", icahn_headline[1])
            winsound.Beep(2500, 400)
        icahn_headline[0] = icahn_headline[1]
        count = count + 1
        time.sleep(1.5)

def srpt():
   count = 0
   while True:
       resp = requests.get("https://www.fda.gov/advisory-committees/advisory-committee-calendar/cellular-tissue-and-gene-therapies-advisory-committee-may-12-2023-meeting-announcement-05122023", headers={"User-Agent": "Mozilla/6.0"})
       soup = BeautifulSoup(resp.content, features = "lxml")
       find = soup.find("tbody")
       find2 = find.find("a", href=True)
       srpt_headline[1] = find2.text
       now = datetime.now().time()
       if srpt_headline[0] != srpt_headline[1] and count != 0:
           print(now, "\t", "FDA Adcomm", "\t", srpt_headline[1])
           winsound.Beep(2500, 400)
           print("https://www.fda.gov" + find2.get("href"))
       srpt_headline[0] = srpt_headline[1]
       count = count + 1
       time.sleep(1.5)

def msft():
    count = 0
    while True:
        resp = requests.get("https://www.microsoft.com/en-us/investor/earnings/FY-2024-Q1/press-release-webcast",
            headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="c-list f-bare")
        find2 = find.findAll("a", href=True)
        msft_headline[1] = find2[2].text
        now = datetime.now().time()
        if msft_headline[0] != msft_headline[1] and count != 0:
            print(now, "\t", "MSFT", "\t", msft_headline[1])
            winsound.Beep(2500, 400)
            print(find2[2].get("href"))
        msft_headline[0] = msft_headline[1]
        count = count + 1
        time.sleep(1.5)

def nikkei():
    count = 0
    while True:
        resp = requests.get("https://asia.nikkei.com/rss/feed/nar?_gl=1", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="xml")
        find = soup.findAll("title")
        nikkei_headline[1] = find[1].text
        now = datetime.now().time()
        if nikkei_headline[0] != nikkei_headline[1] and count != 0:
            print(now, "\t", "Nikkei", "\t", nikkei_headline[1])
            winsound.Beep(2500, 400)
        nikkei_headline[0] = nikkei_headline[1]
        count = count + 1
        time.sleep(1.5)

def bleepcomp():
   count = 0
   while True:
       resp = requests.get("https://www.bleepingcomputer.com/feed/", headers={"User-Agent": "Mozilla/6.0"})
       soup = BeautifulSoup(resp.content, features="xml")
       find = soup.find("item")
       bleepcomp_headline[1] = find.title.text
       link = find.link.text
       now = datetime.now().time()
       if bleepcomp_headline[0] != bleepcomp_headline[1] and count != 0:
           print(now, "\t", "Bleeping Comp", "\t", bleepcomp_headline[1])
           winsound.Beep(2500, 200)
           print(link)
       bleepcomp_headline[0] = bleepcomp_headline[1]
       count = count + 1
       time.sleep(1.5)

def punchbowl():
    count = 0
    while True:
        resp = requests.get("https://punchbowl.news/news/", headers={"User-Agent": "Mozilla/6.0"})
        soup = BeautifulSoup(resp.content, features="lxml")
        find = soup.find(class_="mlArticleLanding__more-from-the")
        find2 = find.find("a", href=True)
        link = find2.get("href")
        punchbowl_headline[1] = find2.find("h5").text
        now = datetime.now().time()
        if punchbowl_headline[0] != punchbowl_headline[1] and count != 0:
            print(now, "\t", "Punchbowl", "\t", Punchbowl_headline[1])
            winsound.Beep(2500, 400)
            print(link)
        punchbowl_headline[0] = punchbowl_headline[1]
        count = count + 1
        time.sleep(1.5)

def hntrbrk():
   count = 0
   while True:
       resp = requests.get("https://hntrbrk.com/feed/", headers={"User-Agent": "Mozilla/4.0"})
       soup = BeautifulSoup(resp.content, features="xml")
       results = soup.find("item")
       hntrbrk_headline[1] = results.title.text
       find = results.find("description")
       desc = find.text
       now = datetime.now().time()
       if hntrbrk_headline[0] != hntrbrk_headline[1] and count != 0:
           print(now, "\t", "Hunterbrook", "\t", hntrbrk_headline[1])
           print(desc)
           winsound.Beep(2500, 400)
       hntrbrk_headline[0] = hntrbrk_headline[1]
       count = count + 1
       time.sleep(1.5)

# Run all
# 1
# citron = threading.Thread(target=citron)
# citron.start()
# # 2
# scorpion = threading.Thread(target=scorpion)
# scorpion.start()
# # 3
# iceberg = threading.Thread(target=iceberg)
# iceberg.start()
# # 4
# statnews = threading.Thread(target=statnews)
# statnews.start()
# # 5
hindenburg = threading.Thread(target=hindenburg)
hindenburg.start()
# # 6
# wolfpack = threading.Thread(target=wolfpack)
# wolfpack.start()
# 7
# whitediam = threading.Thread(target=whitediam)
# whitediam.start()
# 8
# tipranks = threading.Thread(target=tipranks)
# tipranks.start()
# 9
# culper = threading.Thread(target=culper)
# culper.start()
# # 10
# kerrisdaleL = threading.Thread(target=kerrisdaleL)
# kerrisdaleL.start()
# # 11
# kerrisdaleS = threading.Thread(target=kerrisdaleS)
# kerrisdaleS.start()
# # 12
# sp = threading.Thread(target=sp)
# sp.start()
# # 13
# usps = threading.Thread(target=usps)
# usps.start()
# # 14
# cdc = threading.Thread(target=cdc)
# cdc.start()
# # 15
# info = threading.Thread(target=information)
# info.start()
# # 16
# electrek = threading.Thread(target=electrek)
# electrek.start()
# # 17
# insideev = threading.Thread(target=insideev)
# insideev.start()
# 18
# fda = threading.Thread(target=fda)
# fda.start()
# 19
# fda2 = threading.Thread(target=fda2)
# fda2.start()
# 20
# bleecker = threading.Thread(target=bleecker)
# bleecker.start()
# 21
# ftc = threading.Thread(target=ftc)
# ftc.start()
# 22
# sava = threading.Thread(target=sava)
# sava.start()
# 23
# insider = threading.Thread(target=insider)
# insider.start()
# 24
# bearcave = threading.Thread(target=bearcave)
# bearcave.start()
# 25
# spruce = threading.Thread(target=spruce)
# spruce.start()
# 26
# benzinga = threading.Thread(target=benzinga)
# benzinga.start()
# 27
# nytimes = threading.Thread(target=nytimes)
# nytimes.start()
# 28
# pershing = threading.Thread(target=pershing)
# pershing.start()
# 29
nypost = threading.Thread(target=nypost)
nypost.start()
# 30
# cnbc_retail = threading.Thread(target=cnbc_retail)
# cnbc_retail.start()
# 31
aircurrent = threading.Thread(target=aircurrent)
aircurrent.start()
# 33
# sec8k = threading.Thread(target=sec8k)
# sec8k.start()
secRW = threading.Thread(target=secRW)
secRW.start()
# 34
# cnbc_media = threading.Thread(target=cnbc_media)
# cnbc_media.start()
# # 35
# cnbc_tech = threading.Thread(target=cnbc_tech)
# cnbc_tech.start()
# 36
# wapo_amzn = threading.Thread(target=wapo_amzn)
# wapo_amzn.start()
# wapo_tsla = threading.Thread(target=wapo_tsla)
# wapo_tsla.start()
# 37
# cnbc = threading.Thread(target=cnbc)
# cnbc.start()
# 38
# freeport = threading.Thread(target=freeport)
# freeport.start()
# 29
# mingchi = threading.Thread(target=mingchi)
# mingchi.start()
# icahn = threading.Thread(target=icahn)
# icahn.start()
# sarepta = threading.Thread(target=srpt)
# sarepta.start()
# microsoft = threading.Thread(target=msft)
# microsoft.start()
# nikkei = threading.Thread(target=nikkei)
# nikkei.start()
bleepcomp = threading.Thread(target=bleepcomp)
bleepcomp.start()
# faa = threading.Thread(target=faa)
# faa.start()
# punchbowl = threading.Thread(target=punchbowl)
# punchbowl.start()
hntrbrk = threading.Thread(target=hntrbrk)
hntrbrk.start()


# https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=400&Site=945&max=10



# https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=216718
# 216718 is RETA NDA #