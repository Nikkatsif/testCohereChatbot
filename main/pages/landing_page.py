from playwright.sync_api import Page

class Landing_page:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://cohere.com"

    def get_page_url(self):
        return self.url

    def get_signin_button(self):
        return self.page.get_by_role("link", name = "Sign in")
    
    def navigate_to_dashboard(self):
        self.page.goto(self.get_page_url())
        with self.page.expect_popup() as dashboard_page_info:
            self.get_signin_button().click()
        return dashboard_page_info.value