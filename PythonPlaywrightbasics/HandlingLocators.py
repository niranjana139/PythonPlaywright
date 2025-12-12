from BasicPlaywright import BasicPlaywright


class HandlingLocators(BasicPlaywright):

    def verify_locators(self):
        self.page.goto("https://selenium.qabible.in/simple-form-demo.php")

        # ID Locator
        self.page.locator("#button-one")

        # TAG NAME
        self.page.locator("button")

        # NAME locator (converted to CSS since Playwright does not use By.NAME)
        self.page.locator("[name='viewport']")

        # LINK TEXT
        self.page.get_by_text("Simple Form Demo", exact=True)

        # PARTIAL LINK TEXT
        self.page.get_by_text("Simple")

        # CSS SELECTOR
        self.page.locator("button#button-one")

        # XPATH Locators
        self.page.locator("//button[@id='button-one']")
        self.page.locator("//button[text()='Get Total']")
        self.page.locator("//button[starts-with(text(),'Show ')]")

        # AND / OR conditions
        self.page.locator("//button[@id='button-one' and @type='button']")
        self.page.locator("//button[@id='button-one' or @id='button-one-electronics']")

        # Parent axis
        self.page.locator("//div[contains(text(), 'Single Input Field')]/parent::div[@class='card']")

        # Child axis
        self.page.locator("//div[@class='card']/child::button[@id='button-one']")

        # Following axis
        self.page.locator("//button[@id='button-one']/following::div[@class='card']")

        # Preceding axis
        self.page.locator("//button[@id='button-one']/preceding::div[@class='card']")

        # Ancestor axis
        self.page.locator("//div/ancestor::div[@class='card']")

        # Descendant axis
        self.page.locator("//div[@class='card']//descendant::div")



locators = HandlingLocators()
locators.initialize_browser()
locators.verify_locators()
    # locators.browser_close()  # Uncomment to close browser
