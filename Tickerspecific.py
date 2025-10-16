import requests
import re
import time
import webbrowser


import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup


colorama.init(autoreset=True)


###############################################################################
# (1) Load the SEC dictionaries
###############################################################################
def load_cik_ticker_mapping():
   import requests
   cik_ticker = {}
   company_name_to_ticker = {}


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
           cik_idx      = fields.index('cik')
           ticker_idx   = fields.index('ticker')
           name_idx     = fields.index('name')
           exchange_idx = fields.index('exchange')  # Get the index of the 'exchange' field


           for entry in data['data']:
               exchange_field = entry[exchange_idx]
               if exchange_field:
                   exchange = exchange_field.strip()
               else:
                   continue


               # Skip if not Nasdaq/NYSE
               if exchange not in ['Nasdaq', 'NYSE']:
                   continue


               # Extract fields
               cik_field    = entry[cik_idx]
               ticker_field = str(entry[ticker_idx]).strip().upper()
               name_field   = str(entry[name_idx]).strip().upper()


               # Skip if missing
               if not cik_field or not ticker_field or not name_field:
                   continue


               # === NEW LOGIC: Check if ticker looks like a warrant (e.g. ends w/ "W", "WS", "WT") ===
               # Expand this list if you also want to skip "W-", ".WS", etc.
               # For example, ticker.endswith("W") or ticker.endswith("WS") or ...
               if (
                   ticker_field.endswith("W")  or
                   ticker_field.endswith("WS") or
                   ticker_field.endswith("WT")
               ):
                   # This is likely a warrant ticker — skip it so the base ticker remains
                   continue
               # === END NEW LOGIC ===


               # Clean up the CIK
               cik_clean = str(cik_field).lstrip('0')


               # Add to the dictionaries
               cik_ticker[cik_clean] = ticker_field
               company_name_to_ticker[name_field] = ticker_field


       else:
           print(f"Failed to download CIK-Ticker mapping. Status code: {resp.status_code}")


   except Exception as e:
       print(f"Error loading CIK-Ticker mapping: {e}")


   # Optionally, return both dictionaries if you also want name => ticker
   return cik_ticker, company_name_to_ticker




###############################################################################
# (2) The Hindenburg test function
###############################################################################
def hindenburg_test(test_urls, company_name_to_ticker):
   """
   Steps:
     (A) brand_slug_upper in all_tickers => short-circuit
     (B) expansions approach
     (C) partial substring fallback
   """


   # Build a set of all known tickers from the second dictionary:
   #   company_name_to_ticker is { "EHANG HOLDINGS LTD": "EH", ... }
   #   -> but we only want the set of tickers
   all_tickers = set(company_name_to_ticker.values())


   expansions = [
       " INC.", " INC", " INCORPORATED",
       " CORP.", " CORP", " CORPORATION",
       " LTD.", " LTD", " PLC", " SA",
       "",
   ]


   for url in test_urls:
       try:
           # fetch page (simulating real code)
           resp = requests.get(url, headers={"User-Agent": "Mozilla/4.0"}, timeout=10)
           soup = BeautifulSoup(resp.content, 'lxml')


           # brand slug from last path segment
           brand_url = url.rstrip('/')
           brand_slug = brand_url.split('/')[-1]  # e.g. "ehang" or "aile"
           brand_slug_upper = brand_slug.upper()


           ticker_matched = None


           # (A) If brand_slug_upper is an EXACT known ticker -> short-circuit
           if brand_slug_upper in all_tickers:
               ticker_matched = brand_slug_upper


           # (B) expansions approach if none found
           if not ticker_matched:
               for exp in expansions:
                   candidate_name = (brand_slug_upper + exp).strip()
                   # e.g. "EQUINIX INC.", "SEZZLE INC.", "EHANG LTD"
                   if candidate_name in company_name_to_ticker:
                       ticker_matched = company_name_to_ticker[candidate_name]
                       break


           # (C) partial substring fallback
           # If still nothing found, see if brand_slug_upper is inside some official name
           # e.g. "EHANG" in "EHANG HOLDINGS LTD" => ticker="EH"
           # e.g. "LIFESTANCE" in "LIFESTANCE HEALTH GROUP, INC." => ticker="LFST"
           # e.g. "AILE" in "ILEARNINGENGINES, INC." => ticker="AILE"
           if not ticker_matched:
               for comp_name, comp_ticker in company_name_to_ticker.items():
                   if brand_slug_upper in comp_name:
                       print(f"DEBUG: brand_slug_upper={brand_slug_upper} found inside => {comp_name}")
                       ticker_matched = comp_ticker
                       break


           # Print the matched ticker if any
           if ticker_matched:
               color_code = Fore.BLACK + Back.YELLOW
               line = f"{Style.BRIGHT}{color_code}{ticker_matched}{Style.RESET_ALL}"
               print(line)
               print(line)
               print(line)
           if not ticker_matched:
               for comp_name, comp_ticker in company_name_to_ticker.items():
                   if brand_slug_upper in comp_name:
                       print(f"DEBUG: brand_slug_upper={brand_slug_upper} found inside => {comp_name}")
                       ticker_matched = comp_ticker
                       break


           # Then print normal lines, simulating your real code
           now = time.time()
           headline = brand_slug_upper
           print(f"{now}\tHindenburg\t{headline}")
           print("Article URL:", url)


       except Exception as e:
           print(f"Error in hindenburg_test() for URL {url}: {e}")
           continue


###############################################################################
# (3) Main
###############################################################################
if __name__=="__main__":
   print("Loading SEC mapping. This may take a moment...\n")
   cik_ticker_mapping, company_name_to_ticker = load_cik_ticker_mapping()


   # Your custom test URLs
   test_urls = [
       "https://hindenburgresearch.com/equinix/",
       "https://hindenburgresearch.com/sezzle/",
       "https://hindenburgresearch.com/aile",
       "https://hindenburgresearch.com/lifestance/",
       "https://hindenburgresearch.com/ehang/",
       "https://hindenburgresearch.com/roblox/",
       "https://hindenburgresearch.com/lpp/",
       "https://hindenburgresearch.com/temenos/",
       "https://hindenburgresearch.com/renovaro/"
   ]


   print("\nTesting Hindenburg logic with brand_slug = EXACT TICKER, expansions, then partial substring...\n")
   hindenburg_test(test_urls, company_name_to_ticker)


   print("\nDone testing.\n")