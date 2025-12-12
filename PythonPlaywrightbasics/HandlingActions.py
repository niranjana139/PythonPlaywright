from BasicPlaywright import BasicPlaywright
import time


class HandlingActions(BasicPlaywright):

    def verify_right_click(self):
        # Right click on element
        self.page.locator("//a[text()='Home']").click(button="right")
        print("Right click performed successfully")

    def verify_mouse_hover(self):
        # Mouse hover on element
        self.page.locator("//a[text()='Home']").hover()
        print("Mouse hover performed successfully")

    def verify_drag_and_drop(self):
        self.page.goto("https://demoqa.com/droppable")

        drag = self.page.locator("#draggable")
        drop = self.page.locator("#droppable")

        # Drag and drop action
        drag.drag_to(drop)
        print("Drag and drop performed successfully")

    def verify_keyboard_action(self):

        new_page = self.browser.new_page()
        new_page.goto("https://www.google.com")

        time.sleep(2)  # Only for visibility (not required in real tests)

        # Keyboard type + Enter
        new_page.keyboard.type("Playwright Automation")
        new_page.keyboard.press("Enter")
        print("Keyboard actions performed successfully")


actions = HandlingActions()
actions.initialize_browser()

    # actions.verify_right_click()
    # actions.verify_mouse_hover()
    # actions.verify_drag_and_drop()
actions.verify_keyboard_action()

    # actions.browser_close()  # Uncomment to close the browser after execution

