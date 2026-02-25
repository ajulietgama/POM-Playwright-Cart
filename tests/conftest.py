import pytest
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)

    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    login.login("angy.gama@gmail.com", "Poiuytr5+")

    yield page
