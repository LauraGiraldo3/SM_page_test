import time
from utils.browser_interactions import BrowserInteractions
from pom.locators.job_page_locators import JobPageLocators


class JobPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_job_page(self, url: str):
        self.browser_interactions.open_page(url)

    def click_apply_now(self):
        time.sleep(3)
        self.browser_interactions.click_element(JobPageLocators.APPLY_NOW_BUTTON["strategy"],
                                                JobPageLocators.APPLY_NOW_BUTTON["selector"])
        time.sleep(1)

    def fill_form(self, name: str, email: str, number: str, city: str, linkedin: str, message: str):
        self.browser_interactions.input_text(JobPageLocators.NAME_INPUT["strategy"],
                                             JobPageLocators.NAME_INPUT["selector"], name)
        time.sleep(1)
        self.browser_interactions.input_text(JobPageLocators.EMAIL_INPUT["strategy"],
                                             JobPageLocators.EMAIL_INPUT["selector"], email)
        time.sleep(1)
        self.browser_interactions.input_text(JobPageLocators.NUMBER_INPUT["strategy"],
                                             JobPageLocators.NUMBER_INPUT["selector"], number)
        time.sleep(1)
        self.browser_interactions.input_text(JobPageLocators.LOCATION_INPUT["strategy"],
                                             JobPageLocators.LOCATION_INPUT["selector"], city)
        time.sleep(1)
        self.browser_interactions.input_text(JobPageLocators.LINKEDIN_INPUT["strategy"],
                                             JobPageLocators.LINKEDIN_INPUT["selector"], linkedin)
        time.sleep(1)
        self.browser_interactions.input_text(JobPageLocators.MESSAGE_INPUT["strategy"],
                                             JobPageLocators.MESSAGE_INPUT["selector"], message)
        time.sleep(1)

