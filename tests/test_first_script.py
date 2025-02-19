import allure


class TestFirstScript:

    @allure.title('Проверка присутствия блока "Сила в людях"')
    def test_the_power_is_in_people_block(self, main_page, contact_page, tenzor_page):
        main_page.go_to_contacts_page()
        contact_page.go_to_tenzor_page()
        assert tenzor_page.find_man_power_block().is_displayed()

    @allure.title('Проверка открытия страницы "https://tensor.ru/about"')
    def test_open_tenzor_about_page(self, main_page, contact_page, tenzor_page):
        main_page.go_to_contacts_page()
        contact_page.go_to_tenzor_page()
        tenzor_page.find_man_power_block()
        tenzor_page.click_about_button()
        assert tenzor_page.get_url() == 'https://tensor.ru/about'

    @allure.title('Проверка что фотографии в хронологии имеют одинаковый размер')
    def test_photo_size(self, main_page, contact_page, tenzor_page, tenzor_about_page):
        main_page.go_to_contacts_page()
        contact_page.go_to_tenzor_page()
        tenzor_page.find_man_power_block()
        tenzor_page.click_about_button()
        images = tenzor_about_page.get_photo_list()
        heights = [img.size['height'] for img in images]
        widths = [img.size['width'] for img in images]
        assert len(set(heights)) == 1 and len(set(widths)) == 1
