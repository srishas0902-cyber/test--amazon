from playwright.sync_api import Page
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BOX = "#twotabsearchtextbox"
    ANY_RESULT = "div[data-component-type='s-search-result'] h2 a.a-link-normal"

    def __init__(self, page: Page):
        super().__init__(page)

    def go_to_amazon(self):
        from config.settings import BASE_URL
        self.navigate(BASE_URL)

    def search_for(self, query: str):
        print(f"\n[SearchPage] Searching for: '{query}'")
        self.page.locator(self.SEARCH_BOX).fill(query)
        self.page.locator(self.SEARCH_BOX).press("Enter")
        self.page.wait_for_load_state("domcontentloaded")

    def click_first_result(self):
        first = self.page.locator(self.ANY_RESULT).first
        first.wait_for(state="visible")
        product_title = first.inner_text().strip()
        print(f"[SearchPage] Clicking: '{product_title[:80]}'")
        first.click()
        self.page.wait_for_load_state("domcontentloaded")
