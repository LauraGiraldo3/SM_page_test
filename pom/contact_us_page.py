import time
from utils.browser_interactions import BrowserInteractions
from pom.locators.contact_us_page_locators import ContactUsPageLocators


class ContactUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_contact_us_page(self, url: str):
        self.browser_interactions.open_page(url)

    def fill_name_input(self, name: str):
        self.browser_interactions.input_text(ContactUsPageLocators.NAME_INPUT["strategy"],
                                             ContactUsPageLocators.NAME_INPUT["selector"], name)

    def fill_email_input(self, email: str):
        self.browser_interactions.input_text(ContactUsPageLocators.EMAIL_INPUT["strategy"],
                                             ContactUsPageLocators.EMAIL_INPUT["selector"], email)

    def fill_company_input(self, company: str):
        self.browser_interactions.input_text(ContactUsPageLocators.COMPANY_INPUT["strategy"],
                                             ContactUsPageLocators.COMPANY_INPUT["selector"], company)

    def fill_number_input(self, number: str):
        self.browser_interactions.input_text(ContactUsPageLocators.NUMBER_INPUT["strategy"],
                                             ContactUsPageLocators.NUMBER_INPUT["selector"], number)

    def fill_message_input(self, message: str):
        self.browser_interactions.input_text(ContactUsPageLocators.HELP_TEXT_INPUT["strategy"],
                                             ContactUsPageLocators.HELP_TEXT_INPUT["selector"], message)
        self.browser_interactions.scroll()
        time.sleep(1)

    def check_terms_cond(self):
        self.browser_interactions.click_element(ContactUsPageLocators.TERMS_COND_CHECKBOX["strategy"],
                                                ContactUsPageLocators.TERMS_COND_CHECKBOX["selector"])

    def click_send(self):
        self.browser_interactions.click_element(ContactUsPageLocators.SEND_BUTTON["strategy"],
                                                ContactUsPageLocators.SEND_BUTTON["selector"])

    def success_message_is_visible(self):
        return self.browser_interactions.element_is_visible(ContactUsPageLocators.SUCCESS_MESSAGE["strategy"],
                                                            ContactUsPageLocators.SUCCESS_MESSAGE["selector"])

    def error_message_is_visible(self):
        return self.browser_interactions.element_is_visible(ContactUsPageLocators.ERROR_MESSAGE["strategy"],
                                                            ContactUsPageLocators.ERROR_MESSAGE["selector"])
