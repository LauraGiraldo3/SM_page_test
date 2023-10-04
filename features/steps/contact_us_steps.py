from behave import step
from dotenv import load_dotenv
from pom.contact_us_page import ContactUsPage
import os


load_dotenv()


@step("the user fills out all the fields correctly")
def fill_form_correctly(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_out_form(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("COMPANY"), os.getenv("NUMBER"), os.getenv("MESSAGE"))
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("a success message is displayed")
def success_message_is_visible(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    assert contact_us_page.success_message_is_visible(), "the test failed"


@step("the user fills out '{field_name}' with '{invalid_data}'")
def fill_invalid_data(context, field_name, invalid_data):
    contact_us_page = ContactUsPage(context.browser_interactions)
    if invalid_data == "empty":
        invalid_data = " "
    if field_name == "name":
        contact_us_page.fill_out_form(invalid_data, os.getenv("EMAIL"), os.getenv("COMPANY"), os.getenv("NUMBER"), os.getenv("MESSAGE"))
    elif field_name == "email":
        contact_us_page.fill_out_form(os.getenv("NAME"), invalid_data, os.getenv("COMPANY"), os.getenv("NUMBER"), os.getenv("MESSAGE"))
    elif field_name == "company":
        contact_us_page.fill_out_form(os.getenv("NAME"), os.getenv("EMAIL"), invalid_data, os.getenv("NUMBER"), os.getenv("MESSAGE"))
    elif field_name == "number":
        contact_us_page.fill_out_form(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("COMPANY"), invalid_data, os.getenv("MESSAGE"))
    elif field_name == "message":
        contact_us_page.fill_out_form(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("COMPANY"), os.getenv("NUMBER"), invalid_data)
    contact_us_page.check_terms_cond()
    contact_us_page.click_send()


@step("the user do not check the terms and conditions checkbox")
def dont_check_terms_cond(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    contact_us_page.fill_out_form(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("COMPANY"), os.getenv("NUMBER"), os.getenv("MESSAGE"))
    contact_us_page.click_send()


@step("an error message is displayed")
def error_message_is_visible(context):
    contact_us_page = ContactUsPage(context.browser_interactions)
    assert contact_us_page.error_message_is_visible(), "the test failed"
