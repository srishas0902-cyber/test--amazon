import re
from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRICE_SELECTORS = [
        "#corePrice_feature_div .a-price .a-offscreen",
        "#apex_offerDisplay_desktop .a-price .a-offscreen",
        ".priceToPay .a-offscreen",
        "#price_inside_buybox",
        "#priceblock_ourprice",
        "#priceblock_dealprice",
        ".a-price .a-offscreen",
    ]

    ADD_TO_CART_BTN = "#add-to-cart-button"
    MODAL_ADD_BTN = "#attachSiNoCoverage-announce, #attachSiText"
    CART_CONFIRMATION = "#NATC_SMART_WAGON_CONF_MSG_SUCCESS, #huc-v2-order-row-confirm-text"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_price(self) -> str:
        for selector in self.PRICE_SELECTORS:
            try:
                locator = self.page.locator(selector).first
                if locator.is_visible(timeout=2000):
                    raw = locator.inner_text().strip()
                    price = self._clean_price(raw)
                    if price:
                        return price
            except Exception:
                continue

        all_text = self.page.content()
        match = re.search(r'\$[\d,]+\.\d{2}', all_text)
        if match:
            return match.group(0)

        return "Price not found"

    def add_to_cart(self):
        btn = self.page.locator(self.ADD_TO_CART_BTN)
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(2000)

        modal_btn = self.page.locator(self.MODAL_ADD_BTN)
        if modal_btn.is_visible(timeout=3000):
            modal_btn.first.click()
            self.page.wait_for_timeout(1500)

        success = self.page.locator(self.CART_CONFIRMATION)
        try:
            success.first.wait_for(state="visible", timeout=8000)
            print("[ProductPage] Item successfully added to cart.")
        except Exception:
            print("[ProductPage] Could not confirm cart addition.")

    def get_product_title(self) -> str:
        try:
            return self.page.locator("#productTitle").first.inner_text().strip()
        except Exception:
            return "Unknown product"

    @staticmethod
    def _clean_price(raw: str) -> str:
        match = re.search(r'\$[\d,]+\.\d{2}', raw)
        return match.group(0) if match else raw.strip()
