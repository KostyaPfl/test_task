import allure
from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage



class MainPage(BasePage):

    @allure.step('Перейти в раздел "Контакты"')
    def go_to_contacts_page(self):
        self.find_element_with_wait(MainPageLocators.CONTACTS_BUTTON)
        self.click_to_element(MainPageLocators.CONTACTS_BUTTON)
        self.find_element_with_wait(MainPageLocators.MORE_OFFICES_LINK)
        self.click_to_element(MainPageLocators.MORE_OFFICES_LINK)


    @allure.step('Перейти на страницу "Загрузки"')
    def go_to_download_page(self):
        self.find_element_with_wait(MainPageLocators.DOWNLOAD_LOCAL_VERSION)
        self.click_to_element(MainPageLocators.DOWNLOAD_LOCAL_VERSION)
