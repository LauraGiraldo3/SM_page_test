from utils.browser_interactions import BrowserInteractions
from pom.locators.home_page_locators import HomePageLocators
from pom.contact_us_page import ContactUsPage
from pom.join_us_page import JoinUsPage


class HomePage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def open_home_page(self, url: str):
        self.browser_interactions.open_page(url)

    def click_menu(self):
        self.browser_interactions.click_element(HomePageLocators.MENU_BUTTON["strategy"],
                                                HomePageLocators.MENU_BUTTON["selector"])

    def open_contact_us_form(self):
        self.browser_interactions.click_element(HomePageLocators.CONTACT_US_OPTION["strategy"],
                                                HomePageLocators.CONTACT_US_OPTION["selector"])
        return ContactUsPage(self.browser_interactions)

    def open_join_us_page(self):
        self.browser_interactions.click_element(HomePageLocators.JOIN_US_OPTION["strategy"],
                                                HomePageLocators.JOIN_US_OPTION["selector"])
        return JoinUsPage(self.browser_interactions)
