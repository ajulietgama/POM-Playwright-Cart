from pages.dashboard_page import DashboardPage

def test_add_product_to_cart(logged_in_page):
    dashboard = DashboardPage(logged_in_page)
    dashboard.view_product("ZARA COAT 3")
    dashboard.add_to_cart()


# tests/test_dashboard.py


