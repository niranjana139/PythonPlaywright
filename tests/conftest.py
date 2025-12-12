import pytest
import os
from datetime import datetime
import pytest_html
import pytest
from playwright.sync_api import sync_playwright
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"screenshots/{item.name}_{time_stamp}.png"
            page.screenshot(path=screenshot_path)

            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra
#pytest --html=report.html --self-contained-html


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def crossbrowser(request):
    browser_name = request.param

    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}  # ✅ maximize replacement
        )
        page = context.new_page()

        yield page

        context.close()
        browser.close()