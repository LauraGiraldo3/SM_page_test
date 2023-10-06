from selenium.common import TimeoutException
from utils.browser_interactions import BrowserInteractions
from pom.locators.contact_us_page_locators import ContactUsPageLocators


class ContactUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_contact_us_page(self, url: str):
        self.browser_interactions.open_page(url)

    def fill_out_form(self, name: str, email: str, company: str, number: str, message: str):
        self.browser_interactions.input_text(ContactUsPageLocators.NAME_INPUT["strategy"],
                                             ContactUsPageLocators.NAME_INPUT["selector"], name)
        self.browser_interactions.input_text(ContactUsPageLocators.EMAIL_INPUT["strategy"],
                                             ContactUsPageLocators.EMAIL_INPUT["selector"], email)
        self.browser_interactions.input_text(ContactUsPageLocators.COMPANY_INPUT["strategy"],
                                             ContactUsPageLocators.COMPANY_INPUT["selector"], company)
        self.browser_interactions.input_text(ContactUsPageLocators.NUMBER_INPUT["strategy"],
                                             ContactUsPageLocators.NUMBER_INPUT["selector"], number)
        self.browser_interactions.input_text(ContactUsPageLocators.HELP_TEXT_INPUT["strategy"],
                                             ContactUsPageLocators.HELP_TEXT_INPUT["selector"], message)

    def check_terms_cond(self):
        self.browser_interactions.click_element(ContactUsPageLocators.TERMS_COND_CHECKBOX["strategy"],
                                                ContactUsPageLocators.TERMS_COND_CHECKBOX["selector"])

    def click_send(self):
        self.browser_interactions.click_element(ContactUsPageLocators.SEND_BUTTON["strategy"],
                                                ContactUsPageLocators.SEND_BUTTON["selector"])

    def success_message_is_visible(self):
        try:
            self.browser_interactions.element_is_visible(ContactUsPageLocators.SUCCESS_MESSAGE["strategy"],
                                                         ContactUsPageLocators.SUCCESS_MESSAGE["selector"])
        except TimeoutException:
            return False
        else:
            return True

    def general_error_message(self):
        try:
            self.browser_interactions.element_is_visible(ContactUsPageLocators.GENERAL_ERROR_MESSAGE["strategy"],
                                                         ContactUsPageLocators.GENERAL_ERROR_MESSAGE["selector"])
        except TimeoutException:
            return False
        else:
            return True

    def field_error_message(self):
        try:
            self.browser_interactions.element_is_visible(ContactUsPageLocators.FIELD_ERROR_MESSAGE["strategy"],
                                                         ContactUsPageLocators.FIELD_ERROR_MESSAGE["selector"])
        except TimeoutException:
            return False
        else:
            page_lan = self.browser_interactions.get_page_lan()
            element_lan = self.browser_interactions.get_element_lan(ContactUsPageLocators.FIELD_ERROR_MESSAGE["strategy"],
                                                                    ContactUsPageLocators.FIELD_ERROR_MESSAGE["selector"])
            if page_lan[:2] == element_lan[0].lang:
                return True
            else:
                return False
