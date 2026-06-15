import threading
from datetime import datetime

_lock = threading.Lock()


def log(test_name: str, message: str):
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    with _lock:
        print(f"[{ts}] [{test_name}] {message}")
