from typing import Protocol, runtime_checkable
from playwright.sync_api import Page, Locator
from os import getcwd

@runtime_checkable
class DashboardInterface(Protocol):

    def __init__(self, page: Page):
        pass

    def get_login_button(self) -> Locator:
        pass

    def get_profile_email(self) -> Locator:
        pass

    # Returns an indicator that the chatbot has successfully responded
    def get_response_indicator(self) -> Locator:
        pass

    # Returns an indicator that the file has successfully been uploaded
    def get_uploaded_indicator(self) -> Locator:
        pass
    
    # Returns the topic of the conversation with the chatbot, to ensure that it is about the uploaded file
    def get_conversation_topic(self, topic: str) -> Locator:
        pass

    def login(self, email: str, password: str):
        pass

    def logout(self):
        pass

    def go_to_chat(self):
        pass

    def message_chatbot(self, message: str):
        pass

    def upload_pdf(self, file_name: str):
        pass