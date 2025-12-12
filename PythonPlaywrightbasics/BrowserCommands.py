from BasicPlaywright import BasicPlaywright


class HandleBrowserCommands(BasicPlaywright):

    def verify_commands(self):
        # Gets the title of the webpage
        title = self.page.title()
        print(title)

        # Gets the URL of the page
        url = self.page.url
        print(url)

        # Gets the Id of the page (Playwright does not expose window handle like Selenium)
        page_id = id(self.page)
        print(page_id)

        # Gets the source code of the webpage
        page_source = self.page.content()
        print(page_source)


# Main execution
commands = HandleBrowserCommands()
commands.initialize_browser()
commands.verify_commands()
# commands.browser_close()  # Uncomment to close the browser
