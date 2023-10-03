from behave import step
from dotenv import load_dotenv
from pom.join_us_page import JoinUsPage
import os


load_dotenv()


@step("the user select 'QA Automation' job")
def select_qa_job(context):
    join_us_page = JoinUsPage(context.browser_interactions)
    join_us_page.search_job(os.getenv("JOB_NAME"))