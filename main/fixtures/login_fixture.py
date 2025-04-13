from playwright.sync_api import Page
import importlib
import config
import pytest

@pytest.fixture
# Imports the Pages, goes from the landing page to the Dashboard, and logs in
def login_to_dashboard(page: Page, llm_page: str) -> Page:
    try:
        landing_page_module = importlib.import_module("pages." + llm_page + ".landing_page")
        dashboard_module = importlib.import_module("pages." + llm_page + ".dashboard")
    except:
        print("Pages for " + llm_page + " not found!")
        assert False

    email = config.PAGE_CREDENTIALS[llm_page]['email']
    password = config.PAGE_CREDENTIALS[llm_page]['password']
    landing_page = landing_page_module.LandingPage(page)

    dashboard_page = landing_page.navigate_to_dashboard()
    dashboard_page.wait_for_load_state() 

    dashboard = dashboard_module.Dashboard(dashboard_page)
    dashboard.login(email, password)

    return email, dashboard, dashboard_page