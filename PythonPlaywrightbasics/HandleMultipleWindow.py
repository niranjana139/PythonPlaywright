from BasicPlaywright import BasicPlaywright
import time


class HandleMultipleWindow(BasicPlaywright):

    def verify_multiple_window(self):
        # Navigate to the URL
        self.page.goto("https://demo.guru99.com/popup.php")

        # Store the main page reference
        main_page = self.page
        print("Main window opened")

        with self.page.expect_popup() as popup_info:
            self.page.locator("//a[text()='Click Here']").click()

        # Get the newly opened window
        popup_page = popup_info.value
        print("New window opened")

        time.sleep(2)

        # Perform actions on new window
        email_fld = popup_page.locator("//input[@name='emailid']")
        email_fld.fill("abc@gmail.com")

        submit_fld = popup_page.locator("//input[@name='btnLogin']")
        submit_fld.click()

        time.sleep(2)


        main_page.bring_to_front()
        print("Switched back to main window")



multiple_window = HandleMultipleWindow()
multiple_window.initialize_browser()
multiple_window.verify_multiple_window()
multiple_window.browser_close()
