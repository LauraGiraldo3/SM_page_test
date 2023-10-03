import time

from behave import step
from dotenv import load_dotenv
from pom.contact_us_page import ContactUsPage
import os


load_dotenv()


@step("the user fills out all the fields correctly")
def fill_form_correctly(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("a success message is displayed")
def success_message_is_visible(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    assert contact_us_page.success_message_is_visible(), "the test failed"


@step("the user fills out name field with invalid data")
def fill_name_invalid_data(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NUMBER"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("an error message is displayed")
def error_message_is_visible(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    assert contact_us_page.error_message_is_visible(), "the test failed"


@step("the user fills out email field with invalid data")
def fill_email_invalid_data(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("NAME"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("the user fills out company field with invalid data")
def fill_company_invalid_data(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(" ")
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("the user fills out number field with invalid data")
def fill_number_invalid_data(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NAME"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("the user fills out message field with invalid data")
def fill_message_invalid_data(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(" ")
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("the user do not check the terms and conditions checkbox")
def dont_check_terms_cond(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_name_input(os.getenv("NAME"))
    contact_us_page.fill_email_input(os.getenv("EMAIL"))
    contact_us_page.fill_company_input(os.getenv("COMPANY"))
    contact_us_page.fill_number_input(os.getenv("NUMBER"))
    contact_us_page.fill_message_input(os.getenv("MESSAGE"))
    contact_us_page.click_send()
