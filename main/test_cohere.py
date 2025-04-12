from playwright.sync_api import Page, expect
from pages.landing_page import Landing_page
from pages.dashboard import Dashboard
from fixtures.config_fixture import config
from os import getcwd

def test_send_chat(page: Page, config):
    email = config['email']
    password = config['password']
    landing_page = Landing_page(page)

    dashboard_page = landing_page.navigate_to_dashboard()
    dashboard_page.wait_for_load_state() 

    dashboard = Dashboard(dashboard_page)
    dashboard.login(email, password)

    # Assert that the log in was successful, with the correct account 
    dashboard.get_profile_popover().click()
    dashboard_page.wait_for_load_state()
    expect(dashboard.get_profile_email()).to_contain_text(email)

    dashboard.go_to_chat()
    dashboard.message_chatbot("Hello, where are my keys?")

    # Assert that a response has been generated, since it can be upvoted
    expect(dashboard.get_like_button()).to_be_visible(timeout = 15000)

    dashboard.logout()
    dashboard_page.wait_for_load_state()

    # Assert that the logout has been successful
    expect(dashboard.get_login_button()).to_be_visible()


def test_upload_file(page: Page, config):
    email = config['email']
    password = config['password']
    landing_page = Landing_page(page)

    dashboard_page = landing_page.navigate_to_dashboard()
    dashboard_page.wait_for_load_state() 

    dashboard = Dashboard(dashboard_page)
    dashboard.login(email, password)

    # Assert that the log in was successful, with the correct account 
    dashboard.get_profile_popover().click()
    dashboard_page.wait_for_load_state()
    expect(dashboard.get_profile_email()).to_contain_text(email)

    dashboard.go_to_chat()
    dashboard.upload_pdf("the_raven.pdf")

    # Assert that a file has just been uploaded, since only this file will have its checkbox checked
    expect(dashboard.get_uploaded_checkbox()).to_be_visible(timeout = 15000)

    dashboard.message_chatbot("Hello, what is this pdf about?")
    
    # Assert that the chatbot has correctly changed the topic of the conversration to match the topic of the .pdf file
    expect(dashboard_page.get_by_role("main").locator("span").filter(has_text="Edgar Allan Poe").first).to_be_visible(timeout = 20000)

    dashboard.logout()
    dashboard_page.wait_for_load_state()

    # Assert that the logout has been successful
    expect(dashboard.get_login_button()).to_be_visible()