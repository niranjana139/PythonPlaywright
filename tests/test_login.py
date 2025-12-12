import pytest

from Constant import Constant
from pages.LoginPage import LoginPage
from utility.ExcelUtility import ExcelUtility


class TestLogin:
    # @pytest.mark.priority(1)
    # @pytest.mark.smoke
    def test_login_valid(self, page):
        page.goto("https://groceryapp.uniqassosiates.com/admin/login")

        login_page = LoginPage(page)
        excel = ExcelUtility(Constant.file_path)

        username_value = excel.get_string_data(2, 2, "LoginPage")
        password_value = excel.get_string_data(2, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()

        page.wait_for_load_state("networkidle")

        assert page.url == "https://groceryapp.uniqassosiates.com/admin"



    @pytest.mark.parametrize("row", [3, 4])
    def test_login_invalid(self, page, row):

        page.goto("https://groceryapp.uniqassosiates.com/admin/login")

        login_page = LoginPage(page)
        excel = ExcelUtility(Constant.file_path)

        username_value = excel.get_string_data(row, 1, "LoginPage")
        password_value = excel.get_string_data(row, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()

        page.wait_for_load_state("networkidle")

        assert page.url != "https://groceryapp.uniqassosiates.com/admin"
        print("INVALID login attempt URL:", page.url)

'''pytest tests/test_login.py::TestLogin::test_login_invalid --headed --browser=chromium --browser=firefox
Command to perform cross browser testing'''

