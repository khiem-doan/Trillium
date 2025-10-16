# soundboard.py
from pathlib import Path
import os
import winsound

def _default_docs_folder() -> Path:
    # Prefer regular Documents; if you’re on OneDrive, use that if present
    candidates = [
        Path.home() / "Documents",
        Path.home() / "OneDrive" / "Documents",
    ]
    for c in candidates:
        if c.exists():
            return c
    # fallback: create standard Documents
    p = Path.home() / "Documents"
    p.mkdir(parents=True, exist_ok=True)
    return p

class SoundBoard:
    """
    Simple WAV soundboard rooted at a folder (default: Documents).
    Play by base name (stem), e.g. play("business insider") -> looks for "business insider.wav".
    """
    def __init__(self, folder: Path | str | None = None, async_play: bool = True):
        self.folder = Path(folder) if folder else _default_docs_folder()
        self.folder.mkdir(parents=True, exist_ok=True)
        self.async_play = async_play
        self._index: dict[str, Path] = {}
        self.refresh()

    def refresh(self) -> None:
        self._index = {p.stem.lower(): p for p in self.folder.glob("*.wav")}

    def play(self, name: str, *, stop_current: bool = False, fallback_beep=(1000, 200)) -> bool:
        """Play a sound by base name. Returns True if played, else False (and optional beep)."""
        if stop_current:
            winsound.PlaySound(None, winsound.SND_PURGE)

        key = str(name).lower()
        path = self._index.get(key)
        if not path:
            # allow partial match if exact not found
            path = next((p for n, p in self._index.items() if key in n), None)

        if path and path.is_file():
            flags = winsound.SND_FILENAME | (winsound.SND_ASYNC if self.async_play else 0)
            winsound.PlaySound(str(path), flags)
            return True

        if fallback_beep:
            f, d = fallback_beep
            try:
                winsound.Beep(f, d)
            except Exception:
                pass
        return False

    def list(self) -> list[str]:
        """Return available base names (no .wav)."""
        return sorted(self._index.keys())

# default soundboard rooted at your Documents folder
SOUNDS = SoundBoard()