from playwright.sync_api import Page
from config.settings import TIMEOUT


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(TIMEOUT)

    def navigate(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        self.page.locator(selector).first.click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).first.fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).first.inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).first.is_visible()
