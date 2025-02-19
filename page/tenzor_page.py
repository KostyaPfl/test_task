import allure
from locators.tenzor_page_locators import TenzorPageLocators
from page.base_page import BasePage


class TenzorPage(BasePage):

    @allure.step('найти блок "Сила в людях"')
    def find_man_power_block(self):
        self.scroll_to_element(TenzorPageLocators.MAN_POWER_BLOCK)
        return self.find_element_with_wait(TenzorPageLocators.MAN_POWER_BLOCK)

    @allure.step('Нажать кнопку "Подробнее" в блоке "Сила в людях"')
    def click_about_button(self):
        self.find_element_with_wait(TenzorPageLocators.ABOUT_BUTTON)
        self.click_to_element(TenzorPageLocators.ABOUT_BUTTON)
