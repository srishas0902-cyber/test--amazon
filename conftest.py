import pytest
from playwright.sync_api import sync_playwright
from utils.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def browser_page(request):
    test_name = request.node.name
    with sync_playwright() as playwright:
        browser, page = BrowserFactory.create_browser(playwright, test_name=test_name)
        yield page
        browser.close()
