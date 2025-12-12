from BasicPlaywright import BasicPlaywright


class HandleFrames(BasicPlaywright):

    def handle_frames(self):
        # Navigate to the desired URL
        self.page.goto("https://demoqa.com/frames")

        # Find all iframe elements
        total_frames = self.page.locator("iframe")
        print(total_frames.count())   # Print number of frames

        # Switch to specific frame using ID
        frame1 = self.page.frame_locator("iframe#frame1")
        print("Successfully switched to the frame using ID.")

        # Find element inside the frame and print text
        heading = frame1.locator("#sampleHeading")
        print("Successfully switched to the frame and found the element using ID.")
        print(heading.text_content())

        # Switch to frame by index (second iframe)
        frame_by_index = self.page.frame_locator("iframe:nth-of-type(2)")
        print("Successfully switched to the frame using index.")

        # ✅ Playwright automatically returns to main page (no default_content() needed)


frames = HandleFrames()
frames.initialize_browser()
frames.handle_frames()
# frames.browser_close()  # Uncomment to close the browser
