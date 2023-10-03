from behave import step
from dotenv import load_dotenv
from pom.home_page import HomePage
import os


load_dotenv()


@step("the user open the Source Meridian home page")
def go_to_home(context):
    home_page = HomePage(context.browser_interactions)
    home_page.open_home_page(os.getenv("URL"))


@step("the user clicks on menu options")
def click_menu(context):
    home_page = HomePage(context.browser_interactions)
    home_page.click_menu()


@step("the user clicks on 'Contact us' option")
def click_contact_us(context):
    home_page = HomePage(context.browser_interactions)
    home_page.open_contact_us_form()


@step("the user clicks on 'Join us' option")
def click_join_us(context):
    home_page = HomePage(context.browser_interactions)
    home_page.open_join_us_page()