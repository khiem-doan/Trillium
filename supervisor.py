# supervisor.py
import subprocess, threading, sys, os, time
from pathlib import Path

# ---- EDIT THESE THREE PATHS ----
HEADERS = r"C:\Users\Trader\PycharmProjects\Scraper Project\headers_working.py"
NEWS    = r"C:\Users\Trader\PycharmProjects\Scraper Project\news_scrape.py"  # <-- put the REAL path here
# LIVE13F = r"C:\Users\Trader\AppData\Roaming\JetBrains\PyCharmCE2024.2\scratches\13F_Live.py"

CMDS = [
    ("HEADERS", [sys.executable, HEADERS]),
    ("NEWS",    [sys.executable, NEWS]),
    # ("13F",     [sys.executable, LIVE13F]),
]

# Optional: add flags, e.g.:
# ("13F", [sys.executable, LIVE13F, "--monitor", "--poll-min", "2", "--poll-max", "3"])

# Ensure immediate flush & UTF-8 for children
BASE_ENV = os.environ.copy()
BASE_ENV.setdefault("PYTHONUNBUFFERED", "1")
BASE_ENV.setdefault("PYTHONIOENCODING", "utf-8")
BASE_ENV.setdefault("PYTHONUTF8", "1")

def pump(tag, proc):
    prefix = f"[{tag}] "
    # Read line-by-line, never crash on bad bytes
    for line in iter(proc.stdout.readline, ''):
        # line is str because we pass text=True with encoding='utf-8'
        sys.stdout.write(prefix + line)
        sys.stdout.flush()
    proc.stdout.close()

def spawn(tag, cmd):
    # Pick a cwd so any relative file paths still work
    cwd = None
    try:
        script_path = Path(cmd[1])
        cwd = str(script_path.parent)
    except Exception:
        pass

    # Launch with UTF-8 pipe and merged stderr
    return subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,           # line-buffered
        env=BASE_ENV,
        cwd=cwd
    )

def main():
    # Preflight: warn if any paths are wrong
    for tag, cmd in CMDS:
        script = cmd[1] if len(cmd) > 1 else None
        if not script or not Path(script).is_file():
            print(f"[{tag}] ERROR: script not found -> {script}")
    print()

    procs = []
    for tag, cmd in CMDS:
        if len(cmd) > 1 and Path(cmd[1]).is_file():
            p = spawn(tag, cmd)
            procs.append((tag, p))
            threading.Thread(target=pump, args=(tag, p), daemon=True).start()

    # Keep the supervisor alive; restart if any process dies (optional)
    try:
        while True:
            # If you want auto-restart, uncomment:
            # for i, (tag, p) in enumerate(list(procs)):
            #     if p.poll() is not None:
            #         print(f"[{tag}] exited with code {p.returncode}, restarting...")
            #         newp = spawn(tag, dict(CMDS)[tag])
            #         procs[i] = (tag, newp)
            #         threading.Thread(target=pump, args=(tag, newp), daemon=True).start()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[supervisor] Shutting down...")
        for _, p in procs:
            try: p.terminate()
            except Exception: pass

if __name__ == "__main__":
    main()
