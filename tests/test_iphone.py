from pages.search_page import SearchPage
from pages.product_page import ProductPage
from utils.logger import log

TEST_NAME = "TC1 - iPhone"
SEARCH_QUERY = "iPhone"


def test_add_iphone_to_cart(browser_page):
    page = browser_page

    search = SearchPage(page)
    log(TEST_NAME, f"Searching for '{SEARCH_QUERY}'")
    search.go_to_amazon()
    search.search_for(SEARCH_QUERY)

    log(TEST_NAME, "Clicking first result")
    search.click_first_result()

    product = ProductPage(page)
    title = product.get_product_title()
    log(TEST_NAME, f"Product: {title[:100]}")

    price = product.get_price()
    log(TEST_NAME, f"Price: {price}")
    print(f"\n{'='*60}")
    print(f"  [TC1 - iPhone] PRICE RETRIEVED: {price}")
    print(f"{'='*60}\n")

    product.add_to_cart()
    log(TEST_NAME, "Test complete")

    assert price != "Price not found", "Could not retrieve the product price."
