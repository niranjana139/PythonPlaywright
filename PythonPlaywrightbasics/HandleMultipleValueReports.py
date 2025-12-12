from BasicPlaywright import BasicPlaywright


class HandleMultipleValueElements(BasicPlaywright):

    def verify_drop_down(self):
        # Navigate to the URL
        self.page.goto("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        # Select option by visible text
        dropdown = self.page.locator("#dropdowm-menu-1")
        dropdown.select_option(label="C#")
        # By Index
        dropdown.select_option(index=2)
        # By Value
        dropdown.select_option(value="C#")

        # Get all dropdown options
        options = dropdown.locator("option").all()

        for option in options:
            print(option.text_content())
            print(option.is_checked() if option.get_attribute("selected") else False)

        def verify_check_box(self):
            # Navigate to the URL
            self.page.goto("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

            # Click checkbox
            check_box = self.page.locator("//input[@value='option-1']")
            check_box.check()

            # Check selected, enabled, displayed status
            print(check_box.is_checked())     # is_selected()
            print(check_box.is_enabled())     # is_enabled()
            print(check_box.is_visible())     # is_displayed()

    def verify_radio_button(self):
        # Navigate to the URL
        self.page.goto("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        green_radio = self.page.locator("//input[@value='green']")
        green_radio.check()

        print(green_radio.is_checked())
        print(green_radio.is_enabled())
        print(green_radio.is_visible())



multiValueElement = HandleMultipleValueElements()
multiValueElement.initialize_browser()

    # multiValueElement.verify_drop_down()
multiValueElement.verify_check_box()
    # multiValueElement.verify_radio_button()

    # multiValueElement.browser_close()  # Uncomment to close the browser
