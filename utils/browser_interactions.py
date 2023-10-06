from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langdetect import detect_langs


def cast_strategy(strategy: str):
    strategies = {"CSS": By.CSS_SELECTOR, "XPATH": By.XPATH, "ID": By.ID, "CLASS": By.CLASS_NAME}
    return strategies[strategy]


class BrowserInteractions:
    def __init__(self, driver: Chrome) -> object:
        self._driver = driver
        self.time_out = 5

    def open_page(self, url: str):
        self._driver.get(url)

    def click_element(self, strategy: str, selector: str):
        element = WebDriverWait(self._driver, self.time_out).until(EC.element_to_be_clickable((cast_strategy(strategy), selector)))
        self._driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        element.click()

    def input_text(self, strategy: str, selector: str, text: str):
        element = WebDriverWait(self._driver, self.time_out).until(EC.presence_of_element_located((cast_strategy(strategy), selector)))
        element.send_keys(text)

    def element_is_visible(self, strategy: str, selector: str):
        return WebDriverWait(self._driver, self.time_out).until(EC.visibility_of_element_located((cast_strategy(strategy), selector)))

    def load_file(self, strategy: str, selector: str, file_path: str):
        element = WebDriverWait(self._driver, self.time_out).until(EC.presence_of_element_located((cast_strategy(strategy), selector)))
        element.send_keys(file_path)

    def get_page_lan(self):
        return self._driver.find_element(By.XPATH, "//html").get_attribute('lang')

    def get_element_lan(self, strategy: str, selector: str):
        elem_text = self._driver.find_element(cast_strategy(strategy), selector).text
        return detect_langs(elem_text)

    def close_browser(self):
        self._driver.close()




