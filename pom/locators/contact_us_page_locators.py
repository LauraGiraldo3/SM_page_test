class ContactUsPageLocators:
    NAME_INPUT = {"strategy": "ID", "selector": "field_qh4icy"}
    EMAIL_INPUT = {"strategy": "ID", "selector": "field_ocfup1"}
    COMPANY_INPUT = {"strategy": "ID", "selector": "field_29yf4d"}
    NUMBER_INPUT = {"strategy": "ID", "selector": "field_6lruj"}
    HELP_TEXT_INPUT = {"strategy": "ID", "selector": "field_e6lis6"}
    TERMS_COND_CHECKBOX = {"strategy": "ID", "selector": "frm_checkbox_7-0"}
    SEND_BUTTON = {"strategy": "CLASS", "selector": "frm_submit"}
    SUCCESS_MESSAGE = {"strategy": "CLASS", "selector": "frm_message"}
    GENERAL_ERROR_MESSAGE = {"strategy": "CLASS", "selector": "frm_error_style"}
    FIELD_ERROR_MESSAGE = {"strategy": "XPATH", "selector": "(//div[@class='frm_error'])"}
