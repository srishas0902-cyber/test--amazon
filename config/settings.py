import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.amazon.com"

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

LT_USERNAME = os.getenv("LT_USERNAME", "")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY", "")
LT_GRID_URL = f"wss://cdp.lambdatest.com/playwright?user={LT_USERNAME}&accessKey={LT_ACCESS_KEY}"

USE_LAMBDATEST = os.getenv("USE_LAMBDATEST", "false").lower() == "true"

LT_CAPABILITIES = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "platform": "Windows 11",
        "build": "Amazon Automation - Parallel Build",
        "project": "Amazon Cart Tests",
        "network": True,
        "console": True,
        "terminal": True,
        "visual": True,
    }
}
