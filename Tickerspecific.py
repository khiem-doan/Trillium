def test_tiktok_feed():
    import requests
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime, timezone
    import string

    feed_url = "https://www.courtlistener.com/docket/68506893/feed/"
    headers = {
        'User-Agent': 'Your Name; your.email@example.com',  # Replace with your actual name and email
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    resp = requests.get(feed_url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'xml')
        entry = soup.find('entry')
        if entry:
            title = entry.find('title').get_text(strip=True)
            link_tag = entry.find('link', {'rel': 'alternate'})
            entry_url = link_tag['href'] if link_tag else None
            summary_tag = entry.find('summary')
            summary_text = summary_tag.get_text(" ", strip=True) if summary_tag else ""
            summary_text = ''.join(filter(lambda x: x in string.printable, summary_text))

            print("=== NEW COURT ENTRY ===")
            print("Title:", title)
            print("URL:", entry_url)
            print("Summary:", summary_text)

            # If you want to open it in the browser as you do for other scrapers:
            import webbrowser
            webbrowser.open_new_tab(entry_url)

        else:
            print("No entry found in the feed.")
    else:
        print("Failed to fetch feed:", resp.status_code, resp.reason)

# Call the test function to print the first entry
test_tiktok_feed()
