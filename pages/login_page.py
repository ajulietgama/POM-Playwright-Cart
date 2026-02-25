# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str) -> None:
        self.page.get_by_role("textbox", name="email@example.com").fill(email)
        self.page.get_by_role("textbox", name="enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
