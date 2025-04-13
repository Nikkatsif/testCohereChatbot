from playwright.sync_api import Page, expect
import pytest
import config
from fixtures.login_fixture import login_to_dashboard

@pytest.mark.parametrize(
    "llm_page",
    config.PAGES_LIST,
)
def test_send_chat(login_to_dashboard):
    email, dashboard, dashboard_page = login_to_dashboard

    # Assert that the log in was successful, with the correct account 
    expect(dashboard.get_profile_email()).to_contain_text(email)

    dashboard.go_to_chat()
    dashboard.message_chatbot("Hello, where are my keys?")

    # Assert that a response has been generated, with an indicator that only appears if this has indeed happened
    expect(dashboard.get_response_indicator()).to_be_visible(timeout = 15000)

    dashboard.logout()
    dashboard_page.wait_for_load_state()

    # Assert that the logout has been successful
    expect(dashboard.get_login_button()).to_be_visible()

@pytest.mark.parametrize(
    "llm_page",
    config.PAGES_LIST,
)
def test_upload_file(login_to_dashboard):
    email, dashboard, dashboard_page = login_to_dashboard

    # Assert that the log in was successful, with the correct account 
    expect(dashboard.get_profile_email()).to_contain_text(email)

    dashboard.go_to_chat()
    dashboard.upload_pdf("the_raven.pdf")

    # Assert that a file has just been uploaded, with a corresponding indicator
    expect(dashboard.get_uploaded_indicator()).to_be_visible(timeout = 15000)

    dashboard.message_chatbot("Hello, what is this pdf about?")
    
    # Assert that the chatbot has correctly changed the topic of the conversration to match the topic of the .pdf file
    expect(dashboard.get_conversation_topic("Edgar Allan Poe")).to_be_visible(timeout = 20000)

    dashboard.logout()
    dashboard_page.wait_for_load_state()

    # Assert that the logout has been successful
    expect(dashboard.get_login_button()).to_be_visible()