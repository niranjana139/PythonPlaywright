from BasicPlaywright import BasicPlaywright


class HandleTables(BasicPlaywright):

    def verify_handle_tables(self):
        # Navigate to the desired URL
        self.page.goto("https://money.rediff.com/indices/nse")

        # Locate the table element
        table = self.page.locator("//table[@id='dataTable']")
        print("Entire Table Text is:", table.text_content())

        # Fetch only a specific row (3rd row)
        table_row = self.page.locator("//table[@id='dataTable']/tbody/tr[3]")
        print("Third row text is:", table_row.text_content())

        # Fetch only the last row
        last_table_row = self.page.locator("//table[@id='dataTable']/tbody/tr[last()]")
        print("Last row text is:", last_table_row.text_content())


# Main execution
tables = HandleTables()
tables.initialize_browser()
tables.verify_handle_tables()
# tables.browser_close()  # Uncomment to close the browser after execution
