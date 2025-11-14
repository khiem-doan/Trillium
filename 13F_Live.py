#!/usr/bin/env python3
import argparse
import random
import time
import traceback
import webbrowser
import re
import requests
import threading
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ============== Styling ==============
colorama.init(autoreset=True)

def style_red_bold(s: str) -> str:
    return f"{Style.BRIGHT}{Back.RED}{Fore.BLACK}{s}{Style.RESET_ALL}"

def style_green_bold(s: str) -> str:
    return f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK}{s}{Style.RESET_ALL}"

# ============== Optional beep ==============
try:
    import winsound
    def beep():
        try:
            winsound.Beep(5000, 200)
        except Exception:
            pass
except Exception:
    def beep():
        pass

# ============== NVDA-specific ticker overrides ==============
NVDA_TICKER_OVERRIDES = {
    "COREWEAVE INC": "CRWV",
    "NEBIUS GROUP NV": "NBIS",
    "NEBIUS GROUP N V": "NBIS",
    "WERIDE INC": "WRD",
}
def apply_nvda_overrides(rows):
    for r in rows:
        if not r.get('ticker'):
            k = normalize_company_name(r.get('name', '')).replace('.', '')
            if k.startswith('RECURSION PHARMACEUTICALS IN'):
                r['ticker'] = 'RXRX'
                continue
            for key, tkr in NVDA_TICKER_OVERRIDES.items():
                if k.startswith(key):
                    r['ticker'] = tkr
                    break
    return rows

# ============== User agents & polling ==============
USER_AGENTS_DATA = [
    # --- Desktop user agents ---
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.1", "pct": 31.48},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.3", "pct": 24.07},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.3", "pct": 17.59},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.", "pct": 7.41},
    {"ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.", "pct": 4.63},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.", "pct": 3.7},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Herring/97.1.8280.8", "pct": 2.78},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.3", "pct": 1.85},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.", "pct": 1.85},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 AtContent/95.5.5462.5", "pct": 0.93},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.1958", "pct": 0.93},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3", "pct": 0.93},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.", "pct": 0.93},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3", "pct": 0.93},

    # --- Mobile user agents ---
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.3", "pct": 48.62},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Mobile/15E148 Safari/604.", "pct": 16.57},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/27.0 Chrome/125.0.0.0 Mobile Safari/537.3", "pct": 9.94},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/346.1.704810410 Mobile/15E148 Safari/604.", "pct": 4.97},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.", "pct": 3.31},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/131.0.6778.134 Mobile/15E148 Safari/604.", "pct": 2.76},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 OPR/86.0.0.", "pct": 2.21},
    {"ua": "Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135 Mobile Safari/537.3", "pct": 1.66},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.3", "pct": 1.1},
    {"ua": "Mozilla/5.0 (Android 13; Mobile; rv:133.0) Gecko/133.0 Firefox/133.", "pct": 1.1},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.", "pct": 0.55},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.", "pct": 0.55},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; arm_64; Android 15; 24030PN60G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.98 YaBrowser/24.12.1.98.00 SA/3 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 13; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 12; 220733SG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.105 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; NEN-LX1 Build/HUAWEINEN-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 Mobile Safari/537.36 HuaweiBrowser/15.0.4.312 HMSCore/6.14.0.32", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3", "pct": 0.55},
    {"ua": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.3", "pct": 0.55}
]

ua = random.choice(USER_AGENTS_DATA)['ua']
headers = {'User-Agent': ua}
POLL_MIN_SEC = 1.5
POLL_MAX_SEC = 2.9

# ============== SEC session ==============
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# globals for rotation
__SEC_SESSION = None
__SEC_REQ_COUNT = 0
__SEC_MAX_REQS = 5  # rotate after N requests

def create_session():
    """
    Returns a requests.Session configured for SEC with:
      - ASCII-only UA + contact
      - Retry/backoff
      - Session rotation every __SEC_MAX_REQS requests
    """
    global __SEC_SESSION, __SEC_REQ_COUNT

    # rotate session if needed
    if (__SEC_SESSION is None) or (__SEC_REQ_COUNT >= __SEC_MAX_REQS):
        # close old
        try:
            if __SEC_SESSION is not None:
                __SEC_SESSION.close()
        except Exception:
            pass

        # new session
        __SEC_SESSION = requests.Session()

        # pick UA and ensure ASCII
        raw_ua = random.choice(USER_AGENTS_DATA)['ua']
        ua = raw_ua.encode('ascii', 'ignore').decode()
        contact = "John Doe; john.doe@example.com".encode('ascii', 'ignore').decode()

        __SEC_SESSION.headers.update({
            'User-Agent': f'{ua} ({contact})',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'https://www.sec.gov',
            'Connection': 'keep-alive'
        })

        retry = Retry(
            total=4,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD", "OPTIONS"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        __SEC_SESSION.mount("https://", adapter)
        __SEC_SESSION.mount("http://", adapter)

        __SEC_REQ_COUNT = 0  # reset counter

    # increment and return
    __SEC_REQ_COUNT += 1
    return __SEC_SESSION

# ============== Normalization ==============
def normalize_company_name(name: str) -> str:
    n = (name or "").upper().strip()
    n = re.sub(r'\bFINL\b', 'FINANCIAL', n)
    n = re.sub(r'\bHLDGS\b', 'HOLDINGS', n)
    n = re.sub(r'\bP\s*L\s*C\b', 'PLC', n)
    n = re.sub(r'\bAMER\b', 'AMERICA', n)
    n = re.sub(r'\bPETE\b', 'PETROLEUM', n)
    n = re.sub(r'/.*', '', n)
    n = re.sub(r'\bNEW$', '', n)
    n = re.sub(r'[^\w\s\.]', '', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

# ============== SEC name→ticker map ==============
def load_cik_ticker_mapping(debug=False):
    try:
        s = create_session()
        r = s.get("https://www.sec.gov/files/company_tickers_exchange.json", timeout=20)
        if debug:
            print(f"[mapping] status={r.status_code} content-type={r.headers.get('Content-Type')}")
        r.raise_for_status()
        data = r.json()
        fields = data["fields"]
        ni = fields.index("name"); ti = fields.index("ticker"); ei = fields.index("exchange")
        comp2t = {}
        for row in data["data"]:
            exch = (row[ei] or "").strip()
            if exch not in ("Nasdaq", "NYSE"):
                continue
            name = str(row[ni] or "")
            tkr  = str(row[ti] or "").upper()
            if not tkr:
                continue
            comp2t[normalize_company_name(name)] = tkr
        if debug:
            print(f"[mapping] loaded {len(comp2t)} name→ticker pairs")
        return comp2t
    except Exception as e:
        if debug:
            print(f"[mapping] error: {e}")
        return {}

COMPANY2TICKER = load_cik_ticker_mapping()

# ============== ElementTree parser (case-insensitive) ==============
def parse_info_table_etree(xml_bytes: bytes, debug=False):
    """
    Parse a 13F informationTable using stdlib ElementTree.
    Case-insensitive local-name matching; namespace-agnostic.
    """
    import xml.etree.ElementTree as ET

    def ln(tag: str) -> str:
        return tag.split('}', 1)[-1] if '}' in tag else tag

    root = ET.fromstring(xml_bytes)  # may raise

    def find_all_local(root_elem, local_name: str):
        local = local_name.lower()
        return [e for e in root_elem.iter() if ln(e.tag).lower() == local]

    info_nodes = find_all_local(root, 'infoTable')
    if debug:
        root_tag = ln(root.tag)
        print(f"[etree] root={root_tag} infoTable_count={len(info_nodes)}")

    out = []
    for e in info_nodes:
        # nameOfIssuer (first occurrence)
        name = None
        for ch in e.iter():
            if ln(ch.tag).lower() == 'nameofissuer':
                name = (ch.text or '').strip()
                if name:
                    break
        if not name:
            continue

        # shares (sshPrnamt either directly or nested inside shrsOrPrnAmt)
        shares = None
        ssh_text = None
        for ch in e.iter():
            if ln(ch.tag).lower() == 'sshprnamt':
                ssh_text = (ch.text or '').strip()
                if ssh_text:
                    break
        if ssh_text:
            try:
                shares = int(re.sub(r'[^\d]', '', ssh_text))
            except Exception:
                shares = None

        key = normalize_company_name(name)
        tkr = COMPANY2TICKER.get(key) or COMPANY2TICKER.get(key + '.')
        out.append({'name': name, 'ticker': (tkr or None), 'shares': shares})

    return out

# --- REPLACE your parse_13f_filing with this version ---
def parse_13f_filing(url: str, debug: bool = False):
    """
    Robust 13F parser:
      - If passed a viewer URL, rewrite to raw XML.
      - Fetch; if XML, parse via ElementTree with local-name matching.
      - If HTML, parse the XSLT-rendered table.
      - If given an index page, first resolve the best document URL.
    Returns: list of {name, ticker, shares}
    """
    # If user gave an index page, resolve to a document URL first
    if re.search(r'-index\.htm$', url, re.I):
        resolved = find_13f_doc_url(url, debug=debug)
        if not resolved:
            if debug: print(f"[parse_13f_filing] no doc found for index {url}")
            return []
        url = resolved

    # Canonicalize viewer paths and .html suffixes
    canon = canonicalize_info_url(url, debug=debug)

    sess = create_session()
    r = sess.get(canon, timeout=25)
    ct = r.headers.get('Content-Type', '')
    if debug:
        print(f"[fetch] url={canon}")
        print(f"[fetch] status={r.status_code} content-type={ct} bytes={len(r.content)}")
        try:
            print("[fetch] first-bytes:", r.content[:160].decode('utf-8', 'ignore').replace('\n', ' ')[:160])
        except Exception:
            pass
    r.raise_for_status()

    body = r.content
    # If it looks like XML, try ElementTree
    looks_xml = ('xml' in ct.lower()) or body.strip().startswith(b'<?xml') or b'<infoTable' in body[:2000]
    if looks_xml:
        try:
            rows = parse_info_table_etree(body, debug=debug)
            if rows:
                if debug: print(f"[parse_13f_filing] XML parsed rows={len(rows)}")
                else: print(f"[parse_13f_filing] {len(rows)} positions parsed from {canon}")
                return rows
        except Exception as e:
            if debug: print(f"[parse_13f_filing] XML parse exception: {e}")

    # If HTML (e.g., viewer served as text/html), use HTML fallback
    if ('html' in ct.lower()) or b'<html' in body[:2000].lower():
        rows = parse_13f_html_table(body, debug=debug)
        if rows:
            if debug: print(f"[parse_13f_filing] HTML parsed rows={len(rows)}")
            else: print(f"[parse_13f_filing] {len(rows)} positions parsed (HTML) from {canon}")
            return rows

    if debug:
        print(f"[parse_13f_filing] 0 positions parsed from {canon}")
    else:
        print(f"[parse_13f_filing] 0 positions parsed from {canon}")
    return []

# ============== Baselines ==============
def build_nvda_baseline_map():
    rows = [
        ("Applied Digital Corp", "APLD", 7716050),
        ("Arm Holdings PLC", "ARM", 1101249),
        ("CoreWeave Inc", "CRWV", 24182460),
        ("Nebius Group N.V.", "NBIS", 1190476),
        ("Recursion Pharmaceuticals Inc", "RXRX", 7706363),
        ("WeRide Inc", "WRD", 1738563),
    ]
    m = {}
    for name, tkr, sh in rows:
        m[normalize_company_name(name)] = {"name": name, "ticker": tkr, "shares": int(sh)}
    return m

def build_berkshire_baseline_set():
    names = [
        "ALLY FINL INC","AMAZON COM INC","AMERICAN EXPRESS CO","APPLE INC",
        "ATLANTA BRAVES HLDGS INC","BANK AMER CORP","CAPITAL ONE FINL CORP",
        "CHARTER COMMUNICATIONS INC N","CHEVRON CORP NEW","COCA COLA CO",
        "CONSTELLATION BRANDS INC","DAVITA INC","DIAGEO P L C","DOMINOS PIZZA INC",
        "HEICO CORP NEW","JEFFERIES FINL GROUP INC","KRAFT HEINZ CO","KROGER CO",
        "LENNAR CORP","LIBERTY MEDIA CORP DEL","LOUISIANA PAC CORP","MASTERCARD INC",
        "MOODYS CORP","NVR INC","OCCIDENTAL PETE CORP","POOL CORP","SIRIUS XM HOLDINGS INC",
        "T-MOBILE US INC","VERISIGN INC","VISA INC","AON PLC","LIBERTY LATIN AMERICA LTD","CHUBB LIMITED",
    ]
    return {normalize_company_name(n) for n in names}

NVDA_BASELINE = build_nvda_baseline_map()
BRK_BASELINE_SET = build_berkshire_baseline_set()
# --- ADD this helper near your other helpers ---
def canonicalize_info_url(url: str, debug: bool = False) -> str:
    """
    If the URL is the XSLT "viewer" path (…/xslForm13F_XX/…),
    rewrite it to the sibling raw XML path. Also convert .../information_table.html -> .xml.
    """
    new_url = url
    # normalize information_table.html -> .xml
    new_url = re.sub(r'(?i)information_table\.html$', 'information_table.xml', new_url)

    # drop the xslForm13F_*/ segment if present
    new_url = re.sub(r'/xslForm13F_[^/]+/', '/', new_url)

    if debug and new_url != url:
        print(f"[canonicalize] {url} -> {new_url}")
    return new_url


# --- ADD this HTML-table fallback parser ---
def parse_13f_html_table(html_bytes: bytes, debug: bool = False):
    """
    Parse the 13F Information Table when served as HTML (XSLT-rendered).
    We detect the header row containing 'PRN AMT' and then read rows that have
    FormData / FormDataR cells.
    Returns: [{'name': str, 'ticker': str|None, 'shares': int|None}, ...]
    """
    soup = BeautifulSoup(html_bytes, 'lxml')
    table = soup.find('table', attrs={'summary': re.compile(r'Form 13F', re.I)})
    if not table:
        # fallback: any table that contains 'NAME OF ISSUER' header
        for t in soup.find_all('table'):
            if t.find(string=re.compile(r'NAME OF ISSUER', re.I)):
                table = t
                break
    if not table:
        if debug:
            print("[html-parse] no information table found")
        return []

    # Find header row that contains PRN AMT so we know column indices
    header_tr = None
    for tr in table.find_all('tr'):
        txt = ' '.join(td.get_text(strip=True) for td in tr.find_all(['td','th']))
        if re.search(r'\bPRN\s+AMT\b', txt, re.I) and re.search(r'NAME OF ISSUER', txt, re.I):
            header_tr = tr
            break
    if not header_tr:
        # sometimes the header is the 3rd row (as in your sample)
        trs = table.find_all('tr')
        header_tr = trs[2] if len(trs) >= 3 else None
    if not header_tr:
        if debug:
            print("[html-parse] could not locate header row")
        return []

    # Build a column index map
    headers = [td.get_text(strip=True).upper() for td in header_tr.find_all(['td','th'])]
    def col_index(label_pat):
        for i, h in enumerate(headers):
            if re.search(label_pat, h, re.I):
                return i
        return None

    name_idx   = col_index(r'^NAME OF ISSUER$')
    shares_idx = col_index(r'^PRN\s+AMT$')

    if name_idx is None or shares_idx is None:
        # fallback to common positions (name first, shares ~6th)
        name_idx, shares_idx = 0, 5

    rows_out = []
    for tr in header_tr.find_all_next('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        # data rows have FormData / FormDataR classes
        first_td_class = ' '.join(tds[0].get('class', []))
        if 'FormData' not in first_td_class:
            continue

        name = tds[name_idx].get_text(strip=True) if name_idx < len(tds) else ''
        shares_txt = tds[shares_idx].get_text(strip=True) if shares_idx < len(tds) else ''
        shares = None
        if shares_txt:
            try:
                shares = int(re.sub(r'[^\d]', '', shares_txt))
            except Exception:
                shares = None

        key = normalize_company_name(name)
        tkr = COMPANY2TICKER.get(key) or COMPANY2TICKER.get(key + '.')
        rows_out.append({'name': name, 'ticker': (tkr or None), 'shares': shares})

    if debug:
        print(f"[html-parse] parsed rows={len(rows_out)}")
    return rows_out
def find_13f_doc_url(index_url: str, debug: bool = False) -> str | None:
    """
    From a filing '-index.htm' page, pick the best 'INFORMATION TABLE' doc:
      1) Prefer raw XML (.xml without /xslForm13F_*/ in the path)
      2) Else viewer XML (.xml under /xslForm13F_*/)
      3) Else fallback .txt
    Works even when the info-table filename is numeric (e.g., 36917.xml).
    """
    s = create_session()
    r = s.get(index_url, timeout=20)
    if r.status_code != 200:
        if debug:
            print(f"[find-doc] {index_url} -> status {r.status_code}")
        return None

    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find("table", class_=re.compile(r'tableFile', re.I))
    if not table:
        if debug:
            print("[find-doc] no tableFile found")
        return None

    rows = table.find_all("tr")
    if not rows:
        if debug:
            print("[find-doc] empty tableFile")
        return None

    # map header -> index
    headers = [th.get_text(strip=True).upper() for th in rows[0].find_all("th")]
    def idx(name):
        for i, h in enumerate(headers):
            if name in h:
                return i
        return None

    desc_i = idx("DESCRIPTION") or 1
    doc_i  = idx("DOCUMENT")    or 2
    type_i = idx("TYPE")        or 3

    best_raw_xml = None
    best_viewer_xml = None
    fallback_txt = None

    for tr in rows[1:]:
        tds = tr.find_all("td")
        if len(tds) <= max(doc_i, type_i):
            continue

        type_txt = tds[type_i].get_text(strip=True).upper()
        # Only consider the "INFORMATION TABLE" rows
        is_info_table = ("INFORMATION TABLE" in type_txt)

        # Document link(s)
        for a in tds[doc_i].find_all("a", href=True):
            href = a["href"]
            if not href.lower().startswith("http"):
                href = "https://www.sec.gov" + href
            low = href.lower()

            if low.endswith(".xml"):
                if is_info_table:
                    if "/xslform13f_" in low:
                        # viewer XML (served as HTML)
                        if best_viewer_xml is None:
                            best_viewer_xml = href
                    else:
                        # raw XML (preferred)
                        best_raw_xml = href
                # ignore other .xml rows (e.g. primary_doc.xml)
            elif low.endswith(".txt") and fallback_txt is None:
                fallback_txt = href

    if debug:
        print(f"[find-doc] RAW={best_raw_xml} VIEWER={best_viewer_xml} TXT={fallback_txt}")

    return best_raw_xml or best_viewer_xml or fallback_txt

def brk_diff_once(url: str, debug: bool = False):
    label = "BRK One-Off"
    print(f"[{label}] Parsing: {url}")
    rows = parse_13f_filing(url, debug=debug)
    if not rows:
        print(f"[{label}] Parsed 0 positions — cannot compare.")
        return

    # Compare against your fixed Berkshire baseline set of company names
    now_set = {normalize_company_name(r["name"]) for r in rows if r.get("name")}
    base_set = set(BRK_BASELINE_SET)

    new_vs_baseline = sorted(n for n in now_set if n not in base_set)
    missing_vs_baseline = sorted(n for n in base_set if n not in now_set)

    print(f"\n[{label}] NEW vs your baseline list:")
    if new_vs_baseline:
        for n in new_vs_baseline:
            print("  " + style_green_bold(n))
        beep()
    else:
        print("  (none)")

    print(f"\n[{label}] MISSING vs your baseline list:")
    if missing_vs_baseline:
        for n in missing_vs_baseline:
            print("  " + style_red_bold(n))
    else:
        print("  (none)")

# ============== NVDA one-off diff ==============
def nvda_diff_once(url: str, debug=False):
    label = "NVDA One-Off Test"
    print(f"[{label}] Parsing: {url}")
    new_list = parse_13f_filing(url, debug=debug)
    if not new_list:
        print(f"[{label}] Parsed 0 positions — cannot diff. (Fetch/parse issue.)")
        return
    new_list = apply_nvda_overrides(new_list)

    # Ticker-first diff
    old_by_ticker = {v['ticker']: v for v in NVDA_BASELINE.values() if v.get('ticker')}
    new_by_ticker = {r.get('ticker'): r for r in new_list if r.get('ticker')}

    removed = [old_by_ticker[t] for t in old_by_ticker if t not in new_by_ticker]
    added   = [new_by_ticker[t] for t in new_by_ticker if t not in old_by_ticker]

    if not new_by_ticker:
        new_by_name = {normalize_company_name(r['name']): r for r in new_list}
        removed = [NVDA_BASELINE[k] for k in NVDA_BASELINE if k not in new_by_name]
        added   = [new_by_name[k] for k in new_by_name if k not in NVDA_BASELINE]

    print(f"\n[{label}] REMOVED:")
    if removed:
        for r in removed:
            sh = r.get('shares')
            sh_txt = f"{sh:,}" if isinstance(sh, int) else "-"
            print("  " + style_red_bold(f"{r.get('ticker') or 'None'}  {r['name']}  (shares: {sh_txt})"))
    else:
        print("  (none)")

    print(f"\n[{label}] ADDED:")
    if added:
        for a in added:
            sh = a.get('shares')
            sh_txt = f"{sh:,}" if isinstance(sh, int) else "-"
            print("  " + style_green_bold(f"{a.get('ticker') or 'None'}  {a['name']}  (shares: {sh_txt})"))
        beep()
    else:
        print("  (none)")

# ============== Continuous monitors ==============
def monitor_nvda(cik="1045810", label="Nvidia", debug=False):
    session = create_session()
    feed = (f"https://www.sec.gov/cgi-bin/browse-edgar?"
            f"action=getcompany&CIK={cik}&type=13F&owner=include&count=40&output=atom")
    last_processed = datetime.now(timezone.utc)
    seen_entry_links = set()
    baseline_by_name = dict(NVDA_BASELINE)

    print(f"[{label}] Monitoring 13F at {feed}")
    while True:
        try:
            r = session.get(feed, timeout=15)
            if r.status_code != 200:
                time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))
                continue

            doc = BeautifulSoup(r.content, "xml")
            for entry in doc.find_all("entry"):
                cat = entry.find("category")
                term = (cat["term"] if cat and cat.has_attr("term") else "").upper()
                if not term.startswith("13F"):
                    continue

                updated_txt = entry.updated.get_text(strip=True) if entry.updated else None
                if not updated_txt:
                    continue
                try:
                    updated = datetime.fromisoformat(updated_txt)
                except Exception:
                    updated = datetime.strptime(updated_txt, "%Y-%m-%dT%H:%M:%S%z")

                if updated <= last_processed:
                    continue

                link_tag = entry.find("link")
                if not link_tag or not link_tag.has_attr("href"):
                    continue
                filing_page = link_tag["href"]
                if filing_page in seen_entry_links:
                    continue

                doc_url = find_13f_doc_url(filing_page)
                if not doc_url:
                    last_processed = max(last_processed, updated)
                    continue

                print(f"\n[{label}] NEW {term} → {doc_url}")
                new_list = parse_13f_filing(doc_url, debug=debug)
                if not new_list:
                    print(f"[{label}] Parsed 0 positions — skipping.")
                    last_processed = max(last_processed, updated)
                    seen_entry_links.add(filing_page)
                    continue

                new_list = apply_nvda_overrides(new_list)

                old_by_ticker = {v.get('ticker'): v for v in baseline_by_name.values() if v.get('ticker')}
                new_by_ticker = {r.get('ticker'): r for r in new_list if r.get('ticker')}

                if new_by_ticker:
                    removed = [old_by_ticker[t] for t in old_by_ticker if t not in new_by_ticker]
                    added   = [new_by_ticker[t] for t in new_by_ticker if t not in old_by_ticker]
                else:
                    new_by_name = {normalize_company_name(r['name']): r for r in new_list}
                    removed = [baseline_by_name[k] for k in baseline_by_name if k not in new_by_name]
                    added   = [new_by_name[k] for k in new_by_name if k not in baseline_by_name]

                print(f"\n[{label}] REMOVED:")
                if removed:
                    for r in removed:
                        sh = r.get('shares')
                        sh_txt = f"{sh:,}" if isinstance(sh, int) else "-"
                        print("  " + style_red_bold(f"{r.get('ticker') or 'None'}  {r['name']}  (shares: {sh_txt})"))
                else:
                    print("  (none)")

                print(f"\n[{label}] ADDED:")
                if added:
                    for a in added:
                        sh = a.get('shares')
                        sh_txt = f"{sh:,}" if isinstance(sh, int) else "-"
                        print("  " + style_green_bold(f"{a.get('ticker') or 'None'}  {a['name']}  (shares: {sh_txt})"))
                else:
                    print("  (none)")

                beep()
                try:
                    webbrowser.open_new_tab(doc_url)
                except Exception:
                    pass

                baseline_by_name = {normalize_company_name(r['name']): r for r in new_list}
                seen_entry_links.add(filing_page)
                last_processed = max(last_processed, updated)
                break

            time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))

        except Exception as e:
            print(f"[{label}] Error: {e}")
            traceback.print_exc()
            time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))

def monitor_berkshire(cik="1067983", label="Berkshire", debug=False):
    session = create_session()
    feed = (f"https://www.sec.gov/cgi-bin/browse-edgar?"
            f"action=getcompany&CIK={cik}&type=13F&owner=include&count=40&output=atom")
    last_processed = datetime.now(timezone.utc)
    seen_entry_links = set()
    baseline_set = set(BRK_BASELINE_SET)

    print(f"[{label}] Monitoring 13F at {feed}")
    while True:
        try:
            r = session.get(feed, timeout=15)
            if r.status_code != 200:
                time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))
                continue

            doc = BeautifulSoup(r.content, "xml")
            for entry in doc.find_all("entry"):
                term = entry.find("category")["term"].upper()
                if not term.startswith("13F"):
                    continue

                updated = datetime.fromisoformat(entry.updated.text)
                if updated <= last_processed:
                    continue

                link = entry.find("link")["href"]
                if link in seen_entry_links:
                    continue

                doc_url = find_13f_doc_url(link)
                if not doc_url:
                    last_processed = max(last_processed, updated)
                    continue

                print(f"\n[{label}] NEW {term} → {doc_url}")
                holdings = parse_13f_filing(doc_url, debug=debug)
                names_now = {normalize_company_name(h["name"]) for h in holdings}

                new_companies = [h for h in holdings
                                 if normalize_company_name(h["name"]) not in baseline_set]

                if new_companies:
                    print(f"\n[{label}] NEW companies vs your baseline list:")
                    for h in new_companies:
                        print("  " + style_green_bold(h['name']))
                    beep()
                    try:
                        webbrowser.open_new_tab(doc_url)
                    except Exception:
                        pass
                else:
                    print(f"\n[{label}] No new companies vs your baseline list.")

                baseline_set = names_now
                seen_entry_links.add(link)
                last_processed = max(last_processed, updated)
                break

            time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))

        except Exception as e:
            print(f"[{label}] Error: {e}")
            traceback.print_exc()
            time.sleep(random.uniform(POLL_MIN_SEC, POLL_MAX_SEC))

# ============== CLI ==============
def main():
    global POLL_MIN_SEC, POLL_MAX_SEC

    ap = argparse.ArgumentParser()
    ap.add_argument("--nvda-diff", help="Run one-off NVDA diff against an info-table URL and exit.")
    ap.add_argument("--debug", action="store_true", help="Verbose fetch/parse debug.")
    # remove the '--monitor' flag; default is to start monitors
    ap.add_argument("--nvda-only", action="store_true", help="Only start the Nvidia monitor.")
    ap.add_argument("--brk-only",  action="store_true", help="Only start the Berkshire monitor.")
    ap.add_argument("--poll-min", type=float, default=None, help="Min poll sleep seconds.")
    ap.add_argument("--poll-max", type=float, default=None, help="Max poll sleep seconds.")
    args = ap.parse_args()

    # apply optional poll overrides
    if args.poll_min is not None:
        POLL_MIN_SEC = args.poll_min
    if args.poll_max is not None:
        POLL_MAX_SEC = args.poll_max

    # one-off mode
    if args.nvda_diff:
        nvda_diff_once(args.nvda_diff, debug=args.debug)
        return

    # start both monitors by default; -only flags narrow it
    start_nvda = True
    start_brk  = True
    if args.nvda_only and not args.brk_only:
        start_brk = False
    elif args.brk_only and not args.nvda_only:
        start_nvda = False

    if start_nvda:
        threading.Thread(target=monitor_nvda, kwargs={"debug": args.debug}, daemon=True).start()
    if start_brk:
        threading.Thread(target=monitor_berkshire, kwargs={"debug": args.debug}, daemon=True).start()

    # keep the process alive
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[main] Stopping monitors...")



if __name__ == "__main__":
    main()


