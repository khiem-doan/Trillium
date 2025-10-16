import requests
import random
import time
import winsound
import keyboard  # pip install keyboard
from datetime import datetime
from zoneinfo import ZoneInfo

# --- Function to load tickers only from Nasdaq or NYSE ---
def load_nyse_nasdaq_tickers():
    url = "https://www.sec.gov/files/company_tickers_exchange.json"
    headers = {"User-Agent": "Your Name; your.email@example.com"}  # Replace with your details
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print("Error fetching ticker data.")
        return []
    data = resp.json()
    fields = data.get("fields", [])
    if not fields:
        print("Ticker fields not found.")
        return []
    try:
        ticker_index = fields.index("ticker")
        exchange_index = fields.index("exchange")
    except ValueError:
        print("Expected fields not found in the JSON data.")
        return []
    valid_tickers = []
    for entry in data.get("data", []):
        # Get the exchange (if available) and check if it's Nasdaq or NYSE
        if not entry[exchange_index]:
            continue
        exchange = entry[exchange_index].strip()
        if exchange not in ["Nasdaq", "NYSE"]:
            continue
        ticker = entry[ticker_index].strip().upper()
        # Skip tickers ending with "W", "WS", or "WT"
        if ticker.endswith("W") or ticker.endswith("WS") or ticker.endswith("WT"):
            continue
        valid_tickers.append(ticker)
    return valid_tickers

# --- Global: load the valid tickers ---
ticker_list = load_nyse_nasdaq_tickers()
print(f"Loaded {len(ticker_list)} tickers from Nasdaq/NYSE.")

# --- Define some sample reporter names, title templates, and description templates ---
short_reporters = ["Hunterbrook", "Culper", "Scorpion", "Capybara", "FuzzyPanda", "J Capital", "Spruce", "Betaville", "Iceberg"]
title_templates = [
    "BREAKING: As {ticker} Hit by Tariffs, Companies Enabling Chinese Surveillance Remain Nasdaq Listed",
    "ALERT: {ticker} sees an unexpected surge in volume",
    "REPORT: {ticker} faces regulatory scrutiny amid market volatility",
    "UPDATE: Analysts revise outlook for {ticker}",
    "NEWS: {ticker} posts record earnings in Q4"
]
description_templates = [
    "<p>Based on recent analysis, {ticker} is under close scrutiny by analysts. Further details are awaited.</p>",
    "<p>Market watchers report that {ticker} is experiencing unusual trading activity.</p>",
    "<p>Investors are advised to monitor {ticker} as it shows signs of a potential turnaround.</p>"
]

def reaction_test_report():
    while True:
        # --- Pick a random ticker from the filtered ticker_list ---
        if not ticker_list:
            print("No valid tickers available.")
            break
        chosen_ticker = random.choice(ticker_list)
        reporter = random.choice(short_reporters)
        title_text = random.choice(title_templates).format(ticker=chosen_ticker)
        description_text = random.choice(description_templates).format(ticker=chosen_ticker)
        # Build a dummy article URL (for example purposes)
        article_url = f"https://example.com/report/{chosen_ticker.lower()}"

        # --- Get current EST timestamp ---
        output_dt = datetime.now(ZoneInfo("America/New_York"))
        output_time_str = output_dt.strftime("%H:%M:%S.%f")

        # --- Output in the desired format ---
        # Print the ticker three times (each on its own line)
        print(chosen_ticker)
        print(chosen_ticker)
        print(chosen_ticker)
        # Print the report line (timestamp, reporter, and title)
        print(f"{output_time_str}\t{reporter}\t{title_text}")
        # Print the description and article URL lines
        print(f"Description: {description_text}")
        print(f"Article URL: {article_url}")
        # Play the beep sound (just like your original code)
        winsound.Beep(2500, 200)

        # --- Record the output timestamp ---
        t0 = time.time()

        # --- Reaction Test: wait for the user to type in the ticker and press Enter ---
        user_entry = input("Type the ticker and press Enter: ")
        t1 = time.time()

        # --- Reaction Test: wait for the user to press Shift+J twice ---
        print("Now press Shift+J twice (hold Shift and press J each time)...")
        shift_j_count = 0
        while shift_j_count < 2:
            event = keyboard.read_event()  # This blocks until an event occurs.
            if event.event_type == "down" and event.name.lower() == "j" and keyboard.is_pressed("shift"):
                shift_j_count += 1
                print(f"Shift+J pressed {shift_j_count} time(s)")
        t2 = time.time()

        # --- Calculate and output reaction times ---
        reaction_input = t1 - t0
        reaction_shift_j = t2 - t1
        total_reaction = t2 - t0
        print(f"Time from ticker output to user input: {reaction_input:.3f} seconds")
        print(f"Time from user input to Shift+J: {reaction_shift_j:.3f} seconds")
        print(f"Total reaction time: {total_reaction:.3f} seconds")
        print("-" * 80)

        # --- Wait for a random interval (10-60 seconds) before the next report ---
        sleep_interval = random.uniform(10, 60)
        time.sleep(sleep_interval)

if __name__ == "__main__":
    reaction_test_report()
