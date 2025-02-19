from selenium.webdriver.common.by import By


class TenzorPageLocators:
    MAN_POWER_BLOCK = (By.XPATH, "//p[contains(text(),'Сила в людях')]")  #  блок "Сила в людях"
    ABOUT_BUTTON = (By.XPATH, "//a[@href='/about']")  # кнопка подробнее в блоке "Сила в людях"