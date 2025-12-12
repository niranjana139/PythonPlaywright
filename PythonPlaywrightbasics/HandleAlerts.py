from BasicPlaywright import BasicPlaywright
import time


class HandlingAlerts(BasicPlaywright):

    def verify_simple_alert(self):
        # Navigate to URL
        self.page.goto("https://demoqa.com/alerts")

        def handle_dialog(dialog):
            print(dialog.message)
            dialog.accept()

        self.page.on("dialog", handle_dialog)

        # Click alert button
        self.page.locator("#alertButton").click()

        time.sleep(2)
        print("Simple Alert clicked")

    def verify_confirm_alert(self):
        # Navigate to URL
        self.page.goto("https://demoqa.com/alerts")

        # ✅ Handle confirm alert (Accept)
        self.page.on("dialog", lambda dialog: dialog.accept())

        # Click confirm alert button
        self.page.locator("#confirmButton").click()

        time.sleep(2)
        print("Confirm alert clicked")

    def prompt_alert(self):
        # Navigate to URL
        self.page.goto("https://demoqa.com/alerts")

        # ✅ Handle prompt alert with input text
        def handle_prompt(dialog):
            dialog.accept("Niranjana")

        self.page.on("dialog", handle_prompt)

        # Click prompt button
        self.page.locator("#promtButton").click()

        time.sleep(2)
        print("Prompt alert clicked")


# Main execution

alerts = HandlingAlerts()
alerts.initialize_browser()

    # Uncomment the functions you want to run
alerts.verify_simple_alert()
    # alerts.verify_confirm_alert()
    # alerts.prompt_alert()

    # alerts.browser_close()  # Uncomment to close the browser
