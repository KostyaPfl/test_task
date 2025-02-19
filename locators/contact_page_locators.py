from selenium.webdriver.common.by import By


class ContactPageLocators:
    TENZOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")  # баннер "Тензор" на странице контакты
    SELECTED_REGION = (By.XPATH, "//span[contains(@class, 'Region-Chooser__text')]")
    #SELECTED_REGION = (By.XPATH, "//span[contains(text(),'Краснодарский край')]")
    KAMCHATKA_REGION = (By.XPATH, "//span[@title='Камчатский край']")
    PARTNERS_LIST = (By.XPATH, "//div[contains(@class, 'Contacts-List__name')]")