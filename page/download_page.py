import allure
from locators.download_page_locators import DownloadPageLocators
from page.base_page import BasePage
from helpers import wait_for_download_file, get_size
from data import download_file_name


class DownloadPage(BasePage):

    @allure.step('Скачать плагин')
    def download_plugin(self):
        self.find_element_with_wait(DownloadPageLocators.DOWNLOAD_PLUGIN)
        self.click_to_element(DownloadPageLocators.DOWNLOAD_PLUGIN)
        wait_for_download_file(download_file_name)

    @allure.step('получить размер файла указанный на сайте')
    def get_size_from_site(self):
        self.find_element_with_wait(DownloadPageLocators.DOWNLOAD_PLUGIN)
        text = self.get_text_from_element(DownloadPageLocators.DOWNLOAD_PLUGIN)
        return get_size(text)
