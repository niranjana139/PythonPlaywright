from playwright.sync_api import sync_playwright


class BasicPlaywright:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def initialize_browser(self):
        # Start Playwright
        self.playwright = sync_playwright().start()

        # Launch Chromium browser (Chrome equivalent)
        self.browser = self.playwright.chromium.launch(headless=False)

        # Create a new page (tab)
        self.page = self.browser.new_page()

        # Open the URL
        self.page.goto("https://selenium.qabible.in/")

        # Maximize window (set viewport size)
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    def browser_close(self):
        # Close browser and stop Playwright
        self.browser.close()
        self.playwright.stop()


base = BasicPlaywright()
base.initialize_browser()
    # base.browser_close()
