from typing import Protocol, runtime_checkable
from playwright.sync_api import Page, Locator

@runtime_checkable
class LandingPageInterface(Protocol):

    def __init__(self, page: Page):
        pass

    def get_page_url(self) -> str:
        pass

    def get_signin_button(self) -> Locator:
        pass

    def navigate_to_dashboard(self) -> Page:
        pass