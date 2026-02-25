from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    login_page.login("angy.gama@gmail.com", "Poiuytr5+")
