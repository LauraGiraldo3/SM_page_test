from utils.browser_interactions import BrowserInteractions
from pom.locators.join_us_page_locators import JoinUsPageLocators
from pom.job_page import JobPage


class JoinUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_join_us_page(self, url: str):
        self.browser_interactions.open_page(url)

    def search_job(self, job_name: str):
        self.browser_interactions.input_text(JoinUsPageLocators.SEARCH_BOX["strategy"],
                                             JoinUsPageLocators.SEARCH_BOX["selector"], job_name)
        self.browser_interactions.click_element(JoinUsPageLocators.SEARCH_BUTTON["strategy"],
                                                JoinUsPageLocators.SEARCH_BUTTON["selector"])
        self.browser_interactions.click_element(JoinUsPageLocators.QA_JOB["strategy"],
                                                JoinUsPageLocators.QA_JOB["selector"])
        return JobPage(self.browser_interactions)
