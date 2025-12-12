from BasicPlaywright import BasicPlaywright


class HandlingWebElements(BasicPlaywright):

    def verify_commands(self):
        self.page.goto("https://selenium.qabible.in/simple-form-demo.php")

        # Locate the message box and send text
        msg_box = self.page.locator("#single-input-field")
        msg_box.fill("Niranjana")

        # Locate the button and check its display and enabled state
        btn = self.page.locator("#button-one")
        print(btn.is_visible())   # is_displayed()
        print(btn.is_enabled())   # is_enabled()

        btn.click()

        # Locate the message text and print its content and background color
        msg_text = self.page.locator("#message-one")
        print(msg_text.text_content())
        print(msg_text.evaluate("el => getComputedStyle(el).backgroundColor"))

        # Clear the message box
        msg_box.fill("")


# Main execution

locators = HandlingWebElements()
locators.initialize_browser()
locators.verify_commands()
    # locators.browser_close()  # Uncomment to close the browser
