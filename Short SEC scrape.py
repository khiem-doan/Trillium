def blue_orca():
    """
    Blue Orca function:
      - Uses a live RSS-style (listing) page for Blue Orca reports.
      - Finds the row for "Blue Orca is Short Teladoc Health, Inc."
      - Extracts the article URL (from the first <a> tag)
      - Extracts the ticker from the third <td> (e.g. "NYSE: TDOC" → "TDOC")
      - Outputs the ticker three times (highlighted), timestamp, reporter name, headline, and article URL.
      - Opens the article URL in a new browser tab and plays a beep.
    """
    # Use our pre-defined session creation function
    session = create_session()

    # IMPORTANT: Use the Blue Orca reports listing page.
    # (Make sure this URL is the one that contains the table rows.)
    url = "https://www.blueorcacapital.com/category/reports/"

    try:
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Blue Orca: Error fetching the listing page: {e}")
        return

    # Parse the page
    soup = BeautifulSoup(resp.content, 'html.parser')

    # Instead of looking for a <tbody>, we look for all <tr> elements
    rows = soup.find_all('tr')
    if not rows:
        print("Blue Orca: Could not find any <tr> in the page.")
        return

    # Look for the row that contains our target text
    target_row = None
    for row in rows:
        if "Blue Orca is Short Teladoc Health" in row.get_text():
            target_row = row
            break

    if not target_row:
        print("Blue Orca: Could not find the target row for Teladoc Health.")
        return

    # Get the article URL from the first <a> tag in the target row
    a_tag = target_row.find('a', href=True)
    if not a_tag:
        print("Blue Orca: Could not find an <a> tag with href in the target row.")
        return
    article_url = a_tag['href'].strip()

    # The ticker is in the third <td> cell (e.g. "NYSE: TDOC")
    tds = target_row.find_all('td')
    if len(tds) < 3:
        print("Blue Orca: Not enough <td> cells in the target row.")
        return
    ticker_text = tds[2].get_text().strip()  # Expected to be like "NYSE: TDOC"
    parts = ticker_text.split(":")
    if len(parts) < 2:
        print("Blue Orca: Could not parse ticker from the text.")
        return
    ticker = parts[1].strip()

    # Get the headline text from the <a> tag (and remove any "NEW:" prefix)
    headline = a_tag.get_text().replace("NEW:", "").strip()

    # Format the ticker output (triple print, highlighted yellow on black text)
    from datetime import datetime
    now = datetime.now().time()
    ticker_formatted = f"{Style.BRIGHT}{Back.YELLOW}{Fore.BLACK}{ticker}{Style.RESET_ALL}"
    print(ticker_formatted)
    print(ticker_formatted)
    print(ticker_formatted)
    print(f"{now}\t Blue Orca \t {headline}")
    print("Article URL:", article_url)

    # Open the article in a new browser tab and beep
    import webbrowser, winsound
    webbrowser.open_new_tab(article_url)
    winsound.Beep(2500, 200)
