import requests
import random
import time
import winsound
import keyboard  # pip install keyboard
from datetime import datetime
from zoneinfo import ZoneInfo

# --- Your existing function to load NYSE/Nasdaq tickers ---
def load_nyse_nasdaq_tickers():
    url = "https://www.sec.gov/files/company_tickers_exchange.json"
    headers = {"User-Agent": "Your Name; your.email@example.com"}  # <-- put your details
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
        if not entry[exchange_index]:
            continue
        exchange = entry[exchange_index].strip()
        if exchange not in ["Nasdaq", "NYSE"]:
            continue
        ticker = entry[ticker_index].strip().upper()
        if ticker.endswith("W") or ticker.endswith("WS") or ticker.endswith("WT"):
            continue
        valid_tickers.append(ticker)
    return valid_tickers

# --- Load "big" ticker list once ---
BIG_TICKERS = load_nyse_nasdaq_tickers()
print(f"[Crypto Practice] Loaded {len(BIG_TICKERS)} NYSE/Nasdaq tickers.")

# --- Provided crypto-sensitive list (deduped, uppercased) ---
_CRYPTO_RAW = """
HSDT
POAI
MSS
APDN
DJT
HSDT
BMNR
SRM
SBET
FGNX
BREA
BTCM
DFDV
FORD
FTEL
JG
KIDZ
MFH
SOLZ
UPXI
AGRI
ALTS
AMOD
ASNS
BKKT
BTCM
BTCT
CJET
CLIK
EQ
ETOR
FLGC
GAME
HOLO
IVDA
JFBR
JZXN
JG
LAES
LGHL
MBAV
MFH
MRT
NIPG
NVVE
NXTT
PRPH
PSQH
QLGN
QMMM
RELI
SCLX
SDM
SGN
SILO
STSS
TZUP
VVPR
WBUY
WFF
YYAI
KWM
NIVF
WFF
ADTX
AEHL
AGAE
ASST
SMLR
ATHR
ATXG
CDT
CLSK
DEFT
DOMH
DTCK
ECDA
FLD
GNS
IPW
LMFA
LVO
MOGO
MRT
MSW
NAKA
PFSA
PRE
QNTM
RBNE
RZLV
SQNS
SRXH
SUUN
ZOOZ
""".strip().splitlines()

CRYPTO_TICKERS = sorted({t.strip().upper() for t in _CRYPTO_RAW if t.strip()})
print(f"[Crypto Practice] Loaded {len(CRYPTO_TICKERS)} crypto tickers.")

def crypto_practice(rounds: int = 25, interval_sec: float = 3.0):
    """
    Start prompt:
      - Shift+F: normal 25 rounds (50/50 BIG vs CRYPTO; BIG excludes '-' and '*U').
      - Shift+J: previous-mistakes-only (25 rounds sampled from PREVIOUS_MISTAKES).
    Rules (both modes):
      - You must TYPE the ticker correctly (press Enter) BEFORE your action counts.
      - BIG ticker win: after typing correctly, press Shift+F twice within the window.
      - CRYPTO ticker win: after typing correctly, do NOT press Shift+F at all within the window.
      - Pressing Shift+F any number of times during CRYPTO window = LOSS; other keys don't matter.
    Output:
      - Colored WIN/LOSS per round, and final "Total wins" + "Tickers messed up - [...]".
    """
    import random, time, keyboard, winsound
    from datetime import datetime
    from zoneinfo import ZoneInfo
    try:
        from colorama import Fore, Back, Style, init as colorama_init
        colorama_init(autoreset=True)
    except Exception:
        class _Dummy: RESET_ALL=''
        class _F: BLACK=''
        class _B: GREEN=''; RED=''
        Fore=_F(); Back=_B(); Style=_Dummy()

    # ---------- Configure the "Previous Mistakes" list ----------
    PREVIOUS_MISTAKES = [
        "SRXH","MSS","BDL","JFBR","PFSA","TGB","STTK","MOGO","LMFA","TPG",
        "PRE","SQNS","SLV","JG","WNS","BTO","SION","ET","EONR","NVFY",
        "KWM","YXT",
        "CYN","AMOD","TZUP"
    ]

    # ---------- Sanity checks ----------
    def _err(msg): print("[Crypto Practice] " + msg)
    if 'CRYPTO_TICKERS' not in globals() or not CRYPTO_TICKERS:
        _err("CRYPTO_TICKERS is not defined or empty."); return
    if 'BIG_TICKERS' not in globals() or not BIG_TICKERS:
        _err("BIG_TICKERS is not defined or empty."); return

    # ---------- Helpers ----------
    def now_str():
        return datetime.now(ZoneInfo("America/New_York")).strftime("%H:%M:%S.%f")

    def is_crypto(t: str) -> bool:
        return t.upper() in {x.upper() for x in CRYPTO_TICKERS}

    # BIG selection excludes tickers with '-' or ending in 'U'
    def pick_big_ticker():
        candidates = [t for t in BIG_TICKERS if '-' not in t and not t.upper().endswith('U')]
        return random.choice(candidates) if candidates else None

    # ---------- Start-mode prompt ----------
    print("Type Shift+F for normal test, or Shift+J for previous mistakes only")
    mode = None  # "normal" or "previous"
    while mode is None:
        e = keyboard.read_event()
        if e.event_type == "down" and e.name:
            nm = e.name.lower()
            if nm == "f" and keyboard.is_pressed("shift"):
                mode = "normal"
            elif nm == "j" and keyboard.is_pressed("shift"):
                mode = "previous"

    print(f"[Crypto Practice] Mode selected: {mode.upper()}")
    wins = 0
    messed_up = []

    for i in range(1, rounds + 1):
        # ---------- Choose ticker ----------
        if mode == "normal":
            # 50/50 BIG vs CRYPTO
            is_big = (random.random() < 0.5)
            ticker = None
            if is_big:
                ticker = pick_big_ticker()
                # Fallback to crypto if BIG pool filtered out everything (very unlikely)
                if not ticker:
                    is_big = False
            if not is_big:
                ticker = random.choice(CRYPTO_TICKERS)
        else:
            # previous-mistakes-only
            ticker = random.choice(PREVIOUS_MISTAKES)
            # Grade by "normal method": if in CRYPTO_TICKERS => crypto rules; else BIG rules
            is_big = not is_crypto(ticker)

        # ---------- Announce round ----------
        print()
        print(ticker); print(ticker); print(ticker)
        label = "BIG (type + Shift+F twice)" if is_big else "CRYPTO (type + no Shift+F)"
        print(f"{now_str()}\tRound {i}/{rounds}\t{label}")
        try:
            winsound.Beep(2500, 150)
        except Exception:
            pass

        # ---------- Key capture state ----------
        typed_ok = False
        shift_f_after_typed = 0
        buffer = []
        target = ticker.upper()

        def on_event(e):
            nonlocal typed_ok, shift_f_after_typed, buffer
            if e.event_type != "down":
                return
            name = (e.name or "").lower()

            # Build typed buffer until Enter
            if not typed_ok:
                if name == "enter":
                    typed = "".join(buffer).upper()
                    if typed == target:
                        typed_ok = True
                    buffer = []
                    return
                if name == "backspace":
                    if buffer: buffer.pop()
                    return
                # Accept alphanumerics only (keeps it strict)
                if len(name) == 1 and name.isalnum():
                    buffer.append(name)
                return

            # After correct typing, ONLY count Shift+F
            if name == "f" and keyboard.is_pressed("shift"):
                shift_f_after_typed += 1

        hook = keyboard.hook(on_event, suppress=False)

        # ---------- 3-second window ----------
        deadline = time.time() + interval_sec
        try:
            while time.time() < deadline:
                # Early success end if BIG and we've already got 2 Shift+F
                if is_big and typed_ok and shift_f_after_typed >= 2:
                    break
                time.sleep(0.01)
        finally:
            keyboard.unhook(hook)

        # ---------- Score ----------
        if is_big:
            win = (typed_ok and shift_f_after_typed >= 2)
        else:
            # CRYPTO: must have typed correctly AND did NOT press Shift+F at all
            win = (typed_ok and shift_f_after_typed == 0)

        detail = f"(typed_ok={typed_ok}, shiftF_after_typed={shift_f_after_typed})"
        if win:
            line = f"[Crypto Practice] {ticker} -> WIN {detail}"
            print(Back.GREEN + Fore.BLACK + line + Style.RESET_ALL)
            wins += 1
        else:
            line = f"[Crypto Practice] {ticker} -> LOSS {detail}"
            print(Back.RED + Fore.BLACK + line + Style.RESET_ALL)
            messed_up.append(ticker)

        # keep cadence tight to 3s intervals
        remaining = deadline - time.time()
        if remaining > 0:
            time.sleep(remaining)

    # ---------- Summary ----------
    print("\n" + "=" * 48)
    print(f"Total wins: {wins}")
    print(f"Tickers messed up - {messed_up}")
    print("=" * 48)




if __name__ == "__main__":
    crypto_practice()
