from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_element_text_change(self, locator, text):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*locator).text != text)

    def get_page_title(self):
        return self.driver.title

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_url(self):
        current_url = self.driver.current_url
        return current_url
