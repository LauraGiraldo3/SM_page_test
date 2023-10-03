from behave import step
from dotenv import load_dotenv
from pom.job_page import JobPage
import os


load_dotenv()


@step("the user clicks on Apply Now button")
def click_apply(context):
    job_page = JobPage(context.browser_interactions)
    job_page.click_apply_now()


@step("the user can fill out the form")
def fill_out_form(context):
    job_page = JobPage(context.browser_interactions)
    job_page.fill_form(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("NUMBER"), os.getenv("LOCATION"), os.getenv("LINKEDIN"), os.getenv("MESSAGE"))
