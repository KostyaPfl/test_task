from selenium.webdriver.common.by import By


class MainPageLocators:
    MORE_OFFICES_LINK = (By.XPATH, "//a[@href='/contacts']")
    CONTACTS_BUTTON = (By.XPATH, '//div[text()="Контакты"]')
    DOWNLOAD_LOCAL_VERSION = (By.XPATH, "//a[@href='/download']")