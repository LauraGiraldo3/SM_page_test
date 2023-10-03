from utils.web_driver import WebDriverBrowser
from utils.browser_interactions import BrowserInteractions


def before_scenario(context, scenario):
    web_driver = WebDriverBrowser("Chrome").create_driver()
    context.browser_interactions = BrowserInteractions(web_driver)
