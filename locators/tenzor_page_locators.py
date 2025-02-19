from selenium.webdriver.common.by import By


class TenzorPageLocators:
    MAN_POWER_BLOCK = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    ABOUT_BUTTON = (By.XPATH, "//a[@href='/about']")