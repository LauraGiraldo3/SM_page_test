from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cast_strategy(strategy: str):
    strategies = {"CSS": By.CSS_SELECTOR, "XPATH": By.XPATH, "ID": By.ID, "CLASS": By.CLASS_NAME}
    return strategies[strategy]


class BrowserInteractions:
    def __init__(self, driver: Chrome) -> object:
        self._driver = driver
        self.time_out = 10

    def open_page(self, url: str):
        self._driver.get(url)

    def click_element(self, strategy: str, selector: str):
        element = WebDriverWait(self._driver, self.time_out).until(EC.element_to_be_clickable((cast_strategy(strategy), selector)))
        element.click()

    def input_text(self, strategy: str, selector: str, text: str):
        element = WebDriverWait(self._driver, self.time_out).until(EC.presence_of_element_located((cast_strategy(strategy), selector)))
        element.send_keys(text)

    def element_is_visible(self, strategy: str, selector: str):
        return WebDriverWait(self._driver, self.time_out).until(EC.visibility_of_element_located((cast_strategy(strategy), selector)))

    def scroll(self):
        self._driver.execute_script("window.scrollBy(0, 400)")
