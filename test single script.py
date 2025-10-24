import requests
from bs4 import BeautifulSoup
import threading
import webbrowser
import winsound
from datetime import datetime
import random
import re, time, random, traceback, webbrowser
from urllib.parse import urljoin
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from curl_cffi import requests as curlreq
from curl_cffi.requests.exceptions import Timeout as CurlTimeout, RequestException
from colorama import Fore, Back, Style
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
ua = random.choice(USER_AGENTS_DATA)['ua']
headers = {'User-Agent': ua}
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

# --- Add near your globals ---
# pip install curl-cffi bs4 lxml
from curl_cffi import requests as curlreq
from curl_cffi.requests.exceptions import Timeout as CurlTimeout, RequestException
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time, random, traceback


# ===================== StreetInsider (Axios-style) =====================

from curl_cffi import requests as curlreq
from curl_cffi.requests.exceptions import Timeout as CurlTimeout, RequestException
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time, random, traceback
from urllib.parse import urljoin, urlparse

muddywaters_seen = set()

def _build_mw_session(http2=True, impersonate="chrome124"):
    """
    Version-tolerant curl_cffi Session:
    tries http2=, then h2=, then neither (older/newer releases differ).
    """
    kwargs = dict(impersonate=impersonate)
    s = None
    can_toggle_h2 = False
    for attempt in ({"http2": http2}, {"h2": http2}, {}):
        try:
            s = curlreq.Session(**kwargs, **attempt)
            can_toggle_h2 = bool(attempt)
            break
        except TypeError:
            continue
    if s is None:
        s = curlreq.Session(**kwargs)

    s._can_toggle_h2 = can_toggle_h2
    s.headers.update({
        "authority": "muddywatersresearch.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "upgrade-insecure-requests": "1",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://muddywatersresearch.com/",
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"),
        # "connection": "close",  # uncomment if you ever see long-lived stalls
    })
    try:
        s.get("https://muddywatersresearch.com/", timeout=6)
    except Exception:
        pass
    return s

def _extract_ticker_from_title(title: str) -> str | None:
    """
    Pull the FIRST parentheses block; then return the token BEFORE any space or period.
    Examples:
      "(APP US)" -> APP
      "(FTAI US)" -> FTAI
      "(ERF.FP)" -> ERF
      "(CPIPGR)" -> CPIPGR
    """
    m = re.search(r"\(([^)]+)\)", title)
    if not m:
        return None
    inner = m.group(1).strip()
    # split by space or dot; take first chunk
    token = re.split(r"[ .]", inner, maxsplit=1)[0]
    token = re.sub(r"[^A-Za-z0-9]+$", "", token)  # drop any trailing punctuation, just in case
    return token.upper() if token else None

def muddywaters_research(sound_name="muddy waters", poll_range=(6.0, 9.0)):
    """
    Fast poller for https://muddywatersresearch.com/research/
    - Parses the research table rows
    - Dedupe on title
    - Plays sound 'muddy waters' or beeps if unavailable
    """
    base_url = "https://muddywatersresearch.com"
    url = f"{base_url}/research/"

    session = _build_mw_session(http2=True)
    use_http2 = True
    last_recycle = datetime.utcnow()
    req_count = 0
    consec_fail = 0

    while True:
        try:
            # recycle periodically to avoid stale sockets
            if req_count >= 400 or (datetime.utcnow() - last_recycle) > timedelta(minutes=20):
                session.close()
                session = _build_mw_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0

            # single fast request; retry once on timeout
            try:
                resp = session.get(url, timeout=8)
            except CurlTimeout:
                try:
                    resp = session.get(url, timeout=8)
                except CurlTimeout as e:
                    raise

            if resp.status_code in (401, 402, 403, 429, 503):
                print(f"[MuddyWaters] {resp.status_code} from edge. Cooling down briefly.")
                consec_fail += 1
                time.sleep(random.uniform(12, 18))
                continue

            resp.raise_for_status()
            req_count += 1
            consec_fail = 0

            soup = BeautifulSoup(resp.content, "lxml")
            rows = soup.select("#research-table tbody tr")
            if not rows:
                print("[MuddyWaters] No rows found; short sleep.")
                time.sleep(random.uniform(8, 12))
            else:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for tr in rows:
                    a = tr.select_one("td.first a")
                    if not a:
                        continue
                    title = a.get_text(strip=True)
                    href = a.get("href") or ""
                    link = href if href.startswith("http") else urljoin(base_url, href)

                    if not title or title in muddywaters_seen:
                        continue
                    muddywaters_seen.add(title)

                    # ticker logic
                    ticker = _extract_ticker_from_title(title)
                    if ticker:
                        formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
                        print(formatted); print(formatted); print(formatted)
                    else:
                        print(f"MuddyWaters: Could not extract ticker from headline '{title}'.")

                    print(f"{now}\tMuddyWaters\t{title}")
                    print("Article URL:", link)

                    # auto-open & sound
                    try:
                        webbrowser.open_new_tab(link)
                    except Exception:
                        pass

                    try:
                        SOUNDS.play(sound_name, stop_current=True)
                    except Exception:
                        try:
                            import winsound
                            winsound.Beep(1500, 100)
                        except Exception:
                            pass

            time.sleep(random.uniform(*poll_range))

        except CurlTimeout as e:
            print("[MuddyWaters] Timeout; recycling session:", e)
            consec_fail += 1
            session.close()
            if consec_fail >= 3 and getattr(session, "_can_toggle_h2", False):
                use_http2 = not use_http2  # flip h2 <-> h1.1 if timeouts persist
            session = _build_mw_session(http2=use_http2)
            last_recycle = datetime.utcnow()
            req_count = 0
            time.sleep(random.uniform(4, 7))

        except RequestException as e:
            print("[MuddyWaters] RequestException; soft backoff:", e)
            consec_fail += 1
            if consec_fail >= 2:
                session.close()
                session = _build_mw_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))

        except Exception as e:
            print("[MuddyWaters] Error:", e)
            traceback.print_exc()
            consec_fail += 1
            if consec_fail >= 2:
                session.close()
                session = _build_mw_session(http2=use_http2)
                last_recycle = datetime.utcnow()
                req_count = 0
            time.sleep(random.uniform(6, 10))
# ======================================================================

# Example runner (adjust as needed):
if __name__ == "__main__":
    import threading
    t = threading.Thread(target=muddywaters_research,
                         kwargs={"sound_name": "muddy waters", "poll_range": (6.0, 9.0)},
                         daemon=False)
    t.start()
    t.join()

##KEEP THIS
##
##

