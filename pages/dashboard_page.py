from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_button = page.get_by_role("button", name="Add to Cart")
        self.item_added = page.get_by_text("Product Added To Cart")

    def view_product(self, product_name: str) -> None:
        expect(self.page.get_by_text("ZARA COAT")).to_be_visible()

        product_card = self.page.locator(".card-body", has_text=product_name)
        product_card.get_by_role("button", name="View").click()

        expect(self.page.get_by_role("link", name="Continue Shopping")).to_be_visible()

    def add_to_cart(self) -> None:
        self.cart_button.click(force=True)
        expect(self.item_added).to_be_visible()
    
    


#dashboard = DashboardPage(page)
#dashboard.view_product("ZARA COAT 3")

