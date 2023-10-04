import time

from utils.browser_interactions import BrowserInteractions
from pom.locators.job_page_locators import JobPageLocators


class JobPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_job_page(self, url: str):
        self.browser_interactions.open_page(url)

    def click_apply_now(self):
        self.browser_interactions.click_element(JobPageLocators.APPLY_NOW_BUTTON["strategy"],
                                                JobPageLocators.APPLY_NOW_BUTTON["selector"])

    def fill_form(self, name: str, email: str, number: str, city: str, linkedin: str, message: str):
        self.browser_interactions.input_text(JobPageLocators.NAME_INPUT["strategy"],
                                             JobPageLocators.NAME_INPUT["selector"], name)
        self.browser_interactions.input_text(JobPageLocators.EMAIL_INPUT["strategy"],
                                             JobPageLocators.EMAIL_INPUT["selector"], email)
        self.browser_interactions.input_text(JobPageLocators.NUMBER_INPUT["strategy"],
                                             JobPageLocators.NUMBER_INPUT["selector"], number)
        self.browser_interactions.input_text(JobPageLocators.LOCATION_INPUT["strategy"],
                                             JobPageLocators.LOCATION_INPUT["selector"], city)
        self.browser_interactions.load_file(JobPageLocators.DROPZONE_INPUT["strategy"],
                                            JobPageLocators.DROPZONE_INPUT["selector"], "/Users/laura.giraldo/PycharmProjects/SM_page_test/files/montains.pdf")
        self.browser_interactions.input_text(JobPageLocators.LINKEDIN_INPUT["strategy"],
                                             JobPageLocators.LINKEDIN_INPUT["selector"], linkedin)
        self.browser_interactions.input_text(JobPageLocators.MESSAGE_INPUT["strategy"],
                                             JobPageLocators.MESSAGE_INPUT["selector"], message)

