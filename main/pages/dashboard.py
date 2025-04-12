from playwright.sync_api import Page
from os import getcwd

class Dashboard:
    def __init__(self, page: Page):
        self.page = page

    def get_email_field(self):
        return self.page.get_by_role("textbox", name="Email")

    def get_password_field(self):
        return self.page.get_by_role("textbox", name="Password")

    def get_login_button(self):
        return self.page.get_by_role("button", name="Log in ")

    def get_chat_button(self):
        return self.page.get_by_role("link", name="Chat", exact=True)

    def get_message_textbox(self):
        return self.page.get_by_role("textbox", name="Message...")

    def get_profile_popover(self):
        return self.page.get_by_role("button", name="")

    def get_profile_email(self):
        return self.page.locator("[id=\"headlessui-popover-panel-\\:r4\\:\"]").get_by_text("@")

    def get_log_out_button(self):
        return self.page.get_by_role("link", name="Log out")

    def get_like_button(self):
        return self.page.get_by_role("button", name="approve feedback", exact=True)
    
    def get_tools_drawer(self):
        return self.page.get_by_test_id("button-tools-drawer")
    
    def get_files_tab(self):
        return self.page.get_by_role("tab", name="Files")
    
    def get_input_file_selector(self):
        return "input[type='file']"
    
    def get_attachment_listing(self, file_name: str):
        return self.page.get_by_text(file_name)
    
    def get_uploaded_checkbox(self):
        return self.page.get_by_role("checkbox", name="")
    
    def login(self, email: str, password: str):
        self.get_email_field().fill(email)
        self.get_password_field().fill(password)
        self.get_login_button().click()

    def logout(self):
        self.get_profile_popover().click()
        self.get_log_out_button().click()

    def go_to_chat(self):
        self.get_chat_button().click()
        # Dismiss any initial overlays/popups
        buttons = ["Accept All", "Try now "]
        for button in buttons:
            try:
                self.page.get_by_role("button", name=button).click()
            except:
                pass

    def message_chatbot(self, message: str):
        message_textbox = self.get_message_textbox()
        message_textbox.fill(message)
        message_textbox.press('Enter')

    def upload_pdf(self, file_name: str):
        self.get_tools_drawer().click()
        self.get_files_tab().click()
        self.page.wait_for_selector(self.get_input_file_selector(), state="attached", timeout = 5000)

        # Check if the file has already been uploaded
        try:
            self.get_attachment_listing(file_name).click(timeout = 2000)
        except:
            self.page.set_input_files(self.get_input_file_selector(), getcwd() + "/main/resources/" + file_name)