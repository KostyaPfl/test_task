import allure
from helpers import get_file_size_and_delete
from data import download_file_name



class TestFirstScript:

    @allure.title('Проверка соответствия размера скачанного файла с плагином с указанным на сайте')
    def test_file_size_is_equal_to_the_specified(self, main_page, download_page):
        main_page.go_to_download_page()
        download_page.download_plugin()
        file_size = download_page.get_size_from_site()
        actual_file_size = get_file_size_and_delete(download_file_name)
        assert actual_file_size == file_size

