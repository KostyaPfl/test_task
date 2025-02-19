from selenium.webdriver.common.by import By


class MainPageLocators:
    MORE_OFFICES_LINK = (By.XPATH, "//a[@href='/contacts']")  # Кнопка "Контакты" на главной странице
    CONTACTS_BUTTON = (By.XPATH, '//div[text()="Контакты"]')  # ссылка "Еще офисы в регионе" на главной странице
    DOWNLOAD_LOCAL_VERSION = (By.XPATH, "//a[@href='/download']") # Ссылка "Скачать локальные версии"