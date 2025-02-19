import allure
from locators.tenzor_about_page_locators import TenzorAboutPageLocators
from page.base_page import BasePage



class TenzorAboutPage(BasePage):
    @allure.step('Получить список фотографий хронологии')
    def get_photo_list(self):
        #self.scroll_to_element(TenzorAboutPageLocators.WORKING_BLOCK)
        return self.find_elements(TenzorAboutPageLocators.PHOTO_LIST)