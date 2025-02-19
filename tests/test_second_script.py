import allure
from data import home_region, Kamchtka, Url_contains_region

class TestSecondScript:

    @allure.title('Проверка выбора по умолчанию домашнего региона и наличие списка партнеров')
    def test_default_selected_region(self, main_page, contact_page):
        main_page.go_to_contacts_page()
        assert contact_page.get_selected_region() == home_region and len(contact_page.get_partner_list()) > 0

    @allure.title('Проверка изменения региона и списка партнеров')
    def test_changing_region(self, main_page, contact_page):
        main_page.go_to_contacts_page()
        partner_list = contact_page.get_partner_list()
        contact_page.changing_region()
        assert contact_page.get_selected_region() == Kamchtka and contact_page.get_partner_list() != partner_list

    @allure.title('Проверка поставления в url и title выбранного региона')
    def test_url_and_title_changing_region(self, main_page, contact_page):
        main_page.go_to_contacts_page()
        contact_page.changing_region()
        url = contact_page.get_url()
        actual_title = contact_page.get_page_title()
        assert Url_contains_region in url and Kamchtka in actual_title
