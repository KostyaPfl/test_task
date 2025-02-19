import allure
from locators.contact_page_locators import ContactPageLocators
from page.base_page import BasePage


class ContactPage(BasePage):

    @allure.step('Перейти на страницу "тензор"')
    def go_to_tenzor_page(self):
        self.find_element_with_wait(ContactPageLocators.TENZOR_BANNER)
        self.click_to_element(ContactPageLocators.TENZOR_BANNER)
        self.switch_to_window()

    @allure.step('Получить выбранный регион')
    def get_selected_region(self):
        self.find_element_with_wait(ContactPageLocators.SELECTED_REGION)
        return self.get_text_from_element(ContactPageLocators.SELECTED_REGION)

    @allure.step('изменить регион')
    def changing_region(self):
        self.find_element_with_wait(ContactPageLocators.SELECTED_REGION)
        home_region = self.get_text_from_element(ContactPageLocators.SELECTED_REGION)
        self.click_to_element(ContactPageLocators.SELECTED_REGION)
        self.find_element_with_wait(ContactPageLocators.KAMCHATKA_REGION)
        self.click_to_element(ContactPageLocators.KAMCHATKA_REGION)
        self.wait_element_text_change(ContactPageLocators.SELECTED_REGION, home_region)

    @allure.step('Получить список партнеров')
    def get_partner_list(self):
        return self.find_elements(ContactPageLocators.PARTNERS_LIST)
