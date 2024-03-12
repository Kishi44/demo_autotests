import allure
from selenium import webdriver
from UI.Main_page import MainPage
from UI.Support_page import SupportPage



class TestUI:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(driver=self.driver)
        self.support_page = SupportPage(driver=self.driver)


    def test_download_links(self):
        with allure.step('Открываем страницу и переходим на нужную вкладку'):
            self.main_page.open_site()
            self.main_page.open_tab('Поддержка')
        with allure.step('Переходим в раздел для скачивания'):
            self.support_page.open_downloads_page('Скачать')

    def teardown_method(self):
        self.driver.quit()

