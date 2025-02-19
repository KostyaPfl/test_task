from selenium.webdriver.common.by import By


class TenzorAboutPageLocators:
    #WORKING_BLOCK = (By.XPATH, "//h2[contains(text(),'Работаем')]")  #  блок "Работаем"
    #PHOTO_LIST = (By.TAG_NAME, "img")  # кнопка подробнее в блоке "Сила в людях"
    #PHOTO_LIST = (By.XPATH, "//img[contains(class,'block3-image')]")
    PHOTO_LIST = (By.XPATH, "//img[contains(@class, 'block3')]")
