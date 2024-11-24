import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from zoneinfo import ZoneInfo  # Ensure you're using Python 3.9+
import re
import time
import webbrowser
sec8k_headline = [0]*2

def load_cik_ticker_mapping():
    # Placeholder function to load CIK-to-Ticker mapping.
    # In a real implementation, you would load the mapping from a file or API.
    # For this example, we'll define a simple mapping.
    return {
        '1045810': 'NVDA',  # CIK for NVIDIA Corporation
        # Add more mappings as needed
    }

def sec8k():
    headers = {
        'Host': 'www.sec.gov',
        'User-Agent': 'Your Name; your.email@example.com',  # Replace with your actual name and email
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
    }

    # List of ticker symbols to filter
    ticker_filters = ["NVDA"]  # Add the tickers you want to monitor

    opened_links = set()
    script_start_time = datetime.now(timezone.utc)
    first_run = True  # Flag variable

    # Load CIK-to-Ticker mapping
    cik_ticker_mapping = load_cik_ticker_mapping()

    while True:
        try:
            # Fetch recent filings
            url = ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&company=&type=&"
                   "owner=include&start=0&count=100&output=atom")
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"SEC Filings: Error fetching RSS feed: {resp.status_code} {resp.reason}")
                time.sleep(3)
                continue
            feed_content = resp.content
            soup = BeautifulSoup(feed_content, 'xml')  # Use 'xml' parser
            entries = soup.find_all('entry')
            if not entries:
                print("SEC Filings: No entries found in the feed.")
                time.sleep(3)
                continue
            else:
                if first_run:
                    print(f"SEC Filings: Found {len(entries)} entries.")
                    first_run = False  # Set the flag to False after the first run

            for top_entry in entries:
                # Fetch the top link from the entry
                link_tag = top_entry.find('link')
                if link_tag and link_tag.get('href'):
                    top_link = link_tag['href']
                else:
                    continue

                # Get the updated time of the entry (SEC publish timestamp)
                updated_datetime_str = top_entry.updated.get_text()
                updated_datetime = datetime.strptime(updated_datetime_str, '%Y-%m-%dT%H:%M:%S%z')

                # Skip filings older than the script start time
                if updated_datetime <= script_start_time:
                    continue

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

                # Get ticker symbol from the preloaded mapping
                if cik_number and cik_number in cik_ticker_mapping:
                    ticker = cik_ticker_mapping[cik_number]
                else:
                    ticker = 'N/A'

                # Filter by ticker symbol
                if ticker not in ticker_filters:
                    continue  # Skip if the ticker is not in the filter list

                # Only process if this is a new link
                if top_link not in opened_links:
                    # Record the print timestamp (current time)
                    print_timestamp = datetime.now(timezone.utc)

                    # Calculate time difference in seconds
                    time_diff_seconds = (print_timestamp - updated_datetime).total_seconds()

                    # Convert times to EST
                    updated_datetime_est = updated_datetime.astimezone(ZoneInfo('America/New_York'))
                    print_timestamp_est = print_timestamp.astimezone(ZoneInfo('America/New_York'))

                    # Fetching page content
                    page_resp = requests.get(top_link, headers=headers)
                    if page_resp.status_code != 200:
                        continue
                    page_soup = BeautifulSoup(page_resp.content, 'lxml')  # Use 'lxml' parser

                    # Find the document table
                    table = page_soup.find('table', class_='tableFile')
                    if not table:
                        continue
                    # Find the row with the desired document
                    rows = table.find_all('tr')
                    doc_url = None
                    for row in rows[1:]:
                        cols = row.find_all('td')
                        if len(cols) >= 4:
                            doc_link = cols[2].find('a', href=True)['href']
                            doc_url = 'https://www.sec.gov' + doc_link
                            break  # Exit after finding the document

                    if not doc_url:
                        continue  # Skip if we couldn't find the document URL

                    # Format the output
                    output = (f"{form_type_extracted} - {ticker} - {company_name} - "
                              f"SEC Time: {updated_datetime_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Print Time: {print_timestamp_est.strftime('%Y-%m-%d %H:%M:%S %Z')} - "
                              f"Delay: {int(time_diff_seconds)}s - {doc_url}")

                    print(output)

                    # Open the document in the browser
                    webbrowser.open_new_tab(doc_url)
                    # Optionally, you can play a sound or perform other actions here

                    opened_links.add(top_link)

            time.sleep(3)
        except Exception as e:
            import traceback
            print(f"Error in sec8k(): {e}")
            traceback.print_exc()
            time.sleep(3)

if __name__ == "__main__":
    sec8k()

sec8k_thread = threading.Thread(target=sec8k)
sec8k_thread.start()