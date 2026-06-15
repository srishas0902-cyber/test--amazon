import json
from config.settings import (
    BROWSER, HEADLESS, SLOW_MO, TIMEOUT,
    USE_LAMBDATEST, LT_GRID_URL, LT_CAPABILITIES
)


class BrowserFactory:

    @staticmethod
    def create_browser(playwright, test_name: str = "Amazon Test"):
        if USE_LAMBDATEST:
            return BrowserFactory._create_lambdatest_browser(playwright, test_name)
        return BrowserFactory._create_local_browser(playwright)

    @staticmethod
    def _create_local_browser(playwright):
        launch_opts = {
            "headless": HEADLESS,
            "slow_mo": SLOW_MO,
            "args": [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        }
        browser_map = {
            "chromium": playwright.chromium,
            "firefox": playwright.firefox,
            "webkit": playwright.webkit,
        }
        browser_launcher = browser_map.get(BROWSER.lower(), playwright.chromium)
        browser = browser_launcher.launch(**launch_opts)

        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )
        context.set_default_timeout(TIMEOUT)
        page = context.new_page()
        return browser, page

    @staticmethod
    def _create_lambdatest_browser(playwright, test_name: str):
        caps = dict(LT_CAPABILITIES)
        caps["LT:Options"] = dict(caps["LT:Options"])
        caps["LT:Options"]["name"] = test_name
        endpoint = f"{LT_GRID_URL}&capabilities={json.dumps(caps)}"
        print(f"[BrowserFactory] Connecting to LambdaTest: '{test_name}'")
        browser = playwright.chromium.connect(endpoint)
        context = browser.new_context()
        context.set_default_timeout(TIMEOUT)
        page = context.new_page()
        return browser, page
