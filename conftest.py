import pytest
from selenium import webdriver
from page.download_page import DownloadPage
from page.tenzor_about_page import TenzorAboutPage
from page.main_page import MainPage
from page.contact_page import ContactPage
from page.tenzor_page import TenzorPage
from data import main_page_URL
import os


@pytest.fixture()
def driver():
    download_dir = os.getcwd()
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get(main_page_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def contact_page(driver):
    return ContactPage(driver)


@pytest.fixture()
def tenzor_page(driver):
    return TenzorPage(driver)


@pytest.fixture()
def tenzor_about_page(driver):
    return TenzorAboutPage(driver)


@pytest.fixture()
def download_page(driver):
    return DownloadPage(driver)
