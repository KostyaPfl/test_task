from selenium.webdriver.common.by import By


class DownloadPageLocators:
    DOWNLOAD_PLUGIN = (By.XPATH, "//a[contains(@href, 'setup-web')]")