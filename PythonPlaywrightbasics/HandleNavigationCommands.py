from BasicPlaywright import BasicPlaywright


class HandleNavigationCommands(BasicPlaywright):

    def verify_navigation_commands(self):
        # Helps to navigate to another site or another page within the site
        self.page.goto("https://www.amazon.in/")

        # Helps to navigate back to the previous page
        self.page.go_back()

        # Helps to move forward to the next page
        self.page.go_forward()

        # Helps to refresh the page
        self.page.reload()


# Main execution

navigation = HandleNavigationCommands()
navigation.initialize_browser()
navigation.verify_navigation_commands()
    # navigation.browser_close()  # Uncomment to close the browser
